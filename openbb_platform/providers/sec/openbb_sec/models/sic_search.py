"""SEC Standard Industrial Classification Code (SIC) Model."""
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from openbb_provider.abstract.data import Data
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.cot_search import CotSearchQueryParams
from openbb_sec.utils.helpers import sec_session_companies
from pydantic import Field


class SecSicSearchQueryParams(CotSearchQueryParams):
    """
    Fuzzy search for Industry Titles, Reporting Office, and SIC Codes

    Source: https://sec.gov/

    """

    use_cache: bool = Field(
        default=True,
        description="Whether to use the cache or not. The full list will be cached for seven days if True.",
    )


class SecSicSearchData(Data):
    """
    SEC Sector Industrial Code (SIC) Search Data.
    """

    sic: int = Field(description="Sector Industrial Code (SIC)", alias="SIC Code")
    industry: str = Field(description="Industry title.", alias="Industry Title")
    office: str = Field(
        description="Reporting office within the Corporate Finance Office",
        alias="Office",
    )


class SecSicSearchFetcher(
    Fetcher[
        SecSicSearchQueryParams,
        List[SecSicSearchData],
    ]
):
    """SEC Sector Industrial Code (SIC) Search Fetcher."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any], **kwargs: Any
    ) -> SecSicSearchQueryParams:
        return SecSicSearchQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecSicSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from the SEC website table."""

        data = pd.DataFrame()
        results: List[Dict] = []
        url = (
            "https://www.sec.gov/corpfin/"
            "division-of-corporation-finance-standard-industrial-classification-sic-code-list"
        )
        r = (
            sec_session_companies.get(url, timeout=5)
            if query.use_cache is True
            else requests.get(url, timeout=5)
        )

        if r.status_code == 200:
            data = pd.read_html(r.content.decode())[0].astype(str)
            if len(data) == 0:
                return results
            if query:
                data = data[
                    data["SIC Code"].str.contains(query.query, case=False)
                    | data["Office"].str.contains(query.query, case=False)
                    | data["Industry Title"].str.contains(query.query, case=False)
                ]
            data["SIC Code"] = data["SIC Code"].astype(int)
        results = data.to_dict("records")

        return results

    @staticmethod
    def transform_data(data: List[Dict], **kwargs: Any) -> List[SecSicSearchData]:
        return [SecSicSearchData.model_validate(d) for d in data]

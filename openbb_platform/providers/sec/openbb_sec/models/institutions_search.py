"""SEC Institutions Search"""

from typing import Any, Dict, List, Optional, Union

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.cot_search import CotSearchQueryParams
from openbb_sec.utils.helpers import get_all_ciks
from pydantic import Field


class SecInstitutionsSearchQueryParams(CotSearchQueryParams):
    """
    SEC Institutions query. This function assists with finding out the CIK number of a non-public company.

    Fuzzy search can be applied to the name.
    """

    use_cache: bool = Field(
        default=True,
        description="Whether or not to use cache. If True, cache will store for seven days.",
    )


class SecInstitutionsSearchData(Data):
    """SEC Institutions Search Data."""

    name: Optional[str] = Field(
        default=None, description="The name of the institution.", alias="Institution"
    )
    cik: Optional[Union[str, int]] = Field(
        default=None, description="Central Index Key (CIK)", alias="CIK Number"
    )


class SecInstitutionsSearchFetcher(
    Fetcher[
        SecInstitutionsSearchQueryParams,
        List[SecInstitutionsSearchData],
    ]
):
    """Transform the query, extract and transform the data from the SEC."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SecInstitutionsSearchQueryParams:
        """Transform the query."""
        return SecInstitutionsSearchQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecInstitutionsSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the SEC endpoint."""
        institutions = get_all_ciks(use_cache=query.use_cache)
        hp = institutions["Institution"].str.contains(query.query, case=False)
        return institutions[hp].astype(str).to_dict("records")

    @staticmethod
    def transform_data(
        data: List[Dict], **kwargs: Any
    ) -> List[SecInstitutionsSearchData]:
        """Transform the data to the standard format."""
        return [SecInstitutionsSearchData.model_validate(d) for d in data]

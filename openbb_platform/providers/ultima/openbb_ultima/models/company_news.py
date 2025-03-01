"""Ultima Company News Fetcher."""


from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.company_news import (
    CompanyNewsData,
    CompanyNewsQueryParams,
)
from openbb_ultima.utils.helpers import get_data
from pydantic import Field


class UltimaCompanyNewsQueryParams(CompanyNewsQueryParams):
    """Ultima Company News query.

    Source: https://api.ultimainsights.ai/v1/api-docs#/default/get_v1_getOpenBBProInsights__tickers_
    """

    __alias_dict__ = {
        "symbols": "tickers",
    }


class UltimaCompanyNewsData(CompanyNewsData):
    """Ultima Company News Data."""

    __alias_dict__ = {"date": "publishedDate", "text": "summary", "title": "headline"}

    publisher: str = Field(description="Publisher of the news.")
    ticker: str = Field(description="Ticker associated with the news.")
    riskCategory: str = Field(description="Risk category of the news.")


class UltimaCompanyNewsFetcher(
    Fetcher[
        UltimaCompanyNewsQueryParams,
        List[UltimaCompanyNewsData],
    ]
):
    """Ultima Company News Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> UltimaCompanyNewsQueryParams:
        """Transform query."""
        return UltimaCompanyNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: UltimaCompanyNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from Ultima Insights API."""
        token = credentials.get("ultima_api_key") if credentials else ""
        kwargs["auth"] = token

        base_url = "https://api.ultimainsights.ai/v1/getOpenBBProInsights"

        querystring = str(query).split("=")[1].split("'")[1].replace(" ", "")

        data = []
        url = f"{base_url}/{querystring}"
        response = get_data(url, **kwargs)
        data.extend(response)

        return data

    @staticmethod
    def transform_data(
        query: UltimaCompanyNewsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[UltimaCompanyNewsData]:
        """Transform data."""
        results = []
        for ele in data:
            for key in ["8k_filings", "articles", "industry_summary"]:
                for item in ele[key]:
                    # manual assignment required for Pydantic to work
                    item["ticker"] = ele["ticker"]
                    item["date"] = datetime.strptime(
                        item["publishedDate"], "%Y-%m-%d %H:%M:%S"
                    )
                    item["title"] = item["headline"]
                    item["url"] = item["url"]
                    item["publisher"] = item["publisher"]
                    results.append(UltimaCompanyNewsData.model_validate(item))
        return results

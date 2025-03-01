"""FMP Company News."""

from typing import Any, Dict, List, Optional, Union

from openbb_fmp.utils.helpers import get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.company_news import (
    CompanyNewsData,
    CompanyNewsQueryParams,
)
from pydantic import Field


class FMPCompanyNewsQueryParams(CompanyNewsQueryParams):
    """FMP Company News query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-news-api/
    """

    __alias_dict__ = {"symbols": "tickers"}
    page: Optional[int] = Field(
        default=0,
        description="Page number of the results. Use in combination with limit.",
    )


class FMPCompanyNewsData(CompanyNewsData):
    """FMP Company News data."""

    __alias_dict__ = {"date": "publishedDate"}

    symbol: str = Field(description="Ticker of the fetched news.")
    image: Optional[Union[List[str], str]] = Field(
        default=None, description="URL to the image of the news source."
    )
    site: str = Field(description="Name of the news source.")
    images: Optional[Union[List[str], str]] = Field(
        default=None, description="URL to the images of the news."
    )


class FMPCompanyNewsFetcher(
    Fetcher[
        FMPCompanyNewsQueryParams,
        List[FMPCompanyNewsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCompanyNewsQueryParams:
        """Transform the query params."""
        return FMPCompanyNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPCompanyNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3/stock_news"
        data = []
        url = f"{base_url}?page={query.page}&tickers={query.symbols}&limit={query.limit}&apikey={api_key}"
        response = get_data_many(url, **kwargs)

        if len(response) > 0:
            data = sorted(response, key=lambda x: x["publishedDate"], reverse=True)

        return data

    @staticmethod
    def transform_data(
        query: FMPCompanyNewsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPCompanyNewsData]:
        """Return the transformed data."""
        return [FMPCompanyNewsData.model_validate(d) for d in data]

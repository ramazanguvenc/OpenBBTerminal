"""Polygon Company News."""


from typing import Any, Dict, List, Literal, Optional

from openbb_polygon.utils.helpers import get_data_many, get_date_condition
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.company_news import (
    CompanyNewsData,
    CompanyNewsQueryParams,
)
from openbb_provider.utils.helpers import get_querystring
from pydantic import BaseModel, Field, field_validator


class PolygonCompanyNewsQueryParams(CompanyNewsQueryParams):
    """Polygon Company News query.

    Source: https://polygon.io/docs/stocks/get_v2_reference_news
    """

    __alias_dict__ = {"symbols": "ticker"}

    published_utc: Optional[str] = Field(
        default=None,
        description="Date query to fetch articles. Supports operators <, <=, >, >=",
    )
    order: Optional[Literal["asc", "desc"]] = Field(
        default="desc", description="Sort order of the articles."
    )

    @field_validator("limit", mode="before")
    def limit_validator(cls, v: int) -> int:  # pylint: disable=E0213
        """Limit validator."""
        return min(v, 1000)


class PolygonPublisher(BaseModel):
    """PolygonPublisher data model."""

    favicon_url: str = Field(description="Favicon URL.")
    homepage_url: str = Field(description="Homepage URL.")
    logo_url: str = Field(description="Logo URL.")
    name: str = Field(description="Publisher Name.")


class PolygonCompanyNewsData(CompanyNewsData):
    """Source: https://polygon.io/docs/stocks/get_v2_reference_news."""

    __alias_dict__ = {
        "url": "article_url",
        "text": "description",
        "date": "published_utc",
    }

    amp_url: Optional[str] = Field(default=None, description="AMP URL.")
    author: Optional[str] = Field(default=None, description="Author of the article.")
    id: str = Field(description="Article ID.")
    image_url: Optional[str] = Field(default=None, description="Image URL.")
    keywords: Optional[List[str]] = Field(
        default=None, description="Keywords in the article"
    )
    publisher: PolygonPublisher = Field(description="Publisher of the article.")
    tickers: List[str] = Field(description="Tickers covered in the article.")


class PolygonCompanyNewsFetcher(
    Fetcher[
        PolygonCompanyNewsQueryParams,
        List[PolygonCompanyNewsData],
    ]
):
    """Polygon Company News Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> PolygonCompanyNewsQueryParams:
        """Transform query params."""
        return PolygonCompanyNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: PolygonCompanyNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data."""
        api_key = credentials.get("polygon_api_key") if credentials else ""

        base_url = "https://api.polygon.io/v2/reference/news"

        if query.published_utc:
            date, condition = get_date_condition(query.published_utc)

            if condition != "eq":
                query_str = get_querystring(
                    query.model_dump(by_alias=True), ["published_utc"]
                )
                query_str += f"&published_utc.{condition}={date}"
            else:
                query_str = get_querystring(
                    query.model_dump(by_alias=True), ["published_utc"]
                )
                query_str += f"&published_utc={date}"

        else:
            query_str = get_querystring(query.model_dump(by_alias=True), [])

        url = f"{base_url}?{query_str}&apiKey={api_key}"

        return get_data_many(url, "results", **kwargs)

    @staticmethod
    def transform_data(
        query: PolygonCompanyNewsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[PolygonCompanyNewsData]:
        """Transform data."""
        return [PolygonCompanyNewsData.model_validate(d) for d in data]

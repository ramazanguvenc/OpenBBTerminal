"""Intrinio Currency available pairs fetcher."""


from typing import Any, Dict, List, Optional

from openbb_intrinio.utils.helpers import get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.currency_pairs import (
    CurrencyPairsData,
    CurrencyPairsQueryParams,
)
from pydantic import Field


class IntrinioCurrencyPairsQueryParams(CurrencyPairsQueryParams):
    """Intrinio Currency available pairs Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_forex_pairs_v2
    """


class IntrinioCurrencyPairsData(CurrencyPairsData):
    """Intrinio Currency available pairs Data."""

    __alias_dict__ = {"name": "code"}

    code: str = Field(description="Code of the currency pair.", alias="name")
    base_currency: str = Field(
        description="ISO 4217 currency code of the base currency."
    )
    quote_currency: str = Field(
        description="ISO 4217 currency code of the quote currency."
    )


class IntrinioCurrencyPairsFetcher(
    Fetcher[
        IntrinioCurrencyPairsQueryParams,
        List[IntrinioCurrencyPairsData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioCurrencyPairsQueryParams:
        """Transform the query params."""
        return IntrinioCurrencyPairsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: IntrinioCurrencyPairsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""

        base_url = "https://api-v2.intrinio.com"
        url = f"{base_url}/forex/pairs?api_key={api_key}"

        return get_data_many(url, "pairs", **kwargs)

    @staticmethod
    def transform_data(
        query: IntrinioCurrencyPairsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[IntrinioCurrencyPairsData]:
        """Return the transformed data."""
        return [IntrinioCurrencyPairsData.model_validate(d) for d in data]

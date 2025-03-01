"""FMP Currency available pairs fetcher."""


from typing import Any, Dict, List, Optional

from openbb_fmp.utils.helpers import get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.currency_pairs import (
    CurrencyPairsData,
    CurrencyPairsQueryParams,
)
from pydantic import Field


class FMPCurrencyPairsQueryParams(CurrencyPairsQueryParams):
    """FMP Currency available pairs Query.

    Source: http://site.financialmodelingprep.com/developer/docs/stock-ticker-symbol-lookup-api/?direct=true
    """


class FMPCurrencyPairsData(CurrencyPairsData):
    """FMP Currency available pairs Data."""

    symbol: str = Field(description="Symbol of the currency pair.")
    currency: str = Field(description="Base currency of the currency pair.")
    stock_exchange: Optional[str] = Field(
        default=None, description="Stock exchange of the currency pair."
    )
    exchange_short_name: Optional[str] = Field(
        default=None,
        description="Short name of the stock exchange of the currency pair.",
    )


class FMPCurrencyPairsFetcher(
    Fetcher[
        FMPCurrencyPairsQueryParams,
        List[FMPCurrencyPairsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCurrencyPairsQueryParams:
        """Transform the query params."""
        return FMPCurrencyPairsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPCurrencyPairsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"
        url = f"{base_url}/symbol/available-forex-currency-pairs?apikey={api_key}"

        return get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPCurrencyPairsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPCurrencyPairsData]:
        """Return the transformed data."""
        return [FMPCurrencyPairsData.model_validate(d) for d in data]

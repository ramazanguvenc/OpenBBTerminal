"""FMP Equity Peers fetcher."""


from typing import Any, Dict, Optional

from openbb_fmp.utils.helpers import create_url, get_data_one
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.equity_peers import (
    EquityPeersData,
    EquityPeersQueryParams,
)

# FMP SPECIFIC FUNCTIONALITY CURRENTLY


class FMPEquityPeersQueryParams(EquityPeersQueryParams):
    """FMP Equity Peers query.

    Source: https://site.financialmodelingprep.com/developer/docs/#Stock-Peers
    """


class FMPEquityPeersData(EquityPeersData):
    """FMP Equity Peers data."""


class FMPEquityPeersFetcher(
    Fetcher[
        FMPEquityPeersQueryParams,
        FMPEquityPeersData,
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPEquityPeersQueryParams:
        """Transform the query params."""
        return FMPEquityPeersQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPEquityPeersQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> Dict:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = create_url(4, "stock_peers", api_key, query)

        return get_data_one(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPEquityPeersQueryParams, data: dict, **kwargs: Any
    ) -> FMPEquityPeersData:
        """Return the transformed data."""
        data.pop("symbol")
        return FMPEquityPeersData.model_validate(data)

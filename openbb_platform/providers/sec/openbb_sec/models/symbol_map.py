"""SEC Symbol Mapping Tool."""


from typing import Any, Dict, Optional

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.cot_search import CotSearchQueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS
from openbb_sec.utils.helpers import cik_map
from pydantic import Field


class SecSymbolMapQueryParams(CotSearchQueryParams):
    """SEC symbol map query.  This query assists by mapping the CIK number to a ticker symbol."""


class SecSymbolMapData(Data):
    """SEC symbol map Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))


class SecSymbolMapFetcher(
    Fetcher[
        SecSymbolMapQueryParams,
        SecSymbolMapData,
    ]
):
    """Transform the query, extract and transform the data from the SEC."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SecSymbolMapQueryParams:
        """Transform the query."""
        return SecSymbolMapQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecSymbolMapQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> Dict:
        """Return the raw data from the SEC endpoint."""
        return {"symbol": cik_map(int(query.query))}

    @staticmethod
    def transform_data(data: Dict, **kwargs: Any) -> SecSymbolMapData:
        """Transform the data to the standard format."""
        return SecSymbolMapData.model_validate(data)

"""ETF Holdings data model."""

from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class EtfHoldingsQueryParams(QueryParams):
    """ETF Holdings Query Params."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")


class EtfHoldingsData(Data):
    """ETF Holdings Data."""

    symbol: Optional[str] = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "") + " (ETF)"
    )
    name: Optional[str] = Field(description="Name of the ETF holding.")

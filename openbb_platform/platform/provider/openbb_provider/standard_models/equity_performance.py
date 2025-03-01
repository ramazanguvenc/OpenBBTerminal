"""Equity performance data model."""

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class EquityPerformanceQueryParams(QueryParams):
    """Equity Performance QueryParams."""

    sort: str = Field(
        default="desc",
        description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.",
    )


class EquityPerformanceData(Data):
    """Equity performance data."""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str = Field(
        description="Name of the entity.",
    )
    price: float = Field(
        description="Last price.",
    )
    change: float = Field(
        description="Change in price value.",
    )
    percent_change: float = Field(
        description="Percent change.",
    )
    volume: float = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""),
    )

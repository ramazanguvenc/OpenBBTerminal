"""Market Snapshots  data model."""

from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class MarketSnapshotsQueryParams(QueryParams):
    """Market Snapshots Query Params"""


class MarketSnapshotsData(Data):
    """Market Snapshots Data"""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

    open: Optional[float] = Field(
        description=DATA_DESCRIPTIONS.get("open", ""),
        default=None,
    )
    high: Optional[float] = Field(
        description=DATA_DESCRIPTIONS.get("high", ""),
        default=None,
    )
    low: Optional[float] = Field(
        description=DATA_DESCRIPTIONS.get("low", ""),
        default=None,
    )
    close: Optional[float] = Field(
        description=DATA_DESCRIPTIONS.get("close", ""),
        default=None,
    )
    prev_close: Optional[float] = Field(
        description="The previous closing price of the stock.", default=None
    )
    change: Optional[float] = Field(description="The change in price.", default=None)
    change_percent: Optional[float] = Field(
        description="The change, as a percent.", default=None
    )
    volume: Optional[int] = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""), default=None
    )

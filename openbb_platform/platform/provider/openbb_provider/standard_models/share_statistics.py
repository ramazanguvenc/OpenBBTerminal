"""Share Statistics Data Model."""


from datetime import date as dateType
from typing import List, Optional, Set, Union

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class ShareStatisticsQueryParams(QueryParams):
    """Share Statistics Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class ShareStatisticsData(Data):
    """Return Share Statistics Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    date: Optional[dateType] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date", "")
    )
    free_float: Optional[float] = Field(
        default=None,
        description="Percentage of unrestricted shares of a publicly-traded company.",
    )
    float_shares: Optional[float] = Field(
        default=None,
        description="Number of shares available for trading by the general public.",
    )
    outstanding_shares: Optional[float] = Field(
        default=None, description="Total number of shares of a publicly-traded company."
    )
    source: Optional[str] = Field(
        default=None, description="Source of the received data."
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])

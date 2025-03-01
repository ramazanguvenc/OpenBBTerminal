"""Equity Peers data model."""

from typing import List, Set, Union

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import QUERY_DESCRIPTIONS


class EquityPeersQueryParams(QueryParams):
    """Equity Peers query model."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EquityPeersData(Data):
    """Equity Peers data."""

    peers_list: List[str] = Field(
        default_factory=list,
        description="A list of equity peers based on sector, exchange and market cap.",
    )

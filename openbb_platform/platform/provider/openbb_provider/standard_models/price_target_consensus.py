"""Price target consensus data model."""


from typing import List, Optional, Set, Union

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class PriceTargetConsensusQueryParams(QueryParams):
    """Price Target Consensus Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class PriceTargetConsensusData(Data):
    """Price target consensus Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    target_high: Optional[float] = Field(
        default=None, description="High target of the price target consensus."
    )
    target_low: Optional[float] = Field(
        default=None, description="Low target of the price target consensus."
    )
    target_consensus: Optional[float] = Field(
        default=None, description="Consensus target of the price target consensus."
    )
    target_median: Optional[float] = Field(
        default=None, description="Median target of the price target consensus."
    )

    @field_validator("symbol", mode="before", check_fields=False)
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])

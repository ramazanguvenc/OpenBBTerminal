"""Unusual Options data model."""

from typing import Optional

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class OptionsUnusualQueryParams(QueryParams):
    """Unusual Options Query Params"""

    symbol: Optional[str] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("symbol", "") + " (the underlying symbol)",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    def upper_symbol(cls, v: str):
        """Convert symbol to uppercase."""
        return v.upper() if v else None


class OptionsUnusualData(Data):
    """Unusual Options Data."""

    underlying_symbol: Optional[str] = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "") + " (the underlying symbol)",
        default=None,
    )
    contract_symbol: str = Field(description="Contract symbol for the option.")

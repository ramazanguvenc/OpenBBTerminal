"""Earnings call transcript data model."""


from datetime import datetime
from typing import List, Set, Union

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class EarningsCallTranscriptQueryParams(QueryParams):
    """Earnings call transcript rating Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    year: int = Field(description="Year of the earnings call transcript.")

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EarningsCallTranscriptData(Data):
    """Earnings call transcript Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    quarter: int = Field(description="Quarter of the earnings call transcript.")
    year: int = Field(description="Year of the earnings call transcript.")
    date: datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    content: str = Field(description="Content of the earnings call transcript.")

    @field_validator("symbol", mode="before")
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])

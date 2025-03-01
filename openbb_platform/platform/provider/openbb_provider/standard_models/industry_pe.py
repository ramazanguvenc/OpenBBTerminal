"""Industry P/E Ratio data model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class IndustryPEQueryParams(QueryParams):
    """Industry Price to Earnings Ratio Query."""


class IndustryPEData(Data):
    """Industry Price to Earnings Ratio Data."""

    date: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("date", ""), default=None
    )
    exchange: Optional[str] = Field(
        default=None, description="The exchange where the data is from."
    )
    industry: str = Field(description="The name of the industry.")
    pe: float = Field(description="The P/E ratio of the industry.")

"""Treasury Constant Maturity Model."""
from datetime import (
    date as dateType,
)
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class TreasuryConstantMaturityParams(QueryParams):
    """TreasuryConstantMaturity Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Optional[Literal["3m", "2y"]] = Field(
        default="3m",
        description="The maturity",
    )


class TreasuryConstantMaturityData(Data):
    """TreasuryConstantMaturity Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(description="TreasuryConstantMaturity Rate.")

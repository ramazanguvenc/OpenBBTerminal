"""Selected Treasury Constant Maturity Model."""
from datetime import (
    date as dateType,
)
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class SelectedTreasuryConstantMaturityParams(QueryParams):
    """SelectedTreasuryConstantMaturity Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Optional[Literal["10y", "5y", "1y", "6m", "3m"]] = Field(
        default="10y",
        description="The maturity",
    )


class SelectedTreasuryConstantMaturityData(Data):
    """SelectedTreasuryConstantMaturity Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(
        description="Selected Treasury Constant Maturity Rate."
    )

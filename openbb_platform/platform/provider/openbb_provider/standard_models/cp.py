"""Commercial Paper Model."""
from datetime import (
    date as dateType,
)
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class CommercialPaperParams(QueryParams):
    """Commercial Paper Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Literal["overnight", "7d", "15d", "30d", "60d", "90d"] = Field(
        default="30d",
        description="The maturity.",
    )
    category: Literal["asset_backed", "financial", "nonfinancial"] = Field(
        default="financial",
        description="The category.",
    )
    grade: Literal["aa", "a2_p2"] = Field(
        default="aa",
        description="The grade.",
    )


class CommercialPaperData(Data):
    """Commercial Paper Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(description="Commercial Paper Rate.")

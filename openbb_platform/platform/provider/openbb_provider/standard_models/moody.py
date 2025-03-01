"""Moody Corporate Bond Index Model."""
from datetime import (
    date as dateType,
)
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class MoodyCorporateBondIndexParams(QueryParams):
    """Moody Corporate Bond Index Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    index_type: Literal["aaa", "baa"] = Field(
        default="aaa",
        description="The type of series.",
    )


class MoodyCorporateBondIndexData(Data):
    """Moody Corporate Bond Index Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(description="Moody Corporate Bond Index Rate.")

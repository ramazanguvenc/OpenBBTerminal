"""European Central Bank Interest Rates Model."""
from datetime import (
    date as dateType,
)
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class EuropeanCentralBankInterestRatesParams(QueryParams):
    """European Central Bank Interest Rates Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    interest_rate_type: Literal["deposit", "lending", "refinancing"] = Field(
        default="lending",
        description="The type of interest rate.",
    )


class EuropeanCentralBankInterestRatesData(Data):
    """European Central Bank Interest Rates Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(description="European Central Bank Interest Rate.")

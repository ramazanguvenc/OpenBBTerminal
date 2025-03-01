"""Forecast GDP data model."""
from datetime import date as dateType
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class GdpForecastQueryParams(QueryParams):
    """Forecast GDP query."""

    period: Literal["quarter", "annual"] = Field(
        default="annual",
        description=QUERY_DESCRIPTIONS.get("period", "")
        + " Units for nominal GDP period. Either quarter or annual.",
    )
    start_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )
    type: Literal["nominal", "real"] = Field(
        default="real",
        description="Type of GDP to get forecast of. Either nominal or real.",
    )


class GdpForecastData(Data):
    """Forecast GDP data."""

    date: Optional[dateType] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    value: Optional[float] = Field(
        default=None, description="Nominal GDP value on the date."
    )

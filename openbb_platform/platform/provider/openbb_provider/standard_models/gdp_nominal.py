"""Nominal GDP data model."""
from datetime import date as dateType
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class GdpNominalQueryParams(QueryParams):
    """Nominal GDP query."""

    units: Literal["usd", "usd_cap"] = Field(
        default="usd",
        description=QUERY_DESCRIPTIONS.get("units", "")
        + " Units to get nominal GDP in. Either usd or usd_cap indicating per capita.",
    )
    start_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class GdpNominalData(Data):
    """Nominal GDP data."""

    date: Optional[dateType] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    value: Optional[float] = Field(
        default=None, description="Nominal GDP value on the date."
    )

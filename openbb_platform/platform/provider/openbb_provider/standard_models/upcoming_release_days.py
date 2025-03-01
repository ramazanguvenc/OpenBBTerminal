"""Upcoming Release Days standard model."""

from datetime import date as dateType

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class UpcomingReleaseDaysQueryParams(QueryParams):
    """Upcoming Release Days Search Query Params."""


class UpcomingReleaseDaysData(Data):
    """Upcoming Release Days Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="The full name of the asset.")
    exchange: str = Field(description="The exchange the asset is traded on.")
    release_time_type: str = Field(description="The type of release time.")
    release_date: dateType = Field(description="The date of the release.")

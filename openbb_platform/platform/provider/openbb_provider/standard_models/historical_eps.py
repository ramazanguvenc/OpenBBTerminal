"""Historical EPS data model."""


from datetime import date as dateType
from typing import List, Optional, Set, Union

from dateutil import parser
from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class HistoricalEpsQueryParams(QueryParams):
    """Historical Earnings Per Share Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class HistoricalEpsData(Data):
    """Historical Earnings Per Share Data."""

    date: dateType = Field(default=None, description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    announce_time: Optional[str] = Field(
        default=None, description="Timing of the earnings announcement."
    )
    eps_actual: Optional[float] = Field(
        default=None, description="Actual EPS from the earnings date."
    )
    eps_estimated: Optional[float] = Field(
        default=None, description="Estimated EPS for the earnings date."
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        return parser.isoparse(str(v))

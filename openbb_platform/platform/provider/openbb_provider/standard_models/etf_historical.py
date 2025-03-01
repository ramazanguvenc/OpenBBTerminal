"""ETF Historical End of Day Market Price."""

from datetime import date as dateType
from typing import List, Optional, Set, Union

from dateutil import parser
from pydantic import Field, NonNegativeInt, PositiveFloat, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class EtfHistoricalQueryParams(QueryParams):
    """ETF end of day Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")
    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def validate_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase and remove '-'."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EtfHistoricalData(Data):
    """ETF end of day price Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: Optional[NonNegativeInt] = Field(
        description=DATA_DESCRIPTIONS.get("volume", "")
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        return parser.isoparse(str(v))

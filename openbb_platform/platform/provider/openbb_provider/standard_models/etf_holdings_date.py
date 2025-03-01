"""ETF Holdings Date data model."""

from datetime import date as dateType

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class EtfHoldingsDateQueryParams(QueryParams):
    """ETF Holdings Query Params."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")


class EtfHoldingsDateData(Data):
    """ETF Holdings Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))

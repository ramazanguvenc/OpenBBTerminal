"""Top Retail standard model."""

from datetime import date as DateType

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class TopRetailQueryParams(QueryParams):
    """Top Retail Search Query Params."""

    limit: int = Field(description=QUERY_DESCRIPTIONS.get("limit", ""), default=5)


class TopRetailData(Data):
    """Top Retail Search Data."""

    date: DateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    activity: float = Field(description="Activity of the symbol.")
    sentiment: float = Field(
        description="Sentiment of the symbol. 1 is bullish, -1 is bearish."
    )

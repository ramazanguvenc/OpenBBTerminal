"""ETF Search data model."""

from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class EtfSearchQueryParams(QueryParams):
    """ETF Search Query Params."""

    query: Optional[str] = Field(description="Search query.", default="")


class EtfSearchData(Data):
    """ETF Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + "(ETF)")
    name: Optional[str] = Field(description="Name of the ETF.", default=None)

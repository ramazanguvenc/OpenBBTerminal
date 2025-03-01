"""Commitment of Traders Reports Search  data model."""

from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class CotSearchQueryParams(QueryParams):
    """Commitment of Traders Reports Search Query Params."""

    query: str = Field(description="Search query.", default="")


class CotSearchData(Data):
    """Commitment of Traders Reports Search Data."""

    code: str = Field(description="CFTC Code of the report.")
    name: str = Field(description="Name of the underlying asset.")
    category: Optional[str] = Field(
        default=None, description="Category of the underlying asset."
    )
    subcategory: Optional[str] = Field(
        default=None, description="Subcategory of the underlying asset."
    )
    units: Optional[str] = Field(
        default=None, description="The units for one contract."
    )
    symbol: Optional[str] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )

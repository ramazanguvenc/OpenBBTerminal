"""ETF Sectors data model."""

from typing import List, Optional, Set, Union

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import QUERY_DESCRIPTIONS


class EtfSectorsQueryParams(QueryParams):
    """ETF Sectors Query Params."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EtfSectorsData(Data):
    """FMP ETF Sector Info."""

    sector: str = Field(description="Sector of exposure.")
    weight: Optional[float] = Field(
        description="Exposure of the ETF to the sector in normalized percentage points."
    )

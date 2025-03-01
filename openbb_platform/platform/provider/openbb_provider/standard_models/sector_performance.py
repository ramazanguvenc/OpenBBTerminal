"""Sector Performance data model."""

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams


class SectorPerformanceQueryParams(QueryParams):
    """Sector Performance Query."""


class SectorPerformanceData(Data):
    """Sector Performance Data."""

    sector: str = Field(description="The name of the sector.")
    change_percent: float = Field(description="The change in percent from open.")

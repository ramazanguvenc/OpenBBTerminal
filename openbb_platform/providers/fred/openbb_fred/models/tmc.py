"""TreasuryConstantMaturity Fetcher."""


from typing import Any, Dict, List, Optional

from openbb_fred.utils.fred_base import Fred
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.tmc import (
    TreasuryConstantMaturityData,
    TreasuryConstantMaturityParams,
)
from pydantic import field_validator

TMC_PARAMETER_TO_FRED_ID = {
    "3m": "T10Y3M",
    "2y": "T10Y2Y",
}


class FREDTreasuryConstantMaturityParams(TreasuryConstantMaturityParams):
    """TreasuryConstantMaturityParams Query."""


class FREDTreasuryConstantMaturityData(TreasuryConstantMaturityData):
    """TreasuryConstantMaturityParams Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDTreasuryConstantMaturityFetcher(
    Fetcher[
        FREDTreasuryConstantMaturityParams,
        List[FREDTreasuryConstantMaturityData],
    ]
):
    """TreasuryConstantMaturityParams Fetcher."""

    data_type = FREDTreasuryConstantMaturityData

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FREDTreasuryConstantMaturityParams:
        """Transform query."""
        return FREDTreasuryConstantMaturityParams(**params)

    @staticmethod
    def extract_data(
        query: FREDTreasuryConstantMaturityParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any
    ) -> list:
        """Extract data."""
        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = fred.get_series(
            series_id=TMC_PARAMETER_TO_FRED_ID[query.maturity],
            start_date=query.start_date,
            end_date=query.end_date,
            **kwargs,
        )

        return data

    @staticmethod
    def transform_data(
        query: FREDTreasuryConstantMaturityParams, data: list, **kwargs: Any
    ) -> List[FREDTreasuryConstantMaturityData]:
        """Transform data."""
        return [FREDTreasuryConstantMaturityData.model_validate(d) for d in data]

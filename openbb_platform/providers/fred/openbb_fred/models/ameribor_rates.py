"""FRED AMERIBOR Fetcher."""


from typing import Any, Dict, List, Literal, Optional

from openbb_fred.utils.fred_base import Fred
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.ameribor_rates import (
    AMERIBORData,
    AMERIBORQueryParams,
)
from pydantic import Field, field_validator

AMERIBOR_PARAMETER_TO_FRED_ID = {
    "overnight": "AMERIBOR",
    "term_30": "AMBOR30T",
    "term_90": "AMBOR90T",
    "1_week_term_structure": "AMBOR1W",
    "1_month_term_structure": "AMBOR1M",
    "3_month_term_structure": "AMBOR3M",
    "6_month_term_structure": "AMBOR6M",
    "1_year_term_structure": "AMBOR1Y",
    "2_year_term_structure": "AMBOR2Y",
    "30_day_ma": "AMBOR30",
    "90_day_ma": "AMBOR90",
}


class FREDAMERIBORQueryParams(AMERIBORQueryParams):
    """AMERIBOR query."""

    parameter: Literal[
        "overnight",
        "term_30",
        "term_90",
        "1_week_term_structure",
        "1_month_term_structure",
        "3_month_term_structure",
        "6_month_term_structure",
        "1_year_term_structure",
        "2_year_term_structure",
        "30_day_ma",
        "90_day_ma",
    ] = Field(default="overnight", description="Period of AMERIBOR rate.")


class FREDAMERIBORData(AMERIBORData):
    """AMERIBOR data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDAMERIBORFetcher(
    Fetcher[FREDAMERIBORQueryParams, List[Dict[str, List[FREDAMERIBORData]]]]
):
    """FRED AMERIBOR Fetcher."""

    data_type = FREDAMERIBORData

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FREDAMERIBORQueryParams:
        """Transform query."""
        return FREDAMERIBORQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDAMERIBORQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> dict:
        """Extract data."""
        key = credentials.get("fred_api_key") if credentials else ""
        fred_series = AMERIBOR_PARAMETER_TO_FRED_ID[query.parameter]
        fred = Fred(key)
        data = fred.get_series(fred_series, query.start_date, query.end_date, **kwargs)
        return data

    @staticmethod
    def transform_data(
        query: FREDAMERIBORQueryParams, data: dict, **kwargs: Any
    ) -> List[Dict[str, List[FREDAMERIBORData]]]:
        """Transform data."""
        keys = ["date", "value"]
        return [FREDAMERIBORData(**{k: x[k] for k in keys}) for x in data]

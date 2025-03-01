"""HighQualityMarketCorporateBond Fetcher."""


from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from openbb_fred.utils.fred_base import Fred
from openbb_fred.utils.fred_helpers import (
    YIELD_CURVE_SERIES_CORPORATE_PAR,
    YIELD_CURVE_SERIES_CORPORATE_SPOT,
)
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.hqm import (
    HighQualityMarketCorporateBondData,
    HighQualityMarketCorporateBondParams,
)
from pydantic import field_validator


class FREDHighQualityMarketCorporateBondParams(HighQualityMarketCorporateBondParams):
    """HighQualityMarketCorporateBondParams Query."""


class FREDHighQualityMarketCorporateBondData(HighQualityMarketCorporateBondData):
    """HighQualityMarketCorporateBondParams Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDHighQualityMarketCorporateBondFetcher(
    Fetcher[
        FREDHighQualityMarketCorporateBondParams,
        List[FREDHighQualityMarketCorporateBondData],
    ]
):
    """HighQualityMarketCorporateBondParams Fetcher."""

    data_type = FREDHighQualityMarketCorporateBondData

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> FREDHighQualityMarketCorporateBondParams:
        """Transform query."""
        return FREDHighQualityMarketCorporateBondParams(**params)

    @staticmethod
    def extract_data(
        query: FREDHighQualityMarketCorporateBondParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any
    ) -> list:
        """Extract data."""
        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = []

        today = datetime.today().date()
        if query.date and query.date >= today:
            raise ValueError("Date must be in the past.")

        start_date = (
            query.date - timedelta(days=50)
            if query.date
            else today - timedelta(days=50)
        )

        for type_ in query.yield_curve:
            if type_ == "spot":
                fred_series = YIELD_CURVE_SERIES_CORPORATE_SPOT
            elif type_ == "par":
                fred_series = YIELD_CURVE_SERIES_CORPORATE_PAR
            else:
                raise ValueError("Invalid yield curve type.")

            for maturity, id_ in fred_series.items():
                d = fred.get_series(
                    series_id=id_,
                    start_date=start_date,
                    **kwargs,
                )
                for item in d:
                    item["maturity"] = maturity
                    item["yield_curve"] = type_
                data.extend(d)

        return data

    @staticmethod
    def transform_data(
        query: FREDHighQualityMarketCorporateBondParams, data: list, **kwargs: Any
    ) -> List[FREDHighQualityMarketCorporateBondData]:
        """Transform data."""
        return [FREDHighQualityMarketCorporateBondData.model_validate(d) for d in data]

"""Discount Window Primary Credit Rate Fetcher."""

from typing import Any, Dict, List, Literal, Optional

from openbb_fred.utils.fred_base import Fred
from openbb_fred.utils.fred_helpers import get_ice_bofa_series_id
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.ice_bofa import (
    ICEBofAData,
    ICEBofAParams,
)
from pydantic import Field, field_validator


class FREDICEBofAParams(ICEBofAParams):
    """ICEBofAParams Query."""

    category: Literal["all", "duration", "eur", "usd"] = Field(
        default="all", description="The type of category."
    )
    area: Literal["asia", "emea", "eu", "ex_g10", "latin_america", "us"] = Field(
        default="us", description="The type of area."
    )
    grade: Literal[
        "a",
        "aa",
        "aaa",
        "b",
        "bb",
        "bbb",
        "ccc",
        "crossover",
        "high_grade",
        "high_yield",
        "non_financial",
        "non_sovereign",
        "private_sector",
        "public_sector",
    ] = Field(default="non_sovereign", description="The type of grade.")
    options: bool = Field(
        default=False, description="Whether to include options in the results."
    )


class FREDICEBofAData(ICEBofAData):
    """ICEBofAParams Data."""

    __alias_dict__ = {"rate": "value", "title": "fred_series_title"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDICEBofAFetcher(
    Fetcher[
        FREDICEBofAParams,
        List[FREDICEBofAData],
    ]
):
    """ICEBofAParams Fetcher."""

    data_type = FREDICEBofAData

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FREDICEBofAParams:
        """Transform query."""
        return FREDICEBofAParams(**params)

    @staticmethod
    def extract_data(
        query: FREDICEBofAParams, credentials: Optional[Dict[str, str]], **kwargs: Any
    ) -> list:
        """Extract data."""
        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        series = get_ice_bofa_series_id(
            type_=query.index_type,
            category=query.category,
            area=query.area,
            grade=query.grade,
        )

        data = []

        for s in series:
            id_ = s["FRED Series ID"]
            title = s["Title"]
            d = fred.get_series(
                series_id=id_,
                start_date=query.start_date,
                end_date=query.end_date,
                **kwargs,
            )
            for item in d:
                item["title"] = title
            data.extend(d)

        return data

    @staticmethod
    def transform_data(
        query: FREDICEBofAParams, data: list, **kwargs: Any
    ) -> List[FREDICEBofAData]:
        """Transform data."""
        return [FREDICEBofAData.model_validate(d) for d in data]

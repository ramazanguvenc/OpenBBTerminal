"""Yahoo Finance growth tech equities fetcher."""
import re
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.equity_performance import (
    EquityPerformanceData,
    EquityPerformanceQueryParams,
)
from pydantic import Field


class YFGrowthTechEquitiesQueryParams(EquityPerformanceQueryParams):
    """YF asset performance growth tech equities QueryParams.

    Source: https://finance.yahoo.com/screener/predefined/growth_technology_stocks
    """


class YFGrowthTechEquitiesData(EquityPerformanceData):
    """YF asset performance growth tech equities Data."""

    __alias_dict__ = {
        "symbol": "Symbol",
        "name": "Name",
        "volume": "Volume",
        "change": "Change",
        "price": "Price (Intraday)",
        "percent_change": "% Change",
        "market_cap": "Market Cap",
        "avg_volume_3_months": "Avg Vol (3 month)",
        "pe_ratio_ttm": "PE Ratio (TTM)",
    }

    market_cap: str = Field(
        description="Market Cap.",
    )
    avg_volume_3_months: float = Field(
        description="Average volume over the last 3 months in millions.",
    )
    pe_ratio_ttm: Optional[float] = Field(
        description="PE Ratio (TTM).",
        default=None,
    )


class YFGrowthTechEquitiesFetcher(
    Fetcher[YFGrowthTechEquitiesQueryParams, List[YFGrowthTechEquitiesData]]
):
    """YF asset performance undervalued tech equities Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFGrowthTechEquitiesQueryParams:
        """Transform query params."""
        return YFGrowthTechEquitiesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFGrowthTechEquitiesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> pd.DataFrame:
        """Get data from YF."""
        headers = {"user_agent": "Mozilla/5.0"}
        html = requests.get(
            "https://finance.yahoo.com/screener/predefined/growth_technology_stocks",
            headers=headers,
            timeout=10,
        ).text
        html_clean = re.sub(r"(<span class=\"Fz\(0\)\">).*?(</span>)", "", html)
        df = (
            pd.read_html(html_clean, header=None)[0]
            .dropna(how="all", axis=1)
            .replace(float("NaN"), "")
        )
        return df

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: pd.DataFrame,
        **kwargs: Any,
    ) -> List[YFGrowthTechEquitiesData]:
        """Transform data."""
        data["% Change"] = data["% Change"].str.replace("%", "")
        data["Volume"] = data["Volume"].str.replace("M", "").astype(float) * 1000000
        data["Avg Vol (3 month)"] = (
            data["Avg Vol (3 month)"].str.replace("M", "").astype(float) * 1000000
        )
        data = data.apply(pd.to_numeric, errors="ignore")
        data = data.to_dict(orient="records")
        data = sorted(data, key=lambda d: d["Volume"], reverse=query.sort == "desc")
        return [YFGrowthTechEquitiesData.model_validate(d) for d in data]

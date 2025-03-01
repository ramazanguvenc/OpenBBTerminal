"""SEC Schema Files List Fetcher."""


from typing import Any, Dict, List, Optional

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.cot_search import CotSearchQueryParams
from openbb_sec.utils.helpers import get_schema_filelist
from pydantic import Field


class SecSchemaFilesQueryParams(CotSearchQueryParams):
    """SEC Schema Files List By Year. A helper function to generate URLs to XML/XSD files."""

    url: Optional[str] = Field(
        description="Enter an optional URL path to fetch the next level.", default=None
    )


class SecSchemaFilesData(Data):
    """SEC Schema Files Data."""

    files: List = Field(description="Dictionary of URLs to SEC Schema Files")


class SecSchemaFilesFetcher(Fetcher[SecSchemaFilesQueryParams, SecSchemaFilesData]):
    """SEC Schema Files Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SecSchemaFilesQueryParams:
        """Transform the query."""
        return SecSchemaFilesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecSchemaFilesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> Dict:
        """Return the raw data from the SEC endpoint."""

        if query.url and ".xsd" in query.url or query.url and ".xml" in query.url:
            raise ValueError("Invalid URL. This endpoint does not parse the files.")
        results = get_schema_filelist(query.query, query.url)

        return {"files": results}

    @staticmethod
    def transform_data(data: Dict, **kwargs: Any) -> SecSchemaFilesData:
        """Transform the data to the standard format."""
        return SecSchemaFilesData.model_validate(data)

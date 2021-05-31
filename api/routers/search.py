from fastapi import APIRouter, Response
from typing import Optional
from pydantic import constr

from ..models import SearchResponse


router = APIRouter()


@router.get("/search", response_model=SearchResponse)
def get_api_v1_search(
    ip_address: Optional[constr(min_length=1, max_length=15)] = None,
    namespace: Optional[constr(min_length=1, max_length=50)] = None,
    operation: Optional[constr(min_length=1, max_length=15)] = None,
    type: Optional[constr(min_length=1, max_length=15)] = None,
    source: Optional[constr(min_length=1, max_length=50)] = None,
) -> SearchResponse:
    """
    Search Kusto based on query parameters
    """
    return {"total": 2, "next": 1, "pages": 5, "results": []}

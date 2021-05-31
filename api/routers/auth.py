from fastapi import APIRouter, Query
from pydantic import constr
from ..models import (
    LoginBody,
    AuthLoginPostResponse,
    AuthRefreshPostResponse,
    AuthRevokeAccessDeleteResponse,
    AuthRevokeRefreshDeleteResponse,
)

router = APIRouter()


@router.post("/auth/login", response_model=AuthLoginPostResponse)
def login(body: LoginBody = None) -> AuthLoginPostResponse:
    """
    Login user
    """
    return {}


@router.post("/auth/refresh", response_model=AuthRefreshPostResponse)
def auth_refresh(
    authorization: constr(min_length=1, max_length=255) = Query(
        ..., alias="Authorization"
    )
) -> AuthRefreshPostResponse:
    """
    Refresh authorization token
    """
    return {}


@router.delete("/auth/revoke_access", response_model=AuthRevokeAccessDeleteResponse)
def revoke_access() -> AuthRevokeAccessDeleteResponse:
    """
    Revoke access
    """
    return {}


@router.delete("/auth/revoke_refresh", response_model=AuthRevokeRefreshDeleteResponse)
def revoke_refresh() -> AuthRevokeRefreshDeleteResponse:
    """
    Revoke Refresh
    """
    return {}

from fastapi import APIRouter
from typing import Any
from pydantic import constr

router = APIRouter()


@router.get("/user", response_model=Any)
def get_user() -> Any:
    """
    Get a list of users provisioned
    """
    return {} 


@router.get("/user/{username}", response_model=Any)
def get_user_by_username(username: constr(min_length=1, max_length=40)) -> Any:
    """
    Get user by username
    """
    return {}

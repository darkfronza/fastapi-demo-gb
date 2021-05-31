from enum import Enum
from pydantic import BaseModel, Field, conint, constr
from typing import Optional, List, Any, Dict
from datetime import datetime


class AuthLoginPostResponse(BaseModel):
    access_token: Optional[str] = Field(None, example="myaccesstoken")
    refresh_token: Optional[str] = Field(None, example="myrefreshtoken")


class AuthRefreshPostResponse(BaseModel):
    access_token: Optional[str] = Field(None, example="myaccesstoken")


class AuthRevokeAccessDeleteResponse(BaseModel):
    message: Optional[str] = Field(None, example="token revoked")


class AuthRevokeRefreshDeleteResponse(BaseModel):
    message: Optional[str] = Field(None, example="token revoked")


class Error(BaseModel):
    error: Optional[str] = Field(None, example="The specified resource was not found")


class LoginBody(BaseModel):
    password: Optional[str] = Field(None, example="P4$$w0rd!")
    username: Optional[str] = Field(None, example="myuser")


class PaginatedResult(BaseModel):
    next: Optional[str] = Field(None, example="/api/v1/source?page=2&per_page=50")
    pages: Optional[conint(ge=1)] = Field(None, example=1)
    total: Optional[conint(ge=1)] = Field(None, example=1)


class Success(Enum):
    True_ = True
    False_ = False


class EventSuccess(BaseModel):
    success: Optional[Success] = None


class Operation(Enum):
    add = "add"
    remove = "remove"
    retire = "retire"


class Type(Enum):
    host = "host"
    webendpoint = "webendpoint"
    azuresubscription = "azuresubscription"
    database = "database"
    container = "container"
    network = "network"
    ipaddress = "ipaddress"


class Event(BaseModel):
    ip_address: Optional[constr(regex=r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$")] = Field(
        None, example="127.0.0.1"
    )
    namespace: Optional[constr(regex=r"^([a-z0-9]+\.?)*$")] = Field(
        None, example="network.am4.production.leaf.management"
    )
    operation: Optional[Operation] = None
    type: Optional[Type] = None
    timestamp: Optional[conint(ge=1617914365)] = Field(None, example=1617914365)
    metadata: Optional[Dict[str, Any]] = Field(
        None, example={"type": "new", "category": "network"}
    )
    catalog_entry: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="routing"
    )
    owner: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="github/network"
    )
    lifetime: Optional[conint(ge=1, le=31622400)] = Field(None, example=86400)


class SearchResponse(PaginatedResult):
    results: Optional[List[Event]]


class State(Enum):
    active = "active"
    inactive = "inactive"


class Sources(BaseModel):
    source: Optional[str] = Field(None, example="network-yaml")


class State1(Enum):
    active = "active"
    inactive = "inactive"


class Source(BaseModel):
    id: Optional[int] = Field(None, example=1)
    state: Optional[State1] = None
    name: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="network-yaml"
    )
    catalog_entry: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="routing"
    )
    owner: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="github/network"
    )
    username: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="network"
    )
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None


class User(BaseModel):
    id: Optional[int] = Field(None, example=1)
    state: Optional[State] = None
    username: Optional[constr(min_length=1, max_length=40)] = Field(
        None, example="network-yaml"
    )
    sources: Optional[List[Sources]] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None

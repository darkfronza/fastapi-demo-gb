import json
import sys
import traceback

from fastapi import APIRouter, Request
from typing import Any, Optional
from pydantic import constr
from ..models import Event
from ..evhub_client import EventHubClient

from azure.eventhub import EventData
from azure.eventhub.exceptions import EventHubError


router = APIRouter()


@router.get("/source", response_model=Any)
def get_sources() -> Any:
    """
    Get a list of sources
    """    
    return {"sources": []}


@router.get("/source/{name}", response_model=Any)
def get_source_by_name(name: constr(min_length=1, max_length=40)) -> Any:
    """
    Get source by name
    """
    pass


@router.post("/source/{name}/event", response_model=Any)
async def save_source_event_by_name(request: Request,
    name: constr(min_length=1, max_length=40), body: Event = None
) -> Any:
    """
    Send event to source by {name} for persistance to Kusto
    """
    if not name or not body.ip_address:
        return {}

    if not request.app.evhub_client:
        return {"error": "Event Hub client is not connected"}

    data_dict = dict(Source=name, IpAddress=body.ip_address)
    err_msg = ""

    try:
        evdata = EventData(json.dumps(data_dict))
        async with request.app.evhub_client:
            await request.app.evhub_client.send_batch([evdata])
    except ValueError:  # Size exceeds limit. This shouldn't happen if you make sure before hand.
        err_msg = "Size of the event data list exceeds the size limit of a single send"
    except EventHubError as eh_err:
        err_msg= "Sending error: {}".format(eh_err)
    except Exception:
        err_msg = traceback.format_exc()

    if err_msg:
        return {"error": err_msg}
    
    return {"result": "ok"}


@router.get("/source/{name}/search", response_model=Any)
def search_sources(
    name: constr(min_length=1, max_length=40),
    ip_address: Optional[constr(min_length=1, max_length=15)] = None,
    namespace: Optional[constr(min_length=1, max_length=50)] = None,
    operation: Optional[constr(min_length=1, max_length=15)] = None,
    type: Optional[constr(min_length=1, max_length=15)] = None,
) -> Any:
    """
    Search against a source
    """
    return {}

from contextlib import asynccontextmanager
import os
import traceback
import sys

from azure.eventhub.aio import EventHubProducerClient


@asynccontextmanager
async def get_async_client():
    # Enable or disable Azure's own log tracing.
    client = None

    try:
        evhub_conn_str = os.environ["EVENT_HUB_CONN_STR"]
        evhub_name = os.environ["EVENT_HUB_NAME"]
        azure_enable_trace = "AZURE_ENABLE_TRACE" in os.environ
        client = EventHubProducerClient.from_connection_string(
            conn_str=evhub_conn_str,
            eventhub_name=evhub_name,
            logging_enable=azure_enable_trace,
        )
        yield client
    except Exception:
        print(traceback.format_exc(), file=sys.stderr)
    finally:
        await client.close()

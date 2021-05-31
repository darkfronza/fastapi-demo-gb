import os
import sys
import traceback

from azure.eventhub import EventHubProducerClient


class EventHubClient:
    '''
    Manages access to a single Event Hub client.
    '''
    client = None

    @staticmethod
    def get_client():
        if EventHubClient.client is None:
            # Enable or disable Azure's own log tracing.
            azure_enable_trace = "AZURE_ENABLE_TRACE" in os.environ

            try:
                evhub_conn_str = os.environ['EVENT_HUB_CONN_STR']
                evhub_name = os.environ['EVENT_HUB_NAME']
                EventHubClient.client = EventHubProducerClient.from_connection_string(
                        conn_str=evhub_conn_str,
                        eventhub_name=evhub_name,
                        logging_enable=azure_enable_trace)
            except Exception:
                print(traceback.format_exc(), file=sys.stderr)

        return EventHubClient.client

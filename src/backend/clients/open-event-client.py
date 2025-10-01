from src.backend.model.event_request import EventRequest


class OpenEventClient:
    """

    """
    BASE_URL = "https://api.eventyay.com/v1/"

    def __init__(self, llama_client, event_request):
        """
        Initializes new Event Service object
        :param llama_client: Llama client to prompt
        :param event_request: Object with user's preferences
        """
        self.llama_client = llama_client
        self.event_request = event_request

    def get_events_json(self, event_request: EventRequest):
        """
        Gets available events as a json matching its name to a description.
        :param event_request: User's event preferences
        :return: JSON of available events
        """


    def fetch_open_event(self, search_query):
        """
        Fetch events from Open Event (Open-source API) with given search query
        :return: Open Event JSON response
        """

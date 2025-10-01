class EventService:

    def __init__(self, event_request: EventRequest, api_clients: List):
        """
        Initializes event request from user and which APIs to fetch events from
        :param event_request: Event request object
        :param api_clients: List of APIs to fetch from
        """

    def fetch_events(self, event_request: EventRequest):
        """
        Fetches events from each API
        :param event_request: Event request object
        :return: A dict containing events
        """

    def prompt_llama_for_queries(self, vibe: str):
        """
        Prompts Llama (Open-source AI) to give a list of queries that best match the user's vibe

        :param vibe: User's vibe or current feeling to get a list of keywords back for
        :return: AI Response from Llama to use when fetching events.
        """

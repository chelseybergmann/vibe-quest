import unittest
from unittest.mock import MagicMock, patch
from datetime import date
from src.backend.model.event_request import EventRequest
from src.backend.clients.open_event_client import OpenEventClient

class TestOpenEventClient(unittest.TestCase):

    def setUp(self):
        self.mock_llama = MagicMock()
        self.mock_llama.get_search_queries.return_value = ["dinner", "concert", "couples retreat"]

        self.event_request = EventRequest(mood="something romantic", city="Los Angeles", event_date=date(2025, 10, 1))

        self.client = OpenEventClient(llama_client=self.mock_llama, event_request=self.event_request)

    @patch("src.backend.clients.open_event_client.requests.get")
    def test_fetch_open_event_returns_data(self, mock_get):
        """Test fetch_open_event returns the API response data correctly."""
        # Mock the API response
        mock_get.return_value.json.return_value = {
            "data": [
                {"attributes": {"name": "Concert", "description": "Fun concert", "city": "LA"}}
            ]
        }
        mock_get.return_value.raise_for_status = lambda: None

        result = self.client.fetch_open_event("happy music")
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["attributes"]["name"], "Concert")

        # Verify requests.get called with correct parameters
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn("happy music", kwargs["params"]["q"])
        self.assertEqual(kwargs["params"]["filter[location-name]"], "Los Angeles")

    @patch("src.backend.clients.open_event_client.requests.get")
    def test_get_events_json_returns_simplified_events(self, mock_get):
        """Test get_events_json orchestrates query generation and simplification correctly."""
        # Mock API response for both queries
        mock_get.return_value.json.return_value = {
            "data": [
                {"attributes": {"name": "Concert", "description": "Fun concert", "city": "LA"}}
            ]
        }
        mock_get.return_value.raise_for_status = lambda: None

        events = self.client.get_events_json(self.event_request)

        # Check simplified format
        self.assertIsInstance(events, list)
        self.assertEqual(events[0]["name"], "Concert")
        self.assertEqual(events[0]["city"], "LA")

        # Ensure LlamaClient was called
        self.mock_llama.get_search_queries.assert_called_once_with("happy")

    @patch("src.backend.clients.open_event_client.requests.get")
    def test_get_events_json_handles_multiple_queries(self, mock_get):
        """Ensure get_events_json handles multiple queries returned by LlamaClient."""
        # Return different mock data for each query
        def side_effect(*args, **kwargs):
            return MagicMock(
                json=MagicMock(return_value={
                    "data": [{"attributes": {"name": kwargs["params"]["q"], "description": "desc", "city": "LA"}}]
                }),
                raise_for_status=lambda: None
            )
        mock_get.side_effect = side_effect

        events = self.client.get_events_json(self.event_request)
        # Should return 2 events (for the 2 queries)
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["name"], "happy music")
        self.assertEqual(events[1]["name"], "happy art")

if __name__ == "__main__":
    unittest.main()
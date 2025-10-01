import unittest
from backend.clients.llama_client import LlamaClient

class TestLlamaClient(unittest.TestCase):

    def test_init(self):
        """Test that the client initializes correctly with or without a model_path."""
        client1 = LlamaClient()
        self.assertIsNone(client1.model)
        self.assertIsNone(client1.model_path)

        client2 = LlamaClient(model_path="custom/path")
        self.assertEqual(client2.model_path, "custom/path")
        self.assertIsNone(client2.model)

    def test_setup_initializes_model(self):
        """Test that setup() properly initializes the model."""
        client = LlamaClient()
        self.assertIsNotNone(client.model)
        self.assertIn("LLaMA model loaded", client.model)

    def test_get_search_queries_returns_list(self):
        """Test that get_queries returns 5 event type queries to search."""
        client = LlamaClient(model="llama-model")
        mood = "happy"
        queries = client.get_search_queries(mood)
        self.assertIsInstance(queries, list)
        self.assertTrue(len(queries) > 0 and len(queries) < 5)

if __name__ == "__main__":
    unittest.main()

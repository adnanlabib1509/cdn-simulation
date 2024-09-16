import unittest
from unittest.mock import Mock
from src.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.mock_edge_server1 = Mock()
        self.mock_edge_server2 = Mock()
        self.client = Client([self.mock_edge_server1, self.mock_edge_server2])

    def test_request_content(self):
        self.mock_edge_server1.get_content.return_value = ('Content', 'Cache HIT', 0.1)
        self.mock_edge_server2.get_content.return_value = ('Content', 'Cache MISS', 0.2)

        for _ in range(10):  # Run multiple times to test randomness
            server_name, cache_status, response_time, content = self.client.request_content('test-id')
            self.assertIn(server_name, [self.mock_edge_server1.name, self.mock_edge_server2.name])
            self.assertIn(cache_status, ['Cache HIT', 'Cache MISS'])
            self.assertIn(response_time, [0.1, 0.2])
            self.assertEqual(content, 'Content')
            
if __name__ == '__main__':
    unittest.main()
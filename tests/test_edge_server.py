import unittest
from unittest.mock import patch, Mock
from src.edge_server import EdgeServer

class TestEdgeServer(unittest.TestCase):
    def setUp(self):
        self.edge_server = EdgeServer("TestEdge", "http://testorigin.com", cache_size=2)

    @patch('requests.get')
    def test_get_content_cache_miss(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'content': 'Test Content'}
        mock_get.return_value = mock_response

        content, status, _ = self.edge_server.get_content('test-id')
        self.assertEqual(content, 'Test Content')
        self.assertEqual(status, 'Cache MISS')

    @patch('requests.get')
    def test_get_content_cache_hit(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'content': 'Test Content'}
        mock_get.return_value = mock_response

        self.edge_server.get_content('test-id')  # First call to cache the content
        content, status, _ = self.edge_server.get_content('test-id')  # Second call should be a cache hit
        self.assertEqual(content, 'Test Content')
        self.assertEqual(status, 'Cache HIT')

    def test_cache_eviction(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = [
                Mock(json=lambda: {'content': 'Content 1'}),
                Mock(json=lambda: {'content': 'Content 2'}),
                Mock(json=lambda: {'content': 'Content 3'})
            ]

            self.edge_server.get_content('id1')
            self.edge_server.get_content('id2')
            self.edge_server.get_content('id3')  # This should evict 'id1'

            # 'id1' should now be a cache miss
            content, status, _ = self.edge_server.get_content('id1')
            self.assertEqual(status, 'Cache MISS')
            
if __name__ == '__main__':
    unittest.main()
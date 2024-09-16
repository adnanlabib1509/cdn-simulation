import unittest
from unittest.mock import patch
from src.origin_server import OriginServer

class TestOriginServer(unittest.TestCase):
    def setUp(self):
        self.origin_server = OriginServer()

    @patch('src.origin_server.generate_content')
    def test_get_content(self, mock_generate_content):
        mock_generate_content.return_value = "Test Content"
        
        with self.origin_server.app.test_client() as client:
            response = client.get('/content/test-id')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"content": "Test Content"})
    
    def test_content_caching(self):
        with self.origin_server.app.test_client() as client:
            response1 = client.get('/content/test-id')
            content1 = response1.json['content']
            
            response2 = client.get('/content/test-id')
            content2 = response2.json['content']
            
            self.assertEqual(content1, content2)
            
if __name__ == '__main__':
    unittest.main()
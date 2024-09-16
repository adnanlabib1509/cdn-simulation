import random
import time

class Client:
    def __init__(self, edge_servers):
        self.edge_servers = edge_servers

    def request_content(self, content_id):
        edge_server = random.choice(self.edge_servers)
        content, cache_status, response_time = edge_server.get_content(content_id)
        return edge_server.name, cache_status, response_time, content
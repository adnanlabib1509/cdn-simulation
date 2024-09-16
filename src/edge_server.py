import requests
import time
from collections import OrderedDict

class EdgeServer:
    def __init__(self, name, origin_url, cache_size=5):
        self.name = name
        self.origin_url = origin_url
        self.cache = OrderedDict()
        self.cache_size = cache_size

    def get_content(self, content_id):
        start_time = time.time()
        if content_id in self.cache:
            content = self.cache[content_id]
            self.cache.move_to_end(content_id)
            return content, "Cache HIT", time.time() - start_time

        response = requests.get(f"{self.origin_url}/content/{content_id}")
        content = response.json()['content']
        
        if len(self.cache) >= self.cache_size:
            self.cache.popitem(last=False)
        self.cache[content_id] = content
        
        return content, "Cache MISS", time.time() - start_time
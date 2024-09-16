import threading
from src.origin_server import OriginServer
from src.edge_server import EdgeServer
from src.client import Client
import time
import random

def run_simulation(num_requests=100, num_edge_servers=3):
    origin_server = OriginServer()
    server_thread = threading.Thread(target=origin_server.run)
    server_thread.start()
    time.sleep(1)  # Give the server time to start

    edge_servers = [EdgeServer(f"EdgeServer-{i}", "http://localhost:5000") for i in range(num_edge_servers)]
    client = Client(edge_servers)

    total_time = 0
    cache_hits = 0
    cache_misses = 0

    for i in range(num_requests):
        content_id = f"content-{random.randint(1, 10)}"
        server_name, cache_status, response_time, _ = client.request_content(content_id)
        total_time += response_time
        if cache_status == "Cache HIT":
            cache_hits += 1
        else:
            cache_misses += 1
        print(f"Request {i+1}: Served by {server_name}, {cache_status}, Time: {response_time:.4f}s")

    print(f"\nSimulation Complete:")
    print(f"Total Requests: {num_requests}")
    print(f"Cache Hits: {cache_hits}")
    print(f"Cache Misses: {cache_misses}")
    print(f"Average Response Time: {total_time/num_requests:.4f}s")

    # Gracefully shut down the Flask server
    import requests
    try:
        requests.get("http://localhost:5000/shutdown")
    except:
        pass
    server_thread.join(timeout=1)

if __name__ == '__main__':
    run_simulation()
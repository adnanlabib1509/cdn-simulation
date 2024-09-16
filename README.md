# Advanced CDN Simulation Project

This project simulates a Content Delivery Network (CDN) to demonstrate key CDN principles and functionalities. It includes an origin server, multiple edge servers, and client simulations to showcase content caching, distribution, and delivery optimization.

## Project Structure

```
cdn_simulation/
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── origin_server.py
│   ├── edge_server.py
│   ├── client.py
│   └── content_generator.py
└── tests/
    ├── __init__.py
    ├── test_origin_server.py
    ├── test_edge_server.py
    └── test_client.py
```

## Features

1. **Origin Server**: Simulates the main content source with artificial delay.
2. **Edge Servers**: Implement caching mechanism with LRU (Least Recently Used) eviction policy.
3. **Client Simulator**: Generates requests to random edge servers.
4. **Content Generation**: Dynamically creates unique content for each request.
5. **Performance Metrics**: Tracks cache hits/misses and response times.
6. **Scalability**: Supports multiple edge servers and concurrent requests.

## How It Works

1. The Origin Server generates and stores content upon first request.
2. Edge Servers cache content from the Origin Server and serve subsequent requests for the same content.
3. Clients send requests to random Edge Servers.
4. The simulation tracks performance metrics like cache hit rate and response times.

## CDN Principles Demonstrated

1. **Content Caching**: Edge servers store frequently accessed content to reduce origin server load.
2. **Distributed Content Delivery**: Multiple edge servers simulate geographically distributed CDN nodes.
3. **Origin Offloading**: Cached content reduces requests to the origin server.
4. **Latency Reduction**: Cached content is served faster than fetching from the origin.
5. **Cache Eviction**: LRU policy demonstrates how CDNs manage limited cache space.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cdn-simulation.git
   cd cdn-simulation
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Simulation

To run the main simulation:

```
python main.py
```

This will start the simulation with default parameters. You can modify the `main.py` file to adjust the number of requests, edge servers, or other parameters.

## Running Tests

This project includes unit tests to ensure the correct functionality of the Origin Server, Edge Servers, and Client.

### Running All Tests

To run all tests:

```
python -m unittest discover tests
```

This command will discover and run all the tests in the `tests` directory.

### Running Individual Test Files

You can also run each test file individually:

```
python tests/test_origin_server.py
python tests/test_edge_server.py
python tests/test_client.py
```

## Test Coverage

The tests cover the following aspects:

1. **Origin Server Tests**:
   - Verify that content is generated and returned correctly
   - Ensure content is cached after the first request

2. **Edge Server Tests**:
   - Test cache miss scenario
   - Test cache hit scenario
   - Verify correct implementation of cache eviction policy

3. **Client Tests**:
   - Ensure random selection of edge servers
   - Verify correct handling of responses from edge servers

These tests demonstrate the robustness of the simulation and provide confidence in its correct implementation of CDN principles.

## Extending the Project

Here are some ideas for extending the project:

- Implement geographic-based routing for edge server selection.
- Add content expiration and cache invalidation mechanisms.
- Introduce bandwidth simulation and throttling.
- Implement load balancing among edge servers.
- Add visualization of request flow and server locations.

## License

This project is open source and available under the [MIT License](LICENSE).
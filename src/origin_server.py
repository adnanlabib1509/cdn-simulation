from flask import Flask, jsonify
import time
from .content_generator import generate_content

class OriginServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.content = {}
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/content/<content_id>') 
        def get_content(content_id):
            if content_id not in self.content:
                self.content[content_id] = generate_content()
            time.sleep(0.1)  # Simulate processing time
            return jsonify({"content": self.content[content_id]})

    def run(self):
        self.app.run(port=5000)
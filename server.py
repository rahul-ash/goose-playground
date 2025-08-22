#!/usr/bin/env python3
"""
Simple HTTP Server Application

This server listens on port 8080 and handles GET and POST requests,
responding with JSON data including welcome messages and timestamps.
"""

import json
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_json_response(self, data, status_code=200):
        """Send a JSON response with proper headers."""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        response_data = {
            'message': 'Welcome to the Simple HTTP Server!',
            'method': 'GET',
            'timestamp': datetime.datetime.now().isoformat(),
            'path': parsed_path.path,
            'query_params': query_params
        }
        
        self._send_json_response(response_data)
        print(f"GET request received: {self.path}")

    def do_POST(self):
        """Handle POST requests."""
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        try:
            parsed_data = json.loads(post_data) if post_data else {}
        except json.JSONDecodeError:
            parsed_data = {'raw_data': post_data}
        
        response_data = {
            'message': 'POST request received successfully!',
            'method': 'POST',
            'timestamp': datetime.datetime.now().isoformat(),
            'received_data': parsed_data
        }
        
        self._send_json_response(response_data)
        print(f"POST request received with data: {post_data}")

    def log_message(self, format, *args):
        """Override to customize logging."""
        return


def run_server(port=8080):
    """Start the HTTP server on the specified port."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print(f"Starting HTTP server on port {port}...")
    print(f"Server running at http://localhost:{port}/")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("
        httpd.server_close()


if __name__ == '__main__':
    run_server()



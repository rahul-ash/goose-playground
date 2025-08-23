#!/usr/bin/env python3
"""
Simple HTTP Client Application

This client connects to the HTTP server, sends both GET and POST requests,
and displays the server responses in a user-friendly format.
"""

import json
import requests
import sys
from datetime import datetime


class SimpleHTTPClient:
    def __init__(self, server_url='http://localhost:8080'):
        """Initialize the client with server URL."""
        self.server_url = server_url
        self.session = requests.Session()
    
    def send_get_request(self, path='/', params=None):
        """Send a GET request to the server."""
        url = f"{self.server_url}{path}"
        
        print(f"\n🔄 Sending GET request to: {url}")
        if params:
            print(f"📋 Query parameters: {params}")
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            print(f"✅ Response Status: {response.status_code}")
            print(f"📄 Response Headers: {dict(response.headers)}")
            
            # Parse and display JSON response
            json_data = response.json()
            print(f"📦 Response Data:")
            print(json.dumps(json_data, indent=2))
            
            return json_data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ GET request failed: {e}")
            return None
    
    def send_post_request(self, path='/', data=None):
        """Send a POST request to the server."""
        url = f"{self.server_url}{path}"
        
        print(f"\n🔄 Sending POST request to: {url}")
        if data:
            print(f"📋 POST data: {data}")
        
        try:
            headers = {'Content-Type': 'application/json'}
            json_data = json.dumps(data) if data else '{}'
            
            response = self.session.post(url, data=json_data, headers=headers, timeout=10)
            response.raise_for_status()
            
            print(f"✅ Response Status: {response.status_code}")
            print(f"📄 Response Headers: {dict(response.headers)}")
            
            # Parse and display JSON response
            response_data = response.json()
            print(f"📦 Response Data:")
            print(json.dumps(response_data, indent=2))
            
            return response_data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ POST request failed: {e}")
            return None
    
    def run_demo(self):
        """Run a demonstration of client-server communication."""
        print("🚀 Starting HTTP Client Demo")
        print(f"🎯 Target Server: {self.server_url}")
        print("=" * 50)
        
        # Test 1: Simple GET request
        print("\n📋 Test 1: Simple GET request")
        self.send_get_request()
        
        # Test 2: GET request with query parameters
        print("\n📋 Test 2: GET request with query parameters")
        params = {
            'name': 'TestClient',
            'version': '1.0',
            'timestamp': datetime.now().isoformat()
        }
        self.send_get_request('/api/test', params)
        
        # Test 3: Simple POST request
        print("\n📋 Test 3: Simple POST request")
        post_data = {
            'client_name': 'SimpleHTTPClient',
            'message': 'Hello from the client!',
            'timestamp': datetime.now().isoformat(),
            'test_data': {
                'numbers': [1, 2, 3, 4, 5],
                'boolean': True,
                'nested': {'key': 'value'}
            }
        }
        self.send_post_request('/api/data', post_data)
        
        # Test 4: POST request with different data
        print("\n📋 Test 4: POST request with user data")
        user_data = {
            'user_id': 12345,
            'username': 'demo_user',
            'email': 'demo@example.com',
            'preferences': {
                'theme': 'dark',
                'notifications': True,
                'language': 'en'
            }
        }
        self.send_post_request('/api/user', user_data)
        
        print("\n" + "=" * 50)
        print("✅ Client demo completed successfully!")


def check_server_availability(server_url):
    """Check if the server is running and accessible."""
    try:
        response = requests.get(server_url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def main():
    """Main function to run the client application."""
    server_url = 'http://localhost:8080'
    
    # Check if server is running
    print("🔍 Checking server availability...")
    if not check_server_availability(server_url):
        print(f"❌ Server is not running at {server_url}")
        print("💡 Please start the server first by running: python3 server.py")
        sys.exit(1)
    
    print(f"✅ Server is running at {server_url}")
    
    # Create and run client
    client = SimpleHTTPClient(server_url)
    client.run_demo()


if __name__ == '__main__':
    main()

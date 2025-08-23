# Simple HTTP Client-Server Application

A demonstration of HTTP client-server communication using Python. This project consists of a simple HTTP server that handles GET and POST requests, and a client application that connects to the server to demonstrate various types of HTTP requests.

## Features

### Server (`server.py`)
- **HTTP Server**: Listens on port 8080
- **GET Requests**: Handles GET requests with query parameter support
- **POST Requests**: Handles POST requests with JSON data parsing
- **JSON Responses**: All responses are in JSON format with timestamps
- **CORS Support**: Includes Cross-Origin Resource Sharing headers
- **Error Handling**: Graceful handling of malformed JSON data

### Client (`client.py`)
- **HTTP Client**: Connects to the server using the `requests` library
- **GET Requests**: Sends GET requests with optional query parameters
- **POST Requests**: Sends POST requests with JSON data
- **User-Friendly Output**: Displays responses with emojis and formatted JSON
- **Server Availability Check**: Verifies server is running before making requests
- **Comprehensive Demo**: Includes multiple test scenarios

## Requirements

- **Python 3.7+**: Both applications require Python 3.7 or higher
- **requests library**: Required for the client application

### Installing Dependencies

The server uses only Python standard library modules, so no additional dependencies are needed.

For the client, install the `requests` library:

```bash
pip install requests
```

## Usage

### Running the Server

1. **Start the server**:
   ```bash
   python3 server.py
   ```

2. **Expected output**:
   ```
   🚀 Starting HTTP Server...
   📡 Server running on http://localhost:8080
   🔄 Press Ctrl+C to stop the server
   ```

3. **Server endpoints**:
   - **Root endpoint**: `GET http://localhost:8080/`
   - **Any path**: `GET/POST http://localhost:8080/any/path`
   - **Query parameters**: `GET http://localhost:8080/?param1=value1&param2=value2`

### Running the Client

1. **Ensure the server is running** (see above)

2. **Start the client**:
   ```bash
   python3 client.py
   ```

3. **Expected output**:
   ```
   🌐 Simple HTTP Client Demo
   🎯 Target Server: http://localhost:8080
   
   📋 Test 1: Simple GET request
   🔄 Sending GET request to: http://localhost:8080/
   ✅ Response Status: 200 OK
   📦 Response Data:
   {
     "message": "Welcome to the Simple HTTP Server!",
     "method": "GET",
     "timestamp": "2024-01-15 10:30:45",
     "path": "/",
     "query_params": {}
   }
   
   📋 Test 2: GET request with query parameters
   🔄 Sending GET request to: http://localhost:8080/api/test?name=Alice&age=25&city=New+York
   ✅ Response Status: 200 OK
   📦 Response Data:
   {
     "message": "Welcome to the Simple HTTP Server!",
     "method": "GET",
     "timestamp": "2024-01-15 10:30:45",
     "path": "/api/test",
     "query_params": {
       "name": "Alice",
       "age": "25",
       "city": "New York"
     }
   }
   
   📋 Test 3: Simple POST request
   🔄 Sending POST request to: http://localhost:8080/api/data
   📋 POST data: {'action': 'create', 'item': 'document', 'properties': {'title': 'My Document', 'content': 'This is a sample document', 'tags': ['sample', 'demo', 'test']}}
   ✅ Response Status: 200 OK
   📦 Response Data:
   {
     "message": "POST request received successfully!",
     "method": "POST",
     "timestamp": "2024-01-15 10:30:45",
     "received_data": {
       "action": "create",
       "item": "document",
       "properties": {
         "title": "My Document",
         "content": "This is a sample document",
         "tags": ["sample", "demo", "test"]
       }
     }
   }
   
   📋 Test 4: POST request with user data
   🔄 Sending POST request to: http://localhost:8080/api/user
   📋 POST data: {'user_id': 12345, 'username': 'john_doe', 'email': 'john@example.com', 'profile': {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'preferences': {'theme': 'dark', 'notifications': True}}}
   ✅ Response Status: 200 OK
   📦 Response Data:
   {
     "message": "POST request received successfully!",
     "method": "POST",
     "timestamp": "2024-01-15 10:30:45",
     "received_data": {
       "user_id": 12345,
       "username": "john_doe",
       "email": "john@example.com",
       "profile": {
         "first_name": "John",
         "last_name": "Doe",
         "age": 30,
         "preferences": {
           "theme": "dark",
           "notifications": true
         }
       }
     }
   }
   
   ✅ Demo completed successfully!
   ```

## Manual Testing

You can also test the server manually using curl or any HTTP client:

### GET Request Examples

```bash
# Simple GET request
curl http://localhost:8080/

# GET request with query parameters
curl "http://localhost:8080/api/test?name=Alice&age=25"

# GET request to custom path
curl http://localhost:8080/custom/path
```

### POST Request Examples

```bash
# Simple POST request with JSON data
curl -X POST http://localhost:8080/api/data \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello Server", "data": [1, 2, 3]}'

# POST request with form data
curl -X POST http://localhost:8080/api/form \
  -d "name=John&email=john@example.com"
```

## Troubleshooting

### Common Issues

1. **"Connection refused" error**:
   - Make sure the server is running before starting the client
   - Check that port 8080 is not being used by another application

2. **"Module 'requests' not found" error**:
   - Install the requests library: `pip install requests`

3. **"Permission denied" on port 8080**:
   - Try using a different port by modifying the `PORT` variable in `server.py`
   - On some systems, ports below 1024 require administrator privileges

4. **Server not stopping gracefully**:
   - Use `Ctrl+C` to stop the server
   - If the server doesn't stop, use `Ctrl+Z` followed by `kill %1`

## File Structure

```

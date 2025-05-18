# Potholes Service

A service for reporting and tracking potholes with both REST and SOAP APIs.

## Requirements

- Docker
- jq (for formatting JSON in test scripts)
- xmllint (for formatting XML in test scripts)

## Running the Service

```bash
# Build and run with Docker
docker build -t pothole-tracker .
docker run -p 8000:8000 -p 8001:8001 pothole-tracker
```

## API Endpoints

### REST API
- Base URL: http://localhost:8000/api
- Documentation: http://localhost:8000/api/swagger-ui/

### SOAP API
- Endpoint: http://localhost:8001/
- WSDL: http://localhost:8001/?wsdl

## Test Scripts

Shell scripts are provided in the `tests` directory for testing both APIs:

```bash
# Test REST API
./tests/test_rest_api.sh [command]

# Test SOAP API
./tests/test_soap_api.sh [command]
```

Both scripts have the following commands:
- `create_user` - Create a new user
- `get_users` - Get all users
- `create_pothole` - Create a new pothole report  
- `get_potholes` - Get all potholes
- `get_swagger` - Open the API documentation in browser

## Dependencies

The service uses the following fixed dependency versions for compatibility:
- Flask 2.0.1
- Werkzeug 2.0.2
- marshmallow 3.19.0
- flask-apispec 0.11.0

## Dependencies Installation

```bash
# Install Docker
sudo apt-get update
sudo apt-get install docker.io

# Install jq for JSON formatting
sudo apt-get install jq

# Install libxml2-utils for xmllint
sudo apt-get install libxml2-utils
``` 
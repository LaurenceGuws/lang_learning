#!/bin/bash

# Test script for REST API of Potholes Service

HOST="localhost:8000/api"

# Function to display usage
usage() {
    echo "REST API Test Script for Potholes Service"
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  create_user      - Create a new user"
    echo "  get_users        - Get all users"
    echo "  create_pothole   - Create a new pothole report"
    echo "  get_potholes     - Get all potholes"
    echo "  get_swagger      - Open the Swagger UI in browser"
    echo ""
}

# Create a user via REST
create_user() {
    echo "Creating a user via REST API..."
    curl -s -X POST -H "Content-Type: application/json" \
         -d '{"name": "REST Test User", "email": "resttest@example.com", "role": "citizen"}' \
         http://$HOST/users | jq .
}

# Get all users via REST
get_users() {
    echo "Fetching all users via REST API..."
    curl -s http://$HOST/users | jq .
}

# Create a pothole via REST
create_pothole() {
    echo "Creating a pothole via REST API..."
    curl -s -X POST -H "Content-Type: application/json" \
         -d '{
             "street_name": "REST Test Street",
             "reported_by": 1,
             "latitude": 40.7128,
             "longitude": -74.0060,
             "diameter_cm": 30,
             "description": "Test pothole created via REST"
          }' \
         http://$HOST/potholes | jq .
}

# Get all potholes via REST
get_potholes() {
    echo "Fetching all potholes via REST API..."
    curl -s http://$HOST/potholes | jq .
}

# Open Swagger UI in browser
get_swagger() {
    echo "Opening Swagger UI in browser..."
    xdg-open http://$HOST/swagger-ui/ 2>/dev/null || \
    open http://$HOST/swagger-ui/ 2>/dev/null || \
    echo "Could not open browser. Visit http://$HOST/swagger-ui/ manually."
}

# Process command line arguments
if [ $# -eq 0 ]; then
    usage
    exit 1
fi

case "$1" in
    create_user)
        create_user
        ;;
    get_users)
        get_users
        ;;
    create_pothole)
        create_pothole
        ;;
    get_potholes)
        get_potholes
        ;;
    get_swagger)
        get_swagger
        ;;
    *)
        echo "Unknown command: $1"
        usage
        exit 1
        ;;
esac 
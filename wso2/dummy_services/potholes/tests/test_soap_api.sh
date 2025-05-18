#!/bin/bash

# Test script for SOAP API of Potholes Service

HOST="localhost:8001"

# Function to display usage
usage() {
    echo "SOAP API Test Script for Potholes Service"
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  create_user      - Create a new user"
    echo "  get_users        - Get all users"
    echo "  create_pothole   - Create a new pothole report"
    echo "  get_potholes     - Get all potholes"
    echo "  get_swagger      - Open the SOAP WSDL in browser"
    echo ""
}

# Create a user via SOAP
create_user() {
    echo "Creating a user via SOAP API..."
    curl -s -X POST -H "Content-Type: text/xml" -d '
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="http://pothole.tracker.service">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:create_user>
                <urn:name>SOAP Test User</urn:name>
                <urn:email>soaptest@example.com</urn:email>
                <urn:role>admin</urn:role>
            </urn:create_user>
        </soapenv:Body>
    </soapenv:Envelope>' http://$HOST/ | xmllint --format -
}

# Get all users via SOAP
get_users() {
    echo "Fetching all users via SOAP API..."
    curl -s -X POST -H "Content-Type: text/xml" -d '
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="http://pothole.tracker.service">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:get_all_users/>
        </soapenv:Body>
    </soapenv:Envelope>' http://$HOST/ | xmllint --format -
}

# Create a pothole via SOAP
create_pothole() {
    echo "Creating a pothole via SOAP API..."
    curl -s -X POST -H "Content-Type: text/xml" -d '
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="http://pothole.tracker.service">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:create_pothole>
                <urn:street_name>SOAP Test Street</urn:street_name>
                <urn:reported_by>1</urn:reported_by>
                <urn:latitude>40.7128</urn:latitude>
                <urn:longitude>-74.0060</urn:longitude>
                <urn:diameter_cm>25.5</urn:diameter_cm>
                <urn:description>Test pothole created via SOAP</urn:description>
            </urn:create_pothole>
        </soapenv:Body>
    </soapenv:Envelope>' http://$HOST/ | xmllint --format -
}

# Get all potholes via SOAP
get_potholes() {
    echo "Fetching all potholes via SOAP API..."
    curl -s -X POST -H "Content-Type: text/xml" -d '
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="http://pothole.tracker.service">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:get_all_potholes/>
        </soapenv:Body>
    </soapenv:Envelope>' http://$HOST/ | xmllint --format -
}

# Open WSDL in browser
get_swagger() {
    echo "Opening SOAP WSDL in browser..."
    xdg-open http://$HOST/?wsdl 2>/dev/null || \
    open http://$HOST/?wsdl 2>/dev/null || \
    echo "Could not open browser. Visit http://$HOST/?wsdl manually."
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
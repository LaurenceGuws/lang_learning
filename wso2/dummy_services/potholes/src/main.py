import argparse
import threading
from wsgiref.simple_server import make_server
import logging
import os
import sys

# Add the current directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Apply spyne patch before importing soap
from soap_patch import apply_patch
apply_patch()

# Apply flask_apispec patch before importing openapi
from flask_apispec_patch import apply_patch as apply_flask_apispec_patch
apply_flask_apispec_patch()

# Import REST and SOAP apps
from rest import app as rest_app
import soap
import openapi  # Import the OpenAPI documentation module

def run_rest_server(host, port):
    """Run the REST API server."""
    logger.info(f"Starting REST server on http://{host}:{port}")
    rest_app.run(host=host, port=port, debug=False)

def run_soap_server(host, port):
    """Run the SOAP API server."""
    logger.info(f"Starting SOAP server on http://{host}:{port}")
    soap_app = soap.get_wsgi_application()
    server = make_server(host, port, soap_app)
    server.serve_forever()

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Pothole Tracker Service')
    parser.add_argument('--rest-host', default='0.0.0.0', help='REST API host')
    parser.add_argument('--rest-port', type=int, default=8000, help='REST API port')
    parser.add_argument('--soap-host', default='0.0.0.0', help='SOAP API host')
    parser.add_argument('--soap-port', type=int, default=8001, help='SOAP API port')
    args = parser.parse_args()

    # Print welcome message
    logger.info("Starting Pothole Tracker Service")
    logger.info(f"REST API will be available at: http://{args.rest_host}:{args.rest_port}/api")
    logger.info(f"REST API Documentation: http://{args.rest_host}:{args.rest_port}/api/swagger-ui/")
    logger.info(f"SOAP API will be available at: http://{args.soap_host}:{args.soap_port}")
    logger.info(f"SOAP WSDL will be available at: http://{args.soap_host}:{args.soap_port}/?wsdl")
    
    # Check if database exists, if not run the initialization script
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db", "pothole.db")
    if not os.path.exists(db_path):
        logger.info("Database not found, initializing...")
        init_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db", "init.sh")
        current_dir = os.getcwd()
        # Move to the db directory to run the script
        os.chdir(os.path.dirname(init_script))
        os.system("bash init.sh")
        os.chdir(current_dir)
        logger.info("Database initialized successfully.")

    # Start the REST and SOAP servers in separate threads
    soap_thread = threading.Thread(
        target=run_soap_server,
        args=(args.soap_host, args.soap_port),
        daemon=True
    )
    
    rest_thread = threading.Thread(
        target=run_rest_server,
        args=(args.rest_host, args.rest_port),
        daemon=True
    )
    
    soap_thread.start()
    rest_thread.start()
    
    # Keep the main thread alive to handle keyboard interrupts
    try:
        while True:
            soap_thread.join(1)
            rest_thread.join(1)
    except KeyboardInterrupt:
        logger.info("Shutting down servers...")

if __name__ == "__main__":
    main()

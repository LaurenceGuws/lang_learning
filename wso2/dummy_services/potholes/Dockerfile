FROM python:3.10-slim

WORKDIR /app

# Install sqlite3 command-line tool
RUN apt-get update && apt-get install -y sqlite3 && apt-get clean

# Copy requirements first to leverage Docker caching
COPY requirements.txt .
# Install dependencies with specific versions for compatibility
# Flask 2.0.1, marshmallow 3.19.0, flask-apispec 0.11.0, and werkzeug 2.0.2 are pinned for compatibility
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ /app/src/
COPY db/ /app/db/

# Create required directories and set permissions
RUN mkdir -p /app/data && \
    chmod +x /app/db/init.sh


# Expose the REST and SOAP API ports
EXPOSE 8000 8001

# Apply any necessary initialization
RUN cd /app/db && ./init.sh

# Start the application
CMD ["python", "src/main.py"] 
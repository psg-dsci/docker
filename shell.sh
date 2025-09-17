#!/bin/bash
set -euo pipefail

# Build with both a unique and a 'latest' tag
docker build -t flask-app .
# Clean up any existing container
docker rm -f flask-app >/dev/null 2>&1 || true
# Run the new container
docker run -d --name flask-app -p 6000:5000 flask-app

echo "Done"

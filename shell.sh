#!/bin/bash
set -euo pipefail

# Build with both a unique and a 'latest' tag
docker build -t flask-app .
# Clean up any existing container
docker rm -f flask-app >/dev/null 2>&1 || true
# Run the new container
docker run -d --name flask-app -p 5000:5000 flask-app

for i in {1..30}; do
  if curl -fsS http://localhost:5000/ >/dev/null; then
    echo "App is healthy"
    break
  fi
  sleep 1
done

echo "Done"

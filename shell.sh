#!/bin/bash
set -euo pipefail

APP_NAME="flask-app"
REGISTRY="local"

IMAGE_TAG="${REGISTRY}/${APP_NAME}:${SHORT_SHA}"
IMAGE_LATEST="${REGISTRY}/${APP_NAME}:latest"

# Build with both a unique and a 'latest' tag
docker build -t "${IMAGE_TAG}" -t "${IMAGE_LATEST}" .
# Clean up any existing container
docker rm -f "${APP_NAME}" >/dev/null 2>&1 || true
# Run the new container
docker run -d --name "${APP_NAME}" -p 5000:5000 "${IMAGE_TAG}"
# Simple health wait + check (up to ~30s)
for i in {1..30}; do
  if curl -fsS http://localhost:5000/ >/dev/null; then
    echo "App is healthy"
    break
  fi
  sleep 1
done
curl -fsS http://localhost:5000/ >/dev/null || { echo "App not healthy"; exit 1; }

echo "Done: ${IMAGE_TAG}"

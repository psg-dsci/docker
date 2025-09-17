#!/bin/bash
set -euo pipefail
docker build -t flask-app .
docker rm -f flask-app >/dev/null 2>&1 || true
docker run -d --name flask-app -p 7000:5000 flask-app
echo "Done"

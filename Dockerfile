FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first for better caching
COPY requirements.txt .

# Install system dependencies (if you need DNS tools during dev)
RUN apt-get update && apt-get install -y --no-install-recommends bind9-dnsutils && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Environment variables for development
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Use flask run for hot reloading in dev
CMD ["flask", "run"]

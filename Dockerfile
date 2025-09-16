# Use an official Python runtime as a parent image
FROM python:3.10-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install Flask
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 8000 for Flask
ENV_PORT=8000
EXPOSE 8000
# Run app.py when the container launches
CMD ["gunicorn","-b", "0.0.0.0:8000", "app.app"]

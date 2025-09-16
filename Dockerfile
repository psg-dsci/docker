# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port 5000 for Flask
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

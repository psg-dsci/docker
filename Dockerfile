FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=5000
EXPOSE 5000

# Replace "app:app" with your module and Flask app name
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

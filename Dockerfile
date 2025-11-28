# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variable for port

# Create tables, then start the app with Gunicorn on port 8080
CMD python create_tables.py && gunicorn app:app --bind 0.0.0.0:8080

# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (Render sets $PORT automatically)
EXPOSE $PORT

# Run Gunicorn server with Flask app
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:${PORT}", "app:app"]

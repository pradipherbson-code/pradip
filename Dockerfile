# Full-Stack OmniStream Media Downloader Dockerfile
FROM python:3.12-slim

# Install system dependencies including FFmpeg and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables
ENV PORT=5000
ENV HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# Run uvicorn server
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "5000"]

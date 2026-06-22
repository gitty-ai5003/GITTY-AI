FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (including git for repository loading)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY apps/worker/requirements.txt ./apps/worker/requirements.txt
RUN pip install --no-cache-dir -r apps/worker/requirements.txt

# Copy source and libraries
COPY libs/ ./libs/
COPY services/ ./services/
COPY apps/worker/ ./apps/worker/

# Install local libs
RUN pip install -e ./libs/config -e ./libs/logging -e ./libs/exceptions -e ./libs/models -e ./libs/graph -e ./libs/ai -e ./libs/events || true

ENV PYTHONPATH=/app

CMD ["celery", "-A", "apps.worker.worker_app", "worker", "--loglevel=info"]

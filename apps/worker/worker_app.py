from celery import Celery
from libs.config import get_settings
from libs.logging import configure_logging, get_logger

settings = get_settings()
configure_logging(settings.ENV)
logger = get_logger("worker")

# Configure Celery
broker_url = f"amqp://guest:guest@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//"
result_backend = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"

app = Celery(
    "gitty-worker",
    broker=broker_url,
    backend=result_backend
)

app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

@app.task(name="gitty.tasks.health_check")
def worker_health_check():
    logger.info("Executing worker health check task")
    return {"status": "ok", "worker": "gitty-worker"}

@app.task(name="gitty.tasks.index_repository")
def index_repository(repository_id: str, repo_url: str):
    logger.info("Starting repository indexing task", repository_id=repository_id, url=repo_url)
    # Placeholder for Phase 3 ingestion
    return {"status": "indexed", "repository_id": repository_id}

@app.task(name="gitty.tasks.generate_embeddings")
def generate_embeddings(repository_id: str):
    logger.info("Starting embeddings generation task", repository_id=repository_id)
    # Placeholder for Phase 5 embedding
    return {"status": "completed", "repository_id": repository_id}

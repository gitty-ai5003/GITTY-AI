import redis
import pika
from qdrant_client import QdrantClient
from neo4j import GraphDatabase
from libs.logging import get_logger

logger = get_logger(__name__)

class ConnectionChecker:
    def __init__(
        self,
        redis_host: str,
        redis_port: int,
        rabbitmq_host: str,
        rabbitmq_port: int,
        neo4j_uri: str,
        neo4j_user: str,
        neo4j_password: str,
        qdrant_host: str,
        qdrant_port: int,
        graph_mode: str = "sqlite"
    ):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.rabbitmq_host = rabbitmq_host
        self.rabbitmq_port = rabbitmq_port
        self.neo4j_uri = neo4j_uri
        self.neo4j_user = neo4j_user
        self.neo4j_password = neo4j_password
        self.qdrant_host = qdrant_host
        self.qdrant_port = qdrant_port
        self.graph_mode = graph_mode

    def check_redis(self) -> str:
        try:
            r = redis.Redis(host=self.redis_host, port=self.redis_port, socket_timeout=2.0)
            r.ping()
            return "healthy"
        except Exception as e:
            logger.error("Redis health check failed", error=str(e))
            return f"unhealthy: {str(e)}"

    def check_rabbitmq(self) -> str:
        try:
            parameters = pika.ConnectionParameters(
                host=self.rabbitmq_host,
                port=self.rabbitmq_port,
                connection_attempts=1,
                retry_delay=1
            )
            connection = pika.BlockingConnection(parameters)
            if connection.is_open:
                connection.close()
                return "healthy"
            return "unhealthy"
        except Exception as e:
            logger.error("RabbitMQ health check failed", error=str(e))
            return f"unhealthy: {str(e)}"

    def check_neo4j(self) -> str:
        if self.graph_mode.lower() == "sqlite":
            return "skipped (using sqlite graph mode)"
        try:
            with GraphDatabase.driver(
                self.neo4j_uri,
                auth=(self.neo4j_user, self.neo4j_password),
                connection_timeout=2.0
            ) as driver:
                driver.verify_connectivity()
            return "healthy"
        except Exception as e:
            logger.error("Neo4j health check failed", error=str(e))
            return f"unhealthy: {str(e)}"

    def check_qdrant(self) -> str:
        try:
            client = QdrantClient(host=self.qdrant_host, port=self.qdrant_port, timeout=2.0)
            # Try to query collections as a ping
            client.get_collections()
            return "healthy"
        except Exception as e:
            logger.error("Qdrant health check failed", error=str(e))
            return f"unhealthy: {str(e)}"

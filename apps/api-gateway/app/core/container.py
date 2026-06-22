from dependency_injector import containers, providers
from .config import settings
from .providers import ConnectionChecker

class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Core Providers
    connection_checker = providers.Singleton(
        ConnectionChecker,
        redis_host=config.REDIS_HOST,
        redis_port=config.REDIS_PORT,
        rabbitmq_host=config.RABBITMQ_HOST,
        rabbitmq_port=config.RABBITMQ_PORT,
        neo4j_uri=config.NEO4J_URI,
        neo4j_user=config.NEO4J_USER,
        neo4j_password=config.NEO4J_PASSWORD,
        qdrant_host=config.QDRANT_HOST,
        qdrant_port=config.QDRANT_PORT,
        graph_mode=config.GRAPH_MODE
    )

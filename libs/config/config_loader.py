from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class SystemSettings(BaseSettings):
    ENV: str = "development"
    
    # Cache / Session Store
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # Queue
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672

    # Graph modes & Neo4j
    GRAPH_MODE: str = "sqlite" # "sqlite" or "neo4j"
    SQLITE_DB_PATH: str = "gitty_graph.db"
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "gitty_password"

    # Vector store
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    # LLM Settings
    OPENAI_API_KEY: Optional[str] = None
    GEMINI_API_KEY: Optional[str] = None
    CLAUDE_API_KEY: Optional[str] = None
    OLLAMA_URI: str = "http://localhost:11434"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

_settings: Optional[SystemSettings] = None

def get_settings() -> SystemSettings:
    global _settings
    if _settings is None:
        _settings = SystemSettings()
    return _settings

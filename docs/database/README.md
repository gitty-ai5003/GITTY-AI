# Database Design & Schemas

Gitty AI supports two primary graph storage modes:

- **SQLite Graph Storage (Default)**: Used for local, lightweight installations.
- **Neo4j Enterprise mode (Optional)**: Used for enterprise deployments.

Vector indexes are maintained in **Qdrant** for semantic retrieval.
PostgreSQL/Alembic manages system parameters, repositories index status, and security scan logs.

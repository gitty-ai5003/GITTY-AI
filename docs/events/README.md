# Event Broker & Message Schemas

Gitty AI uses RabbitMQ as the central asynchronous message broker.

## Versioned Event Specifications

Refer to `libs/events/schemas.py` for exact schemas:
- **RepositoryIndexedV1**: Fired upon file ingestion scanning success.
- **GraphBuiltV1**: Fired when nodes/edges are updated.
- **EmbeddingCreatedV1**: Fired when chunks vectors are updated.
- **DeadCodeDetectedV1**: Fired upon structural analysis complete.
- **VulnerabilityFoundV1**: Fired on dependency scanner findings.

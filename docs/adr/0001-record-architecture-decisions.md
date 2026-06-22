# ADR 0001: Record Architecture Decisions

- **Status**: Accepted
- **Date**: 2026-06-22
- **Authors**: Principal Software Architect & Staff Engineer

## Context and Problem

Gitty AI is building a highly-scalable, production-grade, self-hostable AI-powered Repository Knowledge Graph Platform. The design calls for structural repository scanning, AST parsing, AI semantic inference, and search engines running concurrently. We need to define a clean codebase structure that enforces SOLID principles, clean hexagonal domain boundaries, robust service orchestration, and decouples identity/security systems from core data extraction algorithms.

## Decision

We adopt a **Clean Architecture, Domain-Driven Design (DDD), Hexagonal, and Monorepo** structure.

1. **Monorepo Layout**: Organize the codebase into:
   - `apps/`: Deployable executable units (API Gateway, Auth Service, Worker, Frontend).
   - `services/`: Specific subdomain microservices (e.g. Graph, Scanner, Parser) containing explicit Hexagonal/DDD structures (`domain`, `application`, `infrastructure`, `interfaces`).
   - `libs/`: Shared packages containing models, algorithms, config loaders, and events schemas.
   - `infrastructure/`: Multi-environment Docker Compose files and monitoring.

2. **API Gateway & Microservices**:
   - `api-gateway` (FastAPI) will route all incoming traffic.
   - `auth-service` (Express/Node.js) owns identity, JWT authorization, and Redis OTP.
   - Core python services communicate via event-driven messaging (RabbitMQ).

3. **Dependency Injection**:
   - Wired using python's `dependency-injector` framework inside API Gateway and services.

4. **Event Versioning**:
   - Domain events are versioned explicitly (e.g. `RepositoryIndexedV1`, `GraphBuiltV1`) to avoid breaking downstream consumers.

5. **Observability**:
   - Prometheus and Grafana dashboards for metrics.
   - OpenTelemetry Collector for distributed trace aggregation.

## Consequences

- **Pros**:
  - Domain models and business logic are completely decoupled from framework and infrastructure choices.
  - Easier to extend or swap out SQLite/Neo4j graph layers, vector databases, or LLM providers.
  - Multi-service scaling configurations can be done safely.
  
- **Cons**:
  - Higher initial setup overhead and boilerplate directory mapping.

# Deployment Strategies

Deployable stack configurations are maintained in `infrastructure/compose/`:

- **Development**:
  `docker compose -f infrastructure/compose/docker-compose.yml -f infrastructure/compose/docker-compose.dev.yml up -d`
- **Production**:
  `docker compose -f infrastructure/compose/docker-compose.yml -f infrastructure/compose/docker-compose.prod.yml up -d`

import pytest
from fastapi.testclient import TestClient
from app.main import app, container
from app.core.providers import ConnectionChecker

# Mock implementation of ConnectionChecker for unit testing
class MockConnectionChecker:
    def check_redis(self) -> str:
        return "healthy"

    def check_rabbitmq(self) -> str:
        return "healthy"

    def check_neo4j(self) -> str:
        return "healthy"

    def check_qdrant(self) -> str:
        return "healthy"

@pytest.fixture(autouse=True)
def override_checker():
    # Override container checker dependency with mock
    mock_checker = MockConnectionChecker()
    with container.connection_checker.override(mock_checker):
        yield

def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"
    assert data["services"]["redis"] == "healthy"
    assert data["services"]["rabbitmq"] == "healthy"
    assert data["services"]["neo4j"] == "healthy"
    assert data["services"]["qdrant"] == "healthy"

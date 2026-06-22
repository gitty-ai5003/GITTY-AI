class GittyError(Exception):
    """Base exception for all Gitty AI errors."""
    def __init__(self, message: str, code: str = "INTERNAL_ERROR"):
        super().__init__(message)
        self.message = message
        self.code = code

class DomainError(GittyError):
    """Exception raised for business domain logic failures."""
    def __init__(self, message: str, code: str = "DOMAIN_ERROR"):
        super().__init__(message, code)

class InfrastructureError(GittyError):
    """Exception raised when an external system dependency fails (Redis, Neo4j, Qdrant)."""
    def __init__(self, message: str, code: str = "INFRASTRUCTURE_ERROR"):
        super().__init__(message, code)

class EntityNotFoundError(DomainError):
    """Raised when looking up an entity that does not exist."""
    def __init__(self, entity_name: str, entity_id: str):
        message = f"{entity_name} with ID {entity_id} was not found."
        super().__init__(message, code="ENTITY_NOT_FOUND")

class ValidationError(DomainError):
    """Raised when inputs fail domain validations."""
    def __init__(self, message: str):
        super().__init__(message, code="VALIDATION_ERROR")

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from libs.logging import configure_logging, get_logger
from libs.exceptions import GittyError
from app.core.config import settings
from app.core.container import ApplicationContainer
from app.api.router import router as api_router

# Initialize structured logging
configure_logging(settings.ENV)
logger = get_logger("api-gateway")

# Initialize and wire dependency injection container
container = ApplicationContainer()
container.config.from_dict(settings.model_dump())
container.wire(packages=["app.api.v1"])

# Initialize FastAPI application
app = FastAPI(
    title="Gitty AI API Gateway",
    description="AI-Powered Repository Knowledge Graph Platform API Gateway",
    version="1.0.0",
)

# Exception handlers
@app.exception_handler(GittyError)
async def gitty_error_handler(request: Request, exc: GittyError):
    logger.error("Domain/Infrastructure Error occurred", message=exc.message, code=exc.code)
    return JSONResponse(
        status_code=400 if exc.code != "ENTITY_NOT_FOUND" else 404,
        content={"message": exc.message, "code": exc.code}
    )

@app.exception_handler(Exception)
async def general_error_handler(request: Request, exc: Exception):
    logger.error("Unhandled Exception occurred", error=str(exc))
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred.", "code": "INTERNAL_SERVER_ERROR"}
    )

app.include_router(api_router)

if __name__ == "__main__":
    logger.info("Starting Gitty AI API Gateway", env=settings.ENV)
    uvicorn.run("apps.api-gateway.app.main:app", host="0.0.0.0", port=8000, reload=(settings.ENV == "development"))

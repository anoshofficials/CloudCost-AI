from fastapi import FastAPI

from app.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered FinOps platform for multi-cloud cost monitoring and optimization."
)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }

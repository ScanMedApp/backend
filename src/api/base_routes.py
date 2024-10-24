from fastapi import APIRouter
from src.settings import logger


router = APIRouter()

# router.include_router(routes.router, tags=[""])


@router.get("/health")
def health_check() -> dict:
    logger.debug("healthcheck")
    return {"message": "Server is running"}

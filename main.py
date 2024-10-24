from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.base_routes import router as base_router
from src.settings import logger


def create_app() -> FastAPI:
    logger.info("Start backend")
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(base_router)
    return application


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)

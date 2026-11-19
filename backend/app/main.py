from fastapi import FastAPI

from app.api import api_router

app = FastAPI(
    title="Movie Recommender API",
    description="API REST para la aplicación Movie Recommender",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
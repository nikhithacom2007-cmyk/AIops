from fastapi import FastAPI
from app.api.train import router as train_router
from app.api.predict import router as predict_router

from app.config import settings
from app.api.routes import router
from app.utils.logger import logger
from app.api.upload import router as upload_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="End-to-End Production Machine Learning Platform"
)

# Include API routes
app.include_router(router)
app.include_router(upload_router)
app.include_router(train_router)
app.include_router(predict_router)
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 AIOps Platform Started Successfully")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 AIOps Platform Stopped")

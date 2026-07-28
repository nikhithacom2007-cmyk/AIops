from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {
        "message": "Welcome to AIOps Platform",
        "status": "Running"
    }

@router.get("/health")
async def health_check():
    return {
        "status": "Healthy",
        "api": "Running"
    }
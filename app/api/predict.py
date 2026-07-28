from fastapi import APIRouter

from app.schemas.predict import (
    PredictionRequest,
    PredictionResponse
)

from app.services.prediction_service import PredictionService

router = APIRouter(
    prefix="/api/v1",
    tags=["Prediction"]
)


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_customer(request: PredictionRequest):

    return PredictionService.predict_customer(
        request.model_dump()
    )
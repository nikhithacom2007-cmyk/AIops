from fastapi import APIRouter

from app.schemas.train import TrainingResponse
from app.services.training_service import TrainingService

router = APIRouter(
    prefix="/api/v1",
    tags=["Training"]
)


@router.post(
    "/train",
    response_model=TrainingResponse
)
def train_model():

    csv_path = "datasets/sample/customer_churn.csv"

    results = TrainingService.train(csv_path)

    return results
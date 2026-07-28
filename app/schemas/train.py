from pydantic import BaseModel
from typing import Dict, List


class TrainingResponse(BaseModel):

    best_model: str

    accuracy: float

    all_models: Dict[str, float]

    feature_names: List[str]
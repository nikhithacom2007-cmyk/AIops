from pydantic import BaseModel
from typing import List, Dict


class UploadResponse(BaseModel):

    filename: str

    rows: int

    columns: int

    size_mb: float

    column_names: List[str]

    data_types: Dict[str, str]

    missing_values: Dict[str, int]

    duplicate_rows: int

    preview: List[Dict]

    message: str
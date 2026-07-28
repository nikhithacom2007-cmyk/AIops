import os

from fastapi import HTTPException

from app.config import settings


ALLOWED_EXTENSIONS = {".csv"}


def validate_file(filename: str, file_size: int):

    extension = os.path.splitext(filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed."
        )

    max_size = settings.MAX_UPLOAD_SIZE * 1024 * 1024

    if file_size > max_size:

        raise HTTPException(
            status_code=400,
            detail=f"File exceeds {settings.MAX_UPLOAD_SIZE} MB."
        )

    return True
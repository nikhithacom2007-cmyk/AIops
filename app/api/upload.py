from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.schemas.upload import UploadResponse
from app.services.dataset_service import DatasetService


router = APIRouter(
    prefix="/api/v1",
    tags=["Dataset"]
)


@router.post(
    "/upload",
    response_model=UploadResponse
)
async def upload_dataset(
    file: UploadFile = File(...)
):

    return await DatasetService.upload_dataset(file)
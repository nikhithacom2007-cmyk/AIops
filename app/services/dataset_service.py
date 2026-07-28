import os
import pandas as pd

from fastapi import UploadFile

from app.config import settings
from app.utils.validator import validate_file
from app.utils.logger import logger


class DatasetService:

    @staticmethod
    async def upload_dataset(file: UploadFile):

        # Read uploaded file
        contents = await file.read()

        # Validate file type and size
        validate_file(
            file.filename,
            len(contents)
        )

        # Create raw dataset folder if it doesn't exist
        os.makedirs(
            settings.RAW_DATASET_PATH,
            exist_ok=True
        )

        # Create complete file path
        save_path = os.path.join(
            settings.RAW_DATASET_PATH,
            file.filename
        )

        # Save uploaded file
        with open(save_path, "wb") as f:
            f.write(contents)

        # Read CSV using Pandas
        df = pd.read_csv(save_path)

        # Basic Information
        rows = len(df)
        columns = len(df.columns)

        size_mb = round(
            len(contents) / (1024 * 1024),
            2
        )

        # Log upload
        logger.info(
            f"Dataset Uploaded : {file.filename}"
        )

        # Return Dataset Profile
        return {

            "filename": file.filename,

            "rows": rows,

            "columns": columns,

            "size_mb": size_mb,

            "column_names": list(df.columns),

            "data_types": {
                col: str(dtype)
                for col, dtype in df.dtypes.items()
            },

            "missing_values": {
                col: int(value)
                for col, value in df.isnull().sum().items()
            },

            "duplicate_rows": int(
                df.duplicated().sum()
            ),

            "preview": df.head().to_dict(
                orient="records"
            ),

            "message": "Dataset uploaded successfully."

        }
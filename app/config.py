from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME", "AIOps Platform")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    DATASET_PATH = os.getenv("DATASET_PATH", "datasets")

    RAW_DATASET_PATH = os.getenv(
        "RAW_DATASET_PATH", "datasets/raw"
    )

    PROCESSED_DATASET_PATH = os.getenv(
        "PROCESSED_DATASET_PATH", "datasets/processed"
    )

    MODEL_PATH = os.getenv(
        "MODEL_PATH", "models"
    )

    PRODUCTION_MODEL_PATH = os.getenv(
        "PRODUCTION_MODEL_PATH", "models/production"
    )

    STAGING_MODEL_PATH = os.getenv(
        "STAGING_MODEL_PATH", "models/staging"
    )

    ARCHIVE_MODEL_PATH = os.getenv(
        "ARCHIVE_MODEL_PATH", "models/archive"
    )

    MAX_UPLOAD_SIZE = int(
        os.getenv("MAX_UPLOAD_SIZE", "10485760")
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    LOG_DIRECTORY = os.getenv(
        "LOG_DIRECTORY", "logs"
    )

    MLFLOW_TRACKING_URI = os.getenv(
        "MLFLOW_TRACKING_URI", "sqlite:///mlflow.db"
    )

    MLFLOW_EXPERIMENT_NAME = os.getenv(
        "MLFLOW_EXPERIMENT_NAME", "AIOpsPlatform"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL", "sqlite:///mlflow.db"
    )

    API_PREFIX = os.getenv(
        "API_PREFIX", "/api/v1"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY", "change-this-secret-key"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY", ""
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT", "development"
    )


settings = Settings()
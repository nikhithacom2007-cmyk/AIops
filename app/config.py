from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")

    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

    DEBUG = os.getenv("DEBUG") == "True"

    DATASET_PATH = os.getenv("DATASET_PATH")

    RAW_DATASET_PATH = os.getenv("RAW_DATASET_PATH")

    PROCESSED_DATASET_PATH = os.getenv(
        "PROCESSED_DATASET_PATH"
    )

    MODEL_PATH = os.getenv("MODEL_PATH")

    PRODUCTION_MODEL_PATH = os.getenv(
        "PRODUCTION_MODEL_PATH"
    )

    STAGING_MODEL_PATH = os.getenv(
        "STAGING_MODEL_PATH"
    )

    ARCHIVE_MODEL_PATH = os.getenv(
        "ARCHIVE_MODEL_PATH"
    )

    MAX_UPLOAD_SIZE = int(
        os.getenv("MAX_UPLOAD_SIZE")
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL")

    LOG_DIRECTORY = os.getenv("LOG_DIRECTORY")

    MLFLOW_TRACKING_URI = os.getenv(
        "MLFLOW_TRACKING_URI"
    )

    MLFLOW_EXPERIMENT_NAME = os.getenv(
        "MLFLOW_EXPERIMENT_NAME"
    )

    DATABASE_URL = os.getenv("DATABASE_URL")

    API_PREFIX = os.getenv("API_PREFIX")

    SECRET_KEY = os.getenv("SECRET_KEY")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    )

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    ENVIRONMENT = os.getenv("ENVIRONMENT")


settings = Settings()
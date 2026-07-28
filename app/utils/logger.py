import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Create logger
logger = logging.getLogger("AIOpsPlatform")
logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# Formatter
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File Handler (5 MB max, keep 3 backups)
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,
    backupCount=3
)
file_handler.setFormatter(formatter)

# Avoid adding handlers multiple times
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
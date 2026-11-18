import logging
import os
from datetime import datetime

from src.paths import project_path

# Give each run its own timestamped log file.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create the logs folder before configuring the file handler.
logs_path = project_path("logs")
os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the root logger so logging calls from other modules use this file.
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
import os
import logging

from datetime import datetime

# Configure logging
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(SCRIPT_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

log_filename = f"{LOG_DIR}/{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_filename)],
)

logger = logging.getLogger(__name__)

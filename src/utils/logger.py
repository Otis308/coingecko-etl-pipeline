import logging
import os
from datetime import datetime


os.makedirs("logs", exist_ok=True)

log_file = (
    f"logs/pipeline_"
    f"{datetime.now().strftime('%Y-%m-%d')}.log"
)

logging.basicConfig(
    filename=log_file,
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)
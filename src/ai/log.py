from loguru import logger
from utils import BASE_PATH, CONFIG

log = logger.bind(name="ai")

log.add(
    BASE_PATH / ".logs" / "ai.log",
    format="{time} | {level} | {message}",
    level=CONFIG.log_level.upper(),
    rotation="10 MB",
    compression="zip",
    filter=lambda record: record["extra"].get("name") == "ai",
)

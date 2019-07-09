import logging


# 获取logger实例
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("log.txt")

# file_handler.addFilter()

file_formatter = logging.Formatter(" %(levelname)s - %(asctime)s -> %(message)s")

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

logger.error("哈哈")

logger.critical("666")
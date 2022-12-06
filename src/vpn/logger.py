import logging
import os
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

os.makedirs('logs', exist_ok=True)
LOG_FILE_PATH = 'logs\\openvpn-tools.log'

logger = logging.Logger('openvpn-tools')
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    '%m/%d/%Y %I:%M:%S %p',
)
stream_handler = StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=1_048_576, backupCount=1)  # 1 MB
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

import logging
from datetime import datetime
import os

FILE_NAME = f"{datetime.now().strftime("%Y%m%d-%H%M%S")}.log"
LOG_PATH = os.path.join(os.getcwd(), 'logs', FILE_NAME)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_PATH, FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
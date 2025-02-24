import logging
import os
from datetime import datetime

# text file in the following convention
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# path for the log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# even though there is a file/ folder, keep on appending the files inside that
os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# overriding the functionality of the logging
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno) d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, 
)

# if __name__ == "__main__":
#     logging.info("Logging has started")
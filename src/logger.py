# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True) #keep on appending the logs in the file if exit

# LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

import logging
import os
from datetime import datetime

# Create unique log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# if __name__ == "__main__":
#     logging.info("Logging has started")

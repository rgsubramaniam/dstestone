import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("D A T A S C I E N C E - P R O J E C T")

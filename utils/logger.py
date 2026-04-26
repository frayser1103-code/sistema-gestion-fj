import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(mensaje):
    logging.error(str(mensaje))

import os
import logging

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure the logger
LOG_FILE = os.path.join("logs", "sql_sim.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger instance
logger = logging.getLogger("sql_sim")

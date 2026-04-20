import logging
from pathlib import Path
from datetime import datetime

# Create logs directory
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Safe timestamp for filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Log file path
log_file_path = LOG_DIR / f"{timestamp}.log"

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("Logging setup complete.")
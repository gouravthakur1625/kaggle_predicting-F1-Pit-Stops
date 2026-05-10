"""logging configuration for project"""
import logging
from datetime import datetime
from src import config

def setup_logger(name: str= "f1_pitstops") -> logging.Logger:
    
    """Setup a logger that writes to file and console"""

    #make sure log directory exists
    config.LOG_DIR.mkdir(exist_ok=True)

    # Create unique log file name with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = config.LOG_DIR / f"{name}_{timestamp}.log"

    # Create logger
    logger= logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Format time | level | module| message
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)-15s | %(message)s',
        datefmt= '%Y-%m-%d %H:%M:%S'
        )
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
import pandas as pd
from src.logger import setup_logger
from pathlib import Path
from src import config 

logger = setup_logger("data_logger")

def load_train() -> pd.DataFrame:

    """
    Load the training data from raw data folder
    
    Returns: 
        pd.DataFrame: The training data
    Raises:
        FileNotFoundError: If the training data file is not found
    """
    logger.info(f"Loading training data from {config.TRAIN_FILE}")

    if not config.TRAIN_FILE.exists():
        logger.error(f"Training data file not found at {config.TRAIN_FILE}")
        raise FileNotFoundError(f"Training data file not found at {config.TRAIN_FILE}")
    
    df = pd.read_csv(config.TRAIN_FILE)
    logger.info(f"Loaded training data with shape {df.shape}")
    return df

def load_test()-> pd.DataFrame:
    """ 
    Load teh test data from raw data folder.
    return pd.DataFrame: The test data
    Raises: 
        FilesNotFoundError: If the test data file is not found
    """    
    logger.info(f"Loading test data from {config.TEST_FILE}")

    if not config.TEST_FILE.exists():
        logger.error(f"Test data file not found at {config.TEST_FILE}")
        raise FileNotFoundError(f"Test data file not found at {config.TEST_FILE}")
    
    df= pd.read_csv(config.TEST_FILE)
    logger.info(f"Loaded test data with shape {df.shape}")
    return df
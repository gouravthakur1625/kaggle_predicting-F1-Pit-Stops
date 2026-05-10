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
def load_submission_data() -> pd.DataFrame:
    """
    Load submission data from raw data folder:
    returns:
        pd.DataFrame: The sample submission data
    """
    logger.info(f"Loading submission data from {config.SUBMISSION_FILE}")
    if not config.SUBMISSION_FILE.exists():
        logger.error(f"Submission data file not found at {config.SUBMISSION_FILE}")
        raise FileNotFoundError(f"Submission data file not found at {config.SUBMISSION_FILE}")
    
    df = pd.read_csv(config.SUBMISSION_FILE)
    logger.info(f"Loaded submission data with shape {df.shape}")
    return df

def save_processed_data(df: pd.DataFrame, filename: str) -> Path:
    """
    Save processed DataFrame to the processed data folder.
    Args:
        df: DataFrame to save.
        filename: Name of the file (e.g., 'train_clean.csv').
    Returns:
        Path: path to the saved file
    """
    config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok= True)
    path = config.PROCESSED_DATA_DIR / filename
    df.to_csv(path, index= False)
    logger.info(f"Processed data saved -> {path} : shape{df.shape}")
    return path

def load_processed_data(filename: str) -> pd.DataFrame:
    """
    load previously saved processed data
    Args:
        filename: Name of the file to load (e.g., 'train_clean.csv').
    Returns:
        pd.DataFrame: Loaded processed data
    """
    path= config.PROCESSED_DATA_DIR / filename
    logger.info(f"Loading processed data from {path}")
    if not path.exists():
        logger.error(f"File not found at {path}")
        raise FileNotFoundError(f"Missing File: {path}")
    df = pd.read_csv(path)
    logger.info(f"Loaded processed data with shape {df.shape}")
    return df

def Save_submission(predictions, ids, filename: str) -> Path:
    """ 
    Save submission file to submission folder

    Args:
        predictions: Array-like of model predictions
        ids: Array-like of corresponding IDs for the predictions
        filename: Name of the submission file (e.g., 'submission_v1.csv')
    """
    if len(predictions) != len(ids):
        logger.error("Length mismatch: Predictions {len(predictions)} V/S IDs {len(ids)}")
        raise ValueError("Predictions and ID's must have same length")
    
    config.SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)
    submission= pd.DataFrame{
        config.ID_COL: ids,
        config.TARGET_COL: predictions
    }
    path= config.SUBMISSION_DIR / filename
    submission.to_csv(path, index= False)
    logger.info(f"Submission saved → {path}")
    logger.info(f"Submission shape: {submission.shape}")
    logger.info(f"Predictions stats — min: {predictions.min():.4f}, "
                f"max: {predictions.max():.4f}, mean: {predictions.mean():.4f}")
    return path
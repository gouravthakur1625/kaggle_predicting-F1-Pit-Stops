from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).parent.parent


# Data Paths
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SUBMISSION_DIR = DATA_DIR / "submissions"

# Model paths
MODEL_DIR = ROOT_DIR/ "models"
LOG_DIR = ROOT_DIR / "logs"

## FILES
TRAIN_FILE = RAW_DATA_DIR / "train.csv"
TEST_FILE = RAW_DATA_DIR / "test.csv"
SUBMISSION_FILE = RAW_DATA_DIR / "sample_submission.csv"

# MODEL SETTING
from pathlib import Path

# path to the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# path to the data folder
DATA_PATH = PROJECT_ROOT / "data"

# put the paths to your project data files below
ORIGINAL_DATA = DATA_PATH / "creditcard.zip"
PROCESSED_DATA = DATA_PATH / "creditcard.parquet"

# put the paths to your project model files below
MODELS_PATH = PROJECT_ROOT / "models"

# put other paths you deem necessary below
REPORTS_PATH = PROJECT_ROOT / "reports"
IMAGES_PATH = REPORTS_PATH / "images"

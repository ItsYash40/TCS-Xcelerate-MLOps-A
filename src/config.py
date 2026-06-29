"""
Global configuration for the Loan Default Prediction Pipeline.
Centralizes project paths, environment variables, and application settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# Project Directories
# ============================================================

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_DIR = os.path.join(BASE_DIR, "logs")

for directory in (DATA_DIR, MODEL_DIR, REPORT_DIR, LOG_DIR):
    os.makedirs(directory, exist_ok=True)

# ============================================================
# Database Configuration
# ============================================================

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "loan_default_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ============================================================
# MLflow Configuration
# ============================================================

MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI",
    "http://localhost:5000"
)

MLFLOW_EXPERIMENT_NAME = "Loan_Default_Prediction"
MLFLOW_MODEL_NAME = "loan-default-xgboost"
MLFLOW_MODEL_STAGE = os.getenv("MLFLOW_MODEL_STAGE", "Production")

# ============================================================
# FastAPI Configuration
# ============================================================

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

# ============================================================
# Airflow Configuration
# ============================================================

AIRFLOW_DAG_ID = "loan_default_training_pipeline"
AIRFLOW_SCHEDULE = "@daily"

# ============================================================
# Training Configuration
# ============================================================

TARGET_COLUMN = "TARGET"
TEST_SIZE = float(os.getenv("TEST_SIZE", 0.2))
RANDOM_STATE = int(os.getenv("RANDOM_STATE", 42))

# ============================================================
# Drift Monitoring
# ============================================================

DATA_DRIFT_THRESHOLD = float(
    os.getenv("DATA_DRIFT_THRESHOLD", 0.30)
)

PERFORMANCE_DROP_THRESHOLD = float(
    os.getenv("PERFORMANCE_DROP_THRESHOLD", 0.05)
)

# ============================================================
# Offline Fallback Model
# ============================================================

ENABLE_OFFLINE_FALLBACK = True

FALLBACK_MODEL_PATH = os.path.join(
    MODEL_DIR,
    "fallback_model.json"
)

# ============================================================
# Logging
# ============================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ============================================================
# HTTP Configuration
# ============================================================

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
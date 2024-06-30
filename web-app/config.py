# ===app config====
import os

DB_ECHO = "1"
DEBUG = 1
PROJECT_NAME = "FastAPI_Library"
VERSION = "0.0.1"

# ===database config====
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
# ===app security config====
security = bool(os.getenv("SECURITY"))
API_KEY = os.getenv("API_KEY")

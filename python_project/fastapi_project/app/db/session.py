import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DATABASE")

logger = logging.getLogger(__name__)

try:
    engine = create_engine(
        url="mysql+pymysql://{}:{}@{}:{}/{}".format(
            DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE
        )
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Connection created successfully")
except Exception:
    logger.warning("Connection could not be created")

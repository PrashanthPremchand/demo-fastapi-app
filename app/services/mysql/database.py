from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib.parse
from app.core.config import settings

safe_password = urllib.parse.quote_plus(settings.DB_PASSWORD)

DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}:{safe_password}@{settings.DB_HOST}:3306/{settings.DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
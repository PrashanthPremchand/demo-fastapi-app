from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

safe_password = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))

DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{safe_password}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv(Path(__file__).resolve().parents[1] / '.env')


def get_database_url() -> str:
    """Build a MySQL connection URL without placing credentials in client code."""
    explicit_url = os.getenv('DATABASE_URL')
    if explicit_url:
        return explicit_url
    host = os.getenv('DB_HOST', 'localhost')
    user = os.getenv('DB_USER', 'portfolio_user')
    password = os.getenv('DB_PASSWORD', '')
    name = os.getenv('DB_NAME', 'portfolio_db')
    return f'mysql+pymysql://{user}:{password}@{host}/{name}?charset=utf8mb4'


DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=280)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

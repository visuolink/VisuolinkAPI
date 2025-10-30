from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv

load_dotenv()

USERNAME = getenv('DATABASE_USERNAME')
PASSWORD = getenv('DATABASE_PASSWORD')
HOSTNAME = getenv('DATABASE_HOSTNAME')
PORT = getenv('DATABASE_PORT')
NAME = getenv('DATABASE_NAME')

DATABASE_URL = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{NAME}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# load file .env
load_dotenv()

# ambil DATABASE_URL dari .env
DATABASE_URL = os.getenv("DATABASE_URL")

# buat koneksi ke PostgreSQL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

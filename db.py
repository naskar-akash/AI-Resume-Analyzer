from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("CONNECTION_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # Check if the connection is alive before using it
)

SessionLocal = sessionmaker(bind=engine)
base = declarative_base()
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("CONNECTION_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # Check if the connection is alive before using it
)

SessionLocal = sessionmaker(bind=engine)
base = declarative_base()

def init_db():
    base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    if 'reports' in inspector.get_table_names():
        columns = [col['name'] for col in inspector.get_columns('reports')]
        if 'results' not in columns:
            with engine.begin() as conn:
                conn.execute(text('ALTER TABLE reports ADD COLUMN results TEXT'))

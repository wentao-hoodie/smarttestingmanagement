# In app/api/deps.py

from typing import Generator
# Make sure this import points to your SessionLocal object
from app.db.session import SessionLocal

def get_db() -> Generator:
    """
    FastAPI dependency to create and manage a database session.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --- Database URL ---
# This line configures the database connection. For this example, we are using
# a local SQLite database file named "test.db" in the project's root directory.
# For a real application, you would replace this with your actual database URL,
# for example, for PostgreSQL:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


# --- SQLAlchemy Engine ---
# The engine is the core interface to the database. The 'connect_args'
# is only needed for SQLite to allow it to be used by multiple threads,
# which is required by FastAPI.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# --- Database Session ---
# SessionLocal is the database session factory. Instances of this class
# will be the actual database sessions you work with in your API endpoints.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
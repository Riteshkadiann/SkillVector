from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
import os
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL database URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/skillvector"
)

# Determine if using Supabase (check for sslmode in URL or add it)
if "supabase.co" in DATABASE_URL:
    # Supabase requires SSL - add it if not already present
    if "sslmode=" not in DATABASE_URL:
        DATABASE_URL = DATABASE_URL + "?sslmode=require"

# Create SQLAlchemy engine with Supabase-compatible settings
engine = create_engine(
    DATABASE_URL,
    # Use NullPool on Render to avoid connection timeouts
    poolclass=NullPool if os.getenv("RENDER") else None,
    # Test connections before using them
    pool_pre_ping=True,
    # Disable echo in production
    echo=os.getenv("DEBUG", "false").lower() == "true",
    # Connection parameters
    connect_args={
        "connect_timeout": 10,
    } if "supabase.co" in DATABASE_URL else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
    except Exception as e:
        print(f"⚠️  Database initialization error: {e}")
        raise

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
is_supabase = "supabase.co" in DATABASE_URL
if is_supabase:
    # Supabase requires SSL - add it if not already present
    if "sslmode=" not in DATABASE_URL:
        DATABASE_URL = DATABASE_URL + "?sslmode=require"

# Detect deployment environment: Render has PORT, RENDER_GIT_COMMIT, or hostname checks
is_production = bool(os.getenv("RENDER") or os.getenv("PORT") or os.getenv("RENDER_GIT_COMMIT"))
use_null_pool = is_production or is_supabase

# Build engine kwargs conditionally
# NullPool doesn't accept pool_size/max_overflow parameters
engine_kwargs: dict = {
    "echo": os.getenv("DEBUG", "false").lower() == "true",
    "pool_pre_ping": True,
}

if use_null_pool:
    engine_kwargs["poolclass"] = NullPool
else:
    # Only add pool parameters for non-NullPool scenarios (local development)
    engine_kwargs["pool_size"] = 5
    engine_kwargs["max_overflow"] = 10

# Add connection args for Supabase
if is_supabase:
    engine_kwargs["connect_args"] = {
        "connect_timeout": 10,
        "keepalives": 1,
        "keepalives_idle": 30,
    }

# Create SQLAlchemy engine with Supabase-compatible settings
engine = create_engine(DATABASE_URL, **engine_kwargs)

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
        import traceback
        print(f"⚠️  Database initialization warning: {str(e)}")
        print(f"   Full traceback: {traceback.format_exc()}")
        print("   (App can still run with in-memory storage for resume/job data)")
        # Don't raise - allow app to start anyway

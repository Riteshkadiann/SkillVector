from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from api.routes_resume import router as resume_router
from api.routes_jobs import router as jobs_router
from api.routes_gap import router as gap_router
from api.routes_roadmap import router as roadmap_router
from core.database import init_db, engine
from models.database_models import *
import os

# Initialize database tables
try:
    init_db()
except Exception as e:
    # App will still start, but database won't be initialized
    pass

app = FastAPI(title="SkillVector", version="1.0.0")

# CORS configuration - restrict in production
allowed_origins = os.getenv("FRONTEND_URL", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router, prefix="/api/resume", tags=["Resume"])
app.include_router(jobs_router, prefix="/api/jobs", tags=["Jobs"])
app.include_router(gap_router, prefix="/api/gap", tags=["Skill Gap"])
app.include_router(roadmap_router, prefix="/api/roadmap", tags=["Roadmap"])

@app.get("/")
def root():
    return {"message": "SkillVector is running ✅"}

@app.get("/health")
def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Test database connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}, 503

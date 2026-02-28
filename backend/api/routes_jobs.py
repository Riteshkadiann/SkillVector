from fastapi import APIRouter, HTTPException
from core.job_analyzer import extract_job_skills
from models.schemas import JobInput

router = APIRouter()

# In-memory store (replace with DB in production)
job_store: dict = {}


@router.post("/analyze")
def analyze_job(data: JobInput):
    """Analyze a job description and extract required skills."""
    if not data.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")

    result = extract_job_skills(data.job_description)
    job_store[data.user_id] = {**result, "job_title": data.job_title}

    return {
        "user_id": data.user_id,
        "job_title": data.job_title,
        "message": "Job analyzed successfully ✅",
        "data": result
    }


@router.get("/{user_id}")
def get_job_analysis(user_id: str):
    """Get stored job analysis for a user."""
    job = job_store.get(user_id)
    if not job:
        raise HTTPException(status_code=404, detail="No job found for this user")
    return {"user_id": user_id, "job": job}

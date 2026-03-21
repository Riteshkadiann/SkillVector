from fastapi import APIRouter, HTTPException
from core.job_analyzer import extract_job_skills
from models.schemas import JobInput
from models.database_models import JobDescription
from core.database import SessionLocal

router = APIRouter()


@router.post("/analyze")
def analyze_job(data: JobInput):
    """Analyze a job description and extract required skills."""
    if not data.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")

    result = extract_job_skills(data.job_description)
    
    # Save to database
    db = SessionLocal()
    try:
        job = JobDescription(
            user_id=data.user_id,
            job_title=data.job_title,
            raw_text=data.job_description,
            required_skills=result.get("required_skills", []),
            preferred_skills=result.get("preferred_skills", []),
            all_skills=result.get("all_skills", []),
            total_skill_count=len(result.get("all_skills", []))
        )
        db.add(job)
        db.commit()
    finally:
        db.close()

    return {
        "user_id": data.user_id,
        "job_title": data.job_title,
        "message": "Job analyzed successfully ✅",
        "data": result
    }


@router.get("/{user_id}")
def get_job_analysis(user_id: str):
    """Get stored job analysis for a user."""
    db = SessionLocal()
    try:
        job = db.query(JobDescription).filter(JobDescription.user_id == user_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="No job found for this user")
        return {
            "user_id": user_id,
            "job": {
                "job_title": job.job_title,
                "required_skills": job.required_skills,
                "preferred_skills": job.preferred_skills,
                "all_skills": job.all_skills
            }
        }
    finally:
        db.close()

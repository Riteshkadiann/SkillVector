from fastapi import APIRouter, HTTPException
from core.roadmap_generator import generate_roadmap
from core.match_scorer import calculate_match_score
from core.skill_gap_engine import detect_skill_gaps, rank_missing_skills, get_top_priority_skills
from core.match_scorer import project_improved_score
from models.schemas import ProgressUpdate
from api.routes_resume import user_profiles
from api.routes_jobs import job_store

router = APIRouter()

progress_store: dict = {}


@router.get("/{user_id}")
def get_roadmap(user_id: str):
    """Generate a personalized learning roadmap for the user."""
    user_data = user_profiles.get(user_id)
    job_data = job_store.get(user_id)

    if not user_data:
        raise HTTPException(status_code=404, detail="Resume not found.")
    if not job_data:
        raise HTTPException(status_code=404, detail="Job description not found.")

    user_skills = user_data["skills"]
    job_skills = job_data["all_skills"]

    missing = detect_skill_gaps(user_skills, job_skills)
    ranked = rank_missing_skills(missing, [job_skills])
    top_skills = get_top_priority_skills(ranked, top_n=8)

    roadmap = generate_roadmap(top_skills, weeks=8)
    current_score = calculate_match_score(user_skills, job_skills)

    projected = project_improved_score(user_skills, job_skills, missing)

    return {
        "user_id": user_id,
        "total_weeks": len(roadmap),
        "roadmap": roadmap,
        "current_match_score": current_score,
        "projected_match_score": projected
    }


@router.put("/progress/{user_id}")
def update_progress(user_id: str, data: ProgressUpdate):
    """Mark skills as completed and recalculate match score."""
    user_data = user_profiles.get(user_id)
    job_data = job_store.get(user_id)

    if not user_data or not job_data:
        raise HTTPException(status_code=404, detail="Missing user or job data")

    progress_store[user_id] = data.completed_skills

    updated_skills = list(set(user_data["skills"] + data.completed_skills))
    new_score = calculate_match_score(updated_skills, job_data["all_skills"])

    return {
        "user_id": user_id,
        "completed_skills": data.completed_skills,
        "updated_match_score": new_score,
        "message": f"Great progress! Your match score is now {new_score}% 🎉"
    }

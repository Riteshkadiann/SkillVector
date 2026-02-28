from fastapi import APIRouter, HTTPException
from core.skill_gap_engine import detect_skill_gaps, rank_missing_skills, get_top_priority_skills
from core.match_scorer import calculate_match_score, project_improved_score
from api.routes_resume import user_profiles
from api.routes_jobs import job_store

router = APIRouter()


@router.get("/{user_id}")
def get_skill_gap(user_id: str):
    """
    Compare user skills vs job skills.
    Returns missing skills, ranked priorities, and match score.
    """
    user_data = user_profiles.get(user_id)
    job_data = job_store.get(user_id)

    if not user_data:
        raise HTTPException(
            status_code=404,
            detail="Resume not found. Please upload your resume first."
        )
    if not job_data:
        raise HTTPException(
            status_code=404,
            detail="Job description not found. Please submit a job description first."
        )

    user_skills = user_data["skills"]
    job_skills = job_data["all_skills"]

    missing = detect_skill_gaps(user_skills, job_skills)
    ranked = rank_missing_skills(missing, [job_skills])
    top_5 = get_top_priority_skills(ranked)
    score = calculate_match_score(user_skills, job_skills)

    projected = project_improved_score(user_skills, job_skills, missing)

    return {
        "user_id": user_id,
        "user_skills": user_skills,
        "job_skills": job_skills,
        "missing_skills": missing,
        "priority_skills": top_5,
        "match_score": score,
        "projected_score_after_learning": projected
    }

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from core.resume_parser import extract_text_from_pdf, parse_resume
from models.schemas import ResumeInput
from models.database_models import Resume
from core.database import SessionLocal

router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), user_id: str = Form(...)):
    """Upload a PDF resume and extract skills."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    contents = await file.read()
    text = extract_text_from_pdf(contents)

    if not text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from PDF")

    parsed = parse_resume(text)
    
    # Save to database
    db = SessionLocal()
    try:
        resume = Resume(
            user_id=user_id,
            raw_text=text,
            skills=parsed.get("skills", {}),
            years_experience=parsed.get("years_experience", 0),
            education=parsed.get("education", ""),
            skill_count=len(parsed.get("skills", {}))
        )
        db.add(resume)
        db.commit()
    finally:
        db.close()

    return {
        "user_id": user_id,
        "message": "Resume parsed successfully ✅",
        "data": parsed
    }


@router.post("/text")
async def submit_resume_text(data: ResumeInput):
    """Submit resume as plain text (alternative to PDF upload)."""
    if not data.raw_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty")

    parsed = parse_resume(data.raw_text)
    
    # Save to database
    db = SessionLocal()
    try:
        resume = Resume(
            user_id=data.user_id,
            raw_text=data.raw_text,
            skills=parsed.get("skills", {}),
            years_experience=parsed.get("years_experience", 0),
            education=parsed.get("education", ""),
            skill_count=len(parsed.get("skills", {}))
        )
        db.add(resume)
        db.commit()
    finally:
        db.close()

    return {
        "user_id": data.user_id,
        "message": "Resume parsed successfully ✅",
        "data": parsed
    }


@router.get("/{user_id}")
def get_resume_profile(user_id: str):
    """Get the stored profile for a user."""
    db = SessionLocal()
    try:
        resume = db.query(Resume).filter(Resume.user_id == user_id).first()
        if not resume:
            raise HTTPException(status_code=404, detail="User profile not found")
        return {
            "user_id": user_id,
            "profile": {
                "skills": resume.skills,
                "years_experience": resume.years_experience,
                "education": resume.education,
                "skill_count": resume.skill_count
            }
        }
    finally:
        db.close()

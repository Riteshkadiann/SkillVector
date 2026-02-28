from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from core.resume_parser import extract_text_from_pdf, parse_resume
from models.schemas import ResumeInput

router = APIRouter()

# In-memory store (replace with DB in production)
user_profiles: dict = {}


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
    user_profiles[user_id] = parsed

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
    user_profiles[data.user_id] = parsed

    return {
        "user_id": data.user_id,
        "message": "Resume parsed successfully ✅",
        "data": parsed
    }


@router.get("/{user_id}")
def get_resume_profile(user_id: str):
    """Get the stored profile for a user."""
    profile = user_profiles.get(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return {"user_id": user_id, "profile": profile}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes_resume import router as resume_router
from api.routes_jobs import router as jobs_router
from api.routes_gap import router as gap_router
from api.routes_roadmap import router as roadmap_router

app = FastAPI(title="SkillVector", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

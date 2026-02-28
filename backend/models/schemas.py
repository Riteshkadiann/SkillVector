from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class ResumeInput(BaseModel):
    user_id: str
    raw_text: str


class JobInput(BaseModel):
    user_id: str
    job_title: str
    job_description: str


class SkillGapResponse(BaseModel):
    user_id: str
    user_skills: List[str]
    job_skills: List[str]
    missing_skills: List[str]
    priority_skills: List[Dict[str, Any]]
    match_score: float
    projected_score_after_learning: float


class RoadmapWeek(BaseModel):
    week: str
    skill: str
    importance_score: float
    resources: List[str]
    micro_project: str
    completed: bool = False


class RoadmapResponse(BaseModel):
    user_id: str
    total_weeks: int
    roadmap: List[RoadmapWeek]
    current_match_score: float
    projected_match_score: float


class ProgressUpdate(BaseModel):
    user_id: str
    completed_skills: List[str]


class ProgressResponse(BaseModel):
    user_id: str
    completed_skills: List[str]
    updated_match_score: float
    message: str

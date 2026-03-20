from sqlalchemy import Column, String, Text, Integer, Float, DateTime, func, Index, JSON
from datetime import datetime
import uuid
from core.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100))
    email = Column(String(150), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Resume(Base):
    __tablename__ = "resumes"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(100), nullable=False, index=True)
    raw_text = Column(Text)
    skills = Column(JSON, default={})
    years_experience = Column(Integer, default=0)
    education = Column(String(50))
    skill_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class JobDescription(Base):
    __tablename__ = "job_descriptions"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(100), nullable=False, index=True)
    job_title = Column(String(150))
    raw_text = Column(Text)
    required_skills = Column(JSON, default={})
    preferred_skills = Column(JSON, default={})
    all_skills = Column(JSON, default={})
    total_skill_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class SkillGap(Base):
    __tablename__ = "skill_gaps"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(100), nullable=False, index=True)
    missing_skills = Column(JSON, default={})
    priority_skills = Column(JSON, default={})
    match_score = Column(Float)
    projected_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class Roadmap(Base):
    __tablename__ = "roadmaps"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(100), nullable=False, index=True)
    roadmap_data = Column(JSON, default={})
    current_score = Column(Float)
    projected_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(100), nullable=False, index=True)
    completed_skills = Column(JSON, default={})
    updated_score = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow)

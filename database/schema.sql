-- AI Career Strategy Engine - PostgreSQL Schema
-- Run this in your PostgreSQL instance to set up the database

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS resumes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(100) NOT NULL,
    raw_text TEXT,
    skills JSONB,
    years_experience INT DEFAULT 0,
    education VARCHAR(50),
    skill_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS job_descriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(100) NOT NULL,
    job_title VARCHAR(150),
    raw_text TEXT,
    required_skills JSONB,
    preferred_skills JSONB,
    all_skills JSONB,
    total_skill_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS skill_gaps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(100) NOT NULL,
    missing_skills JSONB,
    priority_skills JSONB,
    match_score FLOAT,
    projected_score FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS roadmaps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(100) NOT NULL,
    roadmap_data JSONB,
    current_score FLOAT,
    projected_score FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(100) NOT NULL,
    completed_skills JSONB,
    updated_score FLOAT,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for faster lookups
CREATE INDEX IF NOT EXISTS idx_resumes_user_id ON resumes(user_id);
CREATE INDEX IF NOT EXISTS idx_jobs_user_id ON job_descriptions(user_id);
CREATE INDEX IF NOT EXISTS idx_gaps_user_id ON skill_gaps(user_id);
CREATE INDEX IF NOT EXISTS idx_progress_user_id ON progress(user_id);

🧠 SkillVector

> AI-powered career intelligence engine that transforms resumes and job descriptions into quantified skill gap analysis and structured learning roadmaps.

🚀 Live Demo: [Coming Soon]  
📄 API Docs: `/docs`
A career intelligence engine that converts resumes and job descriptions into a quantified skill gap analysis and structured 60-day execution roadmap.

What It Does
1. Extracts skills from resumes and job descriptions using NLP
2. Computes match score via TF-IDF + cosine similarity
3. Ranks missing skills using weighted frequency scoring
4. Generates a prioritized learning roadmap
5. Recalculates match score as progress updates

Architecture
• Backend: FastAPI
• NLP: spaCy
• ML: scikit-learn (TF-IDF, cosine similarity)
• Frontend: React
• DB: PostgreSQL (optional)

Why It’s Different
Not a chatbot.
Not prompt engineering.
A deterministic, algorithm-driven decision engine.

Quick Start
Backend:
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload --port 8010

Frontend:
cd frontend
npm install
npm start

Backend: http://localhost:8010

Frontend: http://localhost:3000

## 📸 Preview

![Dashboard](assets/dashboard.png)
![Match Score](assets/match-score.png)
![Roadmap](assets/roadmap.png)

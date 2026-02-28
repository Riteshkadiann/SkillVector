from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List


def calculate_match_score(user_skills: List[str], job_skills: List[str]) -> float:
    """
    Use TF-IDF + cosine similarity to calculate how well
    a user's skills match a job description.
    Returns a percentage (0-100).
    """
    if not user_skills or not job_skills:
        return 0.0

    user_text = " ".join(user_skills)
    job_text = " ".join(job_skills)

    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform([user_text, job_text])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        score = round(float(similarity[0][0]) * 100, 2)
        return min(score, 100.0)
    except Exception:
        # Fallback: simple overlap ratio
        user_set = set(s.lower() for s in user_skills)
        job_set = set(s.lower() for s in job_skills)
        if not job_set:
            return 0.0
        overlap = len(user_set & job_set)
        return round((overlap / len(job_set)) * 100, 2)


def project_improved_score(
    user_skills: List[str],
    job_skills: List[str],
    skills_to_add: List[str]
) -> float:
    """Calculate what the match score would be after learning new skills."""
    improved_skills = list(set(user_skills + skills_to_add))
    return calculate_match_score(improved_skills, job_skills)

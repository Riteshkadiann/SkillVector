from collections import Counter
from typing import List, Dict
from utils.skill_taxonomy import SKILL_TO_CATEGORY, CATEGORY_PRIORITY


def _dedup_skills(skills: List[str]) -> List[str]:
    """
    Remove skills that are a word-for-word prefix/subset of a longer skill.
    e.g. "version control" gets dropped when "version control systems" exists.
    Keeps the most specific (longest) version of overlapping skills.
    """
    lower = [s.lower().strip() for s in skills]
    keep = []
    for i, s in enumerate(lower):
        # Drop if any OTHER skill starts with this one and is longer
        shadowed = any(
            other.startswith(s) and other != s
            for j, other in enumerate(lower) if i != j
        )
        if not shadowed:
            keep.append(skills[i])
    return keep


def detect_skill_gaps(user_skills: List[str], job_skills: List[str]) -> List[str]:
    """Return every skill in the job that the user doesn't have."""
    user_set = set(s.lower().strip() for s in user_skills)
    job_set  = set(s.lower().strip() for s in job_skills)
    gaps = sorted(list(job_set - user_set))
    return _dedup_skills(gaps)


def rank_missing_skills(
    missing_skills: List[str],
    all_job_descriptions: List[List[str]]
) -> List[Dict]:
    freq_counter = Counter()
    for job_skills in all_job_descriptions:
        for skill in job_skills:
            freq_counter[skill.lower().strip()] += 1

    total_jobs = max(len(all_job_descriptions), 1)

    ranked = []
    for skill in missing_skills:
        skill_lower      = skill.lower().strip()
        freq             = freq_counter.get(skill_lower, 1)
        cat              = SKILL_TO_CATEGORY.get(skill_lower, "unknown")
        cat_priority     = CATEGORY_PRIORITY.get(cat, 5)
        raw_importance   = freq / total_jobs
        priority_bonus   = max(0, (10 - cat_priority)) * 0.04
        specificity      = min(len(skill.split()) * 0.02, 0.1)
        importance_score = round(min(raw_importance + priority_bonus + specificity, 1.0), 3)

        ranked.append({
            "skill":            skill,
            "importance_score": importance_score,
            "frequency":        freq,
            "category":         cat,
        })

    ranked.sort(key=lambda x: (CATEGORY_PRIORITY.get(x["category"], 5), -x["importance_score"]))
    for item in ranked:
        item.pop("category", None)

    return ranked


def get_top_priority_skills(ranked_skills: List[Dict], top_n: int = 10) -> List[Dict]:
    """Return top N priority skills, deduped."""
    top = ranked_skills[:top_n]
    # Dedup priority list too
    skills = [item["skill"] for item in top]
    deduped = set(_dedup_skills(skills))
    return [item for item in top if item["skill"] in deduped]

import re
from utils.skill_taxonomy import ALL_SKILLS

STOP_WORDS = {
    "and","or","the","with","for","from","that","this","have","has","been",
    "are","was","were","will","would","could","should","shall","a","an","in",
    "on","at","to","of","as","by","is","it","its","be","do","not","but","so",
    "yet","via","per","i","we","you","our","your","their","his","her","they",
    "also","well","very","more","most","some","all","any","both","each","when",
    "while","where","which","who","how","what","why","then","than","thus",
    "able","good","great","strong","excellent","high","low","new","current",
    "various","multiple","several","key","main","core","basic","general",
    "including","such","etc","proficiency","proficient","knowledge","skills",
    "skill","ability","abilities","experience","understanding","background",
    "demonstrated","proven","effective","professional","responsible",
    "ensuring","providing","maintaining","managing","supporting","working",
    "using","used","apply","applied","performs","performing","performed",
    "related","relevant","required","preferred","needed","minimum","must",
    "ideally","please","note","join","company","organization","role","position",
    "team","department","duties","tasks","responsibilities","candidate",
    "applicant","person","individual","employer","employee",
}

# Job posting sections that contain skills/requirements
REQUIREMENT_SECTION_HEADERS = [
    "qualifications", "requirements", "required qualifications",
    "minimum qualifications", "what you need", "what we're looking for",
    "skills required", "required skills", "technical skills", "must have",
    "key skills", "preferred qualifications", "ideal candidate",
    "you will have", "you should have", "competencies",
    "experience required", "skills & experience", "key attributes",
    "licences", "licenses", "certifications", "licence/certification",
    "application question", "experience", "key requirements",
]

# Sections to skip (company boilerplate, salary, benefits)
SKIP_SECTION_HEADERS = [
    "why join", "about us", "what we offer", "benefits", "compensation",
    "our culture", "about the company", "equal opportunity", "diversity",
    "pay", "salary", "perks", "who we are",
]

# Sections that mark end of relevant content
END_SECTION_HEADERS = [
    "apply now", "how to apply", "to apply", "interested",
    "job type", "job types", "work location", "expected hours",
    "hiring lab", "career advice", "privacy", "terms",
]


def _clean_skill(phrase: str) -> str:
    phrase = re.sub(r'\s+', ' ', phrase.strip())
    phrase = phrase.strip(".,;:•-–—()[]\"'")
    return phrase.lower().strip()


def _is_valid_skill(phrase: str) -> bool:
    phrase = phrase.strip()
    if not phrase or len(phrase) < 2 or len(phrase) > 60:
        return False
    words = phrase.lower().split()
    if len(words) > 5:
        return False
    meaningful = [w for w in words if w not in STOP_WORDS and len(w) > 1]
    if not meaningful:
        return False
    if re.match(r'^[\d\$\%\+\-\.\&]+$', phrase):
        return False
    if re.match(r'^\d+\s*[-–]\s*\d+', phrase):
        return False
    # Skip salary/price patterns
    if re.search(r'\$\d+', phrase):
        return False
    # Skip HTML entities
    if re.search(r'&[a-z]+;', phrase):
        return False
    return True


def _extract_requirement_skills(job_description: str) -> set:
    """
    Parse the qualifications/requirements sections of a job posting.
    Handles:
    - Bullet point lists
    - Comma-separated skill lists
    - "Minimum X years in Y" → extract Y
    - "Proficiency with X" → extract X
    """
    lines = job_description.split('\n')
    in_requirements = False
    in_skip = False
    req_lines = []

    for line in lines:
        stripped = line.strip()
        lower = stripped.lower()

        # Check end of relevant content
        if any(lower.startswith(h) for h in END_SECTION_HEADERS):
            in_requirements = False
            break

        # Check skip section
        if any(lower.startswith(h) for h in SKIP_SECTION_HEADERS) and len(stripped) < 60:
            in_skip = True
            in_requirements = False
            continue

        # Check requirement section start
        if any(lower == h or lower.startswith(h + ':') or lower.startswith(h + '\n')
               for h in REQUIREMENT_SECTION_HEADERS) and len(stripped) < 60:
            in_requirements = True
            in_skip = False
            continue

        # New section header resets skip flag
        if in_skip and stripped and len(stripped) < 60 and stripped[0].isupper():
            in_skip = False

        if in_requirements and not in_skip:
            req_lines.append(stripped)

    skills = set()

    # Parse each requirement line
    for line in req_lines:
        if not line:
            continue
        # Remove bullet symbols
        line = re.sub(r'^[-•*►▪◦‣]\s*', '', line)
        # Remove parentheticals like (preferred), (required), (2 years)
        line = re.sub(r'\([^)]*\)', '', line)

        # Pattern: "Minimum X years in/of Y" → extract Y
        m = re.search(r'(?:minimum|at least|\d+)\+?\s*years?\s+(?:in|of|as)\s+([^,\.\n]+)', line, re.I)
        if m:
            clean = _clean_skill(m.group(1))
            if _is_valid_skill(clean):
                skills.add(clean)

        # Pattern: "Proficiency/experience/knowledge with/in X" → extract X
        m = re.search(r'(?:proficien(?:t|cy)|experience|knowledge|expertise|skilled?|familiar(?:ity)?)\s+(?:with|in|of)\s+([^,\.\n]+)', line, re.I)
        if m:
            # Split on comma to handle "experience with A, B, and C"
            for part in re.split(r',\s*(?:and\s+)?', m.group(1)):
                clean = _clean_skill(part)
                if _is_valid_skill(clean):
                    skills.add(clean)

        # Comma-separated skill list lines (short lines, many commas)
        if ',' in line and len(line) < 200:
            parts = re.split(r',\s*(?:and\s+)?', line)
            if len(parts) >= 2:
                for part in parts:
                    clean = _clean_skill(part)
                    if _is_valid_skill(clean):
                        skills.add(clean)
            else:
                # Single item line
                clean = _clean_skill(line)
                if _is_valid_skill(clean):
                    skills.add(clean)
        else:
            # Single-item bullet point — take it as-is if short enough
            clean = _clean_skill(line)
            if _is_valid_skill(clean):
                skills.add(clean)

    return skills


def extract_job_skills(job_description: str) -> dict:
    """
    Hybrid job skill extractor:
    Layer 1 — Taxonomy matching: catches all known tech/industry skills
    Layer 2 — Requirements section parsing: catches any skill listed in
               Qualifications/Requirements blocks, regardless of field

    Works for software, security, hospitality, healthcare, finance — any job.
    Never grabs salary numbers, HTML, or boilerplate text.
    """
    text_lower = job_description.lower()

    # ── Layer 1: Taxonomy match ───────────────────────────────────────────────
    taxonomy_skills = set()
    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            taxonomy_skills.add(skill.lower())

    # ── Layer 2: Requirements section parse ───────────────────────────────────
    req_skills = _extract_requirement_skills(job_description)

    # ── Preferred section: find "nice to have" / "preferred" block ────────────
    preferred_skills = set()
    preferred_markers = ["nice to have", "nice-to-have", "preferred qualifications",
                         "assets", "desirable", "bonus points"]
    pref_start = len(job_description)
    for marker in preferred_markers:
        idx = text_lower.find(marker)
        if idx != -1 and idx < pref_start:
            pref_start = idx

    if pref_start < len(job_description):
        pref_text = job_description[pref_start:]
        pref_lower = pref_text.lower()
        for skill in ALL_SKILLS:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, pref_lower):
                preferred_skills.add(skill.lower())
        preferred_skills |= _extract_requirement_skills(pref_text)

    # ── Combine ───────────────────────────────────────────────────────────────
    all_required = taxonomy_skills | req_skills
    preferred_only = preferred_skills - all_required
    all_skills = all_required | preferred_only

    # Final cleanup — remove anything that slipped through
    def clean_final(skills_set):
        cleaned = set()
        for s in skills_set:
            s = s.strip(".,;:•-–—()[]\"'")
            if _is_valid_skill(s) and s not in STOP_WORDS:
                cleaned.add(s)
        return sorted(list(cleaned))

    return {
        "required_skills":   clean_final(all_required),
        "preferred_skills":  clean_final(preferred_only),
        "all_skills":        clean_final(all_skills),
        "total_skill_count": len(all_skills),
    }

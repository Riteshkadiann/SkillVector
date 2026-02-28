import re
import io
import pdfplumber
from utils.skill_taxonomy import ALL_SKILLS

# ─── Stop words — never a skill on their own ─────────────────────────────────
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
    "related","relevant","required","preferred","needed",
}

# ─── Section headers that signal the SKILLS block in a resume ────────────────
SKILLS_SECTION_HEADERS = [
    "skills", "skills & certifications", "skills and certifications",
    "technical skills", "core skills", "key skills", "competencies",
    "core competencies", "certifications", "qualifications",
    "skills & qualifications", "tools & technologies", "areas of expertise",
    "expertise", "proficiencies", "technologies", "tools",
    "licenses", "licences", "certificates",
]

# ─── Headers that mark the END of a skills section ───────────────────────────
END_SECTION_HEADERS = [
    "experience", "work experience", "employment", "education",
    "projects", "awards", "references", "objective", "summary",
    "profile", "interests", "volunteer", "publications",
]

def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        raise ValueError(f"Failed to parse PDF: {str(e)}")
    return text


def _clean_skill(phrase: str) -> str:
    """Normalize a skill candidate."""
    phrase = re.sub(r'\s+', ' ', phrase.strip())
    phrase = phrase.strip(".,;:•-–—()[]\"'")
    return phrase.lower().strip()


def _is_valid_skill(phrase: str) -> bool:
    """
    A valid skill is:
    - 1–5 words long
    - Not purely a stop word
    - Not a number or salary
    - Not a full sentence (no verb indicators)
    - At least 2 characters
    """
    phrase = phrase.strip()
    if not phrase or len(phrase) < 2 or len(phrase) > 60:
        return False
    words = phrase.lower().split()
    if len(words) > 5:
        return False
    # Must have at least one meaningful word
    meaningful = [w for w in words if w not in STOP_WORDS and len(w) > 1]
    if not meaningful:
        return False
    # Skip numbers, salaries, percentages
    if re.match(r'^[\d\$\%\+\-\.]+$', phrase):
        return False
    # Skip year ranges
    if re.match(r'^\d{4}\s*[-–]\s*(\d{4}|present)', phrase.lower()):
        return False
    return True


def _extract_skills_section(text: str) -> list:
    """
    Find and parse the dedicated Skills section of a resume.
    Returns a clean list of skill strings found there.
    """
    lines = text.split('\n')
    in_skills = False
    skills_lines = []

    for line in lines:
        stripped = line.strip()
        lower = stripped.lower()

        # Check if this line IS a skills section header
        if any(lower == h or lower.startswith(h + ' ') or lower.startswith(h + ':')
               for h in SKILLS_SECTION_HEADERS):
            in_skills = True
            continue

        # Check if we've hit a new major section (end of skills)
        if in_skills and stripped:
            # A line that's a section header ends the skills block
            if (len(stripped) < 50 and
                any(lower == h or lower.startswith(h + ' ') or lower.startswith(h + ':')
                    for h in END_SECTION_HEADERS)):
                break
            # Also stop at lines that look like job titles (all caps or title case + pipe/dash + company)
            if re.match(r'^[A-Z][a-zA-Z\s]+[\|\-–]\s*[A-Z]', stripped) and len(stripped) < 80:
                break

        if in_skills:
            skills_lines.append(stripped)

    if not skills_lines:
        return []

    # Parse skills from the collected lines
    skills = set()
    full_text = ' '.join(skills_lines)

    # Split on common delimiters: comma, bullet, pipe, semicolon, period-space
    raw_items = re.split(r'[,•\|;\n]+', full_text)

    for item in raw_items:
        # Handle "Certified in X, Y, Z" → extract X, Y, Z
        item = re.sub(r'^(certified in|proficient in|experience in|knowledge of|skilled in|holds a|valid)\s+',
                      '', item.lower().strip())
        # Remove parenthetical notes
        item = re.sub(r'\(.*?\)', '', item)
        clean = _clean_skill(item)
        if _is_valid_skill(clean):
            skills.add(clean)

    return list(skills)


def extract_skills_from_text(text: str) -> list:
    """
    Hybrid extraction:
    Layer 1 — Taxonomy matching (catches all known tech/soft skills)
    Layer 2 — Skills section parsing (catches ANY skill listed in the resume's skills block)
    """
    text_lower = text.lower()
    found = set()

    # ── Layer 1: Taxonomy match ───────────────────────────────────────────────
    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found.add(skill.lower())

    # ── Layer 2: Skills section parse ─────────────────────────────────────────
    section_skills = _extract_skills_section(text)
    for s in section_skills:
        if _is_valid_skill(s):
            found.add(s)

    return sorted(list(found))


def parse_resume(text: str) -> dict:
    skills = extract_skills_from_text(text)

    exp_matches = re.findall(r'(\d+)\+?\s*years?\s*(?:of\s*)?(?:experience|exp)', text.lower())
    years_exp = max([int(y) for y in exp_matches], default=0)

    education = "unknown"
    if re.search(r'\b(phd|doctorate|ph\.d)\b', text.lower()):
        education = "phd"
    elif re.search(r'\b(master|msc|mba|m\.s|m\.eng)\b', text.lower()):
        education = "masters"
    elif re.search(r'\b(bachelor|bsc|b\.s|b\.tech|b\.e|honours|honor)\b', text.lower()):
        education = "bachelors"
    elif re.search(r'\b(diploma|certificate|college)\b', text.lower()):
        education = "diploma"
    elif re.search(r'\b(high school|secondary school|ged)\b', text.lower()):
        education = "high_school"

    return {
        "skills":           skills,
        "years_experience": years_exp,
        "education":        education,
        "skill_count":      len(skills),
    }

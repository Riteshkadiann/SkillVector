"""
Optional Job Scraper Script
Scrapes job descriptions from a given URL or text input for analysis.

Usage:
    python job_scraper.py --url "https://ca.indeed.com/viewjob?jk=12345"
    python job_scraper.py --search "backend engineer" --location "remote"
"""

import requests
from bs4 import BeautifulSoup
import json
import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from core.job_analyzer import extract_job_skills


def scrape_job_from_url(url: str) -> dict:
    """
    Generic job scraper - extracts text from a job posting URL.
    Works best with simple HTML job pages.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch URL: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove script/style tags
    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()

    # Try to find main job content
    content = ""
    for selector in ['.job-description', '.description', 'main', 'article', '#job-details']:
        el = soup.select_one(selector)
        if el:
            content = el.get_text(separator=' ', strip=True)
            break

    # Fallback: grab all text
    if not content:
        content = soup.get_text(separator=' ', strip=True)

    # Limit to reasonable length
    content = content[:5000]

    print(f"✅ Scraped {len(content)} characters from {url}")
    return {"raw_text": content, "source_url": url}


def analyze_scraped_job(raw_text: str, job_title: str = "Unknown") -> dict:
    """Analyze a scraped job description."""
    skills_data = extract_job_skills(raw_text)
    return {
        "job_title": job_title,
        "required_skills": skills_data["required_skills"],
        "preferred_skills": skills_data["preferred_skills"],
        "all_skills": skills_data["all_skills"],
        "total_skills": skills_data["total_skill_count"]
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape and analyze job descriptions")
    parser.add_argument("--url", help="Job posting URL to scrape")
    parser.add_argument("--title", default="Software Engineer", help="Job title")
    args = parser.parse_args()

    if args.url:
        scraped = scrape_job_from_url(args.url)
        if scraped.get("raw_text"):
            result = analyze_scraped_job(scraped["raw_text"], args.title)
            print("\n📊 Extracted Skills:")
            print(json.dumps(result, indent=2))
    else:
        # Demo mode with sample job text
        sample_job = """
        We are looking for a Backend Engineer with strong Python and FastAPI experience.
        You should know Docker, PostgreSQL, and AWS.
        Experience with Kubernetes and Redis is a plus.
        We use React on the frontend so some knowledge is helpful.
        You should be comfortable with Git, agile workflows, and system design.
        Nice to have: Terraform, Kafka, Spark experience.
        """
        print("🔍 Demo mode - analyzing sample job description...")
        result = analyze_scraped_job(sample_job, "Backend Engineer")
        print("\n📊 Extracted Skills:")
        print(json.dumps(result, indent=2))

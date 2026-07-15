"""
Driver script: builds the College & Career Financial Planning course site,
student workbook, and teacher slide deck from ccr-financial-planning/content/.
Run: python3 build_ccr_site.py
"""
import importlib.util
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_course_site import build_site
from build_workbook_docx import build_workbook
from build_teacher_pptx import build_pptx


def load_package(pkg_name, init_path, pkg_dir):
    spec = importlib.util.spec_from_file_location(pkg_name, init_path, submodule_search_locations=[pkg_dir])
    mod = importlib.util.module_from_spec(spec)
    sys.modules[pkg_name] = mod
    spec.loader.exec_module(mod)
    return mod

ROOT = os.path.dirname(os.path.abspath(__file__))
content = load_package(
    "ccr_content",
    os.path.join(ROOT, "ccr-financial-planning/content/__init__.py"),
    os.path.join(ROOT, "ccr-financial-planning/content"),
)
UNITS = content.UNITS

GITHUB_PAGES_BASE = "https://milesclawson.github.io/test-repo"

COURSE_TITLE = "College & Career Financial Planning"
SCHOOL_NAME = "ISD 197 — Two Rivers High School"
GRADE = "Grades 11-12"
SEMESTER_LABEL = "One Semester · 82 Days"

THEME = {
    "primary": "#1B5E3C",       # money green
    "primary_dk": "#0F3D28",
    "accent": "#F0C14B",        # gold
    "accent_lt": "#FFF8E1",
}

DOWNLOADS = [
    {"file": f"{GITHUB_PAGES_BASE}/downloads/ccr_financial_planning_teacher_slides.pptx",
     "label": "Teacher Slide Deck (PPTX)", "icon": "🖥️",
     "desc": "One slide per lesson, 82 lessons total. Import directly into Google Slides."},
    {"file": f"{GITHUB_PAGES_BASE}/downloads/ccr_financial_planning_student_workbook.docx",
     "label": "Student Workbook (DOCX)", "icon": "📓",
     "desc": "Printable workbook: vocab, warm-ups, guided notes, activities, readings, quizzes, and exit tickets for every lesson."},
]

if __name__ == "__main__":
    downloads_dir = os.path.join(ROOT, "downloads")
    os.makedirs(downloads_dir, exist_ok=True)

    site_path = build_site(
        output_path=os.path.join(ROOT, "ccr-financial-planning", "index.html"),
        course_title=COURSE_TITLE,
        school_name=SCHOOL_NAME,
        grade=GRADE,
        semester_label=SEMESTER_LABEL,
        theme=THEME,
        hero_icon="💵",
        hero_tagline=("Prepares students for the financial realities of life after high school: "
                       "financial psychology, careers and college costs, credit, taxes, insurance, "
                       "and investing. Final assessment: YouScience General Financial Literacy Certification."),
        units=UNITS,
        downloads=DOWNLOADS,
        footer_note="College & Career Financial Planning — ISD 197, Two Rivers High School. Satisfies Minnesota's personal-finance graduation requirement.",
        assessment_label="Unit Assessment",
    )
    print("Site built:", site_path)

    workbook_path = build_workbook(
        output_path=os.path.join(downloads_dir, "ccr_financial_planning_student_workbook.docx"),
        course_title=COURSE_TITLE,
        school_name=SCHOOL_NAME,
        grade=GRADE,
        semester_label=SEMESTER_LABEL,
        primary_hex=THEME["primary"],
        primary_dk_hex=THEME["primary_dk"],
        accent_hex=THEME["accent"],
        units=UNITS,
        intro_text=("This workbook covers all 82 lessons of College & Career Financial Planning. "
                     "It follows the real course scope and sequence: financial psychology, careers and "
                     "majors, selecting a college, applying to college, financial aid, budgeting, taxes "
                     "and credit, career readiness and risk management, and investing."),
    )
    print("Workbook built:", workbook_path)

    pptx_path = build_pptx(
        output_path=os.path.join(downloads_dir, "ccr_financial_planning_teacher_slides.pptx"),
        course_title=COURSE_TITLE,
        school_name=SCHOOL_NAME,
        grade=GRADE,
        semester_label=SEMESTER_LABEL,
        primary_hex=THEME["primary"],
        primary_dk_hex=THEME["primary_dk"],
        accent_hex=THEME["accent"],
        units=UNITS,
        hero_icon="💵",
    )
    print("Slides built:", pptx_path)

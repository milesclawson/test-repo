"""
Driver script: builds the Student Technology Help Desk course site, student
workbook, and teacher slide deck from student-help-desk/content/.
Run: python3 build_helpdesk_site.py
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
    "hd_content",
    os.path.join(ROOT, "student-help-desk/content/__init__.py"),
    os.path.join(ROOT, "student-help-desk/content"),
)
UNITS = content.UNITS

GITHUB_PAGES_BASE = "https://milesclawson.github.io/test-repo"

COURSE_TITLE = "Student Technology Help Desk"
SCHOOL_NAME = "ISD 197 — Two Rivers High School"
GRADE = "Grades 10-12 · Instructor Approval"
SEMESTER_LABEL = "One Semester · 82 Days"

THEME = {
    "primary": "#0E6E8C",       # tech teal
    "primary_dk": "#083E4E",
    "accent": "#FF8A3D",        # circuit orange
    "accent_lt": "#FFF1E6",
}

DOWNLOADS = [
    {"file": f"{GITHUB_PAGES_BASE}/downloads/student_help_desk_teacher_slides.pptx",
     "label": "Teacher Slide Deck (PPTX)", "icon": "🖥️",
     "desc": "One slide per lesson, 82 lessons total. Import directly into Google Slides."},
    {"file": f"{GITHUB_PAGES_BASE}/downloads/student_help_desk_student_workbook.docx",
     "label": "Student Workbook (DOCX)", "icon": "📓",
     "desc": "Printable workbook: vocab, warm-ups, guided notes, activities, readings, quizzes, and exit tickets for every lesson."},
]

if __name__ == "__main__":
    downloads_dir = os.path.join(ROOT, "downloads")
    os.makedirs(downloads_dir, exist_ok=True)

    site_path = build_site(
        output_path=os.path.join(ROOT, "student-help-desk", "index.html"),
        course_title=COURSE_TITLE,
        school_name=SCHOOL_NAME,
        grade=GRADE,
        semester_label=SEMESTER_LABEL,
        theme=THEME,
        hero_icon="🛠️",
        hero_tagline=("A hands-on IT course: run a real help desk, take real tickets, repair real "
                       "Chromebooks, and work toward industry certifications including CompTIA A+, "
                       "the Google IT Support Certificate, and the AVIXA AV Technologist credential."),
        units=UNITS,
        downloads=DOWNLOADS,
        footer_note="Student Technology Help Desk — ISD 197, Two Rivers High School, Media/Library Department.",
        assessment_label="Phase Assessment",
    )
    print("Site built:", site_path)

    workbook_path = build_workbook(
        output_path=os.path.join(downloads_dir, "student_help_desk_student_workbook.docx"),
        course_title=COURSE_TITLE,
        school_name=SCHOOL_NAME,
        grade=GRADE,
        semester_label=SEMESTER_LABEL,
        primary_hex=THEME["primary"],
        primary_dk_hex=THEME["primary_dk"],
        accent_hex=THEME["accent"],
        units=UNITS,
        intro_text=("This workbook covers all 82 lessons of Student Technology Help Desk, across five "
                     "phases: Foundations & Professionalism, Chromebook Mastery & Repair, Networking & "
                     "Classroom Tech, Professional Certification Intensive, and Capstone & Future Pathways."),
    )
    print("Workbook built:", workbook_path)

    pptx_path = build_pptx(
        output_path=os.path.join(downloads_dir, "student_help_desk_teacher_slides.pptx"),
        course_title=COURSE_TITLE,
        school_name=SCHOOL_NAME,
        grade=GRADE,
        semester_label=SEMESTER_LABEL,
        primary_hex=THEME["primary"],
        primary_dk_hex=THEME["primary_dk"],
        accent_hex=THEME["accent"],
        units=UNITS,
        hero_icon="🛠️",
    )
    print("Slides built:", pptx_path)

"""Builds every Whole Foods and Nutrition output from content/.

Run from this folder:  python3 build_wfn.py
Outputs:
  site/                       accessible bilingual website (open site/index.html)
  site/downloads/             Word workbooks, recipe cards, teacher guides, slide decks (EN/ES)
  quia/                       Quia text-file question imports
  accessibility-report.md     automated accessibility audit
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from content import UNITS  # noqa: E402
from build import site as site_b, docx_builder as dx, pptx_builder as px, quia as qb, a11y_audit, budget  # noqa: E402

SITE = os.path.join(ROOT, "site")
DL = os.path.join(SITE, "downloads")
QUIA = os.path.join(ROOT, "quia")


def main():
    os.makedirs(DL, exist_ok=True)
    downloads = []
    for u in UNITS:
        n = f"unit{u['number']:02d}"
        for lang, nm in (("en", "English"), ("es", "Español")):
            dx.build_workbook(u, lang, os.path.join(DL, f"{n}_student_workbook_{lang}.docx"))
            dx.build_recipe_cards(u, lang, os.path.join(DL, f"{n}_recipe_cards_{lang}.docx"))
            px.build_deck(u, lang, os.path.join(DL, f"{n}_teacher_slides_{lang}.pptx"))
            downloads += [
                {"href": f"downloads/{n}_student_workbook_{lang}.docx", "label": f"Unit {u['number']} student workbook ({nm}, Word)"},
                {"href": f"downloads/{n}_recipe_cards_{lang}.docx", "label": f"Unit {u['number']} recipe cards ({nm}, Word)"},
                {"href": f"downloads/{n}_teacher_slides_{lang}.pptx", "label": f"Unit {u['number']} slides ({nm}, PowerPoint)"},
            ]
        dx.build_teacher_guide(u, os.path.join(DL, f"{n}_teacher_guide.docx"))
        qb.build_quia(u, QUIA)
    site_b.build_site(UNITS, SITE, downloads)
    total, labs = budget.report(UNITS, os.path.join(ROOT, "budget-report.md"))
    print(f"Budget so far: {labs} labs, ${total:,.2f}")
    fails = a11y_audit.run(SITE, DL, os.path.join(ROOT, "accessibility-report.md"))
    print(f"Built {len(UNITS)} unit(s). Automated accessibility failures: {fails}")
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)

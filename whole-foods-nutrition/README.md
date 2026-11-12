# Whole Foods and Nutrition — course package

One semester · 90 days · 48 minutes · Grades 11–12 · aligned to YouScience Nutrition and Wellness (Exam 2001).
Scope and sequence: `00-scope-and-sequence.md`. Cert source: `source/Nutrition-and-Wellness.pdf`.

## What is built so far
**Units 1–4 (days 1–21, 9 labs) are complete:** Lab Procedures and Safety Foundations, Math in the Kitchen, Kitchen Equipment and Knife Skills, and The Six Nutrient Classes. Each has a reading, vocabulary, daily lessons, recipes, a 12-question quiz, and a practical rubric, in English and Spanish.
Units 5–19 follow the pacing in `00-scope-and-sequence.md`.
`budget-report.md` totals the estimated food cost of every lab written so far against the $1,000 course budget.

## Open the outputs
| What | Where |
|---|---|
| Student site (English / Español / both) | `site/index.html` (open in any browser, or host the `site/` folder) |
| Student workbook, recipe cards (EN and ES, Word) | `site/downloads/` |
| Teacher guide with answer keys and rubric (Word) | `site/downloads/unitNN_teacher_guide.docx` |
| Teacher slides (EN and ES, PowerPoint) | `site/downloads/` |
| Quia question imports (EN and ES) | `quia/` |
| Food budget tracker | `budget-report.md` |
| Accessibility audit | `accessibility-report.md` |

## How a teacher edits and rebuilds
All content lives in `content/unitNN.py`. Every student-facing sentence is a pair: `T("English", "Español")`.
1. Edit the text in `content/unit01.py` (lessons, recipes, quiz questions, rubric).
2. Run `python3 build_wfn.py` from this folder. Every output is regenerated from the same data, so the site, workbooks, slides, recipes and Quia files never disagree.
3. Check `accessibility-report.md`. The build exits with an error if an automated check fails.

Needs: `pip install python-docx python-pptx`.

To add a unit, copy `content/unit01.py` to `unitNN.py`, edit it, and add it to `content/__init__.py`.
Class layout (8 groups of 4) and group jobs are in `content/common.py`.

## Importing a quiz into Quia
1. Log in to Quia, choose **Question bank**, then **Import questions**, pick `quia/unitNN_quia_questions_en.txt` (or `_es`), and Import.
2. **Test with one question first.** The files follow Quia's published text-import rules (type code on its own line, `*` before the correct choice, `Points:` setting, blank line between questions), but they have not been imported into a live Quia account. If anything is off, export one existing question from your Question bank (Actions > Export selected questions) and compare.
3. `quia/unitNN_quiz_blueprint.csv` maps each question to its certification objective.

## Accessibility (WCAG 2.1 AA / Section 508)
Built in: real headings and lists, table header rows with captions, language tags on every English and Spanish passage, 12pt+ text in documents and 18pt+ in slides, high-contrast colors checked for light and dark modes, keyboard-operable language switch with a skip link, no meaning conveyed by color alone, answer spaces that are labeled cells instead of underscores.

Not automated, so do these before distributing: Word and PowerPoint Accessibility Checker, one screen-reader pass (NVDA or VoiceOver), and a tagged PDF export from Word if you need PDFs (this build makes Word files, not PDFs). The bottom of `accessibility-report.md` lists them.

## Known limits
- **Spanish has not been reviewed by a fluent speaker.** It was machine-assisted. Have a Spanish teacher or qualified translator review it, especially food-safety temperatures and instructions, before students rely on it.
- Cost estimates are rough (about $2–3 per group per lab). Check current prices against your budget.
- Food safety temperatures and handwashing steps follow CDC and USDA guidance. Use your district's approved sanitizer and strength.
- Course policies on Day 1 (grading, retakes, lab eligibility) come from the current syllabus; update `content/unit01.py` if the syllabus changes.
- Peanut-free kitchen: every recipe tells students to check labels. Almond milk (Unit 15) uses tree nuts. The Almond Cow also makes oat milk, which is the nut-allergy track (clean the shared machine thoroughly and run the oat batch first).
- Quiz answer order is shuffled in a repeatable way (`content/__init__.py`); numeric choices stay in order.
- The slides and Word files were checked by script only. They were not opened in PowerPoint or Word.

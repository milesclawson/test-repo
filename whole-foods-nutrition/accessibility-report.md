# Accessibility audit (automated)

Standard targeted: WCAG 2.1 AA / Section 508. This report covers automated structural checks only.

## Color contrast (WCAG AA needs 4.5:1 for normal text)

| Pair | Mode | Ratio | Result |
|---|---|---|---|
| text on background (#1a1a1a on #ffffff) | light | 17.4:1 | PASS |
| muted text (#4a4a4a on #ffffff) | light | 8.9:1 | PASS |
| header text (#ffffff on #1b5e3a) | light | 7.8:1 | PASS |
| link (#0b4f8a on #ffffff) | light | 8.4:1 | PASS |
| link on panel (#0b4f8a on #f2f7f3) | light | 7.8:1 | PASS |
| note text (#5c3200 on #fff4e0) | light | 10.1:1 | PASS |
| heading green on white (#1b5e3a on #ffffff) | light | 7.8:1 | PASS |
| text on background (#f2f2f2 on #121512) | dark | 16.4:1 | PASS |
| muted text (#cfd6d1 on #121512) | dark | 12.4:1 | PASS |
| header text (#0c1f14 on #8fd3a7) | dark | 9.9:1 | PASS |
| link (#9cc9f5 on #121512) | dark | 10.6:1 | PASS |
| link on panel (#9cc9f5 on #1c241f) | dark | 9.1:1 | PASS |
| note text (#ffd9a3 on #2c2111) | dark | 11.8:1 | PASS |

## Website

- `index.html`: all 8 checks passed
- `unit-01.html`: all 8 checks passed
- `unit-02.html`: all 8 checks passed
- `unit-03.html`: all 8 checks passed
- `unit-04.html`: all 8 checks passed

## Word documents

- `unit01_recipe_cards_en.docx`: all 8 checks passed
- `unit01_recipe_cards_es.docx`: all 8 checks passed
- `unit01_student_workbook_en.docx`: all 8 checks passed
- `unit01_student_workbook_es.docx`: all 8 checks passed
- `unit01_teacher_guide.docx`: all 8 checks passed
- `unit02_recipe_cards_en.docx`: all 8 checks passed
- `unit02_recipe_cards_es.docx`: all 8 checks passed
- `unit02_student_workbook_en.docx`: all 8 checks passed
- `unit02_student_workbook_es.docx`: all 8 checks passed
- `unit02_teacher_guide.docx`: all 8 checks passed
- `unit03_recipe_cards_en.docx`: all 8 checks passed
- `unit03_recipe_cards_es.docx`: all 8 checks passed
- `unit03_student_workbook_en.docx`: all 8 checks passed
- `unit03_student_workbook_es.docx`: all 8 checks passed
- `unit03_teacher_guide.docx`: all 8 checks passed
- `unit04_recipe_cards_en.docx`: all 8 checks passed
- `unit04_recipe_cards_es.docx`: all 8 checks passed
- `unit04_student_workbook_en.docx`: all 8 checks passed
- `unit04_student_workbook_es.docx`: all 8 checks passed
- `unit04_teacher_guide.docx`: all 8 checks passed

## Slide decks

- `unit01_teacher_slides_en.pptx`: all 5 checks passed
- `unit01_teacher_slides_es.pptx`: all 5 checks passed
- `unit02_teacher_slides_en.pptx`: all 5 checks passed
- `unit02_teacher_slides_es.pptx`: all 5 checks passed
- `unit03_teacher_slides_en.pptx`: all 5 checks passed
- `unit03_teacher_slides_es.pptx`: all 5 checks passed
- `unit04_teacher_slides_en.pptx`: all 5 checks passed
- `unit04_teacher_slides_es.pptx`: all 5 checks passed

## Not covered by this automated audit (do before distributing)

- Run Microsoft Office Accessibility Checker on each .docx and .pptx.
- Read one page of the site and one Word file with a screen reader (NVDA on Windows, VoiceOver on Mac/iOS) in both languages.
- Export PDFs from Word with the 'Document structure tags for accessibility' option checked, then run Adobe's PDF accessibility check. This build does not generate PDFs.
- Add captions and a transcript for any video or audio you add later.
- Spanish text needs review by a fluent speaker, including the `lang` tags on every passage.
- Keyboard-only walkthrough of the site (Tab through the language buttons and links).

**Result:** PASS - no automated failures

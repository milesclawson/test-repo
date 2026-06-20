"""
Warrior Prep — Student Workbook PDF Builder
Run: python3 warrior_prep_pdf.py
Generates: output/warrior_prep_student_workbook.pdf
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import Color, HexColor, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas as pdfcanvas

from content import UNITS, SCHOOL_NAME, COURSE_TITLE, GRADE
from lesson_meta import BELL_RINGERS, LESSON_TIMING

os.makedirs("output", exist_ok=True)

WARRIOR_RED  = HexColor("#C71414")
WARRIOR_DARK = HexColor("#212121")
WARRIOR_LITE = HexColor("#F5F5F5")
WARRIOR_GOLD = HexColor("#F5E0B2")
CREAM        = HexColor("#FDFAF4")
NOTE_BLUE    = HexColor("#E8F0FE")
RULED_LINE   = HexColor("#C8D0DC")
PAGE_W, PAGE_H = letter


def color_from_tuple(t):
    if isinstance(t, (list, tuple)) and len(t) == 3:
        return Color(t[0], t[1], t[2])
    return WARRIOR_RED


def S(name):
    return STYLES[name]


STYLES = {
    "cover_title":  ParagraphStyle("cover_title",  fontName="Helvetica-Bold",    fontSize=38, textColor=white,       leading=44, alignment=TA_CENTER),
    "cover_sub":    ParagraphStyle("cover_sub",    fontName="Helvetica",          fontSize=16, textColor=WARRIOR_GOLD, leading=22, alignment=TA_CENTER),
    "cover_school": ParagraphStyle("cover_school", fontName="Helvetica",          fontSize=11, textColor=white,       leading=16, alignment=TA_CENTER),
    "unit_title":   ParagraphStyle("unit_title",   fontName="Helvetica-Bold",     fontSize=28, textColor=white,       leading=34),
    "unit_num":     ParagraphStyle("unit_num",     fontName="Helvetica",          fontSize=15, textColor=WARRIOR_GOLD, leading=20),
    "unit_overview":ParagraphStyle("unit_overview",fontName="Helvetica",          fontSize=11, textColor=white,       leading=17),
    "unit_vocab_hdr":ParagraphStyle("unit_vocab_hdr",fontName="Helvetica-Bold",   fontSize=11, textColor=WARRIOR_GOLD,leading=16),
    "unit_vocab":   ParagraphStyle("unit_vocab",   fontName="Helvetica",          fontSize=9,  textColor=white,       leading=14),
    "lesson_title": ParagraphStyle("lesson_title", fontName="Helvetica-Bold",     fontSize=17, textColor=WARRIOR_RED, leading=22, spaceAfter=4),
    "sec_head":     ParagraphStyle("sec_head",     fontName="Helvetica-Bold",     fontSize=11, textColor=WARRIOR_DARK,leading=15, spaceBefore=8, spaceAfter=3),
    "body":         ParagraphStyle("body",         fontName="Helvetica",          fontSize=10, textColor=WARRIOR_DARK,leading=15, spaceAfter=5),
    "body_bold":    ParagraphStyle("body_bold",    fontName="Helvetica-Bold",     fontSize=10, textColor=WARRIOR_DARK,leading=15, spaceAfter=5),
    "small":        ParagraphStyle("small",        fontName="Helvetica",          fontSize=8,  textColor=WARRIOR_DARK,leading=11),
    "small_bold":   ParagraphStyle("small_bold",   fontName="Helvetica-Bold",     fontSize=8,  textColor=WARRIOR_DARK,leading=11),
    "small_it":     ParagraphStyle("small_it",     fontName="Helvetica-Oblique",  fontSize=8,  textColor=HexColor("#444444"), leading=11),
    "vocab_word":   ParagraphStyle("vocab_word",   fontName="Helvetica-Bold",     fontSize=11, textColor=WARRIOR_RED, leading=15),
    "vocab_etym":   ParagraphStyle("vocab_etym",   fontName="Helvetica-Oblique",  fontSize=8,  textColor=HexColor("#666666"), leading=12),
    "vocab_def":    ParagraphStyle("vocab_def",    fontName="Helvetica",          fontSize=9,  textColor=WARRIOR_DARK,leading=13),
    "obj":          ParagraphStyle("obj",          fontName="Helvetica",          fontSize=9.5,textColor=WARRIOR_DARK,leading=13, leftIndent=10, spaceAfter=3),
    "planner_hdr":  ParagraphStyle("planner_hdr",  fontName="Helvetica-Bold",     fontSize=8,  textColor=white,       leading=11, alignment=TA_CENTER),
    "planner_label":ParagraphStyle("planner_label",fontName="Helvetica-Bold",     fontSize=8,  textColor=WARRIOR_DARK,leading=11, alignment=TA_CENTER),
    "planner_cell": ParagraphStyle("planner_cell", fontName="Helvetica",          fontSize=7,  textColor=WARRIOR_DARK,leading=10),
    "test_q":       ParagraphStyle("test_q",       fontName="Helvetica",          fontSize=10, textColor=WARRIOR_DARK,leading=15, leftIndent=6, spaceAfter=3),
    "et_prompt":    ParagraphStyle("et_prompt",    fontName="Helvetica",          fontSize=9.5,textColor=WARRIOR_DARK,leading=14),
    "et_stem":      ParagraphStyle("et_stem",      fontName="Helvetica-Oblique",  fontSize=9.5,textColor=HexColor("#333333"),leading=14),
    "centered":     ParagraphStyle("centered",     fontName="Helvetica",          fontSize=9,  textColor=WARRIOR_DARK,leading=13, alignment=TA_CENTER),
    "h3":           ParagraphStyle("h3",           fontName="Helvetica-Bold",     fontSize=9.5,textColor=WARRIOR_DARK,leading=13, spaceAfter=2, spaceBefore=4),
    "htag_white":   ParagraphStyle("htag_white",   fontName="Helvetica-Bold",     fontSize=9.5,textColor=white,       leading=13),
}


class FooterCanvas(pdfcanvas.Canvas):
    def __init__(self, *args, **kwargs):
        self._saved_page_states = []
        super().__init__(*args, **kwargs)

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_footer()
            super().showPage()
        super().save()

    def _draw_footer(self):
        self.saveState()
        self.setFont("Helvetica", 7.5)
        self.setFillColor(HexColor("#888888"))
        self.drawCentredString(PAGE_W / 2, 0.38 * inch,
            f"{COURSE_TITLE}  ·  Student Workbook  ·  {SCHOOL_NAME}  ·  Page {self._pageNumber}")
        self.setStrokeColor(WARRIOR_RED)
        self.setLineWidth(0.8)
        self.line(inch, 0.54 * inch, PAGE_W - inch, 0.54 * inch)
        self.restoreState()


def ruled(n, w, h=17):
    rows = [[Paragraph("", S("small"))] for _ in range(n)]
    t = Table(rows, colWidths=[w], rowHeights=[h] * n)
    t.setStyle(TableStyle(
        [("LINEBELOW", (0, i), (0, i), 0.4, RULED_LINE) for i in range(n)] +
        [("TOPPADDING", (0, 0), (-1, -1), 1),
         ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
         ("LEFTPADDING", (0, 0), (-1, -1), 3)]
    ))
    return t


def div(text, color=WARRIOR_RED, w=6.5 * inch):
    t = Table([[Paragraph(f"<b>{text}</b>", S("htag_white"))]], colWidths=[w])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def box(label, w, h, bg=None):
    bg = bg or WARRIOR_LITE
    t = Table([[Paragraph(label, S("small"))]], colWidths=[w], rowHeights=[h])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#AAAAAA")),
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


# ────────────────────────────────────────────────────────────────────────────
def build_cover(story):
    inner = [
        Spacer(1, 1.4 * inch),
        Paragraph(COURSE_TITLE, S("cover_title")),
        Spacer(1, 0.12 * inch),
        Paragraph("Student Workbook", S("cover_sub")),
        Spacer(1, 0.35 * inch),
        HRFlowable(width="75%", thickness=1, color=WARRIOR_GOLD, spaceAfter=10),
        Spacer(1, 0.25 * inch),
        Paragraph(f"{GRADE}  ·  Semester Elective", S("cover_sub")),
        Spacer(1, 0.15 * inch),
        Paragraph(SCHOOL_NAME, S("cover_school")),
        Spacer(1, 1.8 * inch),
        Paragraph("Name: ________________________________   Period: ________", S("cover_school")),
        Spacer(1, 0.18 * inch),
        Paragraph("Teacher: ______________________________   Year: __________", S("cover_school")),
    ]
    t = Table([[inner]], colWidths=[6.5 * inch], rowHeights=[9.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_DARK),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)
    story.append(PageBreak())


def build_how_to_use(story):
    story.append(div("HOW TO USE THIS WORKBOOK"))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("Welcome to Warrior Prep!", S("lesson_title")))
    story.append(Paragraph(
        "This workbook is your guide, notebook, and planner for the entire semester. "
        "Here is what's inside and how to get the most out of it.", S("body")))
    story.append(Spacer(1, 0.08 * inch))
    items = [
        ("Bell Ringer (every lesson)",
         "Each lesson starts with a 5-minute bell ringer — a warm-up you begin the moment you sit down. "
         "There are three types: LAUNCH (connects to your own experience), REVIEW (retrieves what you learned last class), "
         "and ANTICIPATION (challenges you to predict or take a position). Write your response before sharing."),
        ("Planner Section (Weeks 1–18)",
         "Starts right after this page. One page per week — use it for ALL six of your courses, "
         "not just Warrior Prep. Write assignments, tests, and projects the day they are assigned."),
        ("Cornell Notes Pages",
         "Every lesson has a Cornell Notes page. Left column = essential questions. Right column = notes. "
         "Bottom = summary in YOUR own words. Early lessons have support built in; later lessons are yours to fill."),
        ("Vocabulary & Morphology",
         "Each lesson has a Word Focus box with the word's etymology (its roots). Learning word roots "
         "helps you understand and remember new vocabulary — and figure out words you've never seen."),
        ("Readings & Comprehension Questions",
         "Every lesson includes a reading passage and five questions. Annotate as you read using your symbols "
         "(* important, ? question, ! surprising, → connection, circle = vocabulary). Answer questions in complete sentences."),
        ("Exit Tickets",
         "The last box in each lesson is your exit ticket. Complete it before or at the end of class. "
         "Formats vary — quick writes, 3-2-1s, sentence stems, vocabulary checks, and more."),
        ("Pre-Tests & Post-Tests",
         "Each unit starts with a pre-test (NOT graded for correctness) and ends with a post-test. "
         "Together they show how far you've grown over the unit."),
    ]
    for title, desc in items:
        story.append(Paragraph(f"<b>{title}</b>", S("body_bold")))
        story.append(Paragraph(desc, S("body")))
        story.append(Spacer(1, 0.04 * inch))

    story.append(Spacer(1, 0.12 * inch))
    story.append(div("AVID CORNELL NOTES — HOW THEY WORK", color=WARRIOR_DARK))
    story.append(Spacer(1, 0.08 * inch))

    ref = Table(
        [
            [Paragraph("LEFT COLUMN\n(Questions/Cues)", S("small_bold")),
             Paragraph("RIGHT COLUMN\n(Notes)", S("small_bold")),
             Paragraph("BOTTOM\n(Summary)", S("small_bold"))],
            [Paragraph("Essential questions,\nkey terms, cues.\n\nFill in DURING\nor right AFTER notes.", S("small")),
             Paragraph("Main notes, facts, ideas, examples.\nIn your OWN words.\n\nLeave space to add later.", S("small")),
             Paragraph("3–5 sentences\nafter the lesson.\n\nNO peeking!\nYour words only.", S("small"))],
        ],
        colWidths=[1.9 * inch, 2.9 * inch, 1.7 * inch]
    )
    ref.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, WARRIOR_DARK),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, HexColor("#AAAAAA")),
        ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_RED),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("BACKGROUND", (0, 1), (-1, 1), WARRIOR_LITE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(ref)
    story.append(PageBreak())


def build_planner(story):
    story.append(div("WARRIOR PREP — SEMESTER PLANNER  (Weeks 1–18)"))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("Your Semester Planner", S("lesson_title")))
    story.append(Paragraph(
        "Use ONE page per week. On Week 1, write your six course names in the Course column. "
        "Carry those names forward each week. Record every assignment, test, or deadline on the "
        "day it is ASSIGNED — not the day it is due. Check your planner at the start and end of every period.",
        S("body")))
    tips = ["Write the assignment and due date.", "✓ = done   → = carried forward",
            "Color-code by subject if helpful.", "Keep this with you all day — not just in Warrior Prep."]
    for tip in tips:
        story.append(Paragraph(f"•  {tip}", S("obj")))
    story.append(PageBreak())

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for wk in range(1, 19):
        # Header
        hdr = Table([[
            Paragraph(f"<b>Week {wk}</b>", S("planner_hdr")),
            Paragraph(f"Dates: _________________________", S("planner_hdr")),
            Paragraph("", S("planner_hdr")),
        ]], colWidths=[0.9 * inch, 4.1 * inch, 1.5 * inch])
        hdr.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_RED),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK),
        ]))
        story.append(hdr)

        # Day headers
        day_row = [Paragraph("Course", S("planner_hdr"))] + [Paragraph(d, S("planner_hdr")) for d in days]
        dh = Table([day_row], colWidths=[1.1 * inch] + [1.08 * inch] * 5)
        dh.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_DARK),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, HexColor("#444444")),
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK),
        ]))
        story.append(dh)

        # 6 course rows
        grid = []
        for i in range(6):
            label = f"Course {i+1}: ___________" if wk == 1 else f"Course {i+1}"
            grid.append([
                Paragraph(label, ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=7, leading=10)),
            ] + [Paragraph("", S("planner_cell"))] * 5)

        g = Table(grid, colWidths=[1.1 * inch] + [1.08 * inch] * 5, rowHeights=[0.6 * inch] * 6)
        grid_style = [
            ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK),
            ("BACKGROUND", (0, 0), (0, -1), WARRIOR_LITE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ]
        for i in range(0, 6, 2):
            grid_style.append(("BACKGROUND", (1, i), (-1, i), CREAM))
        g.setStyle(TableStyle(grid_style))
        story.append(g)

        # Goals row
        goals = Table(
            [[Paragraph("<b>Weekly Goals / Notes / Carry-Forward</b>", S("small_bold"))],
             [ruled(3, 6.5 * inch - 12, h=16)]],
            colWidths=[6.5 * inch]
        )
        goals.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_GOLD),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 1), (-1, 1), 5),
        ]))
        story.append(goals)
        story.append(PageBreak())


def build_unit_title(story, unit):
    uc = color_from_tuple(unit["color"])
    inner = [
        Spacer(1, 1.4 * inch),
        Paragraph(f"Unit {unit['number']}", S("unit_num")),
        Spacer(1, 0.08 * inch),
        Paragraph(unit["name"], S("unit_title")),
        Spacer(1, 0.25 * inch),
        HRFlowable(width="65%", thickness=1, color=WARRIOR_GOLD),
        Spacer(1, 0.25 * inch),
        Paragraph(unit["overview"], S("unit_overview")),
        Spacer(1, 0.4 * inch),
        Paragraph("Unit Vocabulary", S("unit_vocab_hdr")),
        Spacer(1, 0.08 * inch),
    ]
    for v in unit["unit_vocabulary"]:
        inner.append(Paragraph(f"<b>{v['word']}</b>  —  {v['definition']}", S("unit_vocab")))
        inner.append(Spacer(1, 0.04 * inch))

    t = Table([[inner]], colWidths=[6.5 * inch], rowHeights=[9.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), uc),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 40), ("RIGHTPADDING", (0, 0), (-1, -1), 30),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t)
    story.append(PageBreak())


def build_test_page(story, unit, is_pretest=True):
    uc = color_from_tuple(unit["color"])
    label = "PRE-TEST" if is_pretest else "POST-TEST"
    story.append(div(f"Unit {unit['number']}: {unit['name']}  —  {label}", color=uc))
    story.append(Spacer(1, 0.08 * inch))
    if is_pretest:
        story.append(Paragraph(
            "<b>Directions:</b>  Answer as completely as you can RIGHT NOW. This is NOT graded for "
            "correctness — it shows your starting point. Be honest!", S("body")))
    else:
        story.append(Paragraph(f"<b>Directions:</b>  {unit['posttest_prompt']}", S("body")))
    story.append(Spacer(1, 0.08 * inch))
    if is_pretest:
        for i, q in enumerate(unit["pretest"], 1):
            story.append(Paragraph(f"<b>{i}.</b>  {q}", S("test_q")))
            story.append(ruled(4, 6.3 * inch))
            story.append(Spacer(1, 0.06 * inch))
    else:
        story.append(ruled(25, 6.3 * inch))
    story.append(PageBreak())


def build_cornell_page(story, unit, lesson):
    uc = color_from_tuple(unit["color"])
    sc = lesson["scaffolding"]
    vf = lesson["vocab_focus"]

    story.append(div(f"Lesson {lesson['lesson_label']}  —  {lesson['title']}  ·  Cornell Notes", color=uc))
    story.append(Spacer(1, 0.05 * inch))

    # Meta row
    meta = Table([[
        Paragraph("Name: ________________________________", S("small")),
        Paragraph("Date: ______________", S("small")),
        Paragraph("Period: ______", S("small")),
    ]], colWidths=[3.2 * inch, 2.0 * inch, 1.3 * inch])
    meta.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, 0), 0.4, RULED_LINE),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(meta)
    story.append(Spacer(1, 0.06 * inch))

    # Vocab box
    vb = Table([[
        Paragraph(f"<b>Word Focus:</b> {vf['word']}", S("small_bold")),
        Paragraph(f"<i>Etymology:</i> {vf['etymology']}", S("vocab_etym")),
        Paragraph(vf["definition"], S("small")),
    ]], colWidths=[1.7 * inch, 2.4 * inch, 2.4 * inch])
    vb.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, uc),
        ("BACKGROUND", (0, 0), (-1, -1), NOTE_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, HexColor("#B0C0DC")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(vb)
    story.append(Spacer(1, 0.06 * inch))

    # Cornell body
    QW = 1.82 * inch
    NW = 4.58 * inch
    main_h = 5.5 * inch

    # Left column
    lft = []
    if sc <= 2:
        for q in lesson["cornell_questions"]:
            lft.append(Paragraph(f"• {q}", S("small")))
            lft.append(Spacer(1, 0.03 * inch))
        lft.append(Spacer(1, 0.08 * inch))
        lft.append(Paragraph("Your own questions:", S("small_bold")))
        lft.append(ruled(6, QW - 10, h=15))
    else:
        for q in lesson["cornell_questions"][:2]:
            lft.append(Paragraph(f"• {q}", S("small")))
            lft.append(Spacer(1, 0.03 * inch))
        lft.append(ruled(12, QW - 10, h=15))

    # Right column
    rgt = []
    prefilled = lesson.get("prefilled_notes", "")
    if sc == 1 and prefilled:
        rgt.append(Paragraph(
            prefilled.replace("\n", "<br/>"),
            ParagraphStyle("pf", fontName="Helvetica", fontSize=8.5, textColor=HexColor("#1A1A6E"), leading=13.5)
        ))
        rgt.append(Spacer(1, 0.08 * inch))
        rgt.append(Paragraph("Continue your notes below:", S("small_bold")))
        rgt.append(ruled(9, NW - 10, h=17))
    elif sc == 2 and prefilled:
        rgt.append(Paragraph(
            prefilled.replace("\n", "<br/>"),
            ParagraphStyle("pf2", fontName="Helvetica", fontSize=8.5, textColor=HexColor("#1A1A6E"), leading=13.5)
        ))
        rgt.append(ruled(7, NW - 10, h=17))
    else:
        rgt.append(ruled(21, NW - 10, h=17))

    cornell = Table(
        [
            [Paragraph("QUESTIONS / CUES", S("planner_hdr")), Paragraph("NOTES", S("planner_hdr"))],
            [lft, rgt],
        ],
        colWidths=[QW, NW],
        rowHeights=[0.24 * inch, main_h]
    )
    cornell.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, WARRIOR_DARK),
        ("LINEAFTER", (0, 0), (0, -1), 1.2, uc),
        ("BACKGROUND", (0, 0), (0, 0), uc),
        ("BACKGROUND", (1, 0), (1, 0), WARRIOR_DARK),
        ("BACKGROUND", (0, 1), (0, 1), WARRIOR_LITE),
        ("VALIGN", (0, 1), (-1, 1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(cornell)

    # Summary
    summ = Table(
        [[Paragraph("<b>SUMMARY</b>  — Write the main ideas in your own words (complete AFTER the lesson, without looking):", S("small_bold"))],
         [ruled(3, 6.45 * inch - 12, h=17)]],
        colWidths=[6.45 * inch]
    )
    summ.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, WARRIOR_DARK),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#E8E0D0")),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 5),
    ]))
    story.append(Spacer(1, 0.04 * inch))
    story.append(summ)
    story.append(PageBreak())


def build_exit_ticket(story, unit, lesson):
    uc = color_from_tuple(unit["color"])
    et = lesson["exit_ticket"]
    et_type = et.get("type", "quick_write")

    inner = []

    if et_type in ("quick_write", "synthesis_write"):
        inner.append(Paragraph(et["prompt"], S("et_prompt")))
        inner.append(Spacer(1, 0.06 * inch))
        inner.append(ruled(et.get("lines", 5), 6.15 * inch - 12))

    elif et_type == "three_two_one":
        for p in et["prompts"]:
            inner.append(Paragraph(p, S("et_stem")))
            inner.append(ruled(2, 6.15 * inch - 12))
            inner.append(Spacer(1, 0.04 * inch))

    elif et_type == "reflection_scale":
        inner.append(Paragraph(et["prompt"], S("et_prompt")))
        inner.append(Spacer(1, 0.06 * inch))
        sc_t = Table([[
            Paragraph("1\nNot at all", S("centered")), Paragraph("2", S("centered")),
            Paragraph("3\nSomewhat", S("centered")), Paragraph("4", S("centered")),
            Paragraph("5\nAbsolutely", S("centered")),
        ]], colWidths=[1.1 * inch] * 5)
        sc_t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, HexColor("#AAAAAA")),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        inner.append(sc_t)
        inner.append(Spacer(1, 0.06 * inch))
        inner.append(ruled(et.get("lines", 3), 6.15 * inch - 12))

    elif et_type == "sentence_stems":
        for p in et["prompts"]:
            inner.append(Paragraph(p, S("et_stem")))
            inner.append(ruled(2, 6.15 * inch - 12))
            inner.append(Spacer(1, 0.04 * inch))

    elif et_type == "vocabulary_check":
        inner.append(Paragraph(et["prompt"], S("et_prompt")))
        inner.append(Spacer(1, 0.06 * inch))
        pairs = list(zip(et["terms"], et["definitions"]))
        vt = Table([[Paragraph(f"<b>{t}</b>", S("small")), Paragraph(d, S("small"))] for t, d in pairs],
                   colWidths=[2.4 * inch, 3.75 * inch])
        vt.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        inner.append(vt)
        inner.append(Spacer(1, 0.06 * inch))
        inner.append(Paragraph("Write TWO terms in sentences:", S("et_stem")))
        inner.append(ruled(3, 6.15 * inch - 12))

    elif et_type == "planning_response":
        for p in et["prompts"]:
            inner.append(Paragraph(p, S("et_stem")))
            inner.append(ruled(2, 6.15 * inch - 12))
            inner.append(Spacer(1, 0.04 * inch))

    elif et_type == "postcard":
        inner.append(Paragraph(et["prompt"], S("et_prompt")))
        inner.append(Spacer(1, 0.06 * inch))
        pc = Table([[
            ruled(et.get("lines", 5), 3.1 * inch - 12),
            Paragraph("To: My Future 9th-Grade Self\n\nTwo Rivers High School\n1897 Delaware Ave\nMendota Heights, MN 55118",
                      S("small")),
        ]], colWidths=[3.2 * inch, 2.95 * inch])
        pc.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, WARRIOR_DARK),
            ("LINEAFTER", (0, 0), (0, 0), 0.5, HexColor("#AAAAAA")),
            ("BACKGROUND", (1, 0), (1, 0), WARRIOR_LITE),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ]))
        inner.append(pc)

    else:
        inner.append(Paragraph(str(et.get("prompt", "")), S("et_prompt")))
        inner.append(ruled(4, 6.15 * inch - 12))

    et_t = Table(
        [[Paragraph(f"✏  EXIT TICKET  ·  Lesson {lesson['lesson_label']}: {lesson['title']}", S("htag_white"))],
         [inner]],
        colWidths=[6.5 * inch]
    )
    et_t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, uc),
        ("BACKGROUND", (0, 0), (-1, 0), uc),
        ("BACKGROUND", (0, 1), (-1, 1), CREAM),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(et_t)
    story.append(PageBreak())


def build_lesson_content(story, unit, lesson):
    uc = color_from_tuple(unit["color"])
    story.append(div(f"Unit {unit['number']}  ·  Lesson {lesson['lesson_label']}  —  {lesson['title']}", color=uc))
    story.append(Spacer(1, 0.08 * inch))

    # Objectives
    obj_inner = [Paragraph("<b>Learning Objectives</b> — By the end of this lesson you will be able to:", S("small_bold"))]
    for o in lesson["objectives"]:
        obj_inner.append(Paragraph(f"◉  {o}", S("obj")))
    obj_t = Table([[obj_inner]], colWidths=[6.5 * inch])
    obj_t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, uc),
        ("BACKGROUND", (0, 0), (-1, -1), NOTE_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(obj_t)
    story.append(Spacer(1, 0.1 * inch))

    # Content sections
    for sec in lesson["content_sections"]:
        story.append(Paragraph(sec["heading"], S("sec_head")))
        story.append(Paragraph(sec["body"], S("body")))
        act = sec.get("activity")
        if act:
            _render_activity(story, act, uc)
        story.append(Spacer(1, 0.08 * inch))


def _render_activity(story, act, uc):
    at = act["type"]

    if at == "rating_table":
        cols = act["columns"]
        wf = 3.8 * inch
        wc = (6.5 * inch - wf) / len(cols)
        rows = [[Paragraph("Statement", S("small_bold"))] + [Paragraph(c, S("small_bold")) for c in cols]]
        for r in act["rows"]:
            rows.append([Paragraph(r, S("small"))] + [Paragraph("☐", S("centered"))] * len(cols))
        t = Table(rows, colWidths=[wf] + [wc] * len(cols))
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("ALIGN", (1, 0), (-1, -1), "CENTER"), ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)

    elif at == "audit_table":
        cols = act["columns"]
        wf = 2.5 * inch
        wc = (6.5 * inch - wf) / len(cols)
        rows = [[Paragraph("Distractor", S("small_bold"))] + [Paragraph(c, S("small_bold")) for c in cols]]
        for r in act["rows"]:
            rows.append([Paragraph(r, S("small"))] + [Paragraph("☐", S("centered"))] * len(cols))
        t = Table(rows, colWidths=[wf] + [wc] * len(cols))
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("ALIGN", (1, 0), (-1, -1), "CENTER"), ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.05 * inch))
        story.append(Paragraph("My #1 distractor: _______________   My plan to address it:", S("small_bold")))
        story.append(ruled(2, 6.3 * inch))

    elif at == "matrix_sort":
        story.append(box("Draw the Eisenhower Matrix here: 4 quadrants (Urgent/Important, Not Urgent/Important, Urgent/Not Important, Not Urgent/Not Important). Place each numbered task below in the correct quadrant.", 6.5 * inch, 2.0 * inch))
        story.append(Spacer(1, 0.05 * inch))
        for i, task in enumerate(act["tasks"], 1):
            story.append(Paragraph(f"<b>{i}.</b>  {task}", S("small")))

    elif at == "interest_table":
        rows = [[Paragraph("Career Field", S("small_bold")), Paragraph("Description", S("small_bold")),
                 Paragraph("My Interest\n(1–5)", S("small_bold")), Paragraph("Career I Know", S("small_bold"))]]
        for name, desc in act["rows"]:
            rows.append([Paragraph(name, S("small_bold")), Paragraph(desc, S("small")),
                         Paragraph("", S("small")), Paragraph("", S("small"))])
        t = Table(rows, colWidths=[1.6 * inch, 2.4 * inch, 1.0 * inch, 1.5 * inch])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)

    elif at == "two_column_chart":
        rows = [[Paragraph("", S("small_bold")), Paragraph("Course 1", S("small_bold")), Paragraph("Course 2", S("small_bold"))]]
        for field in act["fields"]:
            rows.append([Paragraph(field, S("small_bold")), Paragraph("", S("small")), Paragraph("", S("small"))])
        t = Table(rows, colWidths=[2.0 * inch, 2.25 * inch, 2.25 * inch],
                  rowHeights=[0.24 * inch] + [0.52 * inch] * len(act["fields"]))
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)

    elif at == "venn_diagram":
        story.append(box(f"Venn Diagram: {act['label_a']}  vs.  {act['label_b']}\n\nDraw two overlapping circles. List differences in outer sections, similarities in the overlap.", 6.5 * inch, 2.2 * inch))

    elif at == "guided_reflection":
        for p in act["prompts"]:
            story.append(Paragraph(p, S("et_stem")))
            story.append(ruled(2, 6.3 * inch))
            story.append(Spacer(1, 0.04 * inch))

    elif at == "smart_goal_template":
        for label, hint, lines in act["fields"]:
            story.append(Paragraph(f"<b>{label}</b>  <i>({hint})</i>", S("h3")))
            story.append(ruled(lines, 6.3 * inch))
            story.append(Spacer(1, 0.03 * inch))

    elif at == "study_plan_template":
        for field in act["fields"]:
            story.append(Paragraph(field, S("h3")))
            story.append(ruled(2, 6.3 * inch))
            story.append(Spacer(1, 0.03 * inch))

    elif at == "backward_plan":
        rows = [["Week", "Tasks to Complete", "My Mini-Deadline"]]
        for w in range(act["weeks"], 0, -1):
            rows.append([f"Week {w}", "", ""])
        t = Table(rows, colWidths=[0.8 * inch, 4.0 * inch, 1.7 * inch],
                  rowHeights=[0.24 * inch] + [0.55 * inch] * act["weeks"])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)

    elif at == "role_play":
        for sc in act["scenarios"]:
            story.append(Paragraph(f"<b>Scenario:</b>  {sc}", S("et_stem")))
            story.append(Paragraph("Your script:", S("small_bold")))
            story.append(ruled(2, 6.3 * inch))
            story.append(Spacer(1, 0.04 * inch))

    elif at == "annotation_practice":
        story.append(Paragraph("Write your 2-sentence summary of the passage here:", S("small_bold")))
        story.append(ruled(2, 6.3 * inch))

    elif at == "timed_write":
        story.append(Paragraph(f"Time: {act['minutes']} min  ·  Plan (2 min): __________________  ·  Draft:", S("small_bold")))
        story.append(ruled(act.get("lines", 16), 6.3 * inch))

    elif at == "checklist":
        for item in act["items"]:
            story.append(Paragraph(f"☐  {item}", S("obj")))

    elif at == "gpa_calculator":
        rows = [["Course", "Grade", "Credits", "GPA Points", "Weighted Points"]]
        for c in act["courses"]:
            rows.append([c[0], c[1], c[2], "", ""])
        rows.append(["", "", "TOTAL →", "", ""])
        t = Table(rows, colWidths=[2.6 * inch, 0.8 * inch, 0.8 * inch, 1.15 * inch, 1.15 * inch])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("BACKGROUND", (0, -1), (-1, -1), WARRIOR_GOLD),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)

    elif at == "habits_checklist":
        for item in act["items"]:
            story.append(Paragraph(f"☐  {item}", S("obj")))

    elif at == "commitment_card":
        rows = []
        for f in act["fields"]:
            rows.append([Paragraph(f, S("et_stem"))])
            rows.append([ruled(1, 5.9 * inch - 12, h=18)])
        ct = Table(rows, colWidths=[5.9 * inch])
        ct.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, uc),
            ("BACKGROUND", (0, 0), (-1, -1), CREAM),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ]))
        story.append(ct)

    elif at == "activities_checklist":
        for cat, items in act["categories"].items():
            story.append(Paragraph(f"<b>{cat}</b>", S("h3")))
            trios = [items[i:i+3] for i in range(0, len(items), 3)]
            for trio in trios:
                row = [Paragraph(f"☐  {x}", S("small")) for x in trio]
                while len(row) < 3:
                    row.append(Paragraph("", S("small")))
                t = Table([row], colWidths=[2.1 * inch] * 3)
                t.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
                story.append(t)

    elif at == "time_map":
        cols = act["columns"]
        rows = [["Time"] + cols]
        for h in act["hours"]:
            label = f"{h % 12 or 12}:00 {'AM' if h < 12 else 'PM'}"
            rows.append([label] + [""] * len(cols))
        cw = [0.9 * inch] + [(6.5 * inch - 0.9 * inch) / len(cols)] * len(cols)
        t = Table(rows, colWidths=cw, rowHeights=[0.22 * inch] * len(rows))
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 1),
        ]))
        story.append(t)

    elif at == "schedule_grid":
        rows = [["Period"] + act["semesters"]]
        for p in act["periods"]:
            rows.append([p, "", ""])
        t = Table(rows, colWidths=[1.0 * inch, 2.75 * inch, 2.75 * inch],
                  rowHeights=[0.24 * inch] + [0.52 * inch] * len(act["periods"]))
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), WARRIOR_DARK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)
        if act.get("note"):
            story.append(Paragraph(f"<i>{act['note']}</i>", S("small")))

    elif at == "full_schedule_builder":
        rows = [["Period", "Semester 1 Course", "Semester 2 Course"]]
        for p in range(1, act["periods"] + 1):
            rows.append([f"Period {p}", "", ""])
        t = Table(rows, colWidths=[0.8 * inch, 2.85 * inch, 2.85 * inch],
                  rowHeights=[0.24 * inch] + [0.58 * inch] * act["periods"])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), uc), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)
        if act.get("include_reflection"):
            story.append(Spacer(1, 0.06 * inch))
            story.append(Paragraph("Reflection: Which elective connects most to your Unit 2 career pathway? Explain:", S("small_bold")))
            story.append(ruled(3, 6.3 * inch))

    elif at == "year_plan_summary":
        for label, lines in act["fields"]:
            story.append(Paragraph(label, S("h3")))
            story.append(ruled(lines, 6.3 * inch))
            story.append(Spacer(1, 0.04 * inch))

    elif at == "final_schedule_with_rationale":
        rows = [["Period", "Course Choice", "Why I chose it", "Alternate"]]
        for p in range(1, act["periods"] + 1):
            rows.append([f"Period {p}", "", "", ""])
        t = Table(rows, colWidths=[0.7 * inch, 1.8 * inch, 2.4 * inch, 1.6 * inch],
                  rowHeights=[0.24 * inch] + [0.65 * inch] * act["periods"])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_DARK), ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
            ("BACKGROUND", (0, 0), (-1, 0), uc), ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(t)

    elif at == "question_prep":
        for i in range(1, act["num_questions"] + 1):
            story.append(Paragraph(f"<b>Question {i}:</b>", S("h3")))
            story.append(ruled(act["lines_per_question"], 6.3 * inch))
            story.append(Spacer(1, 0.04 * inch))

    elif at == "panel_notes":
        story.append(ruled(act["lines"], 6.3 * inch))


# ── Main ──────────────────────────────────────────────────────────────────────
def _build_placeholder():
    pass  # replaced by full build() defined after all page builders


# ════════════════════════════════════════════════════════════════════════════
# BELL RINGER PAGE — matches the opening slide of every lesson
# ════════════════════════════════════════════════════════════════════════════

def build_bell_ringer_page(story, unit, lesson):
    uc = color_from_tuple(unit["color"])
    label = lesson["lesson_label"]
    br = BELL_RINGERS.get(label)
    t  = LESSON_TIMING.get(label, {})
    if not br:
        return

    type_colors = {
        "Launch":      WARRIOR_RED,
        "Review":      uc,
        "Anticipation": Color(0.18, 0.49, 0.20),
    }
    chip_color = type_colors.get(br["type"], WARRIOR_RED)

    # ── Header bar ─────────────────────────────────────────────────────────
    header_cells = [
        [Paragraph(f"<b>BELL RINGER  ·  Lesson {label}</b>", S("htag_white")),
         Paragraph("<b>5 minutes</b>", ParagraphStyle(
             "br_time", fontName="Helvetica-Bold", fontSize=9,
             textColor=WARRIOR_GOLD, alignment=TA_RIGHT, leading=12))],
    ]
    hdr_t = Table(header_cells, colWidths=[4.5 * inch, 2.0 * inch])
    hdr_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(hdr_t)

    # ── Type chip + title row ───────────────────────────────────────────────
    chip_style = ParagraphStyle(
        "br_chip", fontName="Helvetica-Bold", fontSize=8,
        textColor=white, alignment=TA_CENTER, leading=11)
    title_style = ParagraphStyle(
        "br_title", fontName="Helvetica-Bold", fontSize=12,
        textColor=WARRIOR_DARK, leading=15)

    chip_row = Table(
        [[Paragraph(br["type"].upper(), chip_style),
          Paragraph(br["title"], title_style)]],
        colWidths=[0.75 * inch, 5.75 * inch]
    )
    chip_row.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), chip_color),
        ("BACKGROUND", (1, 0), (1, 0), WARRIOR_LITE),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(chip_row)
    story.append(Spacer(1, 0.08 * inch))

    # ── Prompt box ─────────────────────────────────────────────────────────
    prompt_style = ParagraphStyle(
        "br_prompt", fontName="Helvetica", fontSize=10,
        textColor=WARRIOR_DARK, leading=15, leftIndent=4)
    # Render newlines in the prompt as separate paragraphs
    prompt_lines = br["prompt"].split("\n")
    prompt_paras = []
    for line in prompt_lines:
        prompt_paras.append(Paragraph(line if line.strip() else " ", prompt_style))
        if line.strip():
            prompt_paras.append(Spacer(1, 0.04 * inch))

    prompt_t = Table([[prompt_paras]], colWidths=[6.3 * inch])
    prompt_t.setStyle(TableStyle([
        ("BOX",        (0, 0), (-1, -1), 1.2, chip_color),
        ("LINEAFTER",  (0, 0), (0, -1), 4, chip_color),
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    story.append(prompt_t)
    story.append(Spacer(1, 0.1 * inch))

    # ── Write your response header ──────────────────────────────────────────
    story.append(div("Write Your Response — Use complete sentences.", color=WARRIOR_DARK, w=6.3 * inch))
    story.append(Spacer(1, 0.06 * inch))
    story.append(ruled(7, 6.3 * inch))
    story.append(Spacer(1, 0.12 * inch))

    # ── 50-minute lesson plan bar ──────────────────────────────────────────
    segments = [
        ("Bell Ringer",  t.get("bell", 5),     WARRIOR_RED),
        ("Intro",        t.get("title", 3),     uc),
        ("Reading",      t.get("read", 10),     HexColor("#1A73E8")),
        ("Questions",    t.get("qs", 7),        HexColor("#2E7D32")),
        ("Content",      t.get("content", 9),   HexColor("#6A1B9A")),
        ("Activity",     t.get("activity", 11), HexColor("#E65C00")),
        ("Exit Ticket",  t.get("exit", 5),      WARRIOR_DARK),
    ]
    total_min = sum(s[1] for s in segments)

    plan_label = ParagraphStyle("pl", fontName="Helvetica-Bold", fontSize=7.5,
                                textColor=WARRIOR_DARK, leading=10)
    story.append(Paragraph(f"Today's 50-Minute Plan", plan_label))
    story.append(Spacer(1, 0.04 * inch))

    total_w = 6.3 * inch
    bar_cells = []
    label_cells = []
    for seg_name, seg_min, seg_color in segments:
        seg_w = (seg_min / total_min) * total_w
        min_label = ParagraphStyle(
            "ml", fontName="Helvetica-Bold", fontSize=7, textColor=white,
            alignment=TA_CENTER, leading=9)
        name_label = ParagraphStyle(
            "nl", fontName="Helvetica", fontSize=6, textColor=WARRIOR_DARK,
            alignment=TA_CENTER, leading=8)
        bar_cells.append(Paragraph(str(seg_min) + " min", min_label))
        label_cells.append(Paragraph(seg_name, name_label))

    col_widths = [(s[1] / total_min) * total_w for s in segments]

    bar_t = Table([bar_cells], colWidths=col_widths, rowHeights=[0.26 * inch])
    bar_t.setStyle(TableStyle(
        [("BACKGROUND", (i, 0), (i, 0), segments[i][2]) for i in range(len(segments))] +
        [("TOPPADDING", (0, 0), (-1, -1), 3),
         ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
         ("LEFTPADDING", (0, 0), (-1, -1), 1),
         ("RIGHTPADDING", (0, 0), (-1, -1), 1),
         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
         ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]
    ))
    lbl_t = Table([label_cells], colWidths=col_widths, rowHeights=[0.2 * inch])
    lbl_t.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(bar_t)
    story.append(lbl_t)
    story.append(PageBreak())


# ════════════════════════════════════════════════════════════════════════════
# READING PAGE (added after Cornell Notes, before content activities)
# ════════════════════════════════════════════════════════════════════════════
from readings import READINGS

def build_reading_page(story, unit, lesson):
    uc = color_from_tuple(unit["color"])
    reading = READINGS.get(lesson["lesson_label"])
    if not reading:
        return

    story.append(div(
        f"Lesson {lesson['lesson_label']}  ·  Reading: {reading['title']}", color=uc))
    story.append(Spacer(1, 0.06 * inch))

    # Source line + audio reference
    label = lesson["lesson_label"]
    src_row = [
        Paragraph(f"<i>Source: {reading['source']}</i>",
                  ParagraphStyle("src", fontName="Helvetica-Oblique", fontSize=8,
                                 textColor=HexColor("#666666"), leading=11)),
        Paragraph(f"🎧 Listen: reading_EN_{label}.m4a",
                  ParagraphStyle("aud", fontName="Helvetica-Oblique", fontSize=8,
                                 textColor=HexColor("#666666"), leading=11, alignment=2)),
    ]
    src_tbl = Table([src_row], colWidths=[4.5 * inch, 2.0 * inch])
    src_tbl.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(src_tbl)
    story.append(Spacer(1, 0.06 * inch))

    # Annotation reminder box
    ann = Table([[Paragraph(
        "As you read: use your annotation symbols  "
        "( * = important  ·  ? = question  ·  ! = surprising  ·  → = connection  ·  circle = vocab )",
        S("small_bold")
    )]], colWidths=[6.5 * inch])
    ann.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, uc),
        ("BACKGROUND", (0, 0), (-1, -1), NOTE_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(ann)
    story.append(Spacer(1, 0.08 * inch))

    # Paragraphs with left margin for annotation marks
    reading_style = ParagraphStyle(
        "rdg", fontName="Helvetica", fontSize=10, leading=16,
        textColor=WARRIOR_DARK, spaceAfter=8, leftIndent=18
    )
    for i, para in enumerate(reading["text"], 1):
        story.append(Paragraph(para, reading_style))

    story.append(Spacer(1, 0.1 * inch))

    # Comprehension questions
    story.append(div("Reading Comprehension Questions", color=uc))
    story.append(Spacer(1, 0.06 * inch))
    story.append(Paragraph(
        "Answer each question in complete sentences. Use evidence from the reading.",
        S("small")))
    story.append(Spacer(1, 0.04 * inch))

    for i, q in enumerate(reading["questions"], 1):
        story.append(Paragraph(f"<b>{i}.</b>  {q}", S("test_q")))
        story.append(ruled(4, 6.3 * inch))
        story.append(Spacer(1, 0.05 * inch))

    story.append(PageBreak())


# ════════════════════════════════════════════════════════════════════════════
# STORY PAGE — realistic fiction discussion bridge, placed after the reading
# ════════════════════════════════════════════════════════════════════════════
from stories import STORIES
from stories_es import STORIES_ES

def build_story_page(story_list, unit, lesson, lang="EN"):
    uc = color_from_tuple(unit["color"])
    label = lesson["lesson_label"]
    s = STORIES.get(label) if lang == "EN" else STORIES_ES.get(label)
    if not s:
        return

    is_es = (lang == "ES")
    hdr_label   = "HISTORIA DE DISCUSIÓN" if is_es else "DISCUSSION STORY"
    audio_note  = (f"🎧 Escucha: story_ES_{label}.m4a" if is_es
                   else f"🎧 Listen: story_EN_{label}.m4a")
    disc_header = "Preguntas de Discusión" if is_es else "Discussion Questions"
    disc_instr  = ("Habla con tu compañero o grupo. Luego escribe tu mejor respuesta."
                   if is_es else
                   "Discuss with your partner or small group. Then write your best thinking below.")

    # ── Header ──────────────────────────────────────────────────────────────
    hdr_cells = [
        [Paragraph(f"<b>{hdr_label}  ·  Lesson {label}</b>",
                   ParagraphStyle("st_hdr", fontName="Helvetica-Bold", fontSize=9,
                                  textColor=white, leading=12)),
         Paragraph(f"<b>Maya · Jordan · Priya · Eli</b>",
                   ParagraphStyle("st_chars", fontName="Helvetica-Bold", fontSize=8,
                                  textColor=WARRIOR_GOLD, leading=12, alignment=TA_RIGHT))],
    ]
    hdr_t = Table(hdr_cells, colWidths=[3.8 * inch, 2.7 * inch])
    hdr_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8), ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story_list.append(hdr_t)

    # ── Title bar ───────────────────────────────────────────────────────────
    title_t = Table(
        [[Paragraph(f"<b>\"{s['title']}\"</b>",
                    ParagraphStyle("st_title", fontName="Helvetica-Bold", fontSize=13,
                                   textColor=uc, leading=17))]],
        colWidths=[6.5 * inch]
    )
    title_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_LITE),
        ("TOPPADDING",    (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
    ]))
    story_list.append(title_t)

    # ── Audio note ──────────────────────────────────────────────────────────
    audio_style = ParagraphStyle(
        "audio_note", fontName="Helvetica-Oblique", fontSize=8,
        textColor=HexColor("#555555"), leading=11)
    story_list.append(Paragraph(audio_note, audio_style))
    story_list.append(Spacer(1, 0.08 * inch))

    # ── Story body ──────────────────────────────────────────────────────────
    fiction_style = ParagraphStyle(
        "fiction", fontName="Helvetica", fontSize=10, leading=16,
        textColor=WARRIOR_DARK, spaceAfter=5, leftIndent=6)
    fiction_italic = ParagraphStyle(
        "fiction_i", fontName="Helvetica-Oblique", fontSize=10, leading=16,
        textColor=HexColor("#333333"), spaceAfter=5, leftIndent=6)

    # Strip leading/trailing whitespace and render paragraphs
    raw_text = s["story"].strip()
    # Split on blank lines for paragraph breaks
    paragraphs = [p.strip() for p in raw_text.split("\n\n") if p.strip()]
    for para in paragraphs:
        # Lines within a paragraph
        lines = [ln.strip() for ln in para.split("\n") if ln.strip()]
        for line in lines:
            if line.startswith("<i>") or line.endswith("</i>"):
                story_list.append(Paragraph(line, fiction_italic))
            else:
                story_list.append(Paragraph(line, fiction_style))

    story_list.append(Spacer(1, 0.1 * inch))

    # ── Discussion questions ─────────────────────────────────────────────────
    story_list.append(div(disc_header, color=uc, w=6.3 * inch))
    story_list.append(Spacer(1, 0.07 * inch))
    story_list.append(Paragraph(disc_instr, S("small")))
    story_list.append(Spacer(1, 0.05 * inch))

    q_style = ParagraphStyle(
        "st_q", fontName="Helvetica", fontSize=9.5, textColor=WARRIOR_DARK,
        leading=14, leftIndent=6, spaceAfter=2)

    for i, q in enumerate(s["questions"], 1):
        bg_color = CREAM if i % 2 == 0 else NOTE_BLUE
        q_t = Table([[Paragraph(f"<b>{i}.</b>  {q}", q_style)]],
                    colWidths=[6.3 * inch])
        q_t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg_color),
            ("TOPPADDING",    (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ]))
        story_list.append(q_t)
        story_list.append(ruled(3, 6.3 * inch))
        story_list.append(Spacer(1, 0.04 * inch))

    story_list.append(PageBreak())


# ── Patch build() to call build_reading_page ─────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════
# MONDAY CHECK-IN PAGE — repeatable weekly template
# ════════════════════════════════════════════════════════════════════════════

NAVY  = HexColor("#1A376A")
GREEN = HexColor("#2E7D32")

def build_monday_page(story):
    """One printable Monday Check-In page per week."""

    # ── Dark header ──────────────────────────────────────────────────────
    hdr_inner = [
        Paragraph("MONDAY CHECK-IN", ParagraphStyle(
            "mci_chip", fontName="Helvetica-Bold", fontSize=9,
            textColor=WARRIOR_GOLD, leading=12, alignment=TA_LEFT)),
        Paragraph("Looking Back at Last Week", ParagraphStyle(
            "mci_title", fontName="Helvetica-Bold", fontSize=18,
            textColor=white, leading=22, alignment=TA_LEFT)),
    ]
    hdr_tbl = Table([[hdr_inner]], colWidths=[6.5 * inch], rowHeights=[0.72 * inch])
    hdr_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(hdr_tbl)

    # Name / date bar
    meta_row = [
        Paragraph("Name: ________________________________", S("small")),
        Paragraph("Week of: ____________________", S("small")),
        Paragraph("Period: _______", S("small")),
    ]
    meta_tbl = Table([meta_row], colWidths=[2.8 * inch, 2.2 * inch, 1.5 * inch])
    meta_tbl.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 0.08 * inch))

    # ── Section 1: Missing Work ──────────────────────────────────────────
    story.append(div("📋  MISSING WORK TRACKER", color=NAVY))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Paragraph(
        "Open Infinite Campus. Log any assignment showing as missing or late.",
        S("small_it")))
    story.append(Spacer(1, 0.05 * inch))

    mw_headers = ["Class / Course", "Assignment Name", "Due Date", "Status / Plan"]
    mw_widths  = [1.4 * inch, 2.1 * inch, 0.9 * inch, 2.1 * inch]
    mw_rows = [[Paragraph(h, S("small_bold")) for h in mw_headers]]
    for _ in range(4):
        mw_rows.append([Paragraph("", S("small"))] * 4)
    mw_tbl = Table(mw_rows, colWidths=mw_widths, rowHeights=[0.24 * inch] + [0.3 * inch] * 4)
    mw_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",  (0, 0), (-1, 0), white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, 1), NOTE_BLUE),
        ("BACKGROUND", (0, 3), (-1, 3), NOTE_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(mw_tbl)

    # Make-up commitment
    commit_tbl = Table([[Paragraph(
        "MY MAKE-UP PLAN:  I will complete __________________________ by __________ during __________________",
        S("small_bold"))]], colWidths=[6.5 * inch])
    commit_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FFF9C4")),
        ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#F9A825")),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    accent_col = Table(
        [[commit_tbl]],
        colWidths=[6.5 * inch],
    )
    story.append(Spacer(1, 0.04 * inch))
    inner_commit = Table([[
        Paragraph(
            "MY MAKE-UP PLAN:  I will complete __________________________ "
            "by __________ during __________________",
            ParagraphStyle("commit", fontName="Helvetica-Bold", fontSize=9,
                           textColor=WARRIOR_DARK, leading=13)),
    ]], colWidths=[6.5 * inch], rowHeights=[0.42 * inch])
    inner_commit.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FFF9C4")),
        ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#F9A825")),
        ("LINEBEFORE", (0, 0), (0, -1), 5, HexColor("#F9A825")),
        ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(inner_commit)
    story.append(Spacer(1, 0.1 * inch))

    # ── Section 2: Test & Quiz Review ───────────────────────────────────
    story.append(div("📝  TEST & QUIZ REVIEW", color=NAVY))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Paragraph(
        "Log any tests or quizzes from last week. If below 70%, write a make-up or retake plan.",
        S("small_it")))
    story.append(Spacer(1, 0.05 * inch))

    tq_headers = ["Class", "Test / Quiz Name", "Score", "Make-Up?", "My Plan"]
    tq_widths  = [0.85 * inch, 1.8 * inch, 0.6 * inch, 0.75 * inch, 2.5 * inch]
    tq_rows = [[Paragraph(h, S("small_bold")) for h in tq_headers]]
    for _ in range(3):
        tq_rows.append([Paragraph("", S("small"))] * 5)
    tq_tbl = Table(tq_rows, colWidths=tq_widths, rowHeights=[0.24 * inch] + [0.3 * inch] * 3)
    tq_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",  (0, 0), (-1, 0), white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 2), (-1, 2), NOTE_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(tq_tbl)
    story.append(Spacer(1, 0.1 * inch))

    # ── Section 3: Notes Review ──────────────────────────────────────────
    story.append(div("📖  NOTES REVIEW FROM OTHER CLASSES", color=NAVY))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Paragraph(
        "Cover your notes. Use your cue column (left side) to quiz yourself. "
        "Then write the single most important idea from each class last week.",
        S("small_it")))
    story.append(Spacer(1, 0.05 * inch))

    nr_headers = ["Class", "Most Important Idea from Last Week", "Still Confused About?"]
    nr_widths  = [1.1 * inch, 3.1 * inch, 2.3 * inch]
    nr_rows = [[Paragraph(h, S("small_bold")) for h in nr_headers]]
    for _ in range(3):
        nr_rows.append([Paragraph("", S("small"))] * 3)
    nr_tbl = Table(nr_rows, colWidths=nr_widths, rowHeights=[0.24 * inch] + [0.38 * inch] * 3)
    nr_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",  (0, 0), (-1, 0), white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 2), (-1, 2), NOTE_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(nr_tbl)
    story.append(Spacer(1, 0.08 * inch))

    # Pair-share prompt
    pair_tbl = Table([[Paragraph(
        "PAIR-SHARE: Tell your partner the most surprising thing you learned in "
        "any class last week. 60 seconds each — GO.",
        ParagraphStyle("pair", fontName="Helvetica-Bold", fontSize=9,
                       textColor=WARRIOR_DARK, leading=13))]], colWidths=[6.5 * inch])
    pair_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NOTE_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(pair_tbl)
    story.append(Spacer(1, 0.1 * inch))

    # ── Section 4: Weekly Win + Goal ────────────────────────────────────
    win_goal = Table([[
        # Weekly Win
        Table([[
            Table([[Paragraph("✅  WEEKLY WIN", ParagraphStyle(
                "ww", fontName="Helvetica-Bold", fontSize=9,
                textColor=WARRIOR_DARK, leading=12))]],
                colWidths=[3.05 * inch], rowHeights=[0.28 * inch],
                style=[("BACKGROUND", (0,0),(-1,-1), WARRIOR_GOLD),
                       ("LEFTPADDING",(0,0),(-1,-1),6),
                       ("TOPPADDING",(0,0),(-1,-1),5)]),
            Paragraph(
                "Write ONE thing you did well last week — academic, athletic, social, or personal.",
                ParagraphStyle("ww_dir", fontName="Helvetica-Oblique", fontSize=8,
                               textColor=WARRIOR_DARK, leading=11)),
            Spacer(1, 0.04 * inch),
            ruled(3, 3.0 * inch),
            ruled(1, 3.0 * inch),
        ]], colWidths=[3.1 * inch]),
        Spacer(1 * inch, 1),
        # Week Goal
        Table([[
            Table([[Paragraph("🎯  MY GOAL FOR THIS WEEK", ParagraphStyle(
                "wg", fontName="Helvetica-Bold", fontSize=9,
                textColor=WARRIOR_DARK, leading=12))]],
                colWidths=[3.05 * inch], rowHeights=[0.28 * inch],
                style=[("BACKGROUND", (0,0),(-1,-1), WARRIOR_GOLD),
                       ("LEFTPADDING",(0,0),(-1,-1),6),
                       ("TOPPADDING",(0,0),(-1,-1),5)]),
            Paragraph(
                "Specific. Achievable. Write it like you mean it.",
                ParagraphStyle("wg_dir", fontName="Helvetica-Oblique", fontSize=8,
                               textColor=WARRIOR_DARK, leading=11)),
            Spacer(1, 0.04 * inch),
            Paragraph("This week I will __________________________________________",
                       S("small")),
            Spacer(1, 0.04 * inch),
            Paragraph("by ________________  so that ______________________________",
                       S("small")),
        ]], colWidths=[3.1 * inch]),
    ]], colWidths=[3.1 * inch, 0.3 * inch, 3.1 * inch])
    story.append(win_goal)
    story.append(PageBreak())


# ════════════════════════════════════════════════════════════════════════════
# FRIDAY PLANNING PAGE — repeatable weekly template
# ════════════════════════════════════════════════════════════════════════════

def build_friday_page(story):
    """One printable Friday Planning page per week."""

    # ── Dark header ──────────────────────────────────────────────────────
    hdr_inner = [
        Paragraph("FRIDAY PLANNING", ParagraphStyle(
            "fp_chip", fontName="Helvetica-Bold", fontSize=9,
            textColor=WARRIOR_GOLD, leading=12, alignment=TA_LEFT)),
        Paragraph("Looking Ahead to Next Week", ParagraphStyle(
            "fp_title", fontName="Helvetica-Bold", fontSize=18,
            textColor=white, leading=22, alignment=TA_LEFT)),
    ]
    hdr_tbl = Table([[hdr_inner]], colWidths=[6.5 * inch], rowHeights=[0.72 * inch])
    hdr_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(hdr_tbl)

    meta_row = [
        Paragraph("Name: ________________________________", S("small")),
        Paragraph("Week of: ____________________", S("small")),
        Paragraph("Period: _______", S("small")),
    ]
    meta_tbl = Table([meta_row], colWidths=[2.8 * inch, 2.2 * inch, 1.5 * inch])
    meta_tbl.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 0.08 * inch))

    # ── Section 1: Upcoming Deadlines ───────────────────────────────────
    story.append(div("📅  UPCOMING DEADLINES — Next 2 Weeks", color=GREEN))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Paragraph(
        "Check Infinite Campus. Log every test, quiz, project, or major assignment.",
        S("small_it")))
    story.append(Spacer(1, 0.05 * inch))

    dl_headers = ["Class", "Assignment / Test / Project", "Due Date", "Points", "Priority"]
    dl_widths  = [0.9 * inch, 2.2 * inch, 0.85 * inch, 0.6 * inch, 1.95 * inch]
    dl_rows = [[Paragraph(h, S("small_bold")) for h in dl_headers]]
    for _ in range(5):
        dl_rows.append([Paragraph("", S("small"))] * 5)
    dl_tbl = Table(dl_rows, colWidths=dl_widths, rowHeights=[0.24 * inch] + [0.3 * inch] * 5)
    dl_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("TEXTCOLOR",  (0, 0), (-1, 0), white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, 1), HexColor("#E8F5E9")),
        ("BACKGROUND", (0, 3), (-1, 3), HexColor("#E8F5E9")),
        ("BACKGROUND", (0, 5), (-1, 5), HexColor("#E8F5E9")),
        ("BOX", (0, 0), (-1, -1), 0.5, GREEN),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(dl_tbl)

    # High-priority flag
    story.append(Spacer(1, 0.04 * inch))
    priority_tbl = Table([[
        Paragraph(
            "HIGHEST PRIORITY this week: _______________________________________________",
            ParagraphStyle("pri", fontName="Helvetica-Bold", fontSize=9,
                           textColor=WARRIOR_DARK, leading=13)),
    ]], colWidths=[6.5 * inch], rowHeights=[0.42 * inch])
    priority_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FFEBEE")),
        ("BOX", (0, 0), (-1, -1), 0.5, WARRIOR_RED),
        ("LINEBEFORE", (0, 0), (0, -1), 5, WARRIOR_RED),
        ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(priority_tbl)
    story.append(Spacer(1, 0.1 * inch))

    # ── Section 2: Activities Tracker ───────────────────────────────────
    story.append(div("🏃  ACTIVITIES NEXT WEEK", color=GREEN))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Paragraph(
        "Log ALL commitments — sports, clubs, religious events, family, work, anything that takes time.",
        S("small_it")))
    story.append(Spacer(1, 0.05 * inch))

    act_headers = ["Day", "Afternoon Activity (3–5 PM)", "Evening Activity (5–9 PM)", "End Time"]
    act_widths  = [0.65 * inch, 2.2 * inch, 2.5 * inch, 1.15 * inch]
    days_list   = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sat / Sun"]
    act_rows = [[Paragraph(h, S("small_bold")) for h in act_headers]]
    for d in days_list:
        act_rows.append([
            Paragraph(d, S("small_bold")),
            Paragraph("", S("small")),
            Paragraph("", S("small")),
            Paragraph("", S("small")),
        ])
    act_tbl = Table(act_rows, colWidths=act_widths,
                    rowHeights=[0.24 * inch] + [0.3 * inch] * 6)
    act_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("TEXTCOLOR",  (0, 0), (-1, 0), white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, 1), HexColor("#E8F5E9")),
        ("BACKGROUND", (0, 3), (-1, 3), HexColor("#E8F5E9")),
        ("BACKGROUND", (0, 5), (-1, 5), HexColor("#E8F5E9")),
        ("BOX", (0, 0), (-1, -1), 0.5, GREEN),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(act_tbl)
    story.append(Spacer(1, 0.1 * inch))

    # ── Section 3: Weekly Plan Grid ──────────────────────────────────────
    story.append(div("🗓️  MY WEEK AT A GLANCE — Build Your Schedule Now", color=GREEN))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Paragraph(
        "Block HOMEWORK time first (⭐). Then write activities. Then protect your bedtime.",
        ParagraphStyle("fp_dir", fontName="Helvetica-Bold", fontSize=8.5,
                       textColor=GREEN, leading=12)))
    story.append(Spacer(1, 0.05 * inch))

    time_labels = ["3–5 PM", "5–6 PM\n(Dinner)", "6–8 PM", "8–9 PM", "9–10 PM\n(Bedtime)"]
    plan_days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    plan_col_w = 1.1 * inch
    label_col_w = 0.7 * inch

    grid_header = [Paragraph("", S("small_bold"))] + [
        Paragraph(d, ParagraphStyle("gh", fontName="Helvetica-Bold", fontSize=8,
                                    textColor=white, leading=11, alignment=TA_CENTER))
        for d in plan_days
    ]
    grid_rows = [grid_header]
    for block in time_labels:
        row = [Paragraph(block, ParagraphStyle(
            "tb", fontName="Helvetica", fontSize=7.5, textColor=WARRIOR_DARK, leading=10))]
        for _ in plan_days:
            row.append(Paragraph("", S("small")))
        grid_rows.append(row)

    grid_tbl = Table(grid_rows,
                     colWidths=[label_col_w] + [plan_col_w] * 5,
                     rowHeights=[0.22 * inch] + [0.36 * inch] * len(time_labels))
    green_stripe = HexColor("#E8F5E9")
    grid_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("BACKGROUND", (0, 0), (0, -1), HexColor("#C8E6C9")),
        ("BACKGROUND", (1, 1), (-1, 1), green_stripe),
        ("BACKGROUND", (1, 3), (-1, 3), green_stripe),
        ("BACKGROUND", (1, 5), (-1, 5), green_stripe),
        ("BOX", (0, 0), (-1, -1), 0.5, GREEN),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(grid_tbl)
    story.append(Spacer(1, 0.06 * inch))

    # Homework protection reminder
    hw_tbl = Table([[Paragraph(
        "⭐  Block your HOMEWORK TIME first — at least 90 minutes on school days. "
        "Everything else fits around it.",
        ParagraphStyle("hw", fontName="Helvetica-Bold", fontSize=9,
                       textColor=GREEN, leading=13))]], colWidths=[6.5 * inch])
    hw_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#E8F5E9")),
        ("BOX", (0, 0), (-1, -1), 0.5, GREEN),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(hw_tbl)
    story.append(Spacer(1, 0.1 * inch))

    # ── Section 4: Commitment Statement ──────────────────────────────────
    story.append(div("💪  MY COMMITMENT FOR NEXT WEEK", color=GREEN))
    story.append(Spacer(1, 0.05 * inch))

    commits = [
        ("I will protect:", "homework time from _______ to _______ on school nights"),
        ("I will finish:", "____________________________________________ by ___________"),
        ("I will ask for help with:", "________________________________ from _________________________"),
        ("I will NOT let:", "____________________________________________ distract me from my plan"),
        ("My sleep goal:", "Bedtime by _______ PM  ·  Wake up by _______ AM — every school day"),
    ]
    commit_rows = []
    for label, fill in commits:
        commit_rows.append([
            Paragraph(label, S("small_bold")),
            Paragraph(fill, S("small_it")),
        ])
    commit_tbl2 = Table(commit_rows, colWidths=[1.6 * inch, 4.9 * inch],
                        rowHeights=[0.28 * inch] * len(commits))
    commit_tbl2.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, GREEN),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, RULED_LINE),
        ("BACKGROUND", (0, 0), (0, -1), HexColor("#E8F5E9")),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(commit_tbl2)
    story.append(Spacer(1, 0.08 * inch))

    # Closing quote
    quote_tbl = Table([[Paragraph(
        "\"The best time to plan your week is before it starts.  You just did that.  "
        "Have a great weekend, Warrior.\"",
        ParagraphStyle("qt", fontName="Helvetica-BoldOblique", fontSize=9,
                       textColor=white, leading=13, alignment=TA_CENTER))]], colWidths=[6.5 * inch])
    quote_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(quote_tbl)
    story.append(PageBreak())


def build():
    from readings import READINGS
    out = "output/warrior_prep_student_workbook.pdf"
    doc = SimpleDocTemplate(out, pagesize=letter,
                            leftMargin=inch, rightMargin=inch,
                            topMargin=0.72 * inch, bottomMargin=0.72 * inch)
    story = []

    build_cover(story)
    build_how_to_use(story)
    build_planner(story)

    for unit in UNITS:
        build_unit_title(story, unit)
        build_test_page(story, unit, is_pretest=True)
        for lesson in unit["lessons"]:
            build_bell_ringer_page(story, unit, lesson)
            build_cornell_page(story, unit, lesson)
            build_reading_page(story, unit, lesson)
            build_story_page(story, unit, lesson, lang="EN")
            build_lesson_content(story, unit, lesson)
            build_exit_ticket(story, unit, lesson)
        build_test_page(story, unit, is_pretest=False)

    doc.build(story, canvasmaker=FooterCanvas)
    print(f"PDF saved → {out}  ({len(story)} flowables)")

    # ── Spanish story supplement ─────────────────────────────────────────────
    out_es = "output/warrior_prep_stories_espanol.pdf"
    doc_es = SimpleDocTemplate(out_es, pagesize=letter,
                               leftMargin=inch, rightMargin=inch,
                               topMargin=0.72 * inch, bottomMargin=0.72 * inch)
    story_es = []

    # Cover page for Spanish supplement
    cover_style = ParagraphStyle("es_cov", fontName="Helvetica-Bold", fontSize=32,
                                 textColor=white, leading=38, alignment=TA_CENTER)
    sub_style   = ParagraphStyle("es_sub", fontName="Helvetica", fontSize=15,
                                 textColor=WARRIOR_GOLD, leading=22, alignment=TA_CENTER)
    note_style  = ParagraphStyle("es_note", fontName="Helvetica", fontSize=11,
                                 textColor=white, leading=17, alignment=TA_CENTER)
    inner_es = [
        Spacer(1, 1.6 * inch),
        Paragraph("Warrior Prep", cover_style),
        Spacer(1, 0.18 * inch),
        Paragraph("Historias de Discusión", sub_style),
        Spacer(1, 0.28 * inch),
        HRFlowable(width="65%", thickness=1, color=WARRIOR_GOLD, spaceAfter=10),
        Spacer(1, 0.22 * inch),
        Paragraph("Suplemento en Español — Lecciones 1.1 a 5.4", sub_style),
        Spacer(1, 0.5 * inch),
        Paragraph(
            "Este cuaderno contiene las 20 historias de ficción realista de Warrior Prep "
            "traducidas al español, con preguntas de discusión para cada lección.\n\n"
            "Cada historia también está disponible como archivo de audio (.m4a):\n"
            "story_ES_[número de lección].m4a",
            note_style),
        Spacer(1, 1.2 * inch),
        Paragraph("Nombre: ________________________________   Período: ________", note_style),
        Spacer(1, 0.18 * inch),
        Paragraph("Maestro/a: _____________________________   Año: ____________", note_style),
    ]
    cover_t = Table([[inner_es]], colWidths=[6.5 * inch], rowHeights=[9.0 * inch])
    cover_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0), ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    story_es.append(cover_t)
    story_es.append(PageBreak())

    for unit in UNITS:
        for lesson in unit["lessons"]:
            build_story_page(story_es, unit, lesson, lang="ES")

    doc_es.build(story_es, canvasmaker=FooterCanvas)
    print(f"Spanish supplement saved → {out_es}  ({len(story_es)} flowables)")

    # ── Weekly Routine Template PDF ──────────────────────────────────────
    out_weekly = "output/warrior_prep_weekly_templates.pdf"
    doc_weekly = SimpleDocTemplate(out_weekly, pagesize=letter,
                                   leftMargin=inch, rightMargin=inch,
                                   topMargin=0.72 * inch, bottomMargin=0.72 * inch)
    weekly = []

    # Cover
    cov_style = ParagraphStyle("wc", fontName="Helvetica-Bold", fontSize=30,
                               textColor=white, leading=36, alignment=TA_CENTER)
    sub_style2 = ParagraphStyle("ws", fontName="Helvetica", fontSize=14,
                                textColor=WARRIOR_GOLD, leading=20, alignment=TA_CENTER)
    note_style2 = ParagraphStyle("wn", fontName="Helvetica", fontSize=10,
                                 textColor=white, leading=15, alignment=TA_CENTER)
    inner_cov = [
        Spacer(1, 1.4 * inch),
        Paragraph("Warrior Prep", cov_style),
        Spacer(1, 0.15 * inch),
        Paragraph("Weekly Routine Templates", sub_style2),
        Spacer(1, 0.25 * inch),
        HRFlowable(width="60%", thickness=1, color=WARRIOR_GOLD, spaceAfter=8),
        Spacer(1, 0.2 * inch),
        Paragraph("Monday Check-In  ·  Friday Planning", sub_style2),
        Spacer(1, 0.5 * inch),
        Paragraph(
            "Use one Monday page and one Friday page every week of the semester.\n\n"
            "Monday: look back — missing work, test review, notes from other classes, weekly win.\n"
            "Friday: look ahead — upcoming deadlines, activities, weekly schedule, commitment.",
            note_style2),
        Spacer(1, 1.0 * inch),
        Paragraph("Name: ________________________________   Period: ________", note_style2),
        Spacer(1, 0.15 * inch),
        Paragraph("Teacher: ______________________________   Semester: ____________", note_style2),
    ]
    cov_t = Table([[inner_cov]], colWidths=[6.5 * inch], rowHeights=[9.0 * inch])
    cov_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARRIOR_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0), ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    weekly.append(cov_t)
    weekly.append(PageBreak())

    # 18 weeks of Monday + Friday pages
    for week_num in range(1, 19):
        build_monday_page(weekly)
        build_friday_page(weekly)

    doc_weekly.build(weekly, canvasmaker=FooterCanvas)
    print(f"Weekly templates saved → {out_weekly}  ({len(weekly)} flowables, 18 weeks × 2 pages)")


if __name__ == "__main__":
    build()


"""PDF layout and rendering using reportlab."""

import re
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    PageBreak, Table, TableStyle, KeepTogether,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, Polygon


_DARK_BLUE  = colors.HexColor("#1a3a5c")
_MID_BLUE   = colors.HexColor("#2e6da4")
_LIGHT_BLUE = colors.HexColor("#eaf1fb")
_ACCENT     = colors.HexColor("#e8a020")
_LIGHT_GRAY = colors.HexColor("#f5f5f5")
_RULE_COLOR = colors.HexColor("#cccccc")
_GREEN      = colors.HexColor("#2e7d32")


# ── Response line helper ────────────────────────────────────────────────────

def _response_line(spaceafter=14):
    """A single full-width ruled response line."""
    return HRFlowable(
        width="100%", thickness=0.6, color=colors.black,
        spaceBefore=16, spaceAfter=spaceafter,
    )


def _response_lines(n=4):
    """n full-width response lines."""
    lines = []
    for _ in range(n):
        lines.append(_response_line())
    return lines


# ── Styles ──────────────────────────────────────────────────────────────────

def _build_styles():
    base = getSampleStyleSheet()
    return {
        "unit_title": ParagraphStyle(
            "unit_title", parent=base["Title"],
            fontSize=26, textColor=_DARK_BLUE,
            spaceAfter=6, alignment=TA_CENTER, leading=32,
        ),
        "unit_subtitle": ParagraphStyle(
            "unit_subtitle", parent=base["Normal"],
            fontSize=14, textColor=_MID_BLUE,
            spaceAfter=4, alignment=TA_CENTER, leading=18,
        ),
        "standard_code": ParagraphStyle(
            "standard_code", parent=base["Normal"],
            fontSize=10, textColor=colors.gray,
            spaceAfter=4, alignment=TA_CENTER,
        ),
        "section_header": ParagraphStyle(
            "section_header", parent=base["Heading1"],
            fontSize=14, textColor=colors.white,
            spaceBefore=10, spaceAfter=6,
            backColor=_DARK_BLUE, leading=20,
            leftIndent=-6, rightIndent=-6,
            borderPad=5,
        ),
        "subsection_header": ParagraphStyle(
            "subsection_header", parent=base["Heading2"],
            fontSize=11, textColor=_DARK_BLUE,
            spaceBefore=10, spaceAfter=3, leading=14,
            borderPad=0,
        ),
        "body": ParagraphStyle(
            "body", parent=base["Normal"],
            fontSize=11, leading=17, spaceAfter=6,
            alignment=TA_JUSTIFY,
        ),
        "body_left": ParagraphStyle(
            "body_left", parent=base["Normal"],
            fontSize=11, leading=17, spaceAfter=4,
        ),
        "primary_source": ParagraphStyle(
            "primary_source", parent=base["Normal"],
            fontSize=10, leading=15,
            leftIndent=12, rightIndent=12,
            textColor=colors.HexColor("#333333"),
            fontName="Times-Roman",
        ),
        "question": ParagraphStyle(
            "question", parent=base["Normal"],
            fontSize=11, leading=16, spaceAfter=4,
            leftIndent=0,
        ),
        "mc_choice": ParagraphStyle(
            "mc_choice", parent=base["Normal"],
            fontSize=11, leading=15, spaceAfter=3,
            leftIndent=20,
        ),
        "vocab_term": ParagraphStyle(
            "vocab_term", parent=base["Normal"],
            fontSize=12, textColor=_DARK_BLUE,
            spaceBefore=8, spaceAfter=2,
            fontName="Helvetica-Bold",
        ),
        "vocab_body": ParagraphStyle(
            "vocab_body", parent=base["Normal"],
            fontSize=10, leading=14, spaceAfter=3,
            leftIndent=12,
        ),
        "morphology": ParagraphStyle(
            "morphology", parent=base["Normal"],
            fontSize=10, leading=14, spaceAfter=3,
            leftIndent=12, textColor=_GREEN,
            fontName="Helvetica-Oblique",
        ),
        "cloze_body": ParagraphStyle(
            "cloze_body", parent=base["Normal"],
            fontSize=11, leading=20, spaceAfter=6,
            alignment=TA_JUSTIFY,
        ),
        "word_bank": ParagraphStyle(
            "word_bank", parent=base["Normal"],
            fontSize=11, leading=16, spaceAfter=4,
            leftIndent=12,
        ),
        "answer_header": ParagraphStyle(
            "answer_header", parent=base["Normal"],
            fontSize=13, textColor=colors.white,
            backColor=_DARK_BLUE, spaceAfter=8,
            spaceBefore=4, alignment=TA_CENTER, leading=18,
        ),
        "answer_body": ParagraphStyle(
            "answer_body", parent=base["Normal"],
            fontSize=10, leading=15, spaceAfter=4, leftIndent=8,
        ),
        "matching_term": ParagraphStyle(
            "matching_term", parent=base["Normal"],
            fontSize=11, leading=15, spaceAfter=2,
        ),
        "callout": ParagraphStyle(
            "callout", parent=base["Normal"],
            fontSize=10, leading=14, spaceAfter=4,
            leftIndent=10, rightIndent=10,
            textColor=colors.HexColor("#333333"),
        ),
    }


# ── Header / footer ─────────────────────────────────────────────────────────

def _header_footer(canvas, doc, unit_title: str):
    canvas.saveState()
    w, h = LETTER
    canvas.setFillColor(_DARK_BLUE)
    canvas.rect(0, h - 0.45 * inch, w, 0.45 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(0.5 * inch, h - 0.29 * inch, unit_title.upper())
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(w - 0.5 * inch, h - 0.29 * inch, "MN Citizenship & Government")
    canvas.setFillColor(colors.gray)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(w / 2, 0.3 * inch, f"Page {doc.page}")
    canvas.restoreState()


# ── Section divider ─────────────────────────────────────────────────────────

def _section(title: str, styles: dict):
    return [
        Spacer(1, 8),
        Paragraph(f"  {title}", styles["section_header"]),
        Spacer(1, 6),
    ]


# ── Text parsers ─────────────────────────────────────────────────────────────

def _inline_bold(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def _parse_passage(text: str, styles: dict):
    flowables = []
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            flowables.append(Spacer(1, 4))
        elif s.startswith("## "):
            flowables.append(Paragraph(s[3:], styles["subsection_header"]))
        elif s.startswith("# "):
            flowables.append(Paragraph(s[2:], styles["subsection_header"]))
        elif s.lower().startswith("big idea:"):
            flowables.append(Spacer(1, 6))
            flowables.append(Paragraph(f"<b>{_inline_bold(s)}</b>", styles["body_left"]))
        else:
            flowables.append(Paragraph(_inline_bold(s), styles["body"]))
    return flowables


def _parse_vocabulary(text: str, styles: dict):
    flowables = []
    for block in text.split("---"):
        block = block.strip()
        if not block:
            continue
        entry = {}
        for line in block.split("\n"):
            line = line.strip()
            if line.startswith("TERM:"):
                entry["term"] = line[5:].strip()
            elif line.startswith("DEFINITION:"):
                entry["definition"] = line[11:].strip()
            elif line.startswith("MORPHOLOGY:"):
                entry["morphology"] = line[11:].strip()
            elif line.startswith("EXAMPLE SENTENCE:"):
                entry["example"] = line[17:].strip()

        if not entry.get("term"):
            continue

        # Vocab card as a shaded table
        term_para   = Paragraph(entry.get("term", ""), styles["vocab_term"])
        def_para    = Paragraph(f"<b>Definition:</b> {entry.get('definition', '')}", styles["vocab_body"])
        morph_para  = Paragraph(f"🔤 <b>Word Parts:</b> {entry.get('morphology', '')}", styles["morphology"])
        ex_para     = Paragraph(f"<b>Example:</b> <i>{entry.get('example', '')}</i>", styles["vocab_body"])

        card = Table(
            [[term_para], [def_para], [morph_para], [ex_para]],
            colWidths=[6.5 * inch],
        )
        card.setStyle(TableStyle([
            ("BOX",         (0, 0), (-1, -1), 1,   _MID_BLUE),
            ("BACKGROUND",  (0, 0), (0, 0),         _LIGHT_BLUE),
            ("BACKGROUND",  (0, 1), (-1, -1),        colors.HexColor("#f9f9f9")),
            ("TOPPADDING",  (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING",(0,0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING",(0, 0), (-1, -1), 10),
        ]))
        flowables.append(card)
        flowables.append(Spacer(1, 8))
    return flowables


def _parse_cloze(text: str, styles: dict):
    flowables = []
    in_word_bank = False
    passage_lines = []
    word_bank_line = ""

    for line in text.split("\n"):
        s = line.strip()
        if s.lower().startswith("word bank:"):
            in_word_bank = True
            word_bank_line = s
        elif in_word_bank:
            word_bank_line += " " + s
        else:
            passage_lines.append(s)

    # Render passage — replace _____________ with underlined blanks
    passage_text = " ".join(l for l in passage_lines if l)
    # Replace blanks with styled underline spans
    parts = re.split(r"(_+)", passage_text)
    html_passage = ""
    for part in parts:
        if re.match(r"^_+$", part):
            html_passage += '<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>'
        else:
            html_passage += _inline_bold(part)
    flowables.append(Paragraph(html_passage, styles["cloze_body"]))
    flowables.append(Spacer(1, 10))

    # Word bank box
    if word_bank_line:
        wb_para = Paragraph(f"<b>{word_bank_line}</b>", styles["word_bank"])
        wb_table = Table([[wb_para]], colWidths=[6.5 * inch])
        wb_table.setStyle(TableStyle([
            ("BOX",          (0,0), (-1,-1), 1.5, _ACCENT),
            ("BACKGROUND",   (0,0), (-1,-1),       colors.HexColor("#fff8e1")),
            ("TOPPADDING",   (0,0), (-1,-1), 8),
            ("BOTTOMPADDING",(0,0), (-1,-1), 8),
            ("LEFTPADDING",  (0,0), (-1,-1), 10),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ]))
        flowables.append(wb_table)
    return flowables


def _parse_multiple_choice(text: str, styles: dict):
    flowables = []
    answer_key_line = ""
    lines = text.split("\n")

    for line in lines:
        s = line.strip()
        if not s:
            flowables.append(Spacer(1, 6))
            continue
        if s.lower().startswith("answer key:"):
            answer_key_line = s
            continue
        # Choice lines: A. B. C. D.
        if re.match(r"^[A-D]\.", s):
            flowables.append(Paragraph(s, styles["mc_choice"]))
        elif re.match(r"^\d+\.", s):
            flowables.append(Spacer(1, 6))
            flowables.append(Paragraph(f"<b>{s}</b>", styles["question"]))
        else:
            flowables.append(Paragraph(s, styles["body_left"]))

    return flowables


def _parse_matching(text: str, styles: dict):
    flowables = []
    col_a = []
    col_b = []
    answer_key = ""

    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        if s.lower().startswith("answer key:"):
            answer_key = s
            continue
        if "|" in s and not s.startswith("COLUMN"):
            parts = s.split("|", 1)
            left  = parts[0].strip()
            right = parts[1].strip() if len(parts) > 1 else ""
            if left:
                col_a.append(left)
            if right:
                col_b.append(right)

    if col_a and col_b:
        # Build two-column table
        rows = []
        for i in range(max(len(col_a), len(col_b))):
            left  = col_a[i] if i < len(col_a) else ""
            right = col_b[i] if i < len(col_b) else ""
            rows.append([
                Paragraph(left,  styles["matching_term"]),
                Paragraph(right, styles["matching_term"]),
            ])
        tbl = Table(rows, colWidths=[3.0 * inch, 3.5 * inch])
        tbl.setStyle(TableStyle([
            ("ROWBACKGROUNDS", (0,0), (-1,-1), [colors.white, _LIGHT_GRAY]),
            ("BOX",            (0,0), (-1,-1), 0.5, _RULE_COLOR),
            ("INNERGRID",      (0,0), (-1,-1), 0.3, _RULE_COLOR),
            ("TOPPADDING",     (0,0), (-1,-1), 5),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 5),
            ("LEFTPADDING",    (0,0), (-1,-1), 8),
            ("RIGHTPADDING",   (0,0), (-1,-1), 8),
        ]))
        flowables.append(tbl)

    return flowables


def _parse_answer_key(text: str, styles: dict):
    flowables = []
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            flowables.append(Spacer(1, 3))
        elif "ANSWER KEY" in s.upper() or "TEACHER COPY" in s.upper():
            flowables.append(Paragraph(s, styles["answer_header"]))
        elif s.startswith("---") or s.startswith("==="):
            flowables.append(HRFlowable(width="100%", thickness=1, color=_RULE_COLOR,
                                        spaceBefore=4, spaceAfter=4))
        else:
            flowables.append(Paragraph(_inline_bold(s), styles["answer_body"]))
    return flowables


# ── Unit infographics ────────────────────────────────────────────────────────

def _make_infographic(unit_number: int) -> Drawing:
    """Return a simple unit-specific Drawing graphic."""
    d = Drawing(468, 160)

    if unit_number == 1:
        # Bar chart: Ways citizens can participate
        labels = ["Vote", "Contact reps", "Attend meetings", "Volunteer", "Protest", "Run for office"]
        values = [85, 62, 45, 58, 30, 12]
        title  = "How Americans Participate in Civic Life (% who have done this)"
        _bar_chart(d, labels, values, title, _MID_BLUE)

    elif unit_number == 2:
        # Pillars of democracy graphic
        _pillars_graphic(d, ["Liberty", "Equality", "Justice", "Common\nGood", "Rule\nof Law"])

    elif unit_number == 3:
        # Selected Bill of Rights
        items = [
            ("1st", "Speech, Religion,\nPress, Assembly"),
            ("2nd", "Bear Arms"),
            ("4th", "No Unreasonable\nSearches"),
            ("5th", "Right to Remain\nSilent"),
            ("6th", "Fair Trial\nby Jury"),
        ]
        _rights_grid(d, items, "Selected Amendments from the Bill of Rights")

    elif unit_number == 4:
        # Three branches diagram
        _branches_diagram(d)

    elif unit_number == 5:
        # Policy process flow
        steps = ["Problem\nIdentified", "Policy\nProposed", "Debated\n& Voted", "Signed\ninto Law", "Enforced\n& Reviewed"]
        _flow_diagram(d, steps, "How a Public Policy Is Made")

    elif unit_number == 6:
        # MN tribal nations count + label
        _tribes_graphic(d)

    return d


def _bar_chart(d, labels, values, title, color):
    """Draw a simple horizontal bar chart using basic shapes."""
    max_val = max(values) or 1
    bar_h = 14
    gap = 5
    label_x = 130
    bar_x = label_x + 4
    max_bar_w = 290
    y_start = 20

    for i, (label, val) in enumerate(zip(labels, values)):
        y = y_start + (len(values) - 1 - i) * (bar_h + gap)
        bar_w = int((val / max_val) * max_bar_w)
        # Bar
        d.add(Rect(bar_x, y, bar_w, bar_h, fillColor=color, strokeColor=colors.white, strokeWidth=0.5))
        # Label (right-aligned before bar)
        d.add(String(bar_x - 4, y + 3, label, fontSize=7, fillColor=colors.HexColor("#333333"), textAnchor="end"))
        # Value
        d.add(String(bar_x + bar_w + 3, y + 3, f"{val}%", fontSize=7, fillColor=colors.gray))

    d.add(String(234, y_start + len(values) * (bar_h + gap) + 4, title,
                 fontSize=8, fillColor=colors.gray, textAnchor="middle"))


def _pillars_graphic(d, labels):
    colors_list = [_DARK_BLUE, _MID_BLUE, _GREEN, colors.HexColor("#7b1fa2"), _ACCENT]
    w = 80
    spacing = 93
    for i, label in enumerate(labels):
        x = 14 + i * spacing
        # Pillar body
        d.add(Rect(x, 20, w, 110, fillColor=colors_list[i % len(colors_list)],
                   strokeColor=colors.white, strokeWidth=1))
        for j, word in enumerate(label.split("\n")):
            d.add(String(x + w/2, 80 - j * 14, word, fontSize=10, fillColor=colors.white,
                         textAnchor="middle", fontName="Helvetica-Bold"))
    d.add(Rect(0, 10, 468, 14, fillColor=_DARK_BLUE, strokeColor=_DARK_BLUE))
    d.add(String(234, 14, "Core Democratic Values", fontSize=9, fillColor=colors.white,
                 textAnchor="middle"))


def _rights_grid(d, items, title):
    col_w = 88
    for i, (amend, desc) in enumerate(items):
        x = 4 + i * col_w
        d.add(Rect(x, 20, col_w - 6, 110, fillColor=_LIGHT_BLUE,
                   strokeColor=_MID_BLUE, strokeWidth=1.5))
        d.add(String(x + (col_w-6)/2, 110, amend, fontSize=16, fillColor=_DARK_BLUE,
                     textAnchor="middle", fontName="Helvetica-Bold"))
        for j, word in enumerate(desc.split("\n")):
            d.add(String(x + (col_w-6)/2, 76 - j * 13, word, fontSize=8,
                         fillColor=_DARK_BLUE, textAnchor="middle"))
    d.add(String(234, 148, title, fontSize=9, fillColor=colors.gray, textAnchor="middle"))


def _branches_diagram(d):
    boxes = [
        (20,  20, "LEGISLATIVE\n(Congress)", _DARK_BLUE,  "Makes laws"),
        (164, 20, "EXECUTIVE\n(President)",  _MID_BLUE,   "Enforces laws"),
        (308, 20, "JUDICIAL\n(Courts)",       _GREEN,      "Interprets laws"),
    ]
    for x, y, label, color, sub in boxes:
        d.add(Rect(x, y, 140, 100, fillColor=color, strokeColor=colors.white, strokeWidth=2))
        for j, line in enumerate(label.split("\n")):
            d.add(String(x + 70, 92 - j * 16, line, fontSize=10, fillColor=colors.white,
                         textAnchor="middle", fontName="Helvetica-Bold"))
        d.add(String(x + 70, 32, sub, fontSize=8, fillColor=colors.white, textAnchor="middle"))
    # Arrows between boxes
    for ax in [160, 304]:
        d.add(Line(ax, 70, ax + 4, 70, strokeColor=colors.white, strokeWidth=1))
    d.add(String(234, 148, "The Three Branches of the U.S. Government", fontSize=9,
                 fillColor=colors.gray, textAnchor="middle"))


def _flow_diagram(d, steps, title):
    box_w = 78
    for i, step in enumerate(steps):
        x = 4 + i * 92
        d.add(Rect(x, 30, box_w, 80, fillColor=_LIGHT_BLUE,
                   strokeColor=_MID_BLUE, strokeWidth=1.5))
        for j, line in enumerate(step.split("\n")):
            d.add(String(x + box_w/2, 72 - j * 14, line, fontSize=9,
                         fillColor=_DARK_BLUE, textAnchor="middle", fontName="Helvetica-Bold"))
        if i < len(steps) - 1:
            ax = x + box_w + 4
            d.add(Line(ax, 70, ax + 8, 70, strokeColor=_DARK_BLUE, strokeWidth=2))
            # Arrowhead
            d.add(String(ax + 9, 67, "▶", fontSize=8, fillColor=_DARK_BLUE))
    d.add(String(234, 148, title, fontSize=9, fillColor=colors.gray, textAnchor="middle"))


def _tribes_graphic(d):
    d.add(Rect(0, 0, 468, 160, fillColor=_LIGHT_BLUE, strokeColor=_MID_BLUE, strokeWidth=1))
    d.add(String(234, 140, "Minnesota's 11 Federally Recognized Tribal Nations",
                 fontSize=11, fillColor=_DARK_BLUE, textAnchor="middle",
                 fontName="Helvetica-Bold"))
    nations = [
        "Bois Forte Band", "Fond du Lac Band", "Grand Portage Band",
        "Leech Lake Band", "Mille Lacs Band", "White Earth Nation",
        "Red Lake Nation", "Red Cliff Band*", "Lower Sioux", "Upper Sioux",
        "Prairie Island",
    ]
    col_size = 4
    for i, name in enumerate(nations):
        col = i % 3
        row = i // 3
        x = 20 + col * 155
        y = 112 - row * 20
        d.add(Circle(x, y + 4, 4, fillColor=_MID_BLUE, strokeColor=colors.white))
        d.add(String(x + 10, y, name, fontSize=8, fillColor=_DARK_BLUE))
    d.add(String(234, 8, "*Red Cliff is Wisconsin-based but has MN connections",
                 fontSize=7, fillColor=colors.gray, textAnchor="middle"))


# ── Main builder ─────────────────────────────────────────────────────────────

def build_pdf(unit: dict, sections: dict, output_dir: Path) -> Path:
    """
    Build a single unit workbook PDF.

    sections keys: 'passage', 'vocabulary', 'cloze', 'multiple_choice',
                   'matching', 'discussion_questions', 'answer_key'
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / unit["filename"]
    styles = _build_styles()

    doc = SimpleDocTemplate(
        str(out_path), pagesize=LETTER,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch, bottomMargin=0.6*inch,
    )

    def on_page(canvas, doc_):
        _header_footer(canvas, doc_, unit["title"])

    story = []

    # ── Title page ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 1.2 * inch))
    story.append(Paragraph("Minnesota Civics Workbook", styles["standard_code"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(f"Unit {unit['number']}", styles["unit_subtitle"]))
    story.append(Paragraph(unit["title"], styles["unit_title"]))
    story.append(Paragraph(unit["subtitle"], styles["unit_subtitle"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(
        f"MN Standard {unit['standard_code']} — Citizenship and Government",
        styles["standard_code"],
    ))
    story.append(Spacer(1, 0.25 * inch))
    story.append(HRFlowable(width="100%", thickness=1.5, color=_MID_BLUE,
                             spaceBefore=0, spaceAfter=10))
    story.append(Paragraph(unit["description"], styles["body"]))
    story.append(Spacer(1, 0.8 * inch))
    story.append(Paragraph(
        "Name: ____________________________ &nbsp;&nbsp; Date: ______________ &nbsp;&nbsp; Period: _____",
        styles["body_left"],
    ))
    story.append(PageBreak())

    # ── Infographic ─────────────────────────────────────────────────────────
    story += _section("Did You Know?", styles)
    infographic = _make_infographic(unit["number"])
    story.append(infographic)
    story.append(Spacer(1, 10))

    # ── Reading passage ──────────────────────────────────────────────────────
    story += _section("Reading Passage", styles)
    story += _parse_passage(sections["passage"], styles)
    story.append(PageBreak())

    # ── Primary source ───────────────────────────────────────────────────────
    ps = unit["primary_source"]
    story += _section("Primary Source Document", styles)
    story.append(Paragraph(f"<b>{ps['title']}</b>", styles["body_left"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(ps["context"], styles["body"]))
    story.append(Spacer(1, 8))

    excerpt_para = Paragraph(f'<i>"{ps["excerpt"]}"</i>', styles["primary_source"])
    src_table = Table([[excerpt_para]], colWidths=[6.5 * inch])
    src_table.setStyle(TableStyle([
        ("BOX",            (0,0), (-1,-1), 1.5, _MID_BLUE),
        ("BACKGROUND",     (0,0), (-1,-1),       _LIGHT_BLUE),
        ("TOPPADDING",     (0,0), (-1,-1), 12),
        ("BOTTOMPADDING",  (0,0), (-1,-1), 12),
        ("LEFTPADDING",    (0,0), (-1,-1), 14),
        ("RIGHTPADDING",   (0,0), (-1,-1), 14),
    ]))
    story.append(src_table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Analyze the Source — Answer these questions:</b>", styles["body_left"]))
    for q in [
        "1. What is the main point of this document?",
        "2. Who created it, and when?",
        "3. How does it connect to what you read in the passage?",
    ]:
        story.append(Spacer(1, 10))
        story.append(Paragraph(q, styles["question"]))
        story += _response_lines(3)

    story.append(PageBreak())

    # ── Vocabulary ───────────────────────────────────────────────────────────
    story += _section("Key Vocabulary & Word Parts", styles)
    story.append(Paragraph(
        "Study these important words. The Word Parts section shows how the word is built — "
        "knowing the parts helps you figure out what new words mean!",
        styles["body_left"],
    ))
    story.append(Spacer(1, 8))
    story += _parse_vocabulary(sections["vocabulary"], styles)
    story.append(PageBreak())

    # ── CLOZE ────────────────────────────────────────────────────────────────
    story += _section("CLOZE Activity — Fill in the Blanks", styles)
    story.append(Paragraph(
        "Directions: Use the Word Bank to fill in the missing words in the passage below.",
        styles["body_left"],
    ))
    story.append(Spacer(1, 8))
    story += _parse_cloze(sections["cloze"], styles)
    story.append(PageBreak())

    # ── Multiple choice ──────────────────────────────────────────────────────
    story += _section("Multiple Choice Questions", styles)
    story.append(Paragraph(
        "Directions: Circle the best answer for each question.",
        styles["body_left"],
    ))
    story.append(Spacer(1, 6))
    story += _parse_multiple_choice(sections["multiple_choice"], styles)
    story.append(PageBreak())

    # ── Matching ─────────────────────────────────────────────────────────────
    story += _section("Matching — Terms and Definitions", styles)
    story.append(Paragraph(
        "Directions: Draw a line or write the letter from Column B that matches each term in Column A.",
        styles["body_left"],
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Column A — Terms</b>", styles["body_left"]))
    story += _parse_matching(sections["matching"], styles)
    story.append(PageBreak())

    # ── Short answer ─────────────────────────────────────────────────────────
    story += _section("Short Answer Questions", styles)
    story.append(Paragraph(
        "Directions: Answer each question in 2–4 complete sentences.",
        styles["body_left"],
    ))
    story.append(Spacer(1, 8))
    for line in sections["discussion_questions"].split("\n"):
        s = line.strip()
        if not s:
            story.append(Spacer(1, 4))
            continue
        story.append(Paragraph(s, styles["question"]))
        story += _response_lines(4)
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ── Answer key ───────────────────────────────────────────────────────────
    story += _parse_answer_key(sections["answer_key"], styles)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    return out_path

"""
Shared teacher slide deck (.pptx) builder — Google Slides compatible.
Given a course config + units, emits: title slide, then per unit a divider
slide, then one slide per lesson (objectives, vocab, warm-up, mini-lesson
bullets, activity, reading callout if present, quiz preview, exit ticket).
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def hexcolor(h):
    h = h.replace("#", "")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def add_blank_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def fill_bg(slide, color):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = color


def add_text(slide, left, top, width, height, text, size=18, bold=False, color=RGBColor(0x1A, 0x1A, 0x1A),
             align=PP_ALIGN.LEFT, font="Calibri", italic=False):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font
    return box


def add_bullets(slide, left, top, width, height, items, size=13, color=RGBColor(0x1A, 0x1A, 0x1A), font="Calibri"):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.name = font
        p.space_after = Pt(6)
    return box


def build_pptx(*, output_path, course_title, school_name, grade, semester_label,
               primary_hex, primary_dk_hex, accent_hex, units, hero_icon):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    primary = hexcolor(primary_hex)
    primary_dk = hexcolor(primary_dk_hex)
    accent = hexcolor(accent_hex)
    white = RGBColor(0xFF, 0xFF, 0xFF)

    # ---- Title slide ----
    slide = add_blank_slide(prs)
    fill_bg(slide, primary_dk)
    add_text(slide, 0.8, 2.3, 11.7, 1.2, course_title, size=44, bold=True, color=white)
    add_text(slide, 0.8, 3.5, 11.7, 0.6, f"{school_name} · {grade} · {semester_label}", size=20, color=accent)
    add_text(slide, 0.8, 4.2, 11.7, 0.6, "Teacher Slide Deck — one slide per lesson, 82 lessons total", size=15, italic=True, color=white)

    total_days = sum(len(u["lessons"]) for u in units)

    for u in units:
        meta, lessons = u["meta"], u["lessons"]

        # Unit divider slide
        slide = add_blank_slide(prs)
        fill_bg(slide, primary)
        add_text(slide, 0.8, 1.0, 11.7, 0.5, f"UNIT {meta['number']}", size=18, bold=True, color=accent)
        add_text(slide, 0.8, 1.5, 11.7, 1.2, meta["name"], size=36, bold=True, color=white)
        add_text(slide, 0.8, 2.7, 11.7, 0.8, meta.get("essential_question", ""), size=18, italic=True, color=white)
        add_text(slide, 0.8, 3.6, 11.7, 0.5, f"Days {meta['days'][0]}–{meta['days'][1]} · {len(lessons)} lessons", size=14, color=accent)
        vocab_words = ", ".join(v["word"] for v in meta.get("vocabulary_bank", []))
        add_text(slide, 0.8, 4.3, 11.7, 2.2, f"Vocabulary bank: {vocab_words}", size=13, color=white)

        for l in lessons:
            slide = add_blank_slide(prs)
            fill_bg(slide, white)
            # Header bar
            hdr = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(0.9))
            hdr.fill.solid()
            hdr.fill.fore_color.rgb = primary
            hdr.line.fill.background()
            tf = hdr.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = f"Day {l['day']}  ·  {l['title']}"
            run.font.size = Pt(22)
            run.font.bold = True
            run.font.color.rgb = white
            tf.margin_left = Inches(0.3)
            tf.vertical_anchor = 1  # middle-ish

            left_col_x = 0.5
            right_col_x = 6.9
            top_y = 1.15

            # Left column: objectives + vocab
            add_text(slide, left_col_x, top_y, 6.0, 0.35, "Objectives", size=15, bold=True, color=primary_dk)
            add_bullets(slide, left_col_x, top_y + 0.4, 6.0, 1.3, l.get("objectives", []), size=12.5)

            vocab_items = [f"{v['word']}: {v.get('definition','')}" for v in l.get("vocab", [])]
            add_text(slide, left_col_x, top_y + 1.8, 6.0, 0.35, "Vocabulary", size=15, bold=True, color=primary_dk)
            add_bullets(slide, left_col_x, top_y + 2.2, 6.0, 1.3, vocab_items, size=12)

            add_text(slide, left_col_x, top_y + 3.6, 6.0, 0.35, "Warm-Up", size=15, bold=True, color=primary_dk)
            add_text(slide, left_col_x, top_y + 4.0, 6.0, 1.0, l.get("warm_up", ""), size=12)

            act = l.get("activity") or {}
            add_text(slide, left_col_x, top_y + 5.05, 6.0, 0.35, "Activity", size=15, bold=True, color=primary_dk)
            add_text(slide, left_col_x, top_y + 5.4, 6.0, 1.6, f"{act.get('title','')}: {act.get('instructions','')}", size=11.5)

            # Right column: mini-lesson bullets + reading + exit ticket
            add_text(slide, right_col_x, top_y, 6.0, 0.35, "Mini-Lesson", size=15, bold=True, color=primary_dk)
            mini_items = [s.get("heading", "") for s in l.get("mini_lesson", [])]
            add_bullets(slide, right_col_x, top_y + 0.4, 6.0, 1.0, mini_items, size=12.5)

            reading = l.get("reading")
            y_cursor = top_y + 1.6
            if reading:
                add_text(slide, right_col_x, y_cursor, 6.0, 0.35,
                         f"Reading ({reading['type'].replace('_',' ').title()})", size=15, bold=True, color=primary_dk)
                add_text(slide, right_col_x, y_cursor + 0.4, 6.0, 0.6, reading.get("title", ""), size=12, italic=True)
                y_cursor += 1.15
            else:
                y_cursor += 0.2

            quiz = l.get("quiz") or {}
            n_q = len(quiz.get("questions", []))
            add_text(slide, right_col_x, y_cursor, 6.0, 0.35, "Quiz", size=15, bold=True, color=primary_dk)
            add_text(slide, right_col_x, y_cursor + 0.4, 6.0, 0.5, f"{n_q} question(s) — see student workbook for full text", size=12)
            y_cursor += 1.0

            et = l.get("exit_ticket") or {}
            box = slide.shapes.add_shape(1, Inches(right_col_x), Inches(y_cursor), Inches(6.0), Inches(1.3))
            box.fill.solid()
            box.fill.fore_color.rgb = primary_dk
            box.line.fill.background()
            btf = box.text_frame
            btf.word_wrap = True
            bp = btf.paragraphs[0]
            brun = bp.add_run()
            brun.text = "EXIT TICKET"
            brun.font.size = Pt(11)
            brun.font.bold = True
            brun.font.color.rgb = accent
            bp2 = btf.add_paragraph()
            brun2 = bp2.add_run()
            brun2.text = et.get("prompt", "")
            brun2.font.size = Pt(12.5)
            brun2.font.color.rgb = white

            # Second slide per lesson: Apply It scenario + Academic Vocabulary word of the day
            app = l.get("application")
            av = l.get("academic_vocab")
            if app or av:
                slide2 = add_blank_slide(prs)
                fill_bg(slide2, white)
                hdr2 = slide2.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(0.9))
                hdr2.fill.solid()
                hdr2.fill.fore_color.rgb = primary_dk
                hdr2.line.fill.background()
                htf = hdr2.text_frame
                htf.word_wrap = True
                hp = htf.paragraphs[0]
                hrun = hp.add_run()
                hrun.text = f"Day {l['day']}  ·  Apply It + Academic Vocabulary"
                hrun.font.size = Pt(20)
                hrun.font.bold = True
                hrun.font.color.rgb = white
                htf.margin_left = Inches(0.3)

                if app:
                    add_text(slide2, 0.5, 1.15, 7.6, 0.4,
                             f"Apply It: {app.get('type','').replace('_',' ').title()}", size=17, bold=True, color=primary_dk)
                    add_text(slide2, 0.5, 1.6, 7.6, 0.4, app.get("title", ""), size=14, bold=True, italic=True, color=primary)
                    add_text(slide2, 0.5, 2.05, 7.6, 3.3, app.get("scenario", ""), size=12)
                    box2 = slide2.shapes.add_shape(1, Inches(0.5), Inches(5.5), Inches(7.6), Inches(1.4))
                    box2.fill.solid()
                    box2.fill.fore_color.rgb = hexcolor("#E8F5E9")
                    box2.line.color.rgb = hexcolor("#C8E6C9")
                    btf2 = box2.text_frame
                    btf2.word_wrap = True
                    bp3 = btf2.paragraphs[0]
                    brun3 = bp3.add_run()
                    brun3.text = "TASK"
                    brun3.font.size = Pt(11)
                    brun3.font.bold = True
                    brun3.font.color.rgb = hexcolor("#1B5E20")
                    bp4 = btf2.add_paragraph()
                    brun4 = bp4.add_run()
                    brun4.text = app.get("task", "")
                    brun4.font.size = Pt(13)
                    brun4.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

                if av:
                    ax = 8.4
                    add_text(slide2, ax, 1.15, 4.4, 0.4, "Academic Vocabulary", size=17, bold=True, color=primary_dk)
                    aw_text = av.get("word", "")
                    if av.get("syllables"):
                        aw_text += f"  ({av['syllables']})"
                    add_text(slide2, ax, 1.6, 4.4, 0.5, aw_text, size=16, bold=True, color=hexcolor("#4527A0"))
                    add_text(slide2, ax, 2.15, 4.4, 1.0, av.get("definition", ""), size=12.5)
                    y3 = 3.2
                    if av.get("morphology"):
                        add_text(slide2, ax, y3, 4.4, 1.0, f"Word study: {av['morphology']}", size=11, italic=True, color=RGBColor(0x55,0x55,0x55))
                        y3 += 1.05
                    if av.get("example"):
                        add_text(slide2, ax, y3, 4.4, 1.0, av["example"], size=11.5, italic=True, color=hexcolor("#4527A0"))

    prs.save(output_path)
    return output_path

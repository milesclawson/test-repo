"""
Shared course website builder.
Given a course config + list of (unit_meta, lessons) tuples, emits a single
self-contained index.html with client-side rendering (one JSON blob, JS
templating) — this is what scales to 80+ lessons without hand-writing a
static page per lesson.

Usage: see build_ccr_site.py / build_helpdesk_site.py
"""
import json
import html as html_mod


def esc(s):
    if s is None:
        return ""
    return html_mod.escape(str(s), quote=True)


def build_site(*, output_path, course_title, school_name, grade, semester_label,
                theme, hero_icon, hero_tagline, units, downloads, footer_note,
                assessment_label="Unit Assessment"):
    """
    theme: dict with keys primary, primary_dk, accent, accent_lt, mascot (emoji)
    units: list of dicts: {"meta": {...UNIT_META...}, "lessons": [...LESSON dicts...]}
    downloads: list of {"file": "relative/path", "label": "...", "desc": "...", "icon": "emoji"}
    """
    total_days = sum(len(u["lessons"]) for u in units)

    # Build the JSON data blob consumed by client-side JS.
    data = {
        "courseTitle": course_title,
        "schoolName": school_name,
        "grade": grade,
        "semesterLabel": semester_label,
        "totalDays": total_days,
        "assessmentLabel": assessment_label,
        "units": [],
    }
    for u in units:
        meta = dict(u["meta"])
        lessons = u["lessons"]
        data["units"].append({
            "number": meta.get("number"),
            "name": meta.get("name"),
            "essential_question": meta.get("essential_question"),
            "overview": meta.get("overview"),
            "vocabulary_bank": meta.get("vocabulary_bank", []),
            "unit_assessment": meta.get("unit_assessment", {}),
            "days": meta.get("days"),
            "lessons": lessons,
        })

    data_json = json.dumps(data, ensure_ascii=False)

    downloads_html = "\n".join(
        f'''<a class="dl-card" href="{esc(d["file"])}" download>
          <div class="dl-icon">{d.get("icon","📄")}</div>
          <div class="dl-title">{esc(d["label"])}</div>
          <div class="dl-desc">{esc(d.get("desc",""))}</div>
        </a>''' for d in downloads
    )

    unit_nav_html = "\n".join(
        f'''<a href="#" data-page="unit-{u['meta']['number']}" onclick="return show('unit-{u['meta']['number']}')">
          <span class="nav-icon">📘</span>Unit {u['meta']['number']} · {esc(u['meta']['name'])}
        </a>''' for u in units
    )

    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(course_title)} — {esc(school_name)}</title>
<style>
:root{{
  --primary:{theme['primary']};--primary-dk:{theme['primary_dk']};
  --accent:{theme['accent']};--accent-lt:{theme['accent_lt']};
  --gray:#F4F4F4;--border:#E0E0E0;--text:#1A1A1A;--muted:#666;
  --white:#fff;--radius:10px;--shadow:0 2px 8px rgba(0,0,0,.08);
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:var(--text);background:#fafafa;display:flex;min-height:100vh}}
#sidebar{{width:260px;flex-shrink:0;background:var(--primary-dk);color:#fff;display:flex;flex-direction:column;min-height:100vh;position:sticky;top:0;height:100vh;overflow-y:auto}}
.sidebar-brand{{padding:20px 18px 14px;border-bottom:1px solid rgba(255,255,255,.15)}}
.sidebar-brand .school{{font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin-bottom:4px}}
.sidebar-brand .course{{font-size:18px;font-weight:700;line-height:1.25;color:#fff}}
.sidebar-brand .grade{{font-size:12px;color:rgba(255,255,255,.6);margin-top:3px}}
.sidebar-mascot{{text-align:center;padding:12px 0 8px;font-size:36px}}
nav{{flex:1;padding:8px 0}}
nav a{{display:flex;align-items:center;gap:10px;padding:9px 18px;font-size:13px;color:rgba(255,255,255,.8);text-decoration:none;transition:background .15s,color .15s;border-left:3px solid transparent}}
nav a:hover{{background:rgba(255,255,255,.08);color:#fff}}
nav a.active{{background:rgba(255,255,255,.12);color:#fff;border-left-color:var(--accent)}}
nav .nav-section{{padding:12px 18px 4px;font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.35)}}
nav a .nav-icon{{font-size:16px;width:20px;text-align:center;flex-shrink:0}}
#main{{flex:1;min-width:0;padding:0}}
.page{{display:none;padding:32px 36px;max-width:1080px}}
.page.active{{display:block}}
.page-hero{{background:linear-gradient(135deg,var(--primary-dk) 0%,var(--primary) 100%);color:#fff;border-radius:var(--radius);padding:28px 32px;margin-bottom:28px;display:flex;align-items:center;gap:24px}}
.page-hero-icon{{font-size:48px;flex-shrink:0}}
.page-hero h1{{font-size:26px;font-weight:700;margin-bottom:4px}}
.page-hero p{{font-size:14px;opacity:.9;line-height:1.6}}
.page-hero .hero-badge{{display:inline-block;background:var(--accent);color:var(--primary-dk);font-size:11px;font-weight:700;padding:3px 10px;border-radius:99px;margin-top:8px;letter-spacing:.04em}}
.section-h{{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:24px 0 12px}}
.section-h:first-child{{margin-top:0}}
.card{{background:var(--white);border:1px solid var(--border);border-radius:var(--radius);padding:20px 22px;box-shadow:var(--shadow);margin-bottom:16px}}
.card-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin-bottom:24px}}
.unit-card{{background:var(--white);border:1px solid var(--border);border-radius:var(--radius);padding:18px;box-shadow:var(--shadow);cursor:pointer;transition:transform .15s,box-shadow .15s;text-decoration:none;color:inherit;display:block}}
.unit-card:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(0,0,0,.12)}}
.unit-card .uc-icon{{font-size:28px;margin-bottom:8px}}
.unit-card .uc-label{{font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}}
.unit-card .uc-title{{font-size:15px;font-weight:600;margin-bottom:6px}}
.unit-card .uc-count{{font-size:12px;color:var(--muted)}}
.lesson-table{{width:100%;border-collapse:collapse;font-size:13.5px}}
.lesson-table th{{text-align:left;padding:10px 12px;background:var(--gray);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--border)}}
.lesson-table td{{padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:top}}
.lesson-table tr:last-child td{{border-bottom:none}}
.lesson-table tr.clickable{{cursor:pointer}}
.lesson-table tr.clickable:hover td{{background:var(--gray)}}
.lesson-num{{font-weight:600;color:var(--primary);white-space:nowrap}}
.tag{{display:inline-block;font-size:10.5px;padding:2px 7px;border-radius:99px;font-weight:600;margin-right:3px;white-space:nowrap}}
.tag-fic{{background:#E8F5E9;color:#1B5E20}}
.tag-gn{{background:#EDE7F6;color:#4527A0}}
.tag-info{{background:#E3F2FD;color:#0D47A1}}
.tag-quiz{{background:#FFF3E0;color:#E65100}}
.tag-app{{background:#E8F5E9;color:#1B5E20}}
.back-link{{display:inline-block;margin-bottom:16px;font-size:13px;color:var(--primary);text-decoration:none;font-weight:600}}
.back-link:hover{{text-decoration:underline}}
.vocab-card{{background:var(--accent-lt);border:1px solid var(--border);border-radius:8px;padding:12px 16px;margin-bottom:8px}}
.vocab-card .vword{{font-weight:700;color:var(--primary-dk);font-size:14px}}
.vocab-card .vsyll{{font-size:12px;color:var(--primary);font-family:Georgia,serif;font-style:italic;margin-top:1px}}
.vocab-card .vdef{{font-size:13px;color:var(--text);margin-top:4px}}
.vocab-card .vmorph{{font-size:12px;color:var(--muted);margin-top:4px;padding-top:4px;border-top:1px dashed var(--border)}}
.vocab-card .vmorph b{{color:var(--primary-dk)}}
.vocab-card .vex{{font-size:12.5px;color:var(--muted);font-style:italic;margin-top:4px}}
.academic-box{{background:#EDE7F6;border:1px solid #D8CCF0;border-radius:8px;padding:14px 16px;margin-bottom:16px}}
.academic-box .aw-label{{font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#4527A0;margin-bottom:6px}}
.academic-box .aw-word{{font-size:16px;font-weight:700;color:#2E1A6B;display:inline-block;margin-right:8px}}
.academic-box .aw-syll{{font-size:13px;color:#4527A0;font-family:Georgia,serif;font-style:italic}}
.academic-box .aw-def{{font-size:13px;margin-top:4px}}
.academic-box .aw-morph{{font-size:12px;color:var(--muted);margin-top:4px}}
.academic-box .aw-ex{{font-size:12.5px;font-style:italic;color:var(--muted);margin-top:4px}}
.app-box{{background:#E8F5E9;border:1px solid #C8E6C9;border-radius:8px;padding:16px 18px;margin-bottom:16px}}
.app-box .app-type{{font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#1B5E20;margin-bottom:6px}}
.app-box .app-title{{font-size:15px;font-weight:700;margin-bottom:8px}}
.app-box .app-scenario{{font-size:13.5px;line-height:1.7;white-space:pre-wrap;margin-bottom:10px}}
.app-box .app-task{{font-size:13px;background:rgba(255,255,255,.6);border-radius:6px;padding:10px 12px;font-weight:600}}
.obj-list{{list-style:none;padding:0}}
.obj-list li{{padding:6px 0 6px 26px;position:relative;font-size:14px}}
.obj-list li::before{{content:"✓";position:absolute;left:0;color:var(--primary);font-weight:700}}
.mini-section{{margin-bottom:14px}}
.mini-section h4{{font-size:14px;font-weight:700;color:var(--primary-dk);margin-bottom:4px}}
.mini-section p{{font-size:13.5px;line-height:1.6;color:var(--text)}}
.activity-box{{background:#FFF8E1;border:1px solid #F0E0A8;border-radius:8px;padding:14px 16px;margin-bottom:16px}}
.activity-box .a-title{{font-weight:700;font-size:14px;color:#8a6d00;margin-bottom:4px}}
.reading-box{{background:#F3F0FF;border:1px solid #DDD3FA;border-radius:8px;padding:16px 18px;margin-bottom:16px}}
.reading-box .r-type{{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#4527A0;margin-bottom:6px}}
.reading-box .r-title{{font-size:15px;font-weight:700;margin-bottom:8px}}
.reading-box .r-body{{font-size:13.5px;line-height:1.7;white-space:pre-wrap;margin-bottom:10px}}
.reading-box .r-questions{{font-size:13px}}
.reading-box .r-questions li{{margin-bottom:4px;margin-left:18px}}
.quiz-box{{background:#FFF3E0;border:1px solid #F0D090;border-radius:8px;padding:14px 16px;margin-bottom:16px}}
.quiz-q{{margin-bottom:12px;font-size:13.5px}}
.quiz-q .qtext{{font-weight:600;margin-bottom:4px}}
.quiz-q .choices{{margin-left:14px;color:var(--text)}}
.quiz-q .choices div{{padding:2px 0}}
.quiz-q .ans{{color:#2E7D32;font-size:12.5px;margin-top:3px;font-weight:600}}
.exit-box{{background:var(--primary-dk);color:#fff;border-radius:8px;padding:16px 18px;margin-bottom:8px}}
.exit-box .e-label{{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--accent);margin-bottom:6px}}
.exit-box .e-prompt{{font-size:14px;line-height:1.5}}
.slide-strip{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}}
.slide-chip{{background:var(--gray);border:1px solid var(--border);border-radius:6px;padding:6px 10px;font-size:12px}}
.dl-card{{display:block;background:var(--white);border:1px solid var(--border);border-radius:var(--radius);padding:18px;box-shadow:var(--shadow);text-decoration:none;color:inherit;transition:transform .15s}}
.dl-card:hover{{transform:translateY(-2px)}}
.dl-icon{{font-size:28px;margin-bottom:8px}}
.dl-title{{font-weight:700;font-size:14px;margin-bottom:4px;color:var(--primary-dk)}}
.dl-desc{{font-size:12.5px;color:var(--muted)}}
.pill-row{{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}}
.pill{{background:var(--accent-lt);color:var(--primary-dk);font-size:12px;font-weight:600;padding:4px 10px;border-radius:99px}}
.lesson-title-row{{display:flex;align-items:center;gap:12px;margin-bottom:6px;flex-wrap:wrap}}
.day-badge{{background:var(--primary);color:#fff;font-weight:700;font-size:13px;padding:4px 12px;border-radius:99px}}
footer.note{{font-size:12px;color:var(--muted);margin-top:24px;padding-top:16px;border-top:1px solid var(--border)}}
@media(max-width:800px){{body{{flex-direction:column}}#sidebar{{width:100%;height:auto;position:relative}}.page{{padding:20px}}}}
</style>
</head>
<body>
<div id="sidebar">
  <div class="sidebar-brand">
    <div class="school">{esc(school_name)}</div>
    <div class="course">{esc(course_title)}</div>
    <div class="grade">{esc(grade)} · {esc(semester_label)}</div>
  </div>
  <div class="sidebar-mascot">{hero_icon}</div>
  <nav>
    <a href="#" data-page="home" class="active" onclick="return show('home')"><span class="nav-icon">🏠</span>Course Home</a>
    <div class="nav-section">Units</div>
    {unit_nav_html}
    <div class="nav-section">Resources</div>
    <a href="#" data-page="pacing" onclick="return show('pacing')"><span class="nav-icon">🗓</span>Pacing Guide (82 Days)</a>
    <a href="#" data-page="teacher" onclick="return show('teacher')"><span class="nav-icon">🧑‍🏫</span>Teacher Resources</a>
  </nav>
</div>

<div id="main">

<div class="page active" id="page-home">
  <div class="page-hero">
    <div class="page-hero-icon">{hero_icon}</div>
    <div>
      <h1>{esc(course_title)}</h1>
      <p>{esc(hero_tagline)}</p>
      <span class="hero-badge">{esc(semester_label)} · {total_days} Lessons</span>
    </div>
  </div>

  <h2 class="section-h">Course units</h2>
  <div class="card-grid" id="unit-cards"></div>

  <h2 class="section-h">Every lesson includes</h2>
  <div class="card-grid">
    <div class="card"><strong>🗣️ Vocabulary support</strong><p style="font-size:13px;color:var(--muted);margin-top:6px">1-3 new terms per lesson with plain-language definitions and in-context examples, recycled across the unit.</p></div>
    <div class="card"><strong>📖 Reading (as applicable)</strong><p style="font-size:13px;color:var(--muted);margin-top:6px">Serialized realistic fiction, graphic-novel-style panel scripts, and informational nonfiction with comprehension questions.</p></div>
    <div class="card"><strong>🧪 Quiz</strong><p style="font-size:13px;color:var(--muted);margin-top:6px">A short mixed multiple-choice / short-answer check tied to the day's objective, plus a longer cumulative unit assessment.</p></div>
    <div class="card"><strong>🚪 Exit ticket</strong><p style="font-size:13px;color:var(--muted);margin-top:6px">One focused prompt every single lesson — a quick check before dismissal.</p></div>
    <div class="card"><strong>🖥️ Teacher slide</strong><p style="font-size:13px;color:var(--muted);margin-top:6px">Slide bullets for every lesson, exported as a full Google Slides-compatible deck.</p></div>
    <div class="card"><strong>📓 Student workbook page</strong><p style="font-size:13px;color:var(--muted);margin-top:6px">Printable workbook page per lesson: vocab, notes space, activity, quiz, and exit ticket.</p></div>
  </div>
</div>

<div class="page" id="page-unit"></div>
<div class="page" id="page-lesson"></div>
<div class="page" id="page-pacing"></div>

<div class="page" id="page-teacher">
  <div class="page-hero">
    <div class="page-hero-icon">🧑‍🏫</div>
    <div>
      <h1>Teacher Resources</h1>
      <p>Downloadable materials for {esc(course_title)}.</p>
    </div>
  </div>
  <h2 class="section-h">Downloadable materials</h2>
  <div class="card-grid">
    {downloads_html}
  </div>
  <footer class="note">{esc(footer_note)}</footer>
</div>

</div>

<script>
const DATA = {data_json};

function show(pageId, scrollTop){{
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('active', a.dataset.page===pageId || (pageId||'').startsWith('unit-') && a.dataset.page===('unit-'+(pageId||'').split('-')[1])));
  const map = {{'home':'page-home','pacing':'page-pacing','teacher':'page-teacher'}};
  let targetId = map[pageId];
  if(!targetId && pageId && pageId.startsWith('unit-')){{ renderUnit(parseInt(pageId.split('-')[1])); targetId='page-unit'; }}
  if(!targetId && pageId && pageId.startsWith('lesson-')){{ renderLesson(parseInt(pageId.split('-')[1])); targetId='page-lesson'; }}
  if(pageId==='pacing') renderPacing();
  if(pageId==='home') renderHome();
  const t=document.getElementById(targetId);
  if(t){{t.classList.add('active'); if(scrollTop!==false) window.scrollTo(0,0);}}
  return false;
}}

function allLessons(){{
  let out=[];
  DATA.units.forEach(u=>u.lessons.forEach(l=>out.push(l)));
  return out;
}}
function findLesson(day){{ return allLessons().find(l=>l.day===day); }}
function findUnit(num){{ return DATA.units.find(u=>u.number===num); }}

function renderHome(){{
  const grid = document.getElementById('unit-cards');
  grid.innerHTML = DATA.units.map(u => `
    <a class="unit-card" href="#" onclick="return show('unit-${{u.number}}')">
      <div class="uc-icon">📘</div>
      <div class="uc-label">Unit ${{u.number}}</div>
      <div class="uc-title">${{u.name}}</div>
      <div class="uc-count">${{u.lessons.length}} lessons · Days ${{u.days[0]}}–${{u.days[1]}}</div>
    </a>`).join('');
}}

function tagsFor(l){{
  let t = '';
  if(l.reading){{
    if(l.reading.type==='graphic_novel') t += '<span class="tag tag-gn">Graphic Novel</span>';
    else if(l.reading.type==='realistic_fiction') t += '<span class="tag tag-fic">Fiction</span>';
    else t += '<span class="tag tag-info">Reading</span>';
  }}
  if(l.quiz && l.quiz.questions && l.quiz.questions.length) t += '<span class="tag tag-quiz">Quiz</span>';
  if(l.application) t += '<span class="tag tag-app">' + l.application.type.replace(/_/g,' ').replace(/\\b\\w/g, c=>c.toUpperCase()) + '</span>';
  return t;
}}

function renderUnit(num){{
  const u = findUnit(num);
  const page = document.getElementById('page-unit');
  const vocabHtml = (u.vocabulary_bank||[]).map(v=>`<div class="vocab-card"><div class="vword">${{v.word}}</div>${{v.syllables?`<div class="vsyll">${{v.syllables}}</div>`:''}}<div class="vdef">${{v.definition}}</div>${{v.morphology?`<div class="vmorph"><b>Word study:</b> ${{v.morphology}}</div>`:''}}</div>`).join('');
  const rows = u.lessons.map(l => `
    <tr class="clickable" onclick="show('lesson-${{l.day}}')">
      <td class="lesson-num">Day ${{l.day}}</td>
      <td>${{l.title}}</td>
      <td>${{tagsFor(l)}}</td>
    </tr>`).join('');
  const uq = u.unit_assessment && u.unit_assessment.questions ? u.unit_assessment.questions.length : 0;
  page.innerHTML = `
    <a class="back-link" href="#" onclick="return show('home')">&larr; Course Home</a>
    <div class="page-hero">
      <div class="page-hero-icon">📘</div>
      <div>
        <h1>Unit ${{u.number}} · ${{u.name}}</h1>
        <p>${{u.essential_question||''}}</p>
        <span class="hero-badge">Days ${{u.days[0]}}–${{u.days[1]}} · ${{u.lessons.length}} lessons</span>
      </div>
    </div>
    <h2 class="section-h">Overview</h2>
    <div class="card"><p style="font-size:14px;line-height:1.6">${{u.overview||''}}</p></div>
    <h2 class="section-h">Unit vocabulary bank</h2>
    <div class="card-grid">${{vocabHtml}}</div>
    <h2 class="section-h">Lessons</h2>
    <div class="card"><table class="lesson-table"><thead><tr><th>Day</th><th>Title</th><th>Includes</th></tr></thead><tbody>${{rows}}</tbody></table></div>
    ${{uq ? `<h2 class="section-h">${{DATA.assessmentLabel}}</h2><div class="card"><p style="font-size:13px;color:var(--muted)">${{uq}} cumulative questions covering the whole unit — see the student workbook or teacher slide deck for the full assessment.</p></div>` : ''}}
  `;
}}

function renderQuiz(quiz){{
  if(!quiz || !quiz.questions) return '';
  return quiz.questions.map(q => `
    <div class="quiz-q">
      <div class="qtext">${{q.q}}</div>
      ${{q.choices ? `<div class="choices">${{q.choices.map(c=>`<div>${{c}}</div>`).join('')}}</div><div class="ans">Answer: ${{q.answer}}</div>` : `<div class="ans">Sample answer: ${{q.sample_answer||''}}</div>`}}
    </div>`).join('');
}}

function renderLesson(day){{
  const l = findLesson(day);
  const u = findUnit(l.unit);
  const page = document.getElementById('page-lesson');
  const vocabHtml = (l.vocab||[]).map(v=>`<div class="vocab-card"><div class="vword">${{v.word}}</div>${{v.syllables?`<div class="vsyll">${{v.syllables}}</div>`:''}}<div class="vdef">${{v.definition}}</div>${{v.morphology?`<div class="vmorph"><b>Word study:</b> ${{v.morphology}}</div>`:''}}<div class="vex">${{v.example||''}}</div></div>`).join('');
  const miniHtml = (l.mini_lesson||[]).map(s=>`<div class="mini-section"><h4>${{s.heading}}</h4><p>${{s.body}}</p></div>`).join('');
  const objHtml = (l.objectives||[]).map(o=>`<li>${{o}}</li>`).join('');
  const readingHtml = l.reading ? `
    <h2 class="section-h">Reading</h2>
    <div class="reading-box">
      <div class="r-type">${{l.reading.type.replace('_',' ')}}</div>
      <div class="r-title">${{l.reading.title}}</div>
      <div class="r-body">${{l.reading.body}}</div>
      ${{l.reading.questions && l.reading.questions.length ? `<div class="r-questions"><strong>Discussion / comprehension questions:</strong><ul>${{l.reading.questions.map(q=>`<li>${{q}}</li>`).join('')}}</ul></div>` : ''}}
    </div>` : '';
  const appHtml = l.application ? `
    <h2 class="section-h">Apply it: ${{l.application.type.replace(/_/g,' ').replace(/\\b\\w/g, c=>c.toUpperCase())}}</h2>
    <div class="app-box">
      <div class="app-type">${{l.application.type.replace(/_/g,' ')}}</div>
      <div class="app-title">${{l.application.title}}</div>
      <div class="app-scenario">${{l.application.scenario}}</div>
      <div class="app-task"><strong>Task:</strong> ${{l.application.task}}</div>
    </div>` : '';
  const av = l.academic_vocab;
  const academicHtml = av ? `
    <h2 class="section-h">Academic vocabulary word of the day</h2>
    <div class="academic-box">
      <span class="aw-word">${{av.word}}</span><span class="aw-syll">${{av.syllables||''}}</span>
      <div class="aw-def">${{av.definition}}</div>
      ${{av.morphology?`<div class="aw-morph"><strong>Word study:</strong> ${{av.morphology}}</div>`:''}}
      ${{av.example?`<div class="aw-ex">${{av.example}}</div>`:''}}
    </div>` : '';
  const slideHtml = (l.slide_bullets||[]).map(b=>`<div class="slide-chip">${{b}}</div>`).join('');
  page.innerHTML = `
    <a class="back-link" href="#" onclick="return show('unit-${{l.unit}}')">&larr; Unit ${{l.unit}} · ${{u.name}}</a>
    <div class="lesson-title-row"><span class="day-badge">Day ${{l.day}}</span><h1 style="font-size:22px">${{l.title}}</h1></div>
    <div class="pill-row">${{tagsFor(l)}}</div>

    <h2 class="section-h">Objectives</h2>
    <div class="card"><ul class="obj-list">${{objHtml}}</ul></div>

    <h2 class="section-h">Vocabulary</h2>
    <div class="card-grid">${{vocabHtml}}</div>

    ${{academicHtml}}

    <h2 class="section-h">Warm-up</h2>
    <div class="card"><p style="font-size:13.5px">${{l.warm_up||''}}</p></div>

    <h2 class="section-h">Mini-lesson</h2>
    <div class="card">${{miniHtml}}</div>

    <h2 class="section-h">Activity</h2>
    <div class="activity-box"><div class="a-title">${{l.activity ? l.activity.title : ''}}</div><p style="font-size:13.5px">${{l.activity ? l.activity.instructions : ''}}</p></div>

    ${{readingHtml}}

    ${{appHtml}}

    <h2 class="section-h">Quiz</h2>
    <div class="quiz-box">${{renderQuiz(l.quiz)}}</div>

    <h2 class="section-h">Exit ticket</h2>
    <div class="exit-box"><div class="e-label">Exit Ticket · Day ${{l.day}}</div><div class="e-prompt">${{l.exit_ticket ? l.exit_ticket.prompt : ''}}</div></div>

    <h2 class="section-h">Teacher slide bullets</h2>
    <div class="slide-strip">${{slideHtml}}</div>
  `;
}}

function renderPacing(){{
  const page = document.getElementById('page-pacing');
  let rows = '';
  DATA.units.forEach(u => {{
    rows += `<tr style="background:var(--gray)"><td colspan="3" style="font-weight:700;padding:8px 12px">Unit ${{u.number}} · ${{u.name}} (Days ${{u.days[0]}}–${{u.days[1]}})</td></tr>`;
    u.lessons.forEach(l => {{
      rows += `<tr class="clickable" onclick="show('lesson-${{l.day}}')"><td class="lesson-num">Day ${{l.day}}</td><td>${{l.title}}</td><td>${{tagsFor(l)}}</td></tr>`;
    }});
  }});
  page.innerHTML = `
    <div class="page-hero">
      <div class="page-hero-icon">🗓</div>
      <div><h1>Full 82-Day Pacing Guide</h1><p>Click any lesson to open it.</p></div>
    </div>
    <div class="card"><table class="lesson-table"><thead><tr><th>Day</th><th>Lesson</th><th>Includes</th></tr></thead><tbody>${{rows}}</tbody></table></div>
  `;
}}

renderHome();
</script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    return output_path

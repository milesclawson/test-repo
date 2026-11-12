"""Accessible, bilingual, static course site (no client-side rendering of content).

Every page is plain server-rendered HTML so screen readers get the real DOM.
Language toggle only shows/hides pre-rendered English and Spanish text.
"""
import html
import os
import shutil

from content import COURSE, DAY_SHAPE, LAB_SHAPE, ROLES, CERT_OBJECTIVES

UI = {
    "skip": ("Skip to main content", "Saltar al contenido principal"),
    "lang_label": ("Language", "Idioma"),
    "english": ("English", "English"),
    "spanish": ("Español", "Español"),
    "both": ("Both", "Ambos"),
    "units": ("Units", "Unidades"),
    "unit": ("Unit", "Unidad"),
    "downloads": ("Downloads", "Descargas"),
    "day": ("Day", "Día"),
    "lab_day": ("Lab day", "Día de laboratorio"),
    "objectives": ("Learning targets", "Metas de aprendizaje"),
    "vocab": ("Vocabulary", "Vocabulario"),
    "bellringer": ("Bellringer", "Actividad de inicio"),
    "instruction": ("Direct instruction", "Instrucción directa"),
    "guided": ("Guided practice", "Práctica guiada"),
    "independent": ("Independent practice", "Práctica independiente"),
    "lab": ("Lab", "Laboratorio"),
    "exit": ("Exit ticket", "Boleto de salida"),
    "reading": ("Reading", "Lectura"),
    "reading_q": ("Reading check", "Comprueba tu lectura"),
    "recipe": ("Recipe card", "Tarjeta de receta"),
    "serves": ("Serves", "Rinde"),
    "minutes": ("Active time (minutes)", "Tiempo activo (minutos)"),
    "ingredients": ("Ingredients", "Ingredientes"),
    "equipment": ("Equipment", "Equipo"),
    "steps": ("Steps", "Pasos"),
    "checkpoint": ("Safety checkpoint", "Punto de control de seguridad"),
    "allergens": ("Allergy note", "Nota sobre alergias"),
    "cost": ("Estimated cost per group", "Costo estimado por grupo"),
    "qty": ("Amount", "Cantidad"),
    "unit_col": ("Unit", "Medida"),
    "item": ("Ingredient", "Ingrediente"),
    "roles": ("Group jobs", "Tareas del grupo"),
    "role": ("Job", "Tarea"),
    "does": ("What you do", "Qué haces"),
    "day_plan": ("The 48 minutes", "Los 48 minutos"),
    "min": ("Minutes", "Minutos"),
    "segment": ("Segment", "Segmento"),
    "practical": ("Unit practical rubric", "Rúbrica de la práctica de la unidad"),
    "criterion": ("Skill", "Habilidad"),
    "high": ("Strong (8-10)", "Sólido (8-10)"),
    "mid": ("Developing (4-7)", "En desarrollo (4-7)"),
    "low": ("Beginning (0-3)", "Inicial (0-3)"),
    "essential": ("Essential question", "Pregunta esencial"),
    "back": ("Back to top", "Volver arriba"),
    "home": ("Course home", "Inicio del curso"),
    "review_note": ("Spanish text is machine-assisted and awaiting review by a fluent speaker.",
                    "El texto en español fue elaborado con ayuda de traducción automática y está pendiente de revisión por un hablante fluido."),
}

CSS = """
:root{--bg:#ffffff;--text:#1a1a1a;--muted:#4a4a4a;--primary:#1b5e3a;--primary-ink:#ffffff;
--link:#0b4f8a;--panel:#f2f7f3;--border:#6b7f72;--accent-bg:#fff4e0;--accent-ink:#5c3200;--focus:#b35900}
@media (prefers-color-scheme:dark){:root{--bg:#121512;--text:#f2f2f2;--muted:#cfd6d1;--primary:#8fd3a7;
--primary-ink:#0c1f14;--link:#9cc9f5;--panel:#1c241f;--border:#8aa293;--accent-bg:#2c2111;--accent-ink:#ffd9a3;--focus:#ffb454}}
*{box-sizing:border-box}
html{font-size:100%}
body{margin:0;background:var(--bg);color:var(--text);font:1.125rem/1.65 system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
a{color:var(--link);text-decoration:underline}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.skip{position:absolute;left:-999px;top:0;background:var(--primary);color:var(--primary-ink);padding:.75rem 1rem;z-index:10}
.skip:focus{left:0}
header.site{background:var(--primary);color:var(--primary-ink);padding:1rem 1.25rem}
header.site a{color:var(--primary-ink)}
header.site .name{font-size:1.4rem;font-weight:700;margin:0}
.wrap{max-width:62rem;margin:0 auto;padding:0 1.25rem}
.langbar{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin-top:.5rem}
.langbar button{font:inherit;padding:.4rem .9rem;border:2px solid var(--primary-ink);background:transparent;color:var(--primary-ink);border-radius:.4rem;cursor:pointer}
.langbar button[aria-pressed=true]{background:var(--primary-ink);color:var(--primary)}
nav.units ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:.5rem}
nav.units{background:var(--panel);border-bottom:1px solid var(--border);padding:.75rem 0}
nav.units a{display:inline-block;padding:.35rem .75rem;border:1px solid var(--border);border-radius:.4rem}
main{padding:1.5rem 0 3rem}
main,td,th,li,p,h1,h2,h3,h4{overflow-wrap:break-word}
.bi>span,.bi>div{min-width:0}
h1{font-size:2rem;line-height:1.25;margin:.5rem 0 1rem}
h2{font-size:1.6rem;margin:2.5rem 0 .75rem;padding-top:.75rem;border-top:3px solid var(--primary)}
h3{font-size:1.25rem;margin:1.5rem 0 .5rem}
section.lesson{margin-bottom:2rem}
.panel{background:var(--panel);border:1px solid var(--border);border-radius:.5rem;padding:1rem 1.25rem;margin:1rem 0}
.note{background:var(--accent-bg);color:var(--accent-ink);border:2px solid var(--accent-ink);border-radius:.5rem;padding:.75rem 1rem;margin:1rem 0}
table{border-collapse:collapse;width:100%;margin:1rem 0}
caption{text-align:left;font-weight:700;padding:.25rem 0}
th,td{border:1px solid var(--border);padding:.5rem .75rem;text-align:left;vertical-align:top}
th{background:var(--panel)}
body[data-lang=en] [lang=es]{display:none}
body[data-lang=es] [lang=en]{display:none}
.bi>span,.bi>div{display:block}
body[data-lang=both] .bi{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
body[data-lang=both] .bi>[lang=es]{border-left:3px solid var(--border);padding-left:1rem}
body[data-lang=both] table .bi,body[data-lang=both] li .bi,body[data-lang=both] dd .bi,body[data-lang=both] dt .bi,body[data-lang=both] nav .bi,body[data-lang=both] .langbar .bi,body[data-lang=both] h3 .bi{display:block}
body[data-lang=both] table .bi>[lang=es],body[data-lang=both] li .bi>[lang=es],body[data-lang=both] dd .bi>[lang=es],body[data-lang=both] dt .bi>[lang=es],body[data-lang=both] nav .bi>[lang=es],body[data-lang=both] .langbar .bi>[lang=es],body[data-lang=both] h3 .bi>[lang=es]{border-left:0;padding-left:0;border-top:1px dashed var(--border);margin-top:.25rem;padding-top:.25rem}
@media (max-width:48rem){body[data-lang=both] .bi{grid-template-columns:1fr;gap:.25rem}
body[data-lang=both] .bi>[lang=es]{border-left:0;padding-left:0;border-top:1px dashed var(--border);padding-top:.25rem}}
.checkpoint{font-weight:700}
.reviewnote{font-size:.95rem;color:var(--muted)}
footer{border-top:1px solid var(--border);padding:1.5rem 0;color:var(--muted)}
@media print{.skip,.langbar,nav.units,.noprint{display:none}body{font-size:12pt}}
@media (max-width:48rem){th,td{padding:.4rem .45rem;font-size:1rem}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

JS = """
(function(){
  var KEY='wfn-lang', body=document.body, btns=document.querySelectorAll('.langbar button');
  function set(l){
    body.setAttribute('data-lang',l);
    btns.forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-l')===l?'true':'false');});
    document.documentElement.setAttribute('lang', l==='es'?'es':'en');
    try{localStorage.setItem(KEY,l);}catch(e){}
  }
  var start='en';
  try{var m=location.search.match(/lang=(en|es|both)/); if(m){start=m[1];} else {start=localStorage.getItem(KEY)||'en';}}catch(e){}
  btns.forEach(function(b){b.addEventListener('click',function(){set(b.getAttribute('data-l'));});});
  set(start);
})();
"""


def e(s):
    return html.escape(s, quote=True)


def bi(t, tag="span", cls=""):
    """Render a bilingual pair as two language-tagged children."""
    c = f' class="bi {cls}"'.replace(" ", " ") if cls else ' class="bi"'
    return f'<{tag}{c}><span lang="en">{e(t["en"])}</span><span lang="es">{e(t["es"])}</span></{tag}>'


def bih(en_html, es_html, tag="span", cls=""):
    """Bilingual pair whose parts are already-escaped HTML (for labels with <strong>)."""
    c = f' class="bi {cls}"' if cls else ' class="bi"'
    return f'<{tag}{c}><span lang="en">{en_html}</span><span lang="es">{es_html}</span></{tag}>'


def comb(key, t, sep=": ", tag="span", cls=""):
    """Plain-text combination 'Label: text' inside ONE bilingual pair (no nested pairs)."""
    en, es = UI[key]
    return bi({"en": f"{en}{sep}{t['en']}", "es": f"{es}{sep}{t['es']}"}, tag, cls)


def lab(key, t, tag="span", cls=""):
    """Bold label followed by text, inside ONE bilingual pair."""
    en, es = UI[key]
    return bih(f"<strong>{e(en)}:</strong> {e(t['en'])}", f"<strong>{e(es)}:</strong> {e(t['es'])}", tag, cls)


def ui(key, tag="span", cls=""):
    en, es = UI[key]
    return bi({"en": en, "es": es}, tag, cls)


def ui_pair(key):
    en, es = UI[key]
    return {"en": en, "es": es}


def page(title_en, title_es, body, units, active=None):
    nav = "".join(
        f'<li><a href="unit-{u["number"]:02d}.html"{" aria-current=\"page\"" if active == u["number"] else ""}>'
        f'{bi({"en": str(u["number"]) + ". " + u["title"]["en"], "es": str(u["number"]) + ". " + u["title"]["es"]})}</a></li>' for u in units)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title_en)} | {e(COURSE['title']['en'])}</title>
<link rel="stylesheet" href="styles.css">
</head>
<body data-lang="en">
<a class="skip" href="#main">{ui('skip')}</a>
<header class="site">
 <div class="wrap">
  <p class="name"><a href="index.html">{bi(COURSE['title'])}</a></p>
  <div class="langbar" role="group" aria-label="Language / Idioma">
   {bi({"en": UI["lang_label"][0] + ":", "es": UI["lang_label"][1] + ":"})}
   <button type="button" data-l="en" aria-pressed="true">English</button>
   <button type="button" data-l="es" aria-pressed="false">Español</button>
   <button type="button" data-l="both" aria-pressed="false">{ui('both')}</button>
  </div>
 </div>
</header>
<nav class="units" aria-label="{e(UI['units'][0])} / {e(UI['units'][1])}"><div class="wrap"><ul>{nav}</ul></div></nav>
<main id="main" tabindex="-1"><div class="wrap">
{body}
</div></main>
<footer><div class="wrap"><p class="reviewnote">{ui('review_note')}</p>
<p>{e(COURSE['school'])} · {e(COURSE['department'])} · {e(COURSE['teacher'])}</p></div></footer>
<script src="app.js"></script>
</body>
</html>
"""


def _table(caption_key, headers, rows):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "".join("<tr>" + "".join(c for c in r) + "</tr>" for r in rows)
    return f'<table><caption>{ui(caption_key)}</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def _vocab_lookup(unit):
    return {v["term"]["en"]: v for v in unit["vocab_bank"]}


def _lesson_html(unit, les):
    vl = _vocab_lookup(unit)
    is_lab = les["kind"] == "lab"
    shape = LAB_SHAPE if is_lab else DAY_SHAPE
    h = [f'<section class="lesson" aria-labelledby="d{les["day"]}">']
    label = UI["lab_day" if is_lab else "day"]
    h.append(f'<h2 id="d{les["day"]}"><span class="bi"><span lang="en">{label[0]} {les["day"]}: {e(les["title"]["en"])}</span>'
             f'<span lang="es">{label[1]} {les["day"]}: {e(les["title"]["es"])}</span></span></h2>')
    rows = [(f"<td>{m}</td><td>{bi({'en': en, 'es': es})}</td>") for m, en, es in shape]
    h.append(f'<table><caption>{ui("day_plan")}</caption><thead><tr><th scope="col">{ui("min")}</th>'
             f'<th scope="col">{ui("segment")}</th></tr></thead><tbody>' + "".join(f"<tr>{r}</tr>" for r in rows) + "</tbody></table>")
    h.append(f'<h3>{ui("objectives")}</h3><ul>' + "".join(f'<li>{bi(o)}</li>' for o in les["objectives"]) + "</ul>")
    terms = [vl[t] for t in les.get("vocab", []) if t in vl]
    if terms:
        h.append(f'<h3>{ui("vocab")}</h3><dl>' + "".join(
            f'<dt>{bi(v["term"])}</dt><dd>{bi(v["definition"])}</dd>' for v in terms) + "</dl>")
    h.append(f'<h3>{ui("bellringer")}</h3><div class="panel">{bi(les["bellringer"], "p")}</div>')
    h.append(f'<h3>{ui("instruction")}</h3>')
    for blk in les["instruction"]:
        h.append(f'<h4>{bi(blk["heading"])}</h4>{bi(blk["body"], "p")}')
    g = les["guided"]
    h.append(f'<h3>{comb("guided", g["title"])}</h3><ol>' + "".join(f'<li>{bi(s)}</li>' for s in g["steps"]) + "</ol>")
    ind = les["independent"]
    h.append(f'<h3>{comb("lab" if ind["kind"] == "lab" else "independent", ind["title"])}</h3><ol>'
             + "".join(f'<li>{bi(s)}</li>' for s in ind["steps"]) + "</ol>")
    if ind.get("recipe"):
        h.append(f'<p><a href="#recipe-{e(ind["recipe"])}">{ui("recipe")}</a></p>')
    h.append(f'<h3>{ui("exit")}</h3><ol>' + "".join(f'<li>{bi(x["q"])}</li>' for x in les["exit"]) + "</ol>")
    h.append("</section>")
    return "\n".join(h)


def _recipe_html(key, r):
    h = [f'<section class="recipe" id="recipe-{key}" aria-labelledby="r-{key}">',
         f'<h2 id="r-{key}">{comb("recipe", r["title"])}</h2>',
         bih(f'<strong>{e(UI["serves"][0])}:</strong> {r["serves"]} · <strong>{e(UI["minutes"][0])}:</strong> {r["active_minutes"]}',
             f'<strong>{e(UI["serves"][1])}:</strong> {r["serves"]} · <strong>{e(UI["minutes"][1])}:</strong> {r["active_minutes"]}', "p"),
         f'<div class="note" role="note">{lab("allergens", r["allergens"], "p")}</div>']
    if r.get("scale_note"):
        h.append(bi(r["scale_note"], "p"))
    rows = [(f'<td>{i["qty"]}</td><td>{bi(i["unit"])}</td><td>{bi(i["item"])}</td>') for i in r["ingredients"]]
    h.append(f'<table><caption>{ui("ingredients")}</caption><thead><tr><th scope="col">{ui("qty")}</th><th scope="col">{ui("unit_col")}</th>'
             f'<th scope="col">{ui("item")}</th></tr></thead><tbody>' + "".join(f"<tr>{x}</tr>" for x in rows) + "</tbody></table>")
    h.append(f'<h3>{ui("equipment")}</h3><ul>' + "".join(f"<li>{bi(x)}</li>" for x in r["equipment"]) + "</ul>")
    h.append(f'<h3>{ui("steps")}</h3><ol>')
    for s in r["steps"]:
        cp = lab("checkpoint", s["checkpoint"], "p", "checkpoint") if s["checkpoint"] else ""
        h.append(f'<li>{bi(s["text"], "div")}{cp}</li>')
    h.append("</ol>")
    h.append(bih(f'<strong>{e(UI["cost"][0])}:</strong> {e(r["cost_per_group"])}', f'<strong>{e(UI["cost"][1])}:</strong> {e(r["cost_per_group"])}', "p") + "</section>")
    return "\n".join(h)


def unit_page(unit, units):
    b = [f'<h1>{bi({"en": UI["unit"][0] + " " + str(unit["number"]) + ": " + unit["title"]["en"], "es": UI["unit"][1] + " " + str(unit["number"]) + ": " + unit["title"]["es"]})}</h1>',
         lab("essential", unit["essential_question"], "p"),
         bi(unit["overview"], "p")]
    # group jobs
    rows = [(f'<td>{bi(r["role"])}</td><td>{bi(r["job"])}</td>') for r in ROLES]
    b.append(f'<table><caption>{ui("roles")}</caption><thead><tr><th scope="col">{ui("role")}</th><th scope="col">{ui("does")}</th></tr></thead><tbody>'
             + "".join(f"<tr>{x}</tr>" for x in rows) + "</tbody></table>")
    # vocab bank
    b.append(f'<h2>{ui("vocab")}</h2><dl>' + "".join(
        f'<dt>{bi(v["term"])}</dt><dd>{bi(v["definition"])}</dd>' for v in unit["vocab_bank"]) + "</dl>")
    # reading
    rd = unit["reading"]
    b.append(f'<h2>{comb("reading", rd["title"])}</h2>' + "".join(bi(p, "p") for p in rd["body"]))
    b.append(f'<h3>{ui("reading_q")}</h3><ol>' + "".join(f'<li>{bi(q["q"])}</li>' for q in rd["questions"]) + "</ol>")
    for les in unit["lessons"]:
        b.append(_lesson_html(unit, les))
    for k, r in unit["recipes"].items():
        b.append(_recipe_html(k, r))
    p = unit["practical"]
    rows = [(f'<td>{bi(c["name"])}</td><td>{bi(c["high"])}</td><td>{bi(c["mid"])}</td><td>{bi(c["low"])}</td>') for c in p["criteria"]]
    b.append(f'<h2>{bi(p["title"])}</h2><table><caption>{ui("practical")}</caption><thead><tr><th scope="col">{ui("criterion")}</th>'
             f'<th scope="col">{ui("high")}</th><th scope="col">{ui("mid")}</th><th scope="col">{ui("low")}</th></tr></thead><tbody>'
             + "".join(f"<tr>{x}</tr>" for x in rows) + "</tbody></table>")
    b.append(f'<p class="noprint"><a href="#main">{ui("back")}</a></p>')
    return page(unit["title"]["en"], unit["title"]["es"], "\n".join(b), units, active=unit["number"])


def index_page(units, downloads):
    b = [f'<h1>{bi(COURSE["title"])}</h1>',
         f'<p>{e(COURSE["department"])} · {e(COURSE["school"])} · {e(COURSE["length"])}</p>',
         bi({"en": "Learn where food comes from, what it does for your body, and how to prepare it safely in our kitchen. "
                   "This course prepares you for the YouScience Nutrition and Wellness certification exam.",
             "es": "Aprende de dónde viene la comida, qué hace por tu cuerpo y cómo prepararla de forma segura en nuestra cocina. "
                   "Este curso te prepara para el examen de certificación Nutrition and Wellness de YouScience."}, "p"),
         f'<h2>{ui("units")}</h2><ol>' + "".join(
             f'<li><a href="unit-{u["number"]:02d}.html">{bi(u["title"])}</a></li>' for u in units) + "</ol>"]
    if downloads:
        b.append(f'<h2>{ui("downloads")}</h2><ul>' + "".join(
            f'<li><a href="{e(d["href"])}">{e(d["label"])}</a></li>' for d in downloads) + "</ul>")
    return page(COURSE["title"]["en"], COURSE["title"]["es"], "\n".join(b), units)


def build_site(units, out_dir, downloads=()):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "styles.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(out_dir, "app.js"), "w", encoding="utf-8") as f:
        f.write(JS)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page(units, downloads))
    for u in units:
        with open(os.path.join(out_dir, f"unit-{u['number']:02d}.html"), "w", encoding="utf-8") as f:
            f.write(unit_page(u, units))

"""Quia question-bank import files (plain UTF-8 text) plus a CSV blueprint.

Format follows Quia's published text-file import rules: type code on its own line, then the question,
then choices with * marking the correct one, optional 'Name: value' settings, blank line between questions.
Test with one question first: Quia's tip is to export an existing question and compare.
"""
import csv
import os


def _q(q, lang):
    lines = ["mc", q["q"][lang].replace("\n", " ")]
    for i, c in enumerate(q["choices"]):
        lines.append(("*" if i == q["answer"] else "") + c[lang].replace("\n", " "))
    lines.append("Points: 1")
    return "\n".join(lines)


def build_quia(unit, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    n = f"unit{unit['number']:02d}"
    for lang in ("en", "es"):
        with open(os.path.join(out_dir, f"{n}_quia_questions_{lang}.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n\n".join(_q(q, lang) for q in unit["quiz"]) + "\n")
    with open(os.path.join(out_dir, f"{n}_quiz_blueprint.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Question", "Cert objective", "Correct answer (EN)", "Question (EN)"])
        for i, q in enumerate(unit["quiz"], 1):
            w.writerow([i, q["cert"], q["choices"][q["answer"]]["en"], q["q"]["en"]])

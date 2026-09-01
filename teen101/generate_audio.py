"""
Teenager 101 -- Audio Generator
Produces M4A audio files for stories and informational readings (English + Spanish).
Output: output/audio/story_EN_1.1.m4a, output/audio/reading_EN_1.1.m4a, etc.

Voices used:
  English: Samantha (natural US English, best quality on macOS)
  Spanish: Paulina  (Mexican Spanish -- es_MX, most natural for US students)

Run from inside the teen101/ directory: python3 generate_audio.py
"""

import os
import re
import subprocess
import tempfile

from stories import STORIES
from stories_es import STORIES_ES
from readings import READINGS
from readings_es import READINGS_ES

OUTPUT_DIR = "output/audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

EN_VOICE = "Samantha"
ES_VOICE = "Paulina"
RATE = 175  # words per minute (default ~200; 175 is slightly slower, better for comprehension)


def strip_html(text: str) -> str:
    """Remove <i> tags but keep the text -- say command doesn't need them."""
    return re.sub(r"<[^>]+>", "", text)


def story_to_script(s: dict, label: str, lang: str = "EN") -> str:
    title = s["title"]
    chars = s.get("characters", [])
    body = strip_html(s["story"].strip())
    questions = s["questions"]

    if lang == "EN":
        intro = (
            f"Teenager 101. Lesson {label}. Discussion Story.\n\n"
            f'"{title}"\n\n'
            f"Characters: {', '.join(chars)}.\n\n"
        )
        q_header = "\n\nDiscussion Questions.\n\n"
        q_prefix = lambda i: f"Question {i}. "
    else:
        intro = (
            f"Teenager 101. Lección {label}. Historia de Discusión.\n\n"
            f'"{title}"\n\n'
            f"Personajes: {', '.join(chars)}.\n\n"
        )
        q_header = "\n\nPreguntas de Discusión.\n\n"
        q_prefix = lambda i: f"Pregunta {i}. "

    script = intro + body + q_header
    for i, q in enumerate(questions, 1):
        script += q_prefix(i) + q + "\n\n"

    return script


def reading_to_script(r: dict, label: str, lang: str = "EN") -> str:
    title = r["title"]
    source = r["source"]
    paragraphs = r["text"]
    questions = r["questions"]

    if lang == "EN":
        intro = (
            f"Teenager 101. Lesson {label}. Informational Reading.\n\n"
            f'"{title}"\n\n'
            f"Source: {source}.\n\n"
        )
        q_header = "\n\nComprehension Questions.\n\n"
        q_prefix = lambda i: f"Question {i}. "
    else:
        intro = (
            f"Teenager 101. Lección {label}. Lectura Informativa.\n\n"
            f'"{title}"\n\n'
            f"Fuente: {source}.\n\n"
        )
        q_header = "\n\nPreguntas de Comprensión.\n\n"
        q_prefix = lambda i: f"Pregunta {i}. "

    script = intro + "\n\n".join(paragraphs) + q_header
    for i, q in enumerate(questions, 1):
        script += q_prefix(i) + q + "\n\n"

    return script


def _speak_to_m4a(script: str, out_path: str, voice: str) -> str:
    aiff_path = out_path.replace(".m4a", ".aiff")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                      delete=False, encoding="utf-8") as f:
        f.write(script)
        script_path = f.name

    say_cmd = ["say", "--voice", voice, "--rate", str(RATE),
               "-o", aiff_path, "-f", script_path]
    result = subprocess.run(say_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] say failed for {out_path}: {result.stderr}")
        os.unlink(script_path)
        return ""

    convert_cmd = ["afconvert", aiff_path, "-o", out_path,
                   "-f", "m4af", "-d", "aac"]
    result = subprocess.run(convert_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] afconvert failed for {out_path}: {result.stderr}")
        out_path = ""
    else:
        os.remove(aiff_path)
        size_kb = os.path.getsize(out_path) // 1024
        print(f"  [ok]   {out_path}  ({size_kb} KB)")

    os.unlink(script_path)
    return out_path


def generate_audio(label: str, s: dict, voice: str, lang: str) -> str:
    out_path = os.path.join(OUTPUT_DIR, f"story_{lang}_{label}.m4a")
    if os.path.exists(out_path):
        print(f"  [skip] {out_path} already exists")
        return out_path
    return _speak_to_m4a(story_to_script(s, label, lang), out_path, voice)


def generate_reading_audio(label: str, r: dict, voice: str, lang: str) -> str:
    out_path = os.path.join(OUTPUT_DIR, f"reading_{lang}_{label}.m4a")
    if os.path.exists(out_path):
        print(f"  [skip] {out_path} already exists")
        return out_path
    return _speak_to_m4a(reading_to_script(r, label, lang), out_path, voice)


def build():
    labels = sorted(STORIES.keys())

    story_total = len(labels) * 2
    print(f"\nGenerating {story_total} story audio files ({len(labels)} lessons x 2 languages)...\n")
    for label in labels:
        en_story = STORIES.get(label)
        es_story = STORIES_ES.get(label)
        if en_story:
            print(f"Story {label} -- English")
            generate_audio(label, en_story, EN_VOICE, "EN")
        if es_story:
            print(f"Story {label} -- Spanish")
            generate_audio(label, es_story, ES_VOICE, "ES")

    r_labels = sorted(READINGS.keys())
    read_total = len(r_labels) * 2
    print(f"\nGenerating {read_total} reading audio files ({len(r_labels)} lessons x 2 languages)...\n")
    for label in r_labels:
        en_reading = READINGS.get(label)
        es_reading = READINGS_ES.get(label)
        if en_reading:
            print(f"Reading {label} -- English")
            generate_reading_audio(label, en_reading, EN_VOICE, "EN")
        if es_reading:
            print(f"Reading {label} -- Spanish")
            generate_reading_audio(label, es_reading, ES_VOICE, "ES")

    sizes = [
        os.path.getsize(os.path.join(OUTPUT_DIR, f))
        for f in os.listdir(OUTPUT_DIR)
        if f.endswith(".m4a")
    ]
    print(f"\nDone. {len(sizes)} audio files in {OUTPUT_DIR}/")
    if sizes:
        total_mb = sum(sizes) / (1024 * 1024)
        print(f"Total audio: {total_mb:.1f} MB")


if __name__ == "__main__":
    build()

"""
Warrior Prep — Audio Generator
Produces M4A audio files for all stories and informational readings (English + Spanish).
Output: output/audio/story_EN_1.1.m4a, output/audio/reading_EN_1.1.m4a, etc.

Voices used:
  English: Samantha (natural US English, best quality on macOS)
  Spanish: Paulina  (Mexican Spanish — es_MX, most natural for US students)
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
RATE     = 175    # words per minute (default ~200; 175 is slightly slower, better for comprehension)


def strip_html(text: str) -> str:
    """Remove <i> tags but keep the text — say command doesn't need them."""
    return re.sub(r"<[^>]+>", "", text)


def story_to_script(s: dict, label: str, lang: str = "EN") -> str:
    """Build the full narration script for a story."""
    title     = s["title"]
    chars     = s.get("characters", [])
    body      = strip_html(s["story"].strip())
    questions = s["questions"]

    if lang == "EN":
        intro = (
            f"Warrior Prep. Lesson {label}. Discussion Story.\n\n"
            f'"{title}"\n\n'
            f"Characters: {', '.join(chars)}.\n\n"
        )
        q_header = "\n\nDiscussion Questions.\n\n"
        q_prefix = lambda i: f"Question {i}. "
        pause_between = "\n\n"
    else:
        intro = (
            f"Warrior Prep. Lección {label}. Historia de Discusión.\n\n"
            f'"{title}"\n\n'
            f"Personajes: {', '.join(chars)}.\n\n"
        )
        q_header = "\n\nPreguntas de Discusión.\n\n"
        q_prefix = lambda i: f"Pregunta {i}. "
        pause_between = "\n\n"

    script = intro + body + q_header
    for i, q in enumerate(questions, 1):
        script += q_prefix(i) + q + pause_between

    return script


def generate_audio(label: str, s: dict, voice: str, lang: str) -> str:
    """
    Generate M4A audio for one story.
    Returns the output file path.
    """
    out_path = os.path.join(OUTPUT_DIR, f"story_{lang}_{label}.m4a")

    aiff_path = out_path.replace(".m4a", ".aiff")
    if os.path.exists(out_path):
        print(f"  [skip] {out_path} already exists")
        return out_path

    script = story_to_script(s, label, lang)

    # Write script to a temp file (avoids shell quoting issues with long text)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                     delete=False, encoding="utf-8") as f:
        f.write(script)
        script_path = f.name

    # Step 1: say → AIFF
    say_cmd = [
        "say",
        "--voice", voice,
        "--rate",  str(RATE),
        "-o", aiff_path,
        "-f", script_path,
    ]
    result = subprocess.run(say_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] say failed for {label} {lang}: {result.stderr}")
        os.unlink(script_path)
        return ""

    # Step 2: AIFF → M4A (AAC, 96 kbps — good quality, small file)
    convert_cmd = [
        "afconvert",
        aiff_path,
        "-o", out_path,
        "-f", "m4af",
        "-d", "aac",
    ]
    result = subprocess.run(convert_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] afconvert failed for {label} {lang}: {result.stderr}")
    else:
        os.remove(aiff_path)   # clean up AIFF
        size_kb = os.path.getsize(out_path) // 1024
        print(f"  [ok]   {out_path}  ({size_kb} KB)")

    os.unlink(script_path)
    return out_path


def reading_to_script(r: dict, label: str, lang: str = "EN") -> str:
    """Build the full narration script for an informational reading."""
    title     = r["title"]
    source    = r["source"]
    paragraphs = r["text"]
    questions  = r["questions"]

    if lang == "EN":
        intro     = (
            f"Warrior Prep. Lesson {label}. Informational Reading.\n\n"
            f'"{title}"\n\n'
            f"Source: {source}.\n\n"
        )
        q_header  = "\n\nComprehension Questions.\n\n"
        q_prefix  = lambda i: f"Question {i}. "
    else:
        intro     = (
            f"Warrior Prep. Lección {label}. Lectura Informativa.\n\n"
            f'"{title}"\n\n'
            f"Fuente: {source}.\n\n"
        )
        q_header  = "\n\nPreguntas de Comprensión.\n\n"
        q_prefix  = lambda i: f"Pregunta {i}. "

    script = intro + "\n\n".join(paragraphs) + q_header
    for i, q in enumerate(questions, 1):
        script += q_prefix(i) + q + "\n\n"

    return script


def generate_reading_audio(label: str, r: dict, voice: str, lang: str) -> str:
    """Generate M4A audio for one informational reading. Returns output path."""
    out_path  = os.path.join(OUTPUT_DIR, f"reading_{lang}_{label}.m4a")
    aiff_path = out_path.replace(".m4a", ".aiff")

    if os.path.exists(out_path):
        print(f"  [skip] {out_path} already exists")
        return out_path

    script = reading_to_script(r, label, lang)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                     delete=False, encoding="utf-8") as f:
        f.write(script)
        script_path = f.name

    say_cmd = ["say", "--voice", voice, "--rate", str(RATE),
                "-o", aiff_path, "-f", script_path]
    result = subprocess.run(say_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] say failed for reading {label} {lang}: {result.stderr}")
        os.unlink(script_path)
        return ""

    convert_cmd = ["afconvert", aiff_path, "-o", out_path,
                   "-f", "m4af", "-d", "aac", "-b", "96000"]
    result = subprocess.run(convert_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] afconvert failed for reading {label} {lang}: {result.stderr}")
    else:
        os.remove(aiff_path)
        size_kb = os.path.getsize(out_path) // 1024
        print(f"  [ok]   {out_path}  ({size_kb} KB)")

    os.unlink(script_path)
    return out_path


def build():
    labels = sorted(STORIES.keys())

    # ── Stories ──────────────────────────────────────────────────────────
    story_total = len(labels) * 2
    story_done  = 0
    print(f"\nGenerating {story_total} story audio files ({len(labels)} lessons × 2 languages)...\n")

    for label in labels:
        en_story = STORIES.get(label)
        es_story = STORIES_ES.get(label)

        if en_story:
            print(f"Story {label} — English")
            generate_audio(label, en_story, EN_VOICE, "EN")
            story_done += 1

        if es_story:
            print(f"Story {label} — Spanish")
            generate_audio(label, es_story, ES_VOICE, "ES")
            story_done += 1

    # ── Readings ─────────────────────────────────────────────────────────
    r_labels = sorted(READINGS.keys())
    read_total = len(r_labels) * 2
    read_done  = 0
    print(f"\nGenerating {read_total} reading audio files ({len(r_labels)} lessons × 2 languages)...\n")

    for label in r_labels:
        en_reading = READINGS.get(label)
        es_reading = READINGS_ES.get(label)

        if en_reading:
            print(f"Reading {label} — English")
            generate_reading_audio(label, en_reading, EN_VOICE, "EN")
            read_done += 1

        if es_reading:
            print(f"Reading {label} — Spanish")
            generate_reading_audio(label, es_reading, ES_VOICE, "ES")
            read_done += 1

    total_done = story_done + read_done
    grand_total = story_total + read_total
    print(f"\nDone. {total_done}/{grand_total} audio files written to {OUTPUT_DIR}/")
    sizes = [
        os.path.getsize(os.path.join(OUTPUT_DIR, f))
        for f in os.listdir(OUTPUT_DIR)
        if f.endswith(".m4a")
    ]
    if sizes:
        total_mb = sum(sizes) / (1024 * 1024)
        print(f"Total audio: {total_mb:.1f} MB")


if __name__ == "__main__":
    build()

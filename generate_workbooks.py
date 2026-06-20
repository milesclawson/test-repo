#!/usr/bin/env python3
"""
Generate MN High School Government Workbooks using the Claude API.

Usage:
    python3 generate_workbooks.py              # generate all 6 units
    python3 generate_workbooks.py --unit 1     # generate only unit 1
"""

import argparse
import sys
from pathlib import Path

import anthropic

from standards import UNITS
from prompts import (
    SYSTEM_PROMPT,
    reading_passage_prompt,
    vocabulary_prompt,
    cloze_prompt,
    multiple_choice_prompt,
    matching_prompt,
    discussion_questions_prompt,
    answer_key_prompt,
)
from pdf_builder import build_pdf

OUTPUT_DIR = Path("output")


def call_claude(client: anthropic.Anthropic, user_prompt: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text


def generate_unit(client: anthropic.Anthropic, unit: dict) -> Path:
    num   = unit["number"]
    title = unit["title"]
    print(f"\n[Unit {num}] {title}")

    print("  → Reading passage...")
    passage = call_claude(client, reading_passage_prompt(unit))

    print("  → Vocabulary & morphology...")
    vocabulary = call_claude(client, vocabulary_prompt(unit, passage))

    print("  → CLOZE activity...")
    cloze = call_claude(client, cloze_prompt(unit, passage))

    print("  → Multiple choice questions...")
    mc = call_claude(client, multiple_choice_prompt(unit))

    print("  → Matching activity...")
    matching = call_claude(client, matching_prompt(unit))

    print("  → Short answer questions...")
    discussion = call_claude(client, discussion_questions_prompt(unit))

    print("  → Answer key...")
    answer_key = call_claude(client, answer_key_prompt(unit, cloze, mc, matching))

    print("  → Building PDF...")
    out_path = build_pdf(
        unit=unit,
        sections={
            "passage":              passage,
            "vocabulary":           vocabulary,
            "cloze":                cloze,
            "multiple_choice":      mc,
            "matching":             matching,
            "discussion_questions": discussion,
            "answer_key":           answer_key,
        },
        output_dir=OUTPUT_DIR,
    )

    print(f"  ✓ Saved: {out_path}")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Generate MN Government workbook PDFs")
    parser.add_argument(
        "--unit",
        type=int,
        choices=[u["number"] for u in UNITS],
        help="Generate only this unit number (1–6). Omit to generate all.",
    )
    args = parser.parse_args()

    client = anthropic.Anthropic()
    units_to_run = [u for u in UNITS if args.unit is None or u["number"] == args.unit]

    print(f"Generating {len(units_to_run)} workbook(s)...")

    generated = []
    for unit in units_to_run:
        try:
            path = generate_unit(client, unit)
            generated.append(path)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"  ERROR on unit {unit['number']}: {e}", file=sys.stderr)

    print(f"\nDone. {len(generated)} PDF(s) written to ./{OUTPUT_DIR}/")
    for p in generated:
        print(f"  {p}")


if __name__ == "__main__":
    main()

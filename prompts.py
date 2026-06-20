"""Prompt templates for each workbook section."""

SYSTEM_PROMPT = """You are an experienced high school social studies curriculum writer specializing in civics and government. You write clear, simple, engaging content for high school students who may struggle with reading.

Rules for ALL content you write:
- Write at a 6th grade reading level (short sentences, common words, clear explanations).
- Every workbook must be fully self-contained. Students need NOTHING except the workbook — no textbook, no internet.
- Define every important term the first time it appears. Use plain language.
- Do not reference external resources, page numbers, or other materials.
- Return only the requested content — no preamble, no "here is your..." framing."""


def reading_passage_prompt(unit: dict) -> str:
    topics = "\n".join(f"- {t}" for t in unit["key_topics"])
    return f"""Write a self-contained informational reading passage for a high school civics workbook.

Unit: {unit['title']}
MN Standard: {unit['standard_code']}
Description: {unit['description']}

Key topics to cover:
{topics}

Requirements:
- Length: approximately 500 words
- Use 3-4 short subheadings (use ## before each heading)
- Write at a 6th grade reading level: short sentences (under 20 words each), everyday vocabulary
- Bold each key vocabulary term the FIRST time it appears (use **term**), then immediately define it in plain language in the same or next sentence
- Use concrete, relatable examples — things a high school student would recognize
- End with a one-sentence summary labeled "Big Idea:"

Return only the passage text. No title."""


def vocabulary_prompt(unit: dict, passage: str) -> str:
    return f"""From the reading passage below, identify the 6 most important vocabulary terms.

Unit: {unit['title']}
Passage:
{passage}

For each term, provide ALL of the following:
1. The term (bold it)
2. A simple definition (6th grade level, 1-2 sentences)
3. Morphology breakdown: identify the root word, any prefix, and any suffix. Explain what each part means and how that helps you understand the word. Example: "Democracy: demo (Greek: people) + cracy (Greek: rule/power) = rule by the people"
4. Use it in a sentence from everyday life

Format each entry exactly like this:
TERM: [word]
DEFINITION: [plain-language definition]
MORPHOLOGY: [prefix if any] + [root] + [suffix if any] — [explanation of how the parts make the meaning]
EXAMPLE SENTENCE: [sentence]
---"""


def cloze_prompt(unit: dict, passage: str) -> str:
    return f"""Create a CLOZE activity based on the reading passage below.

Unit: {unit['title']}
Passage:
{passage}

A CLOZE activity is a passage with key words removed. Students fill in the blanks.

Requirements:
- Rewrite a shorter version of the passage (about 150-200 words), removing 10-12 key content words
- Replace each removed word with a blank line like this: _____________
- The missing words should be important content words (nouns, verbs, key terms) — not small connecting words
- At the end, provide a WORD BANK with all the missing words listed in random order (label it "Word Bank:")
- The activity should test comprehension, not trick students

Return the CLOZE passage with blanks, then the Word Bank. Nothing else."""


def multiple_choice_prompt(unit: dict) -> str:
    return f"""Write 6 multiple choice questions for a high school civics workbook.

Unit: {unit['title']}
MN Standard: {unit['standard_code']}
Description: {unit['description']}

Requirements:
- Questions 1-4: Level 1 COMPREHENSION questions (recall, identify, define) — straightforward, directly from the content
- Questions 5-6: Level 2 APPLICATION questions (use the knowledge in a new situation)
- Each question has exactly 4 answer choices labeled A, B, C, D
- Only ONE answer is clearly correct
- Wrong answers (distractors) should be plausible but clearly wrong if you read carefully
- Write at a 6th grade reading level
- At the end, list the answer key as: Answer Key: 1-X, 2-X, 3-X, 4-X, 5-X, 6-X

Format each question:
[number]. [question text]
A. [choice]
B. [choice]
C. [choice]
D. [choice]
"""


def matching_prompt(unit: dict) -> str:
    return f"""Create a matching activity for a high school civics workbook.

Unit: {unit['title']}
MN Standard: {unit['standard_code']}
Description: {unit['description']}

Requirements:
- Create 8 matching pairs
- Column A (left): key terms or concepts from this unit
- Column B (right): definitions or descriptions — written in simple, plain language
- Mix up the order in Column B so it doesn't match Column A directly
- At the end, list the answer key as: Answer Key: 1-X, 2-X, etc.

Format:
COLUMN A (Terms) | COLUMN B (Definitions)
1. [term] | A. [definition]
2. [term] | B. [definition]
...

Answer Key: 1-X, 2-X, ..."""


def discussion_questions_prompt(unit: dict) -> str:
    return f"""Write 4 short-answer questions for a high school civics workbook.

Unit: {unit['title']}
MN Standard: {unit['standard_code']}
Description: {unit['description']}

Requirements:
- Questions 1-2: Level 1 COMPREHENSION — students recall or explain something directly from the content
- Question 3: Ask students to give a real-life example of a concept from the unit
- Question 4: Ask students to share their own opinion or connection to the topic
- Write questions at a 6th grade reading level
- Each question should be answerable in 2-4 sentences

Number the questions 1-4. Return only the questions, no answers."""


def answer_key_prompt(unit: dict, cloze: str, mc: str, matching: str) -> str:
    return f"""Create a complete TEACHER ANSWER KEY for the following activities.

Unit: {unit['title']}

--- CLOZE ACTIVITY ---
{cloze}

--- MULTIPLE CHOICE ---
{mc}

--- MATCHING ---
{matching}

Requirements:
- Label each section clearly (CLOZE ANSWERS, MULTIPLE CHOICE ANSWERS, MATCHING ANSWERS)
- For CLOZE: list the correct word for each blank in order
- For Multiple Choice and Matching: the answer keys are already embedded above — just reformat them cleanly
- Be brief and clear

Start with: ANSWER KEY — TEACHER COPY ONLY"""

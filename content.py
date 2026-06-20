"""
Warrior Prep — all course content as structured data.
Used by pdf_builder.py, docx_builder.py, and pptx_builder.py
"""

SCHOOL_NAME = "ISD 197 – Two Rivers High School"
COURSE_TITLE = "Warrior Prep"
GRADE = "Grade 8"
WARRIOR_RED = (0.78, 0.08, 0.08)   # #C71414
WARRIOR_DARK = (0.13, 0.13, 0.13)  # #212121
WARRIOR_GOLD = (0.96, 0.88, 0.70)  # #F5E0B2  (light gold tint for note paper)
WHITE = (1, 1, 1)

# ---------------------------------------------------------------------------
# PLANNER
# ---------------------------------------------------------------------------
PLANNER_COURSES = ["", "", "", "", "", ""]   # 6 blank course slots

# ---------------------------------------------------------------------------
# UNITS
# ---------------------------------------------------------------------------
# Each unit has:
#   name, overview, vocabulary (list of {word, etymology, definition}),
#   pretest (list of question strings), posttest_prompt,
#   lessons (list of lesson dicts)
#
# Each lesson has:
#   title, objectives (list), vocab_focus ({word, etymology, definition}),
#   scaffolding level (1=heavy … 4=independent),
#   cornell_questions (pre-printed left-column prompts),
#   prefilled_notes (text or "" — only for scaffolding levels 1-2),
#   content_sections (list of {heading, body, activity}),
#   exit_ticket (dict with type and prompts)

UNITS = [
    # ===================================================================
    # UNIT 1 – EXECUTIVE FUNCTIONING
    # ===================================================================
    {
        "number": 1,
        "name": "Executive Functioning",
        "color": (0.78, 0.08, 0.08),   # Warrior red
        "overview": (
            "In this unit you will explore what executive functioning means, why it matters "
            "for school and life, and how high-performing students develop the habits and "
            "strategies that help them stay organized, focused, and in control of their learning."
        ),
        "unit_vocabulary": [
            {
                "word": "Executive Functioning",
                "etymology": "Latin executivus (to carry out) + Latin functio (performance)",
                "definition": "The mental skills — including working memory, flexible thinking, and self-control — that help you manage yourself and your work."
            },
            {
                "word": "Metacognition",
                "etymology": "Greek meta (beyond/about) + Latin cognitio (knowledge, understanding)",
                "definition": "Thinking about your own thinking; being aware of how you learn and monitoring your understanding."
            },
            {
                "word": "Self-Regulation",
                "etymology": "Latin se (oneself) + Latin regulare (to control, to rule)",
                "definition": "The ability to manage your emotions, impulses, and behavior in order to reach a goal."
            },
            {
                "word": "Prioritize",
                "etymology": "Latin prior (first, more important) + -ize (to make/do)",
                "definition": "To decide which tasks are most important and should be done first."
            },
        ],
        "pretest": [
            "In your own words, what do you think 'executive functioning' means?",
            "Describe TWO strategies you currently use to stay organized at school.",
            "When you have three assignments due on the same day, how do you decide what to do first?",
            "What do you do when you feel distracted or overwhelmed with schoolwork?",
            "On a scale of 1–5, rate your current organizational skills. Explain your rating.",
        ],
        "posttest_prompt": (
            "Revisit the five questions from your pre-test. Answer each question again — "
            "you may use more detail and vocabulary from this unit. Then write 3–5 sentences "
            "describing the most important change you plan to make in how you manage your learning."
        ),
        "lessons": [
            # ----------------------------------------------------------
            # LESSON 1-1
            # ----------------------------------------------------------
            {
                "number": 1,
                "title": "What Is Executive Functioning?",
                "lesson_label": "1.1",
                "scaffolding": 1,
                "objectives": [
                    "Define executive functioning and name at least four EF skills.",
                    "Explain why EF skills matter for school success.",
                    "Identify your current strengths and growth areas using an EF self-assessment.",
                ],
                "vocab_focus": {
                    "word": "Executive Functioning",
                    "etymology": "Latin executivus (to carry out) + Latin functio (performance)",
                    "definition": "The mental skills that help you manage yourself, your tasks, and your goals — like the 'CEO' of your brain."
                },
                "cornell_questions": [
                    "What are EF skills?",
                    "Why does EF matter in school?",
                    "Which EF skill is hardest for me?",
                    "What part of the brain controls EF?",
                ],
                "prefilled_notes": (
                    "Executive Functioning (EF) = mental skills that help us PLAN, FOCUS, REMEMBER, and MANAGE behavior.\n\n"
                    "Key EF Skills:\n"
                    "  • Working Memory — holding info in your mind while using it\n"
                    "  • Cognitive Flexibility — shifting between tasks or ideas\n"
                    "  • Inhibitory Control — stopping impulses; staying on task\n"
                    "  • Planning & Organization — breaking tasks into steps\n"
                    "  • Time Management — estimating & using time well\n"
                    "  • Emotional Regulation — managing frustration, stress\n\n"
                    "Location in the brain: PREFRONTAL CORTEX (front of brain)\n"
                    "  — still developing until age 25!\n\n"
                    "High-performing students USE these skills intentionally — they are LEARNABLE."
                ),
                "content_sections": [
                    {
                        "heading": "The CEO of Your Brain",
                        "body": (
                            "Imagine your brain is a company. The prefrontal cortex is the CEO — it makes "
                            "decisions, manages time, and keeps everyone on track. Executive functioning is "
                            "the collection of skills that CEO uses every single day. The great news: these "
                            "skills are not fixed. They grow with practice, just like a muscle."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "EF Self-Assessment",
                        "body": "Rate yourself honestly on each skill below (1 = I struggle here, 5 = I've got this).",
                        "activity": {
                            "type": "rating_table",
                            "rows": [
                                "I remember to bring the right materials to class.",
                                "I start assignments without being reminded.",
                                "I break big projects into smaller steps.",
                                "I can shift focus when plans change.",
                                "I manage my frustration when school gets hard.",
                                "I estimate how long tasks will take.",
                                "I keep my backpack and binder organized.",
                                "I ask for help when I am confused.",
                            ],
                            "columns": ["1", "2", "3", "4", "5"],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "quick_write",
                    "prompt": "Choose ONE executive functioning skill from today's lesson. Explain what it means and describe a real situation — from school, sports, or daily life — where that skill helped you (or where it could have helped you).",
                    "lines": 4,
                },
            },
            # ----------------------------------------------------------
            # LESSON 1-2
            # ----------------------------------------------------------
            {
                "number": 2,
                "title": "Organization & Planning",
                "lesson_label": "1.2",
                "scaffolding": 1,
                "objectives": [
                    "Explain the difference between being organized and being organized *for learning*.",
                    "Apply a prioritization strategy (Eisenhower Matrix) to a real assignment list.",
                    "Set up and begin using the Warrior Prep planner system.",
                ],
                "vocab_focus": {
                    "word": "Prioritize",
                    "etymology": "Latin prior (first, more important) + -ize (to make/do)",
                    "definition": "To rank tasks by importance and urgency so the most critical work gets done first."
                },
                "cornell_questions": [
                    "What is the difference between urgent and important?",
                    "How does the Eisenhower Matrix work?",
                    "What goes in a planner?",
                    "How does planning reduce stress?",
                ],
                "prefilled_notes": (
                    "TWO TYPES OF ORGANIZATION:\n"
                    "  1. Physical organization — binder, locker, backpack, supplies\n"
                    "  2. Cognitive organization — knowing WHAT to do and WHEN\n\n"
                    "THE EISENHOWER MATRIX — sorting tasks into 4 boxes:\n"
                    "  URGENT + IMPORTANT → Do it NOW\n"
                    "  NOT urgent + IMPORTANT → Schedule it\n"
                    "  URGENT + NOT important → Delegate or minimize\n"
                    "  NOT urgent + NOT important → Eliminate\n\n"
                    "PLANNER BASICS:\n"
                    "  • Write every assignment the day it is given\n"
                    "  • Include the DUE DATE, not just the assignment\n"
                    "  • Check your planner at the START and END of every class\n"
                    "  • Use your Warrior Prep planner pages daily"
                ),
                "content_sections": [
                    {
                        "heading": "Urgent vs. Important — What's the Difference?",
                        "body": (
                            "URGENT tasks demand your attention right now (they have a close deadline). "
                            "IMPORTANT tasks have high value and consequences if ignored — but they may not "
                            "feel pressing. Many students only react to urgent things and never get to the "
                            "important ones. High-performing students learn to schedule important work before "
                            "it becomes urgent."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Practice: Sort Your Tasks",
                        "body": "Look at the assignment list below. Draw the Eisenhower Matrix and place each task in the correct box. Then answer: What should you do first? Why?",
                        "activity": {
                            "type": "matrix_sort",
                            "tasks": [
                                "Math test — tomorrow",
                                "Social studies project — due in 3 weeks",
                                "Clean out your locker",
                                "Reply to a friend's text",
                                "Read 10 pages of your English novel — due Friday",
                                "Watch a TV show",
                                "Study for a quiz — next class period",
                                "Pick a topic for your science fair project — due in 6 weeks",
                            ],
                        },
                    },
                    {
                        "heading": "Planner Set-Up",
                        "body": "Turn to Week 1 in your Warrior Prep planner. Write in your 6 course names. Then record any assignments or tests you already know about in the correct day/course box.",
                        "activity": None,
                    },
                ],
                "exit_ticket": {
                    "type": "reflection_scale",
                    "prompt": "Rate how organized you felt TODAY (1 = not at all, 5 = very organized). Then explain: What is ONE specific thing you will do differently this week to improve your organization?",
                    "lines": 3,
                },
            },
            # ----------------------------------------------------------
            # LESSON 1-3
            # ----------------------------------------------------------
            {
                "number": 3,
                "title": "Working Memory & Focus",
                "lesson_label": "1.3",
                "scaffolding": 2,
                "objectives": [
                    "Describe what working memory is and why it is limited.",
                    "Apply at least two strategies (chunking, brain dump, environment design) to improve focus.",
                    "Conduct a personal distraction audit and create an action plan.",
                ],
                "vocab_focus": {
                    "word": "Metacognition",
                    "etymology": "Greek meta (beyond/about) + Latin cognitio (knowledge, understanding)",
                    "definition": "Thinking about your own thinking — noticing when you are confused, distracted, or need a different strategy."
                },
                "cornell_questions": [
                    "What is working memory?",
                    "Why does chunking help?",
                    "What are my biggest distractors?",
                    "How can I design my environment for focus?",
                ],
                "prefilled_notes": (
                    "WORKING MEMORY = mental 'scratchpad' — holds ~4 items at once\n"
                    "  — Limited capacity: overload → mistakes, forgetting, frustration\n\n"
                    "STRATEGIES TO SUPPORT WORKING MEMORY:\n"
                    "  • Brain Dump — write everything you need to remember on paper BEFORE starting\n"
                    "  • Chunking — group information into meaningful units (e.g., 555-867-5309)\n"
                    "  • One task at a time — multitasking REDUCES performance by up to 40%\n\n"
                    "FOCUS STEALERS (common distractors):\n"
                    "  • Phone notifications\n"
                    "  • Background TV / music with lyrics\n"
                    "  • Hunger / fatigue\n"
                    "  • Clutter in workspace\n\n"
                    "ENVIRONMENT DESIGN:\n"
                    "  — Choose WHERE you study carefully\n"
                    "  — Phone face-down or in another room = big improvement"
                ),
                "content_sections": [
                    {
                        "heading": "The 40% Cost of Multitasking",
                        "body": (
                            "Research from the American Psychological Association shows that task-switching "
                            "— what we call 'multitasking' — reduces productivity by up to 40%. Your brain "
                            "doesn't actually do two things at once; it rapidly switches back and forth, "
                            "and each switch costs time and mental energy. For students, this means doing "
                            "homework while watching TV takes almost twice as long as doing it with the TV off."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Distraction Audit",
                        "body": "Be honest with yourself. For each distractor below, circle how often it affects your study time. Then choose your #1 distractor and write a plan to address it.",
                        "activity": {
                            "type": "audit_table",
                            "rows": [
                                "Phone / social media",
                                "TV / streaming in the background",
                                "Music with lyrics",
                                "Noise from family / roommates",
                                "Hunger",
                                "Fatigue / sleepiness",
                                "Clutter / disorganized workspace",
                                "Anxiety or stress",
                            ],
                            "columns": ["Never", "Sometimes", "Often", "Almost always"],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "three_two_one",
                    "prompts": [
                        "3 things I learned today about working memory or focus:",
                        "2 strategies I will try this week:",
                        "1 question I still have:",
                    ],
                },
            },
            # ----------------------------------------------------------
            # LESSON 1-4
            # ----------------------------------------------------------
            {
                "number": 4,
                "title": "Self-Regulation & Goal-Setting",
                "lesson_label": "1.4",
                "scaffolding": 2,
                "objectives": [
                    "Define self-regulation and explain its connection to academic success.",
                    "Write a SMART goal using the full framework.",
                    "Create a monitoring plan to track progress on their SMART goal.",
                ],
                "vocab_focus": {
                    "word": "Self-Regulation",
                    "etymology": "Latin se (oneself) + Latin regulare (to control, to rule)",
                    "definition": "The ability to manage your own emotions, thoughts, and behavior to work toward a goal, even when things are difficult."
                },
                "cornell_questions": [
                    "What is self-regulation?",
                    "What does SMART stand for?",
                    "How do I monitor my own progress?",
                    "What do I do when I fall off track?",
                ],
                "prefilled_notes": (
                    "SELF-REGULATION = managing yourself to reach a goal\n"
                    "  — Includes: delaying gratification, managing frustration, staying persistent\n\n"
                    "THE SMART GOAL FRAMEWORK:\n"
                    "  S — Specific: What exactly will I do?\n"
                    "  M — Measurable: How will I know I achieved it?\n"
                    "  A — Achievable: Is it realistic for me right now?\n"
                    "  R — Relevant: Does it matter to my life/school goals?\n"
                    "  T — Time-bound: By when will I achieve it?\n\n"
                    "WEAK goal: 'I want to do better in math.'\n"
                    "SMART goal: 'I will earn a B or higher on my next three math tests by studying for "
                    "20 minutes every other day using flashcards. I will check my grade in Infinite Campus "
                    "each Friday.'\n\n"
                    "MONITORING: Check in on your goal every week — what's working? what needs to change?"
                ),
                "content_sections": [
                    {
                        "heading": "The Marshmallow Test — and What It Really Means",
                        "body": (
                            "In a famous study, young children were given a marshmallow and told they could "
                            "eat it now, or wait 15 minutes and get two. Researchers found that children who "
                            "waited tended to have better academic outcomes later in life. But the real lesson "
                            "isn't that some people are born with willpower — it's that strategies matter. "
                            "The children who waited successfully used distraction techniques and mental tricks. "
                            "Self-regulation is a skill, not a personality trait."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Write Your SMART Goal",
                        "body": "Use the template below to write ONE SMART goal you will work on for the rest of this semester. This goal should relate to school — grades, habits, organization, or a specific subject.",
                        "activity": {
                            "type": "smart_goal_template",
                            "fields": [
                                ("S – Specific", "What exactly will I do?", 2),
                                ("M – Measurable", "How will I measure success?", 2),
                                ("A – Achievable", "Why is this realistic for me right now?", 2),
                                ("R – Relevant", "Why does this matter to me?", 2),
                                ("T – Time-bound", "I will achieve this by:", 1),
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "vocabulary_check",
                    "prompt": "Match each term to its definition. Then use TWO of the terms in a sentence that connects to your own life.",
                    "terms": ["Self-regulation", "SMART goal", "Metacognition", "Executive functioning"],
                    "definitions": [
                        "Thinking about your own thinking and learning",
                        "A goal that is Specific, Measurable, Achievable, Relevant, and Time-bound",
                        "Managing your emotions and behavior to reach a goal",
                        "Mental skills that help you plan, focus, and manage yourself",
                    ],
                },
            },
        ],
    },
    # ===================================================================
    # UNIT 2 – CAREER PATHWAYS AT TWO RIVERS
    # ===================================================================
    {
        "number": 2,
        "name": "Career Pathways at Two Rivers",
        "color": (0.13, 0.35, 0.60),   # Navy blue
        "overview": (
            "In this unit you will explore the six Minnesota career fields and the CTE pathways "
            "available at Two Rivers High School. Through reading activities and reflection, you "
            "will connect your interests to real courses and experiences you can pursue starting "
            "in 9th grade."
        ),
        "unit_vocabulary": [
            {
                "word": "Career Pathway",
                "etymology": "Latin carrera (road, course) + Old English paþ (path, track)",
                "definition": "A sequence of courses, experiences, and skills that prepares a person for a specific group of careers."
            },
            {
                "word": "CTE (Career & Technical Education)",
                "etymology": "Latin carrera (course/road) + Latin technica (art, skill) + Latin educare (to lead out, to raise)",
                "definition": "Courses and programs that combine academic learning with real-world technical and career skills."
            },
            {
                "word": "Internship",
                "etymology": "Latin internus (within, inside) — a position inside an organization for learning",
                "definition": "A supervised, hands-on learning experience within a workplace or professional setting."
            },
            {
                "word": "Cluster",
                "etymology": "Old English clyster (bunch, group)",
                "definition": "A group of related careers organized around common knowledge and skills."
            },
        ],
        "pretest": [
            "Name THREE jobs or careers you are curious about. Why do they interest you?",
            "What is a 'career pathway'? Explain in your own words.",
            "What does CTE stand for, and what do you think those courses involve?",
            "Have you ever thought about what you might study in high school or beyond? Describe your current thinking.",
            "What questions do you have about the courses available at Two Rivers High School?",
        ],
        "posttest_prompt": (
            "Revisit your pre-test responses. Then write a paragraph (5–7 sentences) describing: "
            "which career field interests you most, at least two TRHS courses or experiences related "
            "to that field, and one CAPS program you would consider applying for and why."
        ),
        "lessons": [
            {
                "number": 1,
                "title": "Minnesota Career Fields & Pathways",
                "lesson_label": "2.1",
                "scaffolding": 2,
                "objectives": [
                    "Name and describe the six Minnesota career fields.",
                    "Explain the relationship between career fields, clusters, and pathways.",
                    "Identify at least one career field that matches your interests.",
                ],
                "vocab_focus": {
                    "word": "Career Pathway",
                    "etymology": "Latin carrera (road, course) + Old English paþ (path, track)",
                    "definition": "A sequence of related courses, experiences, and skills that leads toward a specific group of careers."
                },
                "cornell_questions": [
                    "What are the 6 MN career fields?",
                    "What is the difference between a field, a cluster, and a pathway?",
                    "Which field matches my interests?",
                    "How are pathways connected to HS courses?",
                ],
                "prefilled_notes": (
                    "MINNESOTA'S 6 CAREER FIELDS:\n"
                    "  1. Engineering, Manufacturing & Technology\n"
                    "  2. Health Sciences Technology\n"
                    "  3. Arts, Communications & Information Systems\n"
                    "  4. Business, Management & Administration\n"
                    "  5. Human Services\n"
                    "  6. Agriculture, Food & Natural Resources\n\n"
                    "STRUCTURE (from broad → specific):\n"
                    "  Career FIELD → Career CLUSTER → Career PATHWAY\n"
                    "  Example: Business (field) → Finance (cluster) → Accounting (pathway)\n\n"
                    "TWO RIVERS connects its courses to these fields — that means the classes "
                    "you choose in HS can prepare you for the career field you're interested in."
                ),
                "content_sections": [
                    {
                        "heading": "Reading: Minnesota Career Fields at Two Rivers",
                        "body": (
                            "Minnesota organizes all careers into six broad fields. Each field contains multiple "
                            "clusters — groups of related industries. Each cluster branches into specific pathways "
                            "that point toward particular jobs and college programs. Two Rivers has deliberately "
                            "designed its course offerings to connect to every one of these six fields, giving you "
                            "the ability to start exploring your interests in 9th grade and build toward a pathway "
                            "over four years."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: Career Field Inventory",
                        "body": "Read the description of each career field below. Rate your interest in each (1 = not interested, 5 = very interested), then list one career from each field that you have heard of.",
                        "activity": {
                            "type": "interest_table",
                            "rows": [
                                ("Engineering, Manufacturing & Technology", "Designing, building, and maintaining systems, structures, and machines."),
                                ("Health Sciences Technology", "Caring for human health — from doctors and nurses to lab technicians and researchers."),
                                ("Arts, Communications & Information Systems", "Creating and communicating through art, music, media, and technology."),
                                ("Business, Management & Administration", "Running organizations, managing finances, marketing products, and leading teams."),
                                ("Human Services", "Supporting people through education, social work, law enforcement, and government."),
                                ("Agriculture, Food & Natural Resources", "Growing food, managing land, protecting ecosystems, and sustaining natural resources."),
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "quick_write",
                    "prompt": "Which career field interests you MOST right now? Write 3–4 sentences explaining your choice. What careers within that field have you heard of or are curious about?",
                    "lines": 4,
                },
            },
            {
                "number": 2,
                "title": "STEM & Health Pathways at TRHS",
                "lesson_label": "2.2",
                "scaffolding": 2,
                "objectives": [
                    "Identify specific TRHS courses that connect to Engineering/Technology and Health Sciences pathways.",
                    "Read and summarize course descriptions from the Academic Planning Guide.",
                    "Evaluate which courses in these fields align with their interests and abilities.",
                ],
                "vocab_focus": {
                    "word": "CTE (Career & Technical Education)",
                    "etymology": "Latin carrera (course/road) + Latin technica (art, skill) + Latin educare (to lead out, to raise)",
                    "definition": "Programs that blend classroom learning with hands-on technical and career-readiness skills."
                },
                "cornell_questions": [
                    "What Engineering/Tech courses does TRHS offer?",
                    "What Health Sciences courses are available?",
                    "What is the CAPS program?",
                    "Which of these courses interest me?",
                ],
                "prefilled_notes": (
                    "ENGINEERING, MANUFACTURING & TECHNOLOGY at TRHS:\n"
                    "  Courses: Basic Auto Mechanics, Small Gas Engine Repair, Super Mileage Car Design I & II,\n"
                    "  Woodworking I-III, Printing Technology, Metals, CADD (Computer-Aided Design & Drafting),\n"
                    "  Math for the Trades\n"
                    "  CAPS Experience: Transportation & Skilled Trades (junior/senior, periods 5-6-7, off-site)\n\n"
                    "HEALTH SCIENCES TECHNOLOGY at TRHS:\n"
                    "  Courses: Human Anatomy & Physiology\n"
                    "  Experiences: Certified Nursing Assistant (CNA), CAPS Healthcare & Medicine\n"
                    "  (junior/senior, off-site at South St. Paul Community Learning Center)\n\n"
                    "CAPS = Career Academy Programs — year-long, immersive, include an internship"
                ),
                "content_sections": [
                    {
                        "heading": "Reading: Course Descriptions from the Planning Guide",
                        "body": (
                            "Two Rivers offers a wide range of technical courses you can take as early as 9th grade. "
                            "In Engineering & Technology, courses like CADD and Woodworking teach you to design, build, "
                            "and problem-solve with real tools. In Health Sciences, Human Anatomy & Physiology gives you "
                            "a rigorous look at how the human body works — a foundation for any health career. "
                            "The CAPS (Career Academy Programs) are the most immersive option: year-long courses where "
                            "you work alongside professionals and complete a real internship."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: Course Connection Chart",
                        "body": "Pick TWO courses from the list above that you find most interesting. For each one, complete the chart below using information from the Academic Planning Guide.",
                        "activity": {
                            "type": "two_column_chart",
                            "fields": ["Course name", "Grade eligible", "What you learn", "Career connection", "My interest rating (1-5)"],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "sentence_stems",
                    "prompts": [
                        "One course in Engineering/Technology or Health Sciences that I would consider taking is _____ because…",
                        "Something I did NOT know about TRHS course options before today is…",
                    ],
                },
            },
            {
                "number": 3,
                "title": "Arts, Business & Human Services Pathways",
                "lesson_label": "2.3",
                "scaffolding": 3,
                "objectives": [
                    "Identify TRHS courses connected to Arts/Communications, Business/Management, and Human Services.",
                    "Compare two different career pathways using evidence from the Academic Planning Guide.",
                    "Articulate how their personal interests and strengths connect to one or more pathways.",
                ],
                "vocab_focus": {
                    "word": "Internship",
                    "etymology": "Latin internus (within, inside) — learning from inside an organization",
                    "definition": "A supervised experience inside a professional workplace that provides real-world career training."
                },
                "cornell_questions": [
                    "What arts/communications courses does TRHS offer?",
                    "What business courses are available?",
                    "How does the Human Services pathway connect to teaching?",
                    "What CAPS programs connect to these fields?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Reading: Arts, Communications & Information Systems",
                        "body": (
                            "Two Rivers has one of the broadest arts offerings in the district. Students can study "
                            "visual art (drawing, painting, ceramics, sculpture, digital art, AP Studio Art), music "
                            "(band, orchestra, choir, guitar, digital music production, music theory), and media "
                            "(video production, mass media production, photography, journalism, yearbook). "
                            "For students interested in technology and computing, Intro to Computer Science and "
                            "AP Computer Science Principles are also in this pathway. The CAPS Computer Science & IT "
                            "program (junior/senior) earns 3 elective credits and an industry-recognized A+ certification."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Reading: Business, Management & Administration",
                        "body": (
                            "Students interested in business can start with Business & Entrepreneurship or Accounting I "
                            "as early as 9th grade. Upper-level options include Personal Finance, AP Business with "
                            "Personal Finance, and Sales, Marketing & School Store Management. The CAPS Business & "
                            "Entrepreneurship program (junior/senior, at Evolve Workplace in St. Paul) earns 2 elective "
                            "credits plus 1 English credit and includes a real business internship. Family and Consumer "
                            "Sciences courses (Intro to Foods, Culinary I & II, Clothing) also fit in the Business pathway."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: Compare Two Pathways",
                        "body": "Choose ANY two career pathways from Units 2.2 or 2.3. Use the Venn Diagram below to compare them. Consider: types of courses, types of careers, skills needed, and whether you can earn college credit.",
                        "activity": {
                            "type": "venn_diagram",
                            "label_a": "Pathway 1: ___________",
                            "label_b": "Pathway 2: ___________",
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "reflection_scale",
                    "prompt": "After exploring three career fields today, rate how clear you feel about your own interests (1 = very unclear, 5 = very clear). Then explain: Which pathway feels most 'like you' and why?",
                    "lines": 4,
                },
            },
            {
                "number": 4,
                "title": "Ag, Food & Natural Resources — and Planning My Path",
                "lesson_label": "2.4",
                "scaffolding": 3,
                "objectives": [
                    "Identify courses and CAPS experiences in the Agriculture/Natural Resources field.",
                    "Synthesize learning from all four career lessons into a personal interest reflection.",
                    "Articulate a potential career field direction and the first TRHS course they would take to explore it.",
                ],
                "vocab_focus": {
                    "word": "Cluster",
                    "etymology": "Old English clyster (bunch, group) — a group of related things organized together",
                    "definition": "In career planning, a cluster is a group of related occupations built around common knowledge and skills."
                },
                "cornell_questions": [
                    "What is the Ag/Natural Resources pathway at TRHS?",
                    "What makes the CAPS Ag program unique?",
                    "Which of the 6 career fields is most interesting to me?",
                    "What course will I take in 9th grade to explore my pathway?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Reading: Agriculture, Food & Natural Resources at TRHS",
                        "body": (
                            "This field may be smaller in course offerings at Two Rivers, but its CAPS program "
                            "is one of the most unique. The CAPS Natural Resources, Sustainability & Food Systems "
                            "program is co-taught by a chemistry and agriculture teacher at Dodge Nature Center in "
                            "West St. Paul. Students explore soil science, food systems, water quality, and sustainable "
                            "agriculture through hands-on labs and fieldwork — and complete a second-semester internship. "
                            "The course earns 2 elective credits plus 1 Chemistry credit. AP Environmental Science "
                            "is also a strong option within this field."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: My Career Pathway Reflection",
                        "body": "Use the prompts below to write a personal reflection on all four career pathway lessons. Use specific course names and pathway titles from the Academic Planning Guide.",
                        "activity": {
                            "type": "guided_reflection",
                            "prompts": [
                                "The career field that interests me most is _______ because…",
                                "Within that field, a specific career I am curious about is…",
                                "At Two Rivers, I could explore this field by taking… (name at least 2 courses)",
                                "One CAPS or internship experience I would consider applying for is… because…",
                                "A career field I had NOT thought about before this unit but now find interesting is…",
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "postcard",
                    "prompt": (
                        "Imagine you are writing a postcard to your future 9th-grade self. In 4–6 sentences, "
                        "tell them: which career pathway you are most curious about, one course at TRHS you "
                        "cannot wait to try, and one piece of advice about exploring their interests."
                    ),
                    "lines": 5,
                },
            },
        ],
    },
    # ===================================================================
    # UNIT 3 – ACADEMIC PREPARATION FOR RIGOROUS COURSES
    # ===================================================================
    {
        "number": 3,
        "name": "Academic Preparation for Rigorous Courses",
        "color": (0.20, 0.50, 0.25),   # Forest green
        "overview": (
            "This unit builds the academic skills you will need to succeed in challenging high school "
            "courses and beyond. You will develop strategies for reading complex texts, writing with "
            "clarity and stamina, studying effectively, and managing long-term academic work — the "
            "exact skills that separate thriving students from struggling ones in rigorous courses."
        ),
        "unit_vocabulary": [
            {
                "word": "Stamina",
                "etymology": "Latin stamina (threads of life, staying power) — from stamen (the warp thread of cloth)",
                "definition": "The ability to sustain effort over time without giving up; in reading/writing, the capacity to focus for extended periods."
            },
            {
                "word": "Annotation",
                "etymology": "Latin annotare (to note down) — ad (to) + notare (to mark)",
                "definition": "Writing notes, questions, and reactions directly on or near a text to deepen understanding."
            },
            {
                "word": "Synthesis",
                "etymology": "Greek synthesis (putting together) — syn (together) + tithenai (to place)",
                "definition": "Combining information from multiple sources or ideas to form a new, deeper understanding."
            },
            {
                "word": "Spaced Practice",
                "etymology": "Latin spatium (space, interval) + Latin practicare (to practice, to perform)",
                "definition": "A study technique in which learning is spread out over multiple shorter sessions rather than crammed into one long session."
            },
        ],
        "pretest": [
            "Describe how you currently read a difficult text (a science article, a history chapter, etc.).",
            "What do you do when you sit down to write and don't know how to start?",
            "How do you study for a test? Walk us through your process step by step.",
            "What is the longest piece of writing you have ever completed? How did you manage it?",
            "What subject do you find most academically challenging and why?",
        ],
        "posttest_prompt": (
            "Revisit your pre-test responses. Rewrite your answer to Question 3 (how you study for a test) "
            "using at least three strategies from this unit. Then write a paragraph describing how your "
            "approach to reading or writing has changed as a result of this unit."
        ),
        "lessons": [
            {
                "number": 1,
                "title": "Active Reading & Annotation",
                "lesson_label": "3.1",
                "scaffolding": 2,
                "objectives": [
                    "Explain the difference between passive and active reading.",
                    "Apply a consistent annotation system to a challenging text.",
                    "Use context clues and morphology to define unknown vocabulary.",
                ],
                "vocab_focus": {
                    "word": "Annotation",
                    "etymology": "Latin annotare (to note down) — ad (to) + notare (to mark)",
                    "definition": "Writing notes, questions, reactions, and connections directly on or beside a text while reading."
                },
                "cornell_questions": [
                    "What is active reading?",
                    "What does a good annotation look like?",
                    "How do context clues help with vocabulary?",
                    "Why is annotating better than highlighting?",
                ],
                "prefilled_notes": (
                    "PASSIVE READING: eyes move across the page, mind wanders → poor retention\n"
                    "ACTIVE READING: you interact with the text → deep understanding\n\n"
                    "ANNOTATION SYSTEM (use consistently):\n"
                    "  * = important idea\n"
                    "  ? = I don't understand this / I have a question\n"
                    "  ! = surprising or interesting\n"
                    "  → = connection to something else I know\n"
                    "  Circle = unknown vocabulary word\n"
                    "  Underline = key term or main idea\n"
                    "  Margin notes = summarize the paragraph in your own words\n\n"
                    "CONTEXT CLUES — when you hit an unknown word:\n"
                    "  1. Look at surrounding sentences for clues\n"
                    "  2. Break the word into parts (prefix, root, suffix)\n"
                    "  3. Substitute a guess and check if the sentence makes sense"
                ),
                "content_sections": [
                    {
                        "heading": "Why Highlighting Doesn't Work",
                        "body": (
                            "Studies show that students who highlight passages retain barely more information than "
                            "students who don't. Why? Because highlighting is a passive activity — your hand moves "
                            "but your brain doesn't do anything. Annotation forces you to think: 'What does this mean? "
                            "Why does it matter? How does it connect to what I already know?' That thinking IS learning."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Practice: Annotate This Passage",
                        "body": (
                            "Read the passage below. Use the annotation system from your notes. "
                            "After reading, write a 2-sentence summary in the margin.\n\n"
                            "\"Neuroplasticity is the brain's ability to reorganize itself by forming new neural connections "
                            "throughout life. Unlike a computer, which has fixed hardware, the human brain can actually "
                            "change its physical structure in response to learning and experience. When you practice a skill "
                            "repeatedly, the neural pathways associated with that skill become stronger and more efficient — "
                            "a process sometimes described as 'neurons that fire together, wire together.' This means that "
                            "the mental skills you practice in school — reading, analyzing, writing, problem-solving — are "
                            "literally reshaping your brain. Every time you push through a difficult text or work through a "
                            "challenging math problem, you are making yourself smarter.\""
                        ),
                        "activity": {
                            "type": "annotation_practice",
                            "passage_included": True,
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "three_two_one",
                    "prompts": [
                        "3 annotation symbols I will use and what they mean:",
                        "2 ways active reading is different from passive reading:",
                        "1 word from today's passage I looked up or figured out from context:",
                    ],
                },
            },
            {
                "number": 2,
                "title": "Writing Stamina & Clarity",
                "lesson_label": "3.2",
                "scaffolding": 3,
                "objectives": [
                    "Define writing stamina and explain why it is a learnable skill.",
                    "Apply a structured process (plan → draft → revise) to a short writing task.",
                    "Use precise vocabulary and varied sentence structure to improve clarity.",
                ],
                "vocab_focus": {
                    "word": "Stamina",
                    "etymology": "Latin stamina (threads of life, staying power) — from stamen (the warp thread of cloth)",
                    "definition": "The ability to sustain effort without quitting; in writing, the capacity to write productively for extended periods."
                },
                "cornell_questions": [
                    "What is writing stamina?",
                    "What is the plan-draft-revise process?",
                    "What makes writing clear and precise?",
                    "How do I push through writer's block?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "The Plan-Draft-Revise Cycle",
                        "body": (
                            "Strong writers don't just sit down and write perfectly the first time. They use a process. "
                            "PLAN: spend 2–5 minutes before writing. Jot down your main idea, 2–3 supporting points, "
                            "and any key evidence. DRAFT: write without stopping — don't edit as you go; just get your "
                            "thinking down. REVISE: read your draft and ask, 'Is this clear? Is every sentence necessary? "
                            "Did I use precise words?' In rigorous high school courses, you will be expected to write "
                            "under time pressure (timed essays, in-class writes). Building writing stamina now means "
                            "that pressure won't stop you."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Timed Write: Building Your Stamina",
                        "body": (
                            "You have 12 minutes to respond to this prompt. Use the Plan-Draft-Revise process. "
                            "Do NOT stop writing once you begin your draft.\n\n"
                            "PROMPT: What is the most important skill a student needs to succeed in high school? "
                            "Use specific evidence from your own experience or from what you have learned in this "
                            "course to support your answer."
                        ),
                        "activity": {
                            "type": "timed_write",
                            "minutes": 12,
                            "lines": 16,
                        },
                    },
                    {
                        "heading": "Revision: Making It Clearer",
                        "body": "Exchange your draft with a partner. Use the checklist below to give feedback. Then revise your own draft based on the feedback you receive.",
                        "activity": {
                            "type": "checklist",
                            "items": [
                                "The main idea is clear in the first 2 sentences.",
                                "Each paragraph has one main point.",
                                "Specific examples or evidence are included.",
                                "Vague words (thing, stuff, good, bad) have been replaced with precise ones.",
                                "There are no run-on sentences or fragments.",
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "quick_write",
                    "prompt": "What is ONE thing you did in today's timed write that you are proud of? What is ONE thing you will work on next time? Be specific.",
                    "lines": 3,
                },
            },
            {
                "number": 3,
                "title": "Study Strategies & Spaced Practice",
                "lesson_label": "3.3",
                "scaffolding": 3,
                "objectives": [
                    "Distinguish between effective and ineffective study strategies using research evidence.",
                    "Apply spaced practice and retrieval practice to a real upcoming test or assignment.",
                    "Build a personal study schedule using their planner.",
                ],
                "vocab_focus": {
                    "word": "Spaced Practice",
                    "etymology": "Latin spatium (space, interval) + Latin practicare (to practice, perform)",
                    "definition": "Spreading studying across multiple sessions over time, rather than cramming everything into one session."
                },
                "cornell_questions": [
                    "Why doesn't cramming work long-term?",
                    "What is retrieval practice?",
                    "What is the spacing effect?",
                    "How do I build a study schedule?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "What the Research Says",
                        "body": (
                            "Decades of cognitive science research have identified a clear hierarchy of study strategies. "
                            "At the bottom: re-reading notes and highlighting (low effectiveness). Near the top: "
                            "RETRIEVAL PRACTICE (testing yourself — flashcards, practice problems, writing from memory) "
                            "and SPACED PRACTICE (spreading study sessions over days and weeks). The spacing effect is "
                            "one of the most replicated findings in all of psychology: you remember far more when you "
                            "study in short, spaced sessions than in one long cram session — even if the total study "
                            "time is the same. In AP and advanced courses at TRHS, the amount of material is too large "
                            "to cram. Spacing and retrieval aren't just better — they're necessary."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: Build a Study Plan",
                        "body": "Identify ONE upcoming test or major assignment in any of your current classes. Use your planner and the template below to build a spaced study plan for it.",
                        "activity": {
                            "type": "study_plan_template",
                            "fields": [
                                "Subject / Assignment:",
                                "Due date / Test date:",
                                "Study Session 1 (date & what I will do):",
                                "Study Session 2 (date & what I will do):",
                                "Study Session 3 (date & what I will do):",
                                "How I will test myself (retrieval practice method):",
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "reflection_scale",
                    "prompt": "How different is this study approach from what you normally do? (1 = same as always, 5 = completely different). Explain the most important change you will make and when you will start.",
                    "lines": 3,
                },
            },
            {
                "number": 4,
                "title": "Managing Long-Term Projects & Self-Advocacy",
                "lesson_label": "3.4",
                "scaffolding": 4,
                "objectives": [
                    "Break a long-term project into a backward-planned sequence of steps.",
                    "Demonstrate self-advocacy skills through role-play (asking a teacher for help).",
                    "Apply synthesis skills by connecting learning from Units 1–3.",
                ],
                "vocab_focus": {
                    "word": "Synthesis",
                    "etymology": "Greek synthesis (putting together) — syn (together) + tithenai (to place)",
                    "definition": "Combining multiple pieces of information or ideas to build a new, deeper understanding — going beyond summary."
                },
                "cornell_questions": [
                    "What is backward planning?",
                    "What is self-advocacy?",
                    "How does synthesis connect to college and career readiness?",
                    "What skills from Units 1-3 connect here?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Backward Planning a Long-Term Project",
                        "body": (
                            "When you receive a long-term assignment, high-performing students start at the END "
                            "and work backward. Step 1: Write down the final deadline. Step 2: Identify all the "
                            "tasks that must be done before the final product is ready. Step 3: Assign each task "
                            "its own deadline, working backward from the final due date. Step 4: Enter each task "
                            "in your planner. This makes a project that felt overwhelming feel manageable — because "
                            "each day you know exactly what you need to do."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: Backward Plan a Project",
                        "body": "Use the timeline below to backward-plan either a real upcoming project or this scenario: 'You have 3 weeks to write a 5-page research paper on a historical event.'",
                        "activity": {
                            "type": "backward_plan",
                            "weeks": 3,
                        },
                    },
                    {
                        "heading": "Self-Advocacy: Asking for Help",
                        "body": (
                            "One of the most important skills in rigorous courses is knowing when and how to ask for help. "
                            "Research shows that students who ask questions and seek help learn more — but many students "
                            "avoid asking out of embarrassment or not knowing how. With a partner, practice this script:\n\n"
                            "'Hi [Teacher's name], I was working on [assignment] and I'm having trouble with [specific part]. "
                            "I've already tried [what I attempted]. Could you help me understand [specific question]?'\n\n"
                            "Notice: be specific. Saying 'I don't get it' gets a different response than explaining exactly "
                            "what you tried and where you got stuck."
                        ),
                        "activity": {
                            "type": "role_play",
                            "scenarios": [
                                "You bombed a quiz and want to understand what went wrong.",
                                "You have a project due in 2 weeks and don't understand the requirements.",
                                "You missed class and need to catch up on notes.",
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "synthesis_write",
                    "prompt": (
                        "Look back at Units 1, 2, and 3. Choose ONE skill from EACH unit that you think will be "
                        "most important for your success in 9th grade. Write a paragraph (5–7 sentences) explaining "
                        "your three choices and how they connect to each other."
                    ),
                    "lines": 7,
                },
            },
        ],
    },
    # ===================================================================
    # UNIT 4 – MY 9TH GRADE YEAR PLAN
    # ===================================================================
    {
        "number": 4,
        "name": "My 9th Grade Year Plan",
        "color": (0.50, 0.25, 0.60),   # Purple
        "overview": (
            "In this unit you will use the Two Rivers Academic Planning Guide to build a realistic, "
            "personalized plan for your 9th grade year. You will draft a course schedule, map out "
            "your time outside of school, explore activities and athletics, and create a daily time "
            "management plan that reflects who you are and what you want to accomplish."
        ),
        "unit_vocabulary": [
            {
                "word": "Prerequisite",
                "etymology": "Latin prae (before) + requirere (to need, to seek) — something required before you can proceed",
                "definition": "A course or requirement that must be completed before a student can enroll in a more advanced course."
            },
            {
                "word": "Credit",
                "etymology": "Latin creditum (something entrusted) — from credere (to believe, to trust)",
                "definition": "A unit of academic achievement; at TRHS, a semester-long course typically earns 0.5 credits, and a full-year course earns 1 credit."
            },
            {
                "word": "GPA (Grade Point Average)",
                "etymology": "Latin gradus (step, rank) + Medieval Latin punctum (point) — an average of your academic performance",
                "definition": "A number (on a 4.0 scale at TRHS) that represents your average grade across all courses. Weighted courses can earn up to 4.8."
            },
            {
                "word": "Elective",
                "etymology": "Latin electus (chosen, selected) — from eligere (to choose, to pick out)",
                "definition": "A course that a student chooses based on personal interest; not required for graduation but counts toward total credits."
            },
        ],
        "pretest": [
            "Name THREE courses you know you will be required to take in 9th grade at TRHS.",
            "What is a GPA and how is it calculated?",
            "List any activities, clubs, or sports you are considering joining in high school.",
            "How many hours per night do you currently spend on homework? How many do you think you will need in high school?",
            "What does it mean to 'plan your time'? What strategies do you currently use?",
        ],
        "posttest_prompt": (
            "Attach or summarize your completed 9th Grade Mock Schedule from Lesson 4.2. Then write a "
            "paragraph (5–7 sentences) describing how you plan to balance your academic work, "
            "extracurricular activities, and personal time during your 9th grade year. Use specific "
            "times, course names, and activity names."
        ),
        "lessons": [
            {
                "number": 1,
                "title": "Reading the Academic Planning Guide",
                "lesson_label": "4.1",
                "scaffolding": 3,
                "objectives": [
                    "Locate and summarize graduation requirements for the Class of 2029 and beyond.",
                    "Explain the difference between required courses, electives, and CAPS experiences.",
                    "Identify which 9th grade courses are required and which are student-choice.",
                ],
                "vocab_focus": {
                    "word": "Prerequisite",
                    "etymology": "Latin prae (before) + requirere (to need, to seek)",
                    "definition": "A course that must be completed before enrolling in a more advanced one — your entry ticket to the next level."
                },
                "cornell_questions": [
                    "What are the graduation requirements for class of 2029+?",
                    "Which 9th grade courses are required?",
                    "What is the difference between required and elective?",
                    "What is a prerequisite and why does it matter?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Graduation Requirements for Class of 2029 and Beyond",
                        "body": (
                            "To graduate from Two Rivers, students must earn a minimum of 23 credits. Required areas include: "
                            "Language Arts (4 credits), Social Studies (4 credits), Mathematics (3 credits — through Algebra II minimum), "
                            "Science (3 credits — Earth & Space Science, Biology, plus Chemistry or Physics), "
                            "Physical Education & Health (1.5 credits), Warrior Seminar (0.5 credits), "
                            "Arts (1 credit), Personal Finance (0.5 credits), and Electives (5.5 credits). "
                            "This means more than half of your credits are REQUIRED — but nearly a third are yours to choose."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Activity: Required vs. Choice — 9th Grade Edition",
                        "body": "Based on the Warrior Graduation Plan (Class of 2029+) and the Academic Planning Guide, fill in the chart below for your 9th grade year.",
                        "activity": {
                            "type": "schedule_grid",
                            "periods": ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5", "Period 6", "Period 7"],
                            "semesters": ["Semester 1", "Semester 2"],
                            "note": "Use the graduation plan on pages 12-13 of the Academic Planning Guide to fill in required courses, then use elective slots for courses of your choice.",
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "sentence_stems",
                    "prompts": [
                        "One thing I did NOT know about TRHS graduation requirements before today is…",
                        "A required 9th grade course I am looking forward to is _____ because…",
                        "A question I still have about building my schedule is…",
                    ],
                },
            },
            {
                "number": 2,
                "title": "My Mock 9th Grade Schedule",
                "lesson_label": "4.2",
                "scaffolding": 4,
                "objectives": [
                    "Create a complete, realistic mock 9th grade course schedule using the Academic Planning Guide.",
                    "Select elective courses that align with personal interests and/or career pathway goals.",
                    "Verify that their schedule meets all 9th grade requirements.",
                ],
                "vocab_focus": {
                    "word": "Elective",
                    "etymology": "Latin electus (chosen, selected) — from eligere (to choose, to pick out)",
                    "definition": "A course chosen by the student that goes beyond required coursework — your opportunity to follow your interests."
                },
                "cornell_questions": [
                    "What electives could I take in 9th grade?",
                    "How do I know if I meet prerequisites?",
                    "What is Warrior Seminar?",
                    "How do my electives connect to my career interests?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Warrior Seminar — Your Built-In Support",
                        "body": (
                            "Every 9th grader takes Warrior Seminar (unless in AVID or AP Human Geo Enrichment). "
                            "This course is designed specifically to help you transition to high school — it covers "
                            "time management, note-taking strategies, career awareness, and builds your post-secondary "
                            "portfolio. You'll meet with a professional mentor four times during the year. This course "
                            "is DIRECTLY connected to Warrior Prep — everything you learn here will help you succeed there."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Build Your Mock Schedule",
                        "body": (
                            "Use the Academic Planning Guide to build your complete 9th grade mock schedule below. "
                            "Fill in ALL 7 periods for both semesters. Be sure to: include all required courses, "
                            "choose electives that connect to your career interests from Unit 2, check prerequisites, "
                            "and verify you are on the right math track."
                        ),
                        "activity": {
                            "type": "full_schedule_builder",
                            "periods": 7,
                            "semesters": 2,
                            "include_reflection": True,
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "quick_write",
                    "prompt": "Look at your completed mock schedule. Which course are you most excited about and why? Which course concerns you most and why? What can you do NOW to prepare for that course?",
                    "lines": 5,
                },
            },
            {
                "number": 3,
                "title": "Activities, Clubs & Sports at TRHS",
                "lesson_label": "4.3",
                "scaffolding": 4,
                "objectives": [
                    "Identify at least 5 activities, clubs, or sports available at TRHS.",
                    "Evaluate how involvement in extracurriculars connects to skills, relationships, and college readiness.",
                    "Create a personal list of activities they want to try in 9th grade.",
                ],
                "vocab_focus": {
                    "word": "Credit",
                    "etymology": "Latin creditum (something entrusted) — from credere (to believe, trust)",
                    "definition": "In school, a unit of earned academic achievement. In life, earned trust and recognition for your work and involvement."
                },
                "cornell_questions": [
                    "What activities are available at TRHS?",
                    "Why do activities matter beyond just 'fun'?",
                    "What is the time commitment for athletics?",
                    "How do I balance activities and academics?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Why Get Involved?",
                        "body": (
                            "Research consistently shows that students who are involved in extracurricular activities "
                            "have higher GPAs, better attendance, and stronger social connections than students who are not. "
                            "Activities build skills you can't get in a classroom: leadership, teamwork, time management under "
                            "pressure, commitment, and resilience. They also appear on your college applications and résumé. "
                            "Perhaps most importantly, finding something you love at TRHS makes school a place you WANT to be."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "TRHS Activities, Clubs & Sports Directory",
                        "body": "Below is a partial list of activities available at Two Rivers. Circle anything that interests you. Put a star next to your top 3.",
                        "activity": {
                            "type": "activities_checklist",
                            "categories": {
                                "Clubs": [
                                    "Art Club", "Asian & Pacific Islander Club", "Bass Fishing", "Bowling",
                                    "Digital Wellbeing", "Dungeons & Dragons", "GISA", "Jewish Student Union",
                                    "Library Club", "LiveGreen", "Model United Nations", "Muslim Student Association",
                                    "Pickleball", "Ping Pong", "Pokemon", "Pom Squad", "Sports Analytics",
                                    "Trap Shooting", "Unified Club", "Women in STEM",
                                ],
                                "Activities": [
                                    "Debate", "Fall Play", "Jazz Band", "Marching Band", "Musical",
                                    "One Act Play", "Robotics", "Science Olympiad", "Speech", "Vocal Jazz",
                                    "Winterguard", "Cheer",
                                ],
                                "Service Groups": [
                                    "ALMAS", "Key Club", "LINK Crew", "National Honor Society", "Student Council",
                                    "Tech Warriors",
                                ],
                                "Fall Sports": [
                                    "Cross Country (Boys)", "Cross Country (Girls)", "Football",
                                    "Soccer (Boys)", "Soccer (Girls)", "Swimming & Diving (Girls)",
                                    "Tennis (Girls)", "Volleyball",
                                ],
                                "Winter Sports": [
                                    "Basketball (Boys)", "Basketball (Girls)", "Dance", "Gymnastics",
                                    "Hockey (Boys)", "Hockey (Girls)", "Nordic Skiing (Boys)",
                                    "Nordic Skiing (Girls)", "Swimming & Diving (Boys)", "Wrestling",
                                ],
                                "Spring Sports": [
                                    "Baseball", "Golf (Boys)", "Golf (Girls)", "Lacrosse (Boys)",
                                    "Lacrosse (Girls)", "Soccer (Fall)", "Softball", "Tennis (Boys)",
                                    "Track & Field (Boys)", "Track & Field (Girls)",
                                ],
                            },
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "planning_response",
                    "prompts": [
                        "My top 3 activities/clubs/sports I want to try in 9th grade:",
                        "One reason I chose each one:",
                        "One concern I have about balancing activities with schoolwork:",
                        "One strategy I will use to manage that balance:",
                    ],
                },
            },
            {
                "number": 4,
                "title": "My Daily Time Map",
                "lesson_label": "4.4",
                "scaffolding": 4,
                "objectives": [
                    "Create a realistic daily schedule that accounts for school, homework, activities, and personal time.",
                    "Identify and protect dedicated study time in their 9th grade schedule.",
                    "Combine their mock course schedule, activity list, and time map into a coherent 9th Grade Year Plan.",
                ],
                "vocab_focus": {
                    "word": "GPA (Grade Point Average)",
                    "etymology": "Latin gradus (step, rank) + Medieval Latin punctum (point)",
                    "definition": "A numerical summary of your academic performance on a 4.0 scale; a key measure colleges and employers use to evaluate students."
                },
                "cornell_questions": [
                    "How many hours do I have in a school day beyond classes?",
                    "What is a realistic homework estimate for 9th grade?",
                    "How do I protect time for sleep?",
                    "What does a balanced 9th grade day look like?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "The Math of Your Day",
                        "body": (
                            "School day: 8:25 AM–3:05 PM = 6 hours 40 minutes. Sleep: TRHS recommends 8–9 hours "
                            "(research shows teens need at least 8). That's 16–17 hours accounted for. You have "
                            "7–8 hours left for: homework (TRHS expects at least 1.5 hours/night for 9th grade), "
                            "activities and sports (typically 2–3 hours on practice days), eating and commute, "
                            "family time, and yes — screen time and downtime. When you map it out, the math "
                            "is tight. High performers protect their homework time first, then schedule everything else around it."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Build Your Daily Time Map",
                        "body": "Fill in a realistic schedule for a typical school day and a typical activity/sport day in 9th grade. Include wake-up time, school, activities, homework, meals, and bedtime.",
                        "activity": {
                            "type": "time_map",
                            "hours": list(range(6, 24)),  # 6 AM to 11 PM
                            "columns": ["School Day", "Activity/Sport Day"],
                        },
                    },
                    {
                        "heading": "My 9th Grade Year Plan — Putting It All Together",
                        "body": "You now have all the pieces of your 9th Grade Year Plan. Complete the summary below, referencing your work from Lessons 4.1–4.4.",
                        "activity": {
                            "type": "year_plan_summary",
                            "fields": [
                                ("My 9th grade courses (list all 7 periods):", 7),
                                ("My top 3 extracurricular activities:", 3),
                                ("My daily homework time (time and location):", 2),
                                ("My #1 academic goal for 9th grade:", 2),
                                ("One thing I am most excited about:", 2),
                                ("One thing I am most nervous about, and my plan for it:", 3),
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "synthesis_write",
                    "prompt": (
                        "Imagine it is the end of your 9th grade year and it went exactly as you hoped. "
                        "Write 5–7 sentences describing what that year looked like: your grades, your activities, "
                        "how you managed your time, and how you felt. Be specific — use course names, activity names, "
                        "and real details from your plan."
                    ),
                    "lines": 7,
                },
            },
        ],
    },
    # ===================================================================
    # UNIT 5 – TRANSITION TO HIGH SCHOOL
    # ===================================================================
    {
        "number": 5,
        "name": "Transition to High School",
        "color": (0.60, 0.40, 0.10),   # Amber/orange
        "overview": (
            "In this final unit you will take everything you have learned and connect it directly "
            "to the experience of being a new student at Two Rivers High School. You will understand "
            "how grades and credits work, explore how to get involved, finalize your course selections, "
            "and hear directly from current TRHS students who have been in your shoes."
        ),
        "unit_vocabulary": [
            {
                "word": "Weighted Grade",
                "etymology": "Old English gewiht (weight, heaviness) + Latin gradus (step, rank)",
                "definition": "A grade that counts for more than a standard grade on the GPA scale, awarded for AP, CIS, and college-credit courses at TRHS (up to 4.8 instead of 4.0)."
            },
            {
                "word": "Transcript",
                "etymology": "Latin transcribere (to copy over) — trans (across) + scribere (to write)",
                "definition": "Your official academic record — a document listing all your courses, grades, and credits earned in high school."
            },
            {
                "word": "BARR (Building Assets, Reducing Risks)",
                "etymology": "Acronym: Building Assets, Reducing Risks — a research-based model of student support",
                "definition": "A program at TRHS where 9th graders are placed on teams of 3-4 teachers who communicate regularly to support student success."
            },
            {
                "word": "Concurrent Enrollment (CE)",
                "etymology": "Latin concurrere (to run together) + Latin enrollare (to enter on a roll/list)",
                "definition": "Taking a high school course that also earns college credit, taught by a college-approved high school teacher."
            },
        ],
        "pretest": [
            "How is a high school GPA different from a middle school grade? What do you already know?",
            "What questions do you have about high school grades, credits, or graduation?",
            "What is ONE thing that makes you excited about starting high school?",
            "What is ONE thing that makes you nervous about starting high school?",
            "What advice do you wish someone had given you before starting middle school?",
        ],
        "posttest_prompt": (
            "Write a letter (at least two paragraphs) to an 8th grader who is about to take Warrior Prep next year. "
            "Tell them: what you learned in this course, what you would do differently if you could go back, "
            "your top three pieces of advice for transitioning to Two Rivers, and what you are most looking forward "
            "to in 9th grade."
        ),
        "lessons": [
            {
                "number": 1,
                "title": "Grades, Credits & GPA at TRHS",
                "lesson_label": "5.1",
                "scaffolding": 4,
                "objectives": [
                    "Explain how credits, GPA, and weighted grades work at TRHS.",
                    "Calculate a sample GPA using the TRHS grading scale.",
                    "Identify the academic habits that protect and grow a strong GPA.",
                ],
                "vocab_focus": {
                    "word": "Weighted Grade",
                    "etymology": "Old English gewiht (weight, heaviness) + Latin gradus (step, rank)",
                    "definition": "A grade that earns more GPA points, rewarding students who take advanced courses like AP and CIS."
                },
                "cornell_questions": [
                    "How is TRHS GPA calculated?",
                    "What is a weighted grade?",
                    "How does the credit system work?",
                    "What happens if I fail a required course?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "How Grades Work at TRHS",
                        "body": (
                            "TRHS uses a 4.0 GPA scale for standard courses and a 4.8 scale for AP, CIS (College in the Schools), "
                            "and college-credit courses. The school year has four quarters; your semester grade (the grade that appears "
                            "on your transcript) is calculated from two quarters. A semester course earns 0.5 credits; a full-year course "
                            "earns 1.0 credit. You need 23 total credits to graduate. Dropping a course after week 10 results in an F "
                            "for that semester — so choose carefully and stay in courses you've started."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "GPA Practice",
                        "body": "Using the grading scale from the Academic Planning Guide, calculate the GPA for the sample student below. Then answer: What grade in which course would have the biggest positive impact on this GPA?",
                        "activity": {
                            "type": "gpa_calculator",
                            "courses": [
                                ("Language Arts 9", "B+", "1.0", "standard"),
                                ("Human Geography & Ethnic Studies", "A-", "1.0", "standard"),
                                ("Geometry", "B", "1.0", "standard"),
                                ("Earth & Space Science", "B-", "1.0", "standard"),
                                ("Warrior Seminar", "A", "0.5", "standard"),
                                ("Woodworking I", "A", "0.5", "standard"),
                                ("Intro to Organized Sports", "B+", "0.5", "standard"),
                            ],
                        },
                    },
                    {
                        "heading": "Habits That Protect Your GPA",
                        "body": "Review the list below. Check the habits you already have. Circle the ones you want to build.",
                        "activity": {
                            "type": "habits_checklist",
                            "items": [
                                "I turn in all assignments on time.",
                                "I use a planner to track due dates.",
                                "I check my grades in Infinite Campus at least once a week.",
                                "I ask for help before I fall too far behind.",
                                "I use Warrior Time (Wednesday) to catch up or get ahead.",
                                "I study over multiple days, not just the night before.",
                                "I communicate with my teacher if I need an extension.",
                                "I read feedback on returned work and apply it next time.",
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "quick_write",
                    "prompt": "If your goal is a 3.5 GPA in 9th grade, what does that mean in real terms (what grades do you need)? What is the single most important habit you will commit to in order to reach that goal?",
                    "lines": 4,
                },
            },
            {
                "number": 2,
                "title": "Getting Involved at TRHS",
                "lesson_label": "5.2",
                "scaffolding": 4,
                "objectives": [
                    "Explain the connection between extracurricular involvement and academic and social well-being.",
                    "Develop a personal strategy for trying new activities while maintaining academic balance.",
                    "Identify at least one activity, one club/service group, and one sport they plan to explore.",
                ],
                "vocab_focus": {
                    "word": "BARR (Building Assets, Reducing Risks)",
                    "etymology": "Acronym for Building Assets, Reducing Risks — a model of structured team support for 9th graders",
                    "definition": "A TRHS program that places every 9th grader on a small team of teachers who regularly communicate to support their success."
                },
                "cornell_questions": [
                    "What does BARR mean for 9th graders?",
                    "Why do activities improve academic performance?",
                    "How do I decide what to join without overcommitting?",
                    "How do I find out about try-outs and sign-ups?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "The BARR Advantage",
                        "body": (
                            "One of the best things about starting at TRHS is BARR. As a 9th grader, you will be "
                            "assigned to a team of 3-4 teachers who have ALL of your classmates in at least one class. "
                            "These teachers meet regularly to talk about how their students are doing — academically, "
                            "socially, emotionally. If you're struggling, your BARR teacher will notice and reach out. "
                            "If you're thriving, they'll know that too. You are NOT going to fall through the cracks "
                            "at TRHS — the structure won't let you, as long as you show up."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "The 'Try One Thing' Challenge",
                        "body": (
                            "Research on high school students shows that students who are involved in at least one "
                            "extracurricular activity are significantly more likely to feel connected to school and "
                            "graduate on time. The challenge: pick at least ONE thing you've never done before and "
                            "commit to trying it in the first semester. It doesn't have to be the thing you stick with "
                            "forever — it just has to get you in the door."
                        ),
                        "activity": {
                            "type": "commitment_card",
                            "fields": [
                                "I commit to trying: ___________",
                                "Why I chose it: ___________",
                                "When sign-ups/try-outs happen: ___________",
                                "Someone I will do it with (or go alone — that's brave too): ___________",
                            ],
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "reflection_scale",
                    "prompt": "How confident do you feel about getting involved at TRHS? (1 = not confident at all, 5 = very confident). Explain what would help you feel more confident.",
                    "lines": 3,
                },
            },
            {
                "number": 3,
                "title": "Finalizing My Fall Schedule",
                "lesson_label": "5.3",
                "scaffolding": 4,
                "objectives": [
                    "Review and finalize their mock 9th grade course schedule.",
                    "Identify 2–3 alternate course selections in case first choices are unavailable.",
                    "Write a brief course rationale explaining their scheduling choices.",
                ],
                "vocab_focus": {
                    "word": "Transcript",
                    "etymology": "Latin transcribere (to copy over) — trans (across) + scribere (to write)",
                    "definition": "Your permanent academic record — every course, every grade, every credit, from 9th grade through graduation."
                },
                "cornell_questions": [
                    "Why do I need alternate course selections?",
                    "What is a course rationale?",
                    "How does my schedule connect to my transcript?",
                    "What do I do if I don't like a course?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Your Schedule is Your Foundation",
                        "body": (
                            "The courses you take in 9th grade are the foundation of your high school transcript. "
                            "They determine which courses you can take in 10th grade (because of prerequisites), "
                            "how your GPA starts, and how your interests develop. At TRHS, all registrations are "
                            "considered final after submission — so it is critical to think carefully about your "
                            "choices now. You must also identify alternate courses in case your first choice is "
                            "unavailable. This is not a punishment — it's smart planning."
                        ),
                        "activity": None,
                    },
                    {
                        "heading": "Finalize & Justify Your Schedule",
                        "body": "Complete the final schedule below. For each course choice, write ONE sentence explaining why you chose it. Then identify an alternate for each elective slot.",
                        "activity": {
                            "type": "final_schedule_with_rationale",
                            "periods": 7,
                            "include_alternates": True,
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "three_two_one",
                    "prompts": [
                        "3 courses I am taking in 9th grade and why I chose each:",
                        "2 things I am doing to prepare for my most challenging course:",
                        "1 alternate course I identified and why:",
                    ],
                },
            },
            {
                "number": 4,
                "title": "TRHS Student Panel",
                "lesson_label": "5.4",
                "scaffolding": 4,
                "objectives": [
                    "Generate thoughtful, specific questions for current TRHS students.",
                    "Actively listen and take notes during the student panel.",
                    "Synthesize panel insights into personal action steps for 9th grade.",
                ],
                "vocab_focus": {
                    "word": "Concurrent Enrollment (CE)",
                    "etymology": "Latin concurrere (to run together) + Latin enrollare (to enter on a roll/list)",
                    "definition": "A high school course that also earns college credit — you start building your college transcript while still in high school."
                },
                "cornell_questions": [
                    "What do I want to know from current HS students?",
                    "What surprised me about the panel?",
                    "What is one thing I will do differently because of what I heard?",
                    "What questions do I still have?",
                ],
                "prefilled_notes": "",
                "content_sections": [
                    {
                        "heading": "Preparing Your Questions",
                        "body": (
                            "Great questions lead to great answers. Before the panel begins, write down at least FIVE "
                            "questions you genuinely want answered by current Two Rivers students. Think about: academics, "
                            "social life, activities, what surprised them, what they wish they had known, what advice they "
                            "have for you. The best questions are specific, not generic. 'What's high school like?' "
                            "will get a vague answer. 'What did you do when you got your first bad grade?' will get a real one."
                        ),
                        "activity": {
                            "type": "question_prep",
                            "lines_per_question": 2,
                            "num_questions": 5,
                        },
                    },
                    {
                        "heading": "Panel Notes",
                        "body": "Use this space to take notes during the student panel. Write the speaker's name (or 'Student A, B, C...') and the key ideas you want to remember.",
                        "activity": {
                            "type": "panel_notes",
                            "lines": 18,
                        },
                    },
                ],
                "exit_ticket": {
                    "type": "synthesis_write",
                    "prompt": (
                        "Write a paragraph (5–7 sentences) in response to this prompt: "
                        "What is the MOST important thing you heard from the panel today, and how will it change "
                        "how you approach 9th grade? Be specific — reference what was actually said."
                    ),
                    "lines": 7,
                },
            },
        ],
    },
]

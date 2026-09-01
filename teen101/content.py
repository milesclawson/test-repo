"""
Teenager 101 -- Friendly Hills Middle School
Course content as structured data: units, lessons, vocabulary, Cornell notes
cues, and exit tickets. Used by build_workbook.py and build_slides.py.

Currently scoped to UNIT 1 (Basic Life Skills, lessons 1.1-1.4) as a pilot.
Extend the UNITS list with the same shape to add Units 2-6.
"""

SCHOOL_NAME = "Friendly Hills Middle School"
COURSE_TITLE = "Teenager 101"
MASCOT = "Warriors"

# Brand colors (hex, no #) -- match index.html :root variables
RED = "C41230"
RED_DK = "8B0000"
RED_LT = "FDECEA"
GOLD = "F5B800"
GOLD_LT = "FFF8E1"
GOLD_DK = "B8860B"
GRAY = "F4F4F4"
BORDER = "E0E0E0"
INK = "222222"
MUTED = "666666"

# ---------------------------------------------------------------------------
# UNITS
# ---------------------------------------------------------------------------
# Each lesson has:
#   label, title, key_topics, objectives (list), vocabulary (list of
#   {word, definition}), cornell_questions (cue-column prompts for notes),
#   exit_ticket (single prompt string)

UNITS = [
    {
        "number": 1,
        "name": "Basic Life Skills",
        "overview": (
            "Students learn the household skills their parents wish they'd been taught "
            "earlier. From reading a laundry label to sewing on a button, this unit builds "
            "independence and confidence at home."
        ),
        "lessons": [
            {
                "label": "1.1",
                "title": "Laundry Basics",
                "key_topics": "Sort colors, read care labels, wash/dry cycles",
                "objectives": [
                    "Sort a mixed load of laundry correctly by color and fabric type.",
                    "Read and interpret common care-label symbols.",
                    "Choose the correct wash cycle and water temperature for a given load.",
                ],
                "vocabulary": [
                    {"word": "Care label", "definition": "The tag inside a clothing item that tells you how to safely wash, dry, and iron it."},
                    {"word": "Colorfast", "definition": "A fabric that keeps its dye and won't bleed color onto other clothes in the wash."},
                    {"word": "Agitation", "definition": "The washing machine's tumbling/spinning motion that works detergent through the fabric."},
                    {"word": "Detergent dose", "definition": "The correct amount of soap for a load, based on load size and water hardness -- too much leaves residue."},
                ],
                "cornell_questions": [
                    "Why sort by color before washing?",
                    "What do the 3 most common care-label symbols mean?",
                    "Hot, warm, or cold -- when do you use each?",
                    "What happens if you overload the washer?",
                ],
                "exit_ticket": "You have one red t-shirt, three white socks, and a pair of jeans. Which items go in the same load, and what water temperature would you pick? Explain your reasoning in 2-3 sentences.",
            },
            {
                "label": "1.2",
                "title": "Basic Sewing & Mending",
                "key_topics": "Thread a needle, sew a button, patch a hole",
                "objectives": [
                    "Thread a needle and tie a secure knot.",
                    "Sew a four-hole button back onto fabric so it won't fall off again.",
                    "Patch a small hole or seam using a basic running stitch.",
                ],
                "vocabulary": [
                    {"word": "Running stitch", "definition": "A simple in-and-out stitch used to close a seam or patch fabric."},
                    {"word": "Shank", "definition": "A small thread stem left under a button so it can move freely without popping the fabric."},
                    {"word": "Seam", "definition": "The line where two pieces of fabric are stitched together."},
                    {"word": "Mending", "definition": "Repairing torn, ripped, or loose clothing instead of throwing it away."},
                ],
                "cornell_questions": [
                    "What are the steps to thread a needle?",
                    "Why does a sewn-on button need a shank?",
                    "What is a running stitch used for?",
                    "Why mend clothes instead of replacing them?",
                ],
                "exit_ticket": "A button just fell off your favorite jacket. Write out, in order, the steps you'd take to sew it back on.",
            },
            {
                "label": "1.3",
                "title": "Dishes & Kitchen Cleaning",
                "key_topics": "Proper washing order, sanitizing, drying",
                "objectives": [
                    "Wash dishes in the correct order to avoid cross-contamination.",
                    "Explain why hot water and dish soap sanitize surfaces.",
                    "Properly dry and store clean dishes.",
                ],
                "vocabulary": [
                    {"word": "Cross-contamination", "definition": "When bacteria from one surface (like a cutting board used for raw chicken) spreads to another surface or food."},
                    {"word": "Sanitize", "definition": "To reduce germs on a surface to a safe level, usually with heat or a cleaning chemical."},
                    {"word": "Grease cutting", "definition": "The ability of dish soap to break down fat and oil so it rinses away instead of sticking."},
                    {"word": "Air dry", "definition": "Letting dishes dry naturally in a rack instead of towel-drying them, which reduces germ transfer."},
                ],
                "cornell_questions": [
                    "What's the correct order to wash dishes in and why?",
                    "How does soap actually remove grease?",
                    "What is cross-contamination and how do you avoid it?",
                    "Why is air drying better than a dish towel?",
                ],
                "exit_ticket": "You just cooked dinner and have a greasy pan, two drinking glasses, and a cutting board that had raw chicken on it. What order do you wash them in, and why does the order matter?",
            },
            {
                "label": "1.4",
                "title": "Home Organization",
                "key_topics": "Declutter, storage systems, daily routines",
                "objectives": [
                    "Apply a simple decision rule to decide what to keep, donate, or toss.",
                    "Design a storage system for a small space.",
                    "Build a daily routine that keeps a room from becoming cluttered again.",
                ],
                "vocabulary": [
                    {"word": "Declutter", "definition": "The process of removing items you don't need, use, or want from a space."},
                    {"word": "Zone", "definition": "A defined area of a room dedicated to one purpose, like a homework zone or a charging zone."},
                    {"word": "Maintenance habit", "definition": "A small, repeated action (like a 5-minute nightly reset) that keeps a space organized long-term."},
                    {"word": "Storage system", "definition": "A consistent way of grouping and containing items so everything has a 'home.'"},
                ],
                "cornell_questions": [
                    "What questions help you decide keep vs. donate vs. toss?",
                    "What does it mean to give a room 'zones'?",
                    "Why do maintenance habits matter more than one big cleanup?",
                    "What's one realistic daily routine you could actually stick to?",
                ],
                "exit_ticket": "Pick one real space in your room that's currently cluttered. Name the space, and write one specific change you could make this week to organize it.",
            },
        ],
    },
    {
        "number": 2,
        "name": "Basic Gardening",
        "overview": (
            "Students learn where food actually comes from and how to grow it. The unit follows the "
            "full gardening lifecycle: planning the bed, building healthy soil, composting, planting, "
            "managing pests, watering efficiently, and harvesting at the right time. The unit "
            "culminates in building a real or simulated garden bed."
        ),
        "lessons": [
            {
                "label": "2.1",
                "title": "Garden Planning",
                "key_topics": "Site selection, layout, what to grow",
                "objectives": [
                    "Evaluate a location for sun exposure, drainage, and access to water.",
                    "Choose plants appropriate for the local growing season and available space.",
                    "Sketch a basic garden layout using correct plant spacing.",
                ],
                "vocabulary": [
                    {"word": "Full sun", "definition": "An area that receives at least 6 hours of direct sunlight per day -- required by most vegetables."},
                    {"word": "Site selection", "definition": "The process of choosing where to put a garden based on sunlight, drainage, and access to water."},
                    {"word": "Growing season", "definition": "The period between the last spring frost and the first fall frost when plants can safely grow outdoors."},
                ],
                "cornell_questions": [
                    "What does a garden site need to succeed?",
                    "How much sun do most vegetables need?",
                    "Why does drainage matter for plant roots?",
                    "How do you decide what to plant where?",
                ],
                "exit_ticket": "Describe a real spot (your yard, a school courtyard, a windowsill) and evaluate it as a garden site: how much sun does it get, and what would you plant there?",
            },
            {
                "label": "2.2",
                "title": "Soil Science",
                "key_topics": "Soil types, pH, amendments, nutrients",
                "objectives": [
                    "Identify the three basic soil types and their properties.",
                    "Explain what soil pH measures and why it matters for plant health.",
                    "Describe how amendments improve soil quality.",
                ],
                "vocabulary": [
                    {"word": "pH", "definition": "A scale from 0-14 measuring how acidic or alkaline soil is; most vegetables prefer 6.0-7.0."},
                    {"word": "Amendment", "definition": "Any material (like compost or lime) added to soil to improve its structure or nutrient content."},
                    {"word": "Loam", "definition": "A balanced mix of sand, silt, and clay considered ideal for gardening."},
                ],
                "cornell_questions": [
                    "What are the three basic soil types?",
                    "What does soil pH tell you?",
                    "What's an amendment and why add one?",
                    "What does 'loam' mean and why is it ideal?",
                ],
                "exit_ticket": "If a soil test showed your garden's pH was too acidic for tomatoes, what would you do about it, based on today's lesson?",
            },
            {
                "label": "2.3",
                "title": "Composting",
                "key_topics": "Browns vs. greens, bin setup, troubleshooting",
                "objectives": [
                    "Explain the difference between 'browns' and 'greens' in composting.",
                    "Set up and maintain a basic compost bin.",
                    "Diagnose and fix common compost problems (smell, no heat, pests).",
                ],
                "vocabulary": [
                    {"word": "Browns", "definition": "Carbon-rich compost materials like dry leaves, cardboard, and straw."},
                    {"word": "Greens", "definition": "Nitrogen-rich compost materials like fruit scraps, coffee grounds, and grass clippings."},
                    {"word": "Decomposition", "definition": "The natural breakdown of organic material by microbes, fungi, and insects into usable soil nutrients."},
                ],
                "cornell_questions": [
                    "What's the difference between browns and greens?",
                    "What ratio of browns to greens works best?",
                    "Why does a compost pile need air and water?",
                    "What causes a compost pile to smell bad?",
                ],
                "exit_ticket": "Your compost pile smells terrible. Based on today's lesson, what's most likely wrong and how would you fix it?",
            },
            {
                "label": "2.4",
                "title": "Planting Seeds & Starts",
                "key_topics": "Seed depth, spacing, transplant shock",
                "objectives": [
                    "Determine correct planting depth and spacing for common seeds.",
                    "Explain the difference between direct-sowing and using starts.",
                    "Describe how to minimize transplant shock.",
                ],
                "vocabulary": [
                    {"word": "Direct sow", "definition": "Planting seeds straight into the garden soil instead of starting them indoors."},
                    {"word": "Transplant shock", "definition": "The stress a plant experiences when moved from one growing environment to another, often causing wilting."},
                    {"word": "Hardening off", "definition": "Gradually exposing indoor-started seedlings to outdoor conditions before transplanting."},
                ],
                "cornell_questions": [
                    "How do you know how deep to plant a seed?",
                    "What's the difference between direct sowing and starts?",
                    "What causes transplant shock?",
                    "What does 'hardening off' mean and why do it?",
                ],
                "exit_ticket": "You have tomato starts ready to go in the ground. Describe the steps you'd take to transplant them with the least shock possible.",
            },
            {
                "label": "2.5",
                "title": "Pests & Plant Health",
                "key_topics": "Identify pests, organic solutions, companion planting",
                "objectives": [
                    "Identify common garden pests and the damage they cause.",
                    "Describe at least two organic pest-control methods.",
                    "Explain how companion planting can reduce pest problems.",
                ],
                "vocabulary": [
                    {"word": "Companion planting", "definition": "Growing certain plants near each other because they help one another repel pests, improve growth, or use space well."},
                    {"word": "Organic pest control", "definition": "Managing pests without synthetic chemical pesticides, using methods like insecticidal soap, row covers, or beneficial insects."},
                    {"word": "Beneficial insect", "definition": "An insect, like a ladybug, that helps a garden by eating pests or pollinating plants."},
                ],
                "cornell_questions": [
                    "What signs tell you a pest is damaging a plant?",
                    "Name two organic ways to control pests.",
                    "What is companion planting?",
                    "Give one example of a helpful plant pairing.",
                ],
                "exit_ticket": "Your bean plants have holes in the leaves and you spot small green bugs on the underside. What's your organic plan to deal with it?",
            },
            {
                "label": "2.6",
                "title": "Watering & Irrigation",
                "key_topics": "Watering schedules, deep vs. shallow, drought signs",
                "objectives": [
                    "Explain the difference between deep and shallow watering and why deep watering is usually better.",
                    "Recognize signs of both underwatering and overwatering.",
                    "Design a simple watering schedule for a home garden.",
                ],
                "vocabulary": [
                    {"word": "Deep watering", "definition": "Watering slowly and thoroughly so moisture reaches deep into the soil, encouraging strong root growth."},
                    {"word": "Irrigation", "definition": "Any method of supplying water to plants, from a hose to a drip system."},
                    {"word": "Drought stress", "definition": "Visible signs a plant is not getting enough water, like wilting or curling leaves."},
                ],
                "cornell_questions": [
                    "Why is deep watering usually better than shallow, frequent watering?",
                    "What are signs of underwatering?",
                    "What are signs of overwatering?",
                    "What time of day is best to water, and why?",
                ],
                "exit_ticket": "Your garden's leaves are yellowing and the soil feels soggy. Is this a sign of underwatering or overwatering, and what would you change?",
            },
            {
                "label": "2.7",
                "title": "Harvesting",
                "key_topics": "When to pick, how to pick, storing produce",
                "objectives": [
                    "Identify ripeness cues for common garden vegetables.",
                    "Use correct techniques to harvest without damaging the plant.",
                    "Store harvested produce to maximize freshness.",
                ],
                "vocabulary": [
                    {"word": "Ripeness cue", "definition": "A visible or tactile sign (color, firmness, size) that tells you produce is ready to pick."},
                    {"word": "Succession harvest", "definition": "Picking a crop like lettuce or beans repeatedly over time instead of all at once."},
                    {"word": "Curing", "definition": "Letting certain vegetables (like squash or onions) sit in a dry, ventilated place after harvest to extend storage life."},
                ],
                "cornell_questions": [
                    "How do you know when a vegetable is ready to pick?",
                    "Why does technique matter when harvesting?",
                    "What is a succession harvest?",
                    "How should different produce be stored after picking?",
                ],
                "exit_ticket": "You're not sure if your zucchini is ready to pick. What ripeness cues would you check, based on today's lesson?",
            },
            {
                "label": "2.8",
                "title": "Build a Garden Bed",
                "key_topics": "Raised bed construction, first planting day",
                "objectives": [
                    "Explain the benefits of a raised garden bed over an in-ground plot.",
                    "Describe the basic steps to construct a raised bed.",
                    "Apply everything learned this unit to plan a first planting day.",
                ],
                "vocabulary": [
                    {"word": "Raised bed", "definition": "A garden plot built above ground level, contained by a frame, filled with soil."},
                    {"word": "Soil depth", "definition": "How many inches of growing soil a bed needs for healthy root development, usually at least 8-12 inches."},
                    {"word": "Planting plan", "definition": "A map of what will be planted where, based on spacing, sun, and companion planting."},
                ],
                "cornell_questions": [
                    "What are the benefits of a raised bed?",
                    "What materials are commonly used to build one?",
                    "How much soil depth do most vegetables need?",
                    "What goes into a planting-day checklist?",
                ],
                "exit_ticket": "You're building your first raised bed this weekend. List three things from this unit you'll make sure to get right.",
            },
        ],
    },
    {
        "number": 3,
        "name": "Personal Finance & Time Management",
        "overview": (
            "Students learn how money works before they earn their first paycheck. The unit covers "
            "how marketers manipulate spending, the difference between needs and wants, building a "
            "real budget, saving strategies, time management, resume writing, job searching, and "
            "interview skills."
        ),
        "lessons": [
            {
                "label": "3.1",
                "title": "How Marketing Works",
                "key_topics": "Advertising tactics, emotional buying, brand loyalty",
                "objectives": [
                    "Identify common advertising tactics used to influence buying decisions.",
                    "Explain the difference between rational and emotional buying.",
                    "Describe how brand loyalty is built and why companies invest in it.",
                ],
                "vocabulary": [
                    {"word": "Target audience", "definition": "The specific group of people an advertisement is designed to appeal to."},
                    {"word": "Emotional buying", "definition": "Making a purchase decision based on feelings (fear of missing out, excitement, belonging) rather than need."},
                    {"word": "Brand loyalty", "definition": "A consumer's tendency to keep buying from the same company instead of comparing alternatives."},
                ],
                "cornell_questions": [
                    "What are common tactics advertisers use?",
                    "What's the difference between emotional and rational buying?",
                    "How do companies build brand loyalty?",
                    "How can you protect yourself from manipulative ads?",
                ],
                "exit_ticket": "Think of an ad you've seen recently. What tactic did it use, and what emotion was it trying to trigger?",
            },
            {
                "label": "3.2",
                "title": "Needs vs. Wants",
                "key_topics": "Maslow's hierarchy, opportunity cost, impulse buying",
                "objectives": [
                    "Distinguish between needs and wants using Maslow's hierarchy.",
                    "Explain opportunity cost using a real spending example.",
                    "Identify triggers for impulse buying and one strategy to resist them.",
                ],
                "vocabulary": [
                    {"word": "Opportunity cost", "definition": "The value of the next-best option you give up when you choose to spend money or time on something else."},
                    {"word": "Impulse buying", "definition": "Making an unplanned purchase decision in the moment, often driven by emotion."},
                    {"word": "Hierarchy of needs", "definition": "Maslow's theory ranking human needs from basic survival (food, shelter) up to higher goals like self-esteem."},
                ],
                "cornell_questions": [
                    "What's the difference between a need and a want?",
                    "What does opportunity cost mean?",
                    "What triggers impulse buying?",
                    "What's one strategy to resist an impulse buy?",
                ],
                "exit_ticket": "You have $40. Name one need and one want you could spend it on, and explain the opportunity cost of choosing one over the other.",
            },
            {
                "label": "3.3",
                "title": "Building a Budget",
                "key_topics": "50/30/20 rule, tracking spending, adjusting",
                "objectives": [
                    "Apply the 50/30/20 rule to a sample income.",
                    "Track spending across at least three categories.",
                    "Adjust a budget in response to overspending in one category.",
                ],
                "vocabulary": [
                    {"word": "Budget", "definition": "A plan for how you'll spend and save your income over a set period of time."},
                    {"word": "Fixed expense", "definition": "A cost that stays roughly the same each month, like a phone bill."},
                    {"word": "Discretionary spending", "definition": "Money spent on non-essential wants, like entertainment or eating out."},
                ],
                "cornell_questions": [
                    "What does the 50/30/20 rule recommend?",
                    "What's the difference between a fixed and variable expense?",
                    "Why track spending instead of just estimating?",
                    "What do you do when you overspend in one category?",
                ],
                "exit_ticket": "You earn $100 a month from a part-time job. Using the 50/30/20 rule, sketch out how you'd divide it.",
            },
            {
                "label": "3.4",
                "title": "Saving & Compound Interest",
                "key_topics": "Pay yourself first, interest, saving goals",
                "objectives": [
                    "Explain the 'pay yourself first' saving strategy.",
                    "Describe how compound interest grows savings over time.",
                    "Set a specific, realistic savings goal.",
                ],
                "vocabulary": [
                    {"word": "Pay yourself first", "definition": "Setting aside savings immediately when you get money, before spending on anything else."},
                    {"word": "Compound interest", "definition": "Interest calculated on both the original amount saved and the interest it has already earned."},
                    {"word": "Principal", "definition": "The original amount of money saved or invested, before interest is added."},
                ],
                "cornell_questions": [
                    "What does 'pay yourself first' mean?",
                    "How is compound interest different from simple interest?",
                    "Why does starting to save early matter so much?",
                    "What makes a savings goal realistic?",
                ],
                "exit_ticket": "If you saved $10 a month starting today, what's one specific goal you'd be saving toward, and roughly how long would it take?",
            },
            {
                "label": "3.5",
                "title": "Time Management",
                "key_topics": "Priority matrix, scheduling, avoiding procrastination",
                "objectives": [
                    "Sort tasks using an urgent/important priority matrix.",
                    "Build a realistic weekly schedule.",
                    "Identify a personal procrastination trigger and one strategy to counter it.",
                ],
                "vocabulary": [
                    {"word": "Priority matrix", "definition": "A tool for sorting tasks into four categories based on urgency and importance."},
                    {"word": "Procrastination", "definition": "Delaying a task you know you should be doing, usually in favor of something easier or more enjoyable."},
                    {"word": "Time block", "definition": "A specific chunk of time set aside in a schedule for one task or activity."},
                ],
                "cornell_questions": [
                    "What are the four categories in a priority matrix?",
                    "How is 'urgent' different from 'important'?",
                    "What usually causes procrastination?",
                    "What's one strategy to beat procrastination?",
                ],
                "exit_ticket": "List three things you need to do this week and sort them into urgent/important categories using today's matrix.",
            },
            {
                "label": "3.6",
                "title": "Writing a Resume",
                "key_topics": "Format, action verbs, what to include at 14-15",
                "objectives": [
                    "Identify the standard sections of a resume.",
                    "Use action verbs to describe experience and skills.",
                    "Determine what a 14-15 year old can realistically include on a first resume.",
                ],
                "vocabulary": [
                    {"word": "Resume", "definition": "A short document summarizing your skills, experience, and education for a potential employer."},
                    {"word": "Action verb", "definition": "A strong verb (organized, led, built) used to describe accomplishments on a resume."},
                    {"word": "Transferable skill", "definition": "A skill learned in one setting (like babysitting or sports) that applies to a job in a different setting."},
                ],
                "cornell_questions": [
                    "What sections belong on a resume?",
                    "Why use action verbs instead of plain descriptions?",
                    "What's a transferable skill? Give an example.",
                    "What can a 14-15 year old realistically list with no work history yet?",
                ],
                "exit_ticket": "List two transferable skills you already have (from school, sports, chores, or volunteering) that could go on a first resume.",
            },
            {
                "label": "3.7",
                "title": "Job Search Skills",
                "key_topics": "Where to look, applications, references",
                "objectives": [
                    "Identify realistic places a teenager can look for a first job.",
                    "Complete a sample job application accurately and professionally.",
                    "Explain what makes someone a good reference.",
                ],
                "vocabulary": [
                    {"word": "Reference", "definition": "A person who can vouch for your character and reliability to a potential employer."},
                    {"word": "Application", "definition": "The form or process used to formally request consideration for a job."},
                    {"word": "Work permit", "definition": "Official documentation some states require for minors to legally work."},
                ],
                "cornell_questions": [
                    "Where can a 14-15 year old realistically look for work?",
                    "What information does a typical job application ask for?",
                    "Who makes a good reference, and who should you avoid asking?",
                    "What is a work permit and when might you need one?",
                ],
                "exit_ticket": "Name two people you could ask to be a reference, and explain why each would speak well of you.",
            },
            {
                "label": "3.8",
                "title": "Interview Skills",
                "key_topics": "Common questions, body language, thank-you notes",
                "objectives": [
                    "Prepare answers for common interview questions.",
                    "Demonstrate confident, professional body language.",
                    "Write a brief thank-you note after a mock interview.",
                ],
                "vocabulary": [
                    {"word": "Elevator pitch", "definition": "A short, prepared summary of who you are and what you offer, deliverable in about 30 seconds."},
                    {"word": "Body language", "definition": "Nonverbal communication -- posture, eye contact, handshake -- that shapes a first impression."},
                    {"word": "Follow-up", "definition": "A message sent after an interview, usually to say thank you and reaffirm interest."},
                ],
                "cornell_questions": [
                    "What are common interview questions to prepare for?",
                    "What body language signals confidence?",
                    "Why send a thank-you note after an interview?",
                    "What should an elevator pitch include?",
                ],
                "exit_ticket": "Write a 2-3 sentence answer to the interview question: 'Why should we hire you?'",
            },
        ],
    },
    {
        "number": 4,
        "name": "Basic Home Repair",
        "overview": (
            "Students learn to identify and safely use common tools, patch walls, fix a leaky faucet, "
            "replace a light switch, and maintain a bike. Each lesson emphasizes safety protocols "
            "before touching any tool."
        ),
        "lessons": [
            {
                "label": "4.1",
                "title": "Tools & Safety",
                "key_topics": "Identify tools, PPE, tool safety rules",
                "objectives": [
                    "Identify common hand tools and their correct use.",
                    "Explain why personal protective equipment (PPE) matters for home repair.",
                    "State the core safety rules for working with tools.",
                ],
                "vocabulary": [
                    {"word": "PPE", "definition": "Personal Protective Equipment -- gear like safety glasses or gloves that protects you while working."},
                    {"word": "Torque", "definition": "The rotational force applied when turning a tool like a screwdriver or wrench."},
                    {"word": "Tool safety rule", "definition": "A guideline (like always cutting away from your body) that prevents injury when using tools."},
                ],
                "cornell_questions": [
                    "What are five common hand tools and their uses?",
                    "What PPE should you wear for basic repairs?",
                    "What's the golden rule for tool safety?",
                    "What should you do with a tool you don't recognize?",
                ],
                "exit_ticket": "Name one tool from today's lesson, what it's used for, and one safety rule you'd follow while using it.",
            },
            {
                "label": "4.2",
                "title": "Patching & Painting",
                "key_topics": "Spackle, sand, prime, paint walls",
                "objectives": [
                    "Patch a small hole in drywall using spackle.",
                    "Sand and prime a patched surface before painting.",
                    "Apply paint evenly using correct technique.",
                ],
                "vocabulary": [
                    {"word": "Spackle", "definition": "A putty-like compound used to fill small holes and cracks in walls before painting."},
                    {"word": "Primer", "definition": "A preparatory coating applied before paint to help it stick evenly and cover better."},
                    {"word": "Drywall", "definition": "The panel material most interior walls are made of."},
                ],
                "cornell_questions": [
                    "What are the steps to patch a small hole?",
                    "Why sand a patch before painting it?",
                    "What does primer do that paint alone doesn't?",
                    "What's good painting technique?",
                ],
                "exit_ticket": "Put these in the correct order: paint, sand, spackle, prime. Explain why the order matters.",
            },
            {
                "label": "4.3",
                "title": "Basic Plumbing",
                "key_topics": "Unclog drains, fix running toilets, shut-off valves",
                "objectives": [
                    "Unclog a slow drain using a safe, non-chemical method.",
                    "Diagnose and fix a common cause of a running toilet.",
                    "Locate and use a shut-off valve in an emergency.",
                ],
                "vocabulary": [
                    {"word": "Shut-off valve", "definition": "A valve that stops water flow to a fixture, used in plumbing emergencies."},
                    {"word": "Flapper valve", "definition": "The rubber piece inside a toilet tank that seals the drain -- a common cause of running toilets when worn out."},
                    {"word": "P-trap", "definition": "The curved pipe under a sink that holds water to block sewer gas and often catches clogs."},
                ],
                "cornell_questions": [
                    "What's a safe first step for a clogged drain?",
                    "What usually causes a toilet to keep running?",
                    "Where do you find a shut-off valve, and when would you use one?",
                    "What is a P-trap and why does it matter?",
                ],
                "exit_ticket": "A toilet won't stop running. Based on today's lesson, what's the most likely cause and what would you check first?",
            },
            {
                "label": "4.4",
                "title": "Basic Electrical (Safe)",
                "key_topics": "Replace outlets/switches, circuit breaker, never touch live wires",
                "objectives": [
                    "Explain how to safely shut off power before any electrical work.",
                    "Describe the steps to replace a light switch or outlet cover.",
                    "State the non-negotiable safety rule for working with electricity.",
                ],
                "vocabulary": [
                    {"word": "Circuit breaker", "definition": "A safety switch in the electrical panel that cuts power to a circuit to prevent overload or fire."},
                    {"word": "Live wire", "definition": "A wire currently carrying electrical current -- never to be touched without confirming power is off."},
                    {"word": "Voltage tester", "definition": "A tool used to confirm a wire or outlet has no electrical current before working on it."},
                ],
                "cornell_questions": [
                    "What's the very first step before any electrical work?",
                    "How do you find and use the circuit breaker panel?",
                    "What is a voltage tester used for?",
                    "What is the one rule you never break with electricity?",
                ],
                "exit_ticket": "Before replacing a light switch, list the exact safety steps you'd take in order, starting with the circuit breaker.",
            },
            {
                "label": "4.5",
                "title": "Bike Repair & Maintenance",
                "key_topics": "Fix a flat, adjust brakes, chain lubrication",
                "objectives": [
                    "Repair or replace a flat bike tire.",
                    "Adjust brakes for proper stopping performance.",
                    "Clean and lubricate a bike chain correctly.",
                ],
                "vocabulary": [
                    {"word": "Inner tube", "definition": "The inflatable rubber tube inside a bike tire that holds air."},
                    {"word": "Brake pad", "definition": "The part of a brake that presses against the wheel rim to slow the bike."},
                    {"word": "Chain lubrication", "definition": "Applying oil to a bike chain to reduce friction and prevent rust."},
                ],
                "cornell_questions": [
                    "What are the steps to fix a flat tire?",
                    "How do you know if brakes need adjusting?",
                    "Why does a chain need regular lubrication?",
                    "What tools does basic bike maintenance require?",
                ],
                "exit_ticket": "Your bike brakes feel loose and don't stop you quickly. What would you check and adjust, based on today's lesson?",
            },
        ],
    },
    {
        "number": 5,
        "name": "Babysitting 101",
        "overview": (
            "One of the most popular first jobs for teenagers -- and one where real safety knowledge "
            "matters. Students practice emergency scenarios, learn age-appropriate child development, "
            "and build the business skills to market themselves and get hired."
        ),
        "lessons": [
            {
                "label": "5.1",
                "title": "Business & Leadership",
                "key_topics": "Rates, marketing, client agreements, professionalism",
                "objectives": [
                    "Set a fair, competitive babysitting rate.",
                    "Create a simple flyer or pitch to market babysitting services.",
                    "Explain what belongs in a client agreement before the first job.",
                ],
                "vocabulary": [
                    {"word": "Client agreement", "definition": "A simple written or verbal understanding covering rate, hours, expectations, and emergency contacts before a job."},
                    {"word": "Professionalism", "definition": "Reliable, respectful, responsible behavior that builds trust with clients."},
                    {"word": "Rate", "definition": "The amount charged per hour (or per job) for babysitting services."},
                ],
                "cornell_questions": [
                    "How do you set a fair babysitting rate?",
                    "What belongs in a client agreement?",
                    "How can you market yourself as a babysitter?",
                    "What does professionalism look like on the job?",
                ],
                "exit_ticket": "Write out three questions you'd ask a parent before agreeing to babysit for the first time.",
            },
            {
                "label": "5.2",
                "title": "Home Safety Assessment",
                "key_topics": "Hazard checklist, emergency numbers, house rules",
                "objectives": [
                    "Complete a home safety walkthrough to identify hazards.",
                    "Gather emergency numbers and information before a job begins.",
                    "Explain why learning house rules matters before parents leave.",
                ],
                "vocabulary": [
                    {"word": "Hazard", "definition": "Anything in a home that could cause injury to a child, like an unlocked cabinet or an exposed outlet."},
                    {"word": "Emergency contact sheet", "definition": "A list of phone numbers (parents, poison control, a neighbor) kept accessible during a babysitting job."},
                    {"word": "House rules", "definition": "The specific expectations a family sets for behavior, screen time, food, and bedtime."},
                ],
                "cornell_questions": [
                    "What should a home safety walkthrough check for?",
                    "What belongs on an emergency contact sheet?",
                    "Why ask about house rules before parents leave?",
                    "What's one hazard many people overlook?",
                ],
                "exit_ticket": "List three hazards you'd check for during a home safety walkthrough before babysitting somewhere new.",
            },
            {
                "label": "5.3",
                "title": "Emergency Response",
                "key_topics": "When to call 911, choking, burns, falls, fire",
                "objectives": [
                    "Determine when a situation requires calling 911 versus a parent.",
                    "Describe the correct first response to choking, burns, falls, and fire.",
                    "Explain what information to give a 911 dispatcher.",
                ],
                "vocabulary": [
                    {"word": "911 dispatcher", "definition": "The emergency operator who answers 911 calls and sends help."},
                    {"word": "First response", "definition": "The immediate action taken in an emergency before professional help arrives."},
                    {"word": "Triage", "definition": "Quickly judging how serious a situation is to decide what to do first."},
                ],
                "cornell_questions": [
                    "When do you call 911 versus a parent first?",
                    "What's the first response to a choking child?",
                    "What's the first response to a small burn?",
                    "What information does a 911 dispatcher need?",
                ],
                "exit_ticket": "A child in your care falls and is holding their arm, crying, but breathing normally. Walk through what you'd do, in order.",
            },
            {
                "label": "5.4",
                "title": "Child Development: Ages 0-5",
                "key_topics": "Milestones, age-appropriate play, safe sleep",
                "objectives": [
                    "Identify developmental milestones for children ages 0-5.",
                    "Choose age-appropriate play activities for toddlers and preschoolers.",
                    "Explain safe sleep practices for infants.",
                ],
                "vocabulary": [
                    {"word": "Developmental milestone", "definition": "A skill or ability (like walking or first words) that most children reach around a certain age."},
                    {"word": "Safe sleep", "definition": "Guidelines (back to sleep, empty crib, firm mattress) that reduce the risk of infant sleep-related death."},
                    {"word": "Age-appropriate play", "definition": "Activities matched to a child's developmental stage -- neither too easy nor too advanced."},
                ],
                "cornell_questions": [
                    "What are a few milestones for a 2-year-old?",
                    "What makes an activity age-appropriate for a toddler?",
                    "What are the core safe sleep rules for infants?",
                    "Why does age-appropriate play matter for development?",
                ],
                "exit_ticket": "You're babysitting a 3-year-old for two hours. Name two age-appropriate activities you'd plan and why they fit.",
            },
            {
                "label": "5.5",
                "title": "Child Development: Ages 6-10",
                "key_topics": "Independence, peer dynamics, screen time",
                "objectives": [
                    "Describe how independence needs shift for children ages 6-10.",
                    "Explain how peer dynamics affect a school-age child's behavior.",
                    "Apply a reasonable approach to managing screen time.",
                ],
                "vocabulary": [
                    {"word": "Peer dynamics", "definition": "How a child's friendships and social relationships influence their mood and behavior."},
                    {"word": "Independence", "definition": "A child's growing ability and desire to do things without adult help."},
                    {"word": "Screen time limit", "definition": "A boundary set on how much time a child spends on devices or TV."},
                ],
                "cornell_questions": [
                    "How does independence show up differently at age 6-10 than at age 2-5?",
                    "How do peer dynamics affect a school-age child's mood?",
                    "What's a reasonable approach to screen time as a babysitter?",
                    "What should you do if a house rule conflicts with what a child asks for?",
                ],
                "exit_ticket": "An 8-year-old asks for 'just one more episode' past their screen-time limit. What would you say and do?",
            },
            {
                "label": "5.6",
                "title": "Feeding & Bedtime Routines",
                "key_topics": "Meal prep for kids, bedtime resistance, sleep safety",
                "objectives": [
                    "Prepare a simple, safe snack or meal for a child.",
                    "Describe strategies to handle bedtime resistance calmly.",
                    "Explain why consistency matters in a bedtime routine.",
                ],
                "vocabulary": [
                    {"word": "Bedtime resistance", "definition": "A child's pushback against going to sleep, often through stalling tactics."},
                    {"word": "Choking hazard", "definition": "A food or object small or shaped in a way that could block a young child's airway."},
                    {"word": "Routine consistency", "definition": "Following the same steps in the same order each night, which helps children feel secure and fall asleep more easily."},
                ],
                "cornell_questions": [
                    "What foods are common choking hazards for young kids?",
                    "What are calm strategies for bedtime resistance?",
                    "Why does routine consistency help kids sleep?",
                    "What should a basic bedtime routine include?",
                ],
                "exit_ticket": "A 4-year-old keeps getting out of bed asking for 'one more thing.' What calm, consistent strategy would you use?",
            },
            {
                "label": "5.7",
                "title": "First Aid Basics",
                "key_topics": "Cuts, burns, sprains, allergic reactions, epi-pen",
                "objectives": [
                    "Clean and bandage a minor cut correctly.",
                    "Apply first aid for a minor burn or sprain.",
                    "Recognize signs of a serious allergic reaction and know the basic epi-pen response.",
                ],
                "vocabulary": [
                    {"word": "Allergic reaction", "definition": "The body's immune response to a substance it treats as harmful, ranging from mild to life-threatening."},
                    {"word": "Anaphylaxis", "definition": "A severe, potentially life-threatening allergic reaction requiring immediate epinephrine and 911."},
                    {"word": "RICE method", "definition": "Rest, Ice, Compression, Elevation -- the basic first-aid approach to a sprain."},
                ],
                "cornell_questions": [
                    "What are the steps to clean and bandage a cut?",
                    "What is the RICE method used for?",
                    "What are signs of a serious allergic reaction?",
                    "What do you do if a child needs an epi-pen?",
                ],
                "exit_ticket": "A child scrapes their knee and it's bleeding lightly. Walk through the first-aid steps you'd take, in order.",
            },
            {
                "label": "5.8",
                "title": "Hands-Only CPR",
                "key_topics": "Rate, depth, AED basics, rescue breathing intro",
                "objectives": [
                    "Describe the correct rate and depth for hands-only CPR.",
                    "Explain when hands-only CPR is appropriate versus CPR with rescue breaths.",
                    "Identify the basic function of an AED.",
                ],
                "vocabulary": [
                    {"word": "Hands-only CPR", "definition": "Chest-compression-only CPR recommended for untrained bystanders responding to an adult in cardiac arrest."},
                    {"word": "AED", "definition": "Automated External Defibrillator -- a device that can shock a heart back into a normal rhythm."},
                    {"word": "Compression rate", "definition": "How fast chest compressions should be given during CPR, about 100-120 per minute."},
                ],
                "cornell_questions": [
                    "What is the correct rate for hands-only CPR?",
                    "How deep should compressions be?",
                    "What does an AED do?",
                    "When is hands-only CPR the right choice?",
                ],
                "exit_ticket": "In your own words, explain hands-only CPR to someone who has never heard of it -- what do you do, and how fast?",
            },
        ],
    },
    {
        "number": 6,
        "name": "Basic Food Prep",
        "overview": (
            "Students learn the foundation of cooking: food safety and the danger zone, how to use a "
            "knife without cutting themselves, cooking vocabulary, and how to operate the appliances "
            "they'll actually find at home -- air fryer, Instant Pot, convection toaster oven, and "
            "no-bake techniques."
        ),
        "lessons": [
            {
                "label": "6.1",
                "title": "Food Safety",
                "key_topics": "Danger zone, cross-contamination, the 2-hour rule",
                "objectives": [
                    "Identify the temperature 'danger zone' for food safety.",
                    "Explain cross-contamination and how to prevent it.",
                    "Apply the 2-hour rule for perishable food.",
                ],
                "vocabulary": [
                    {"word": "Danger zone", "definition": "The temperature range (40-140°F) where bacteria grow fastest on food."},
                    {"word": "2-hour rule", "definition": "The guideline that perishable food shouldn't sit at room temperature for more than 2 hours."},
                    {"word": "Foodborne illness", "definition": "Sickness caused by eating food contaminated with bacteria, viruses, or toxins."},
                ],
                "cornell_questions": [
                    "What temperature range is the 'danger zone'?",
                    "What is cross-contamination?",
                    "What is the 2-hour rule?",
                    "What are common causes of foodborne illness?",
                ],
                "exit_ticket": "Leftover pasta sat out on the counter for 3 hours after dinner. Based on the 2-hour rule, what should you do with it?",
            },
            {
                "label": "6.2",
                "title": "Knife Safety & Skills",
                "key_topics": "Grip, curl, safe cutting techniques, knife care",
                "objectives": [
                    "Demonstrate a safe knife grip and claw hand position.",
                    "Perform basic cuts (slice, dice) safely.",
                    "Explain how to clean and store a knife safely.",
                ],
                "vocabulary": [
                    {"word": "Claw grip", "definition": "Curling your fingertips under and guiding with your knuckles to keep fingers safe while cutting."},
                    {"word": "Rock chop", "definition": "A cutting motion that keeps the knife tip on the board while the back rises and falls."},
                    {"word": "Blade care", "definition": "Properly cleaning, drying, and storing a knife to keep it sharp and safe."},
                ],
                "cornell_questions": [
                    "What is the claw grip and why use it?",
                    "What's the difference between slicing and dicing?",
                    "Why is a sharp knife actually safer than a dull one?",
                    "How should a knife be cleaned and stored?",
                ],
                "exit_ticket": "Explain the claw grip to someone who's never cut a vegetable before, in your own words.",
            },
            {
                "label": "6.3",
                "title": "Cooking Terms & Methods",
                "key_topics": "Sauté, simmer, roast, fold, deglaze -- reading a recipe",
                "objectives": [
                    "Define common cooking verbs used in recipes.",
                    "Match a cooking method to the right type of dish.",
                    "Read and follow a simple recipe accurately.",
                ],
                "vocabulary": [
                    {"word": "Sauté", "definition": "To cook food quickly in a small amount of fat over fairly high heat."},
                    {"word": "Simmer", "definition": "To cook liquid just below boiling, with small bubbles breaking the surface."},
                    {"word": "Deglaze", "definition": "To add liquid to a hot pan to loosen browned bits stuck to the bottom, adding flavor to a sauce."},
                ],
                "cornell_questions": [
                    "What's the difference between sautéing and simmering?",
                    "What does 'fold' mean in a recipe?",
                    "What does deglazing a pan accomplish?",
                    "Why does the order of steps in a recipe matter?",
                ],
                "exit_ticket": "A recipe tells you to 'sauté the onions, then deglaze the pan.' Explain what you'd actually do, step by step.",
            },
            {
                "label": "6.4",
                "title": "Air Fryer Cooking",
                "key_topics": "How it works, temperature, timing, cleanup",
                "objectives": [
                    "Explain how an air fryer cooks food differently than an oven.",
                    "Set appropriate temperature and time for a common air fryer dish.",
                    "Clean an air fryer basket correctly after use.",
                ],
                "vocabulary": [
                    {"word": "Convection", "definition": "Cooking method that circulates hot air around food, which is how an air fryer works."},
                    {"word": "Preheat", "definition": "Bringing an appliance up to cooking temperature before adding food."},
                    {"word": "Basket capacity", "definition": "How much food an air fryer basket can hold without overcrowding, which affects how evenly food cooks."},
                ],
                "cornell_questions": [
                    "How does an air fryer cook food?",
                    "Why does overcrowding the basket cause uneven cooking?",
                    "What's a typical temperature range for air frying?",
                    "How do you clean an air fryer basket safely?",
                ],
                "exit_ticket": "You're air-frying a full bag of frozen fries but they're not getting crispy. What's most likely wrong, based on today's lesson?",
            },
            {
                "label": "6.5",
                "title": "Instant Pot Basics",
                "key_topics": "Pressure cooking, steam release, common recipes",
                "objectives": [
                    "Explain how pressure cooking speeds up cooking time.",
                    "Describe the difference between natural and quick steam release.",
                    "Identify basic safety rules for using a pressure cooker.",
                ],
                "vocabulary": [
                    {"word": "Pressure cooking", "definition": "Cooking food in a sealed pot where trapped steam raises pressure and temperature, cooking food faster."},
                    {"word": "Quick release", "definition": "Manually venting steam immediately after cooking to open the pot faster."},
                    {"word": "Natural release", "definition": "Letting pressure drop on its own over time before opening the pot."},
                ],
                "cornell_questions": [
                    "Why does pressure cooking cook food faster?",
                    "What's the difference between quick and natural release?",
                    "What safety rule matters most with a pressure cooker?",
                    "What kinds of food work well in an Instant Pot?",
                ],
                "exit_ticket": "Explain to someone new why they should NEVER force open a pressure cooker lid before the pressure has released.",
            },
            {
                "label": "6.6",
                "title": "Convection & Toaster Oven",
                "key_topics": "Fan cooking, temp adjustment, broil vs. bake",
                "objectives": [
                    "Explain how convection (fan) cooking differs from standard baking.",
                    "Adjust temperature or time correctly when using convection mode.",
                    "Distinguish between broiling and baking.",
                ],
                "vocabulary": [
                    {"word": "Convection bake", "definition": "A setting that uses a fan to circulate hot air, cooking food faster and more evenly than standard bake."},
                    {"word": "Broil", "definition": "Cooking with direct, intense heat from above, used for browning or quick-cooking thin foods."},
                    {"word": "Temperature adjustment", "definition": "Lowering a recipe's stated temperature (often by 25°F) when using convection mode."},
                ],
                "cornell_questions": [
                    "How does convection cooking differ from standard baking?",
                    "Why do you often lower the temperature for convection?",
                    "What's the difference between broiling and baking?",
                    "What foods work well under a broiler?",
                ],
                "exit_ticket": "A recipe calls for baking at 375°F. If you're using convection mode, what would you likely adjust and why?",
            },
            {
                "label": "6.7",
                "title": "No-Bake Cooking",
                "key_topics": "Energy balls, overnight oats, parfaits, smoothies",
                "objectives": [
                    "Prepare a no-bake snack using correct ratios of ingredients.",
                    "Explain why no-bake recipes rely on binding ingredients instead of heat.",
                    "Safely store a no-bake dish for later.",
                ],
                "vocabulary": [
                    {"word": "Binder", "definition": "An ingredient (like nut butter or honey) that holds a no-bake recipe together without cooking."},
                    {"word": "Overnight oats", "definition": "A no-cook breakfast made by soaking oats in liquid in the refrigerator overnight."},
                    {"word": "Layering", "definition": "Building a dish like a parfait in distinct layers for texture and presentation."},
                ],
                "cornell_questions": [
                    "What is a 'binder' in a no-bake recipe?",
                    "Why do overnight oats work without cooking?",
                    "What makes a good parfait layering order?",
                    "How should no-bake food be stored?",
                ],
                "exit_ticket": "Describe how you'd make a basic parfait layering order, and explain why that order makes sense.",
            },
        ],
    },
]


def get_lesson(label):
    """Look up a single lesson dict by label, e.g. '1.1'."""
    for unit in UNITS:
        for lesson in unit["lessons"]:
            if lesson["label"] == label:
                return unit, lesson
    return None, None


def all_lesson_labels():
    return [lesson["label"] for unit in UNITS for lesson in unit["lessons"]]

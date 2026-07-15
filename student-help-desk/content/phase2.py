PHASE_2_META = {
    "number": 2,
    "name": "Chromebook Mastery & Repair",
    "essential_question": "What does it take to diagnose, repair, and responsibly track a device from the moment it breaks to the moment it's back in a student's hands (or retired for parts)?",
    "overview": "Phase 2 moves students from general professionalism into the hands-on core of the job: ChromeOS troubleshooting, physical screen and internal-component repair, and the inventory discipline that keeps a whole fleet of school devices accountable. Students work toward the ACER Chromebook Repair certification while practicing on real tools and real guides (iFixit, Crucial Advisor) before ever touching a live device.",
    "vocabulary_bank": [
        {"word": "ChromeOS", "definition": "The lightweight operating system that runs on Chromebooks, built by Google, updates automatically, and runs most apps through the browser or Play Store.",
         "syllables": "CHROME-oh-ess", "morphology": "Not a Greek/Latin root word — a brand-name compound: 'Chrome' (Google's browser) + 'OS,' an acronym for Operating System (O = Operating, S = System)."},
        {"word": "Powerwash", "definition": "A Chromebook's factory reset. It wipes local data and settings back to default but keeps the device enrolled to the school's domain if it was enrolled before.",
         "syllables": "POW-er-wash", "morphology": "Compound word: 'power' (strong, forceful) + 'wash' (to clean) — modeled on the term for blasting dirt off a surface with a pressure washer, applied here to wiping a device's data clean."},
        {"word": "Recovery Mode", "definition": "A special boot process used to fully reinstall ChromeOS from a USB drive when the device won't start or update normally and a Powerwash isn't enough.",
         "syllables": "ree-KUV-er-ee mode", "morphology": "Latin re- (back, again) + capere (to take, seize) form 'recovery' (taking back); 'mode' comes from Latin modus (a manner or way of doing something)."},
        {"word": "Enrollment", "definition": "The process of registering a Chromebook to a school's Google Admin domain so IT staff can push settings, restrictions, and apps to it remotely.",
         "syllables": "en-ROLL-ment", "morphology": "French en- (into) + rolle (a roll of paper used as a register or list) + -ment (noun-forming suffix) — literally 'the act of entering onto a list.'"},
        {"word": "LCD Panel", "definition": "The actual screen component inside a laptop or Chromebook that displays the image (liquid crystal display).",
         "syllables": "L-C-D PAN-uhl (said as three letters, then 'panel')", "morphology": "Acronym: L = Liquid, C = Crystal, D = Display."},
        {"word": "Bezel", "definition": "The plastic frame around the screen that holds the LCD panel in place and snaps or screws into the rest of the case.",
         "syllables": "BEH-zul", "morphology": "From Old French 'bisel,' the slanted edge cut around a gemstone or watch glass to hold it in its setting — borrowed directly from French jewelry and clockmaking terms, no Greek/Latin root."},
        {"word": "Daughterboard", "definition": "A small circuit board connected to the motherboard that handles one specific job, like the charging port or headphone jack.",
         "syllables": "DAW-ter-bord", "morphology": "Compound word: 'daughter' (a smaller unit branching off a larger one) + 'board' (circuit board) — named by analogy to the 'motherboard' it connects to."},
        {"word": "Serial Number", "definition": "A unique number assigned by the manufacturer that identifies one specific physical device, never duplicated on any other unit.",
         "syllables": "SEER-ee-ul NUM-ber", "morphology": "Latin series (a row, chain, or sequence) + -al (adjective-forming suffix) — describes a number that marks one item's unique place in a sequence."},
        {"word": "Asset Tag", "definition": "A sticker or label a school district adds on top of the serial number to track a device in its own inventory system.",
         "syllables": "ASS-et tag", "morphology": "'Asset' traces to Old French assez (enough, sufficient), later meaning a valuable possession; 'tag' is a Germanic-origin word for a small label attached to an item."},
        {"word": "Repair Log", "definition": "A written record of what was wrong with a device, what was done to fix it, who did it, and when.",
         "syllables": "ree-PAIR log", "morphology": "Latin re- (again) + parare (to make ready, prepare) form 'repair' (to make ready again); 'log' comes from an old nautical term for a ship's written voyage record."},
        {"word": "Repair-vs-Scrap", "definition": "The decision process technicians use to figure out whether fixing a device is worth the cost and time, or whether it makes more sense to scrap it for usable parts.",
         "syllables": "ree-PAIR vur-sus SKRAP", "morphology": "'Repair' (Latin re- + parare, 'to make ready again') + 'vs.,' short for Latin versus (turned against); 'scrap' comes from Old Norse skrap (bits, scraps left over)."},
    ],
    "unit_assessment": {
        "title": "Phase 2 Assessment: Chromebook Mastery & Repair",
        "questions": [
            {"type": "multiple_choice", "q": "A Chromebook won't boot at all, even after several restarts and a Powerwash attempt from the sign-in screen. What's the next troubleshooting step?", "choices": ["A. Replace the daughterboard", "B. Boot into Recovery Mode and reinstall ChromeOS from a USB drive", "C. Remove the bezel and check the LCD panel", "D. Enroll the device again"], "answer": "B"},
            {"type": "multiple_choice", "q": "A teacher's Chromebook is stuck asking to be enrolled to a domain it shouldn't belong to. What's most likely going on?", "choices": ["A. The battery is swollen", "B. The daughterboard failed", "C. The device is enrolled to the wrong Google Admin domain or needs deprovisioning", "D. The LCD panel needs replacing"], "answer": "C"},
            {"type": "multiple_choice", "q": "During a screen replacement, why does skipping ESD grounding matter even if nobody gets hurt?", "choices": ["A. It voids the warranty automatically", "B. It can silently damage the LCD panel or motherboard with static electricity", "C. It only matters for keyboard repairs", "D. It slows down the repair, nothing else"], "answer": "B"},
            {"type": "multiple_choice", "q": "A Chromebook charges fine with one charger but not another, and the battery tests healthy. What's the most likely next step?", "choices": ["A. Powerwash the device", "B. Test the charging port daughterboard before ordering a new battery", "C. Remove the bezel", "D. Look up the serial number"], "answer": "B"},
            {"type": "multiple_choice", "q": "Why does a repair log need the device's serial number, not just a description of the problem?", "choices": ["A. It's required by ChromeOS", "B. It ties the specific repair to one specific physical device so there's a clear history and accountability", "C. It's only needed for warranty claims, nothing else", "D. Serial numbers are optional for school-owned devices"], "answer": "B"},
            {"type": "multiple_choice", "q": "A five-year-old Chromebook needs a $60 daughterboard and the model is barely used in the fleet anymore. Repair-vs-scrap thinking says:", "choices": ["A. Always repair every device no matter the cost", "B. Scrap it immediately and throw away all the parts", "C. Weigh cost and remaining usefulness; consider keeping it as a parts donor instead of repairing", "D. Enrollment status decides this, not cost"], "answer": "C"},
            {"type": "short_answer", "q": "Explain the difference between a Powerwash and Recovery Mode, including when a tech would choose one over the other.", "sample_answer": "A Powerwash wipes local data and settings on a device that still boots and runs ChromeOS normally; a tech uses it for glitches or before reassigning a device. Recovery Mode fully reinstalls ChromeOS itself from a USB drive and is needed when the device won't boot or update at all, which Powerwash can't fix."},
            {"type": "short_answer", "q": "Why does a school district put its own Asset Tag on a device that already has a manufacturer Serial Number?", "sample_answer": "The Serial Number identifies the device to the manufacturer, but the Asset Tag links it to the district's own records, like which cart or classroom it's assigned to, its purchase date, and its repair history, which the manufacturer's number alone doesn't track."},
            {"type": "short_answer", "q": "Describe what belongs in a well-written repair log entry.", "sample_answer": "A good entry includes the device's serial number and asset tag, the date, the symptom reported, what was diagnosed, exactly which part was replaced (if any), the tech's name, and any follow-up needed, written in plain, specific language instead of vague notes like 'fixed it.'"},
            {"type": "short_answer", "q": "In the Day 34 reading, how did the missing device eventually get traced, and what does that show about why logging matters even for quick fixes?", "sample_answer": "The crew traced the missing device by working backward through the repair log to find the last entry connected to it, which exposed a point where someone had borrowed it for a quick fix without logging it back in. It shows that skipping even a small logging step breaks the whole chain of accountability."},
        ],
    },
    "days": [19, 36],
}

PHASE_2_LESSONS = [
    {
        "day": 19,
        "unit": 2,
        "lesson_in_unit": 1,
        "title": "Meet ChromeOS",
        "objectives": [
            "I can explain what ChromeOS is and how it differs from Windows and macOS.",
            "I can identify basic ChromeOS interface elements a new user would need help finding.",
            "I can describe why schools like ours standardize on Chromebooks.",
        ],
        "vocab": [
            {"word": "ChromeOS", "definition": "The lightweight operating system that runs on Chromebooks, built by Google, updates automatically, and runs most apps through the browser or Play Store.",
             "example": "When a teacher says their Chromebook 'looks different than my laptop at home,' it's usually because ChromeOS works differently than Windows or macOS.",
             "syllables": "CHROME-oh-ess", "morphology": "Not a Greek/Latin root word — a brand-name compound: 'Chrome' (Google's browser) + 'OS,' an acronym for Operating System (O = Operating, S = System)."},
        ],
        "academic_vocab": {
            "word": "Differentiate",
            "definition": "To recognize and explain how two or more things are different from each other.",
            "syllables": "dif-er-EN-shee-ate",
            "morphology": "Latin dis- (apart) + ferre (to carry) — literally 'to carry apart,' i.e., to set things apart from each other.",
            "example": "Today you'll differentiate ChromeOS from Windows and macOS by comparing how each one runs apps and installs updates.",
        },
        "warm_up": "Think about the last time you used a Chromebook versus a Windows laptop or a Mac. What felt different? Write down two things you noticed.",
        "mini_lesson": [
            {"heading": "What ChromeOS Actually Is", "body": "ChromeOS is a lightweight operating system built by Google that runs on Chromebooks. Instead of installing big desktop programs, most ChromeOS apps run through the Chrome browser, the Play Store, or a Linux container for more advanced tools. It updates itself automatically in the background, boots in seconds, and needs almost no antivirus software or manual maintenance the way Windows machines often do. Everything ties back to a Google account, which is why signing in with the right account matters so much for troubleshooting."},
            {"heading": "Why Schools Standardize on Chromebooks", "body": "Districts like ours choose Chromebooks because they're affordable, durable enough for daily student use, and centrally managed through the Google Admin console. IT staff can push settings, apps, and restrictions to hundreds of devices at once instead of configuring each one by hand. Repairs are also more standardized across models than with a mix of random laptop brands, which is part of why this phase of the course focuses so heavily on Chromebook hardware specifically."},
            {"heading": "Where the Help Desk Fits In", "body": "Starting today, expect more tickets about ChromeOS itself: accounts that won't sign in, apps that won't load, settings that look wrong. Keep using your Phase 1 intake skills, get the real problem before touching the device, since a surprising number of 'broken Chromebook' tickets turn out to be a sign-in issue or a misunderstood setting, not a hardware problem at all."},
        ],
        "activity": {
            "title": "ChromeOS Scavenger Hunt",
            "instructions": "Pair students up with a lab Chromebook and a checklist of interface elements to locate: the Settings gear, an installed extension icon, the Play Store, and the sync/enrollment icon in the account menu. First pair to correctly find and explain all four out loud wins. Debrief by asking which item was hardest to find and why a new user might get stuck there too.",
        },
        "application": {
            "type": "case_study",
            "title": "The Substitute Teacher's Confusion",
            "scenario": "A substitute teacher named Ms. Ruiz is covering a class for the day. She's used to the Windows laptop cart at her regular school and has never touched a Chromebook before. She's handed one to take attendance and immediately gets stuck: she's looking for a 'C: drive' to find her files, tries right-clicking to find 'Task Manager' when a tab freezes, and looks around the screen for a desktop icon to 'install' the attendance program. A student notices and says, 'Just open the Play Store, it's already there,' but Ms. Ruiz doesn't know what that means either. Frustrated, she submits a help desk ticket that just says: 'Laptop is broken, I can't get my work done.' When a tech opens the ticket, nothing about the device is actually broken.",
            "task": "In pairs, identify three specific moments where Ms. Ruiz's confusion comes from expecting Windows behavior instead of ChromeOS behavior, then write the 2-3 sentence explanation you'd give her, in plain language, that would get her unstuck without any jargon.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "Which of these is true about ChromeOS compared to Windows or macOS?", "choices": ["A. It requires manual antivirus installation", "B. Most apps run through the browser, Play Store, or a Linux container", "C. It never updates automatically", "D. It cannot connect to a Google account"], "answer": "B"},
                {"type": "multiple_choice", "q": "Why do districts often standardize on Chromebooks for student devices?", "choices": ["A. They are the most expensive option available", "B. They can only be managed one at a time", "C. They are centrally managed through Google Admin and are generally affordable and durable", "D. They require the most manual maintenance"], "answer": "C"},
                {"type": "short_answer", "q": "A student says their 'Chromebook is broken' because an app icon won't open. What should you check before assuming it's a hardware problem?", "sample_answer": "Check whether the student is signed into the correct Google account, whether the app needs an internet connection, and whether it's a settings or permissions issue before assuming anything is physically wrong with the device."},
            ],
        },
        "exit_ticket": {"prompt": "In one sentence, explain to a friend who's never used one what a Chromebook actually is."},
        "slide_bullets": [
            "ChromeOS: lightweight OS built by Google",
            "Apps run through browser, Play Store, or Linux container",
            "Auto-updates, fast boot, minimal maintenance",
            "Tied to a Google account for sign-in and sync",
            "Managed centrally through Google Admin console",
            "Most 'broken Chromebook' tickets start with intake, not tools",
        ],
    },
    {
        "day": 20,
        "unit": 2,
        "lesson_in_unit": 2,
        "title": "Powerwash: The Chromebook Factory Reset",
        "objectives": [
            "I can explain what a Powerwash does and does not fix.",
            "I can walk a user through performing a Powerwash safely.",
            "I can decide when Powerwash is (and isn't) the right first troubleshooting step.",
        ],
        "vocab": [
            {"word": "Powerwash", "definition": "A Chromebook's factory reset. It wipes local data and settings back to default but keeps the device enrolled to the school's domain if it was enrolled before.",
             "example": "Before handing a Chromebook to a new student, the desk usually runs a Powerwash to clear out the last user's files and settings.",
             "syllables": "POW-er-wash", "morphology": "Compound word: 'power' (strong, forceful) + 'wash' (to clean) — modeled on the term for blasting dirt off a surface with a pressure washer, applied here to wiping a device's data clean."},
        ],
        "academic_vocab": {
            "word": "Justify",
            "definition": "To give solid reasons that support a decision or choice.",
            "syllables": "JUS-tuh-fy",
            "morphology": "Latin justus (right, fair) + -ficare (to make) — literally 'to make right.'",
            "example": "When you sort a ticket into the 'Powerwash' pile, be ready to justify why that ticket doesn't need something more serious like Recovery Mode.",
        },
        "warm_up": "If someone told you 'just reset it' about a glitchy phone or laptop, what do you think that actually erases? Guess before we cover it.",
        "mini_lesson": [
            {"heading": "What Powerwash Wipes (and What It Keeps)", "body": "A Powerwash erases local data, downloaded files, and personal settings on a Chromebook, returning it close to how it looked out of the box. If the device is enrolled to the district's Google Admin domain, it stays enrolled after a Powerwash and will pull down district policies again on next sign-in. It does not fix hardware problems and does not touch anything already saved to Google Drive, since that lives in the cloud, not on the device."},
            {"heading": "How to Trigger One Safely", "body": "Powerwash normally lives under Settings, Advanced, Reset settings, Powerwash. If a device is too broken to reach settings, holding Ctrl+Alt+Shift+R at the sign-in screen brings up the same reset option. Always warn the user first: anything saved only to local Downloads, not Drive, will be gone. Confirm you're on the right device before starting, since there's no undo once it runs."},
            {"heading": "When Powerwash Helps (and When It Doesn't)", "body": "Powerwash is a great first move for a corrupted profile, weird app glitches, or prepping a device to hand off to a new user. It is the wrong move for cracked screens, dead batteries, or ports that don't work, since those are physical problems no software reset can touch. Jumping straight to Powerwash without listening to the actual symptom is the same intake mistake this course covered back in Phase 1."},
        ],
        "activity": {
            "title": "Powerwash Ticket Triage",
            "instructions": "Hand out four mock tickets: a glitchy sign-in screen, a cracked screen, a device with no sound, and a Chromebook being reassigned to a new student. In pairs, students decide which tickets actually call for a Powerwash and which need something else, then one pair demonstrates an actual Powerwash on a lab Chromebook while the rest of the class watches and takes notes on each step.",
        },
        "application": {
            "type": "real_world_problem",
            "title": "Slow, Glitchy, and Not Obviously Broken",
            "scenario": "A ninth-grader turns in a ticket: their Chromebook has been acting up for about two weeks. Tabs freeze constantly, apps take forever to open, and twice this week the whole screen locked up at the sign-in screen and needed to be force-restarted by holding the power button. The student says it's always been their device, no one else uses it, and it hasn't been dropped or gotten wet. It still charges fine and the screen looks physically undamaged. There's no note of any recent Powerwash or reassignment on this device in the tracking sheet, and it isn't a graduating senior's device being prepped for handoff.",
            "task": "Decide whether Powerwash is the right first move here, and if so, write the exact warning you'd give the student beforehand about what will and won't be saved, then list the two menu steps or the keyboard shortcut you'd use to start it.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What happens to district enrollment after a Powerwash on an enrolled Chromebook?", "choices": ["A. The device is permanently un-enrolled", "B. Enrollment stays and re-applies on next sign-in", "C. Enrollment only works after a second Powerwash", "D. Powerwash has no effect on enrollment either way"], "answer": "B"},
                {"type": "multiple_choice", "q": "Which ticket is the best fit for a Powerwash as the first step?", "choices": ["A. A cracked LCD screen", "B. A device that won't charge at all", "C. A device glitching after being reassigned from a previous student", "D. A daughterboard that failed"], "answer": "C"},
                {"type": "short_answer", "q": "A student is upset because files disappeared after a Powerwash. What should the tech have explained beforehand?", "sample_answer": "The tech should have told the student that anything saved only locally (like the Downloads folder) would be erased, and that only files saved to Google Drive are safe during a Powerwash."},
            ],
        },
        "exit_ticket": {"prompt": "Write the one warning you'd always give a user before running a Powerwash on their device."},
        "slide_bullets": [
            "Powerwash = factory reset for ChromeOS",
            "Wipes local data and settings, not Drive files",
            "Enrolled devices stay enrolled after Powerwash",
            "Trigger: Settings > Advanced > Powerwash, or Ctrl+Alt+Shift+R at sign-in",
            "Good for glitches or reassigning a device",
            "Not a fix for hardware problems",
        ],
    },
    {
        "day": 21,
        "unit": 2,
        "lesson_in_unit": 3,
        "title": "When Powerwash Isn't Enough: Recovery Mode",
        "objectives": [
            "I can explain what Recovery Mode does and how it differs from a Powerwash.",
            "I can create a ChromeOS recovery USB drive using the Chromebook Recovery Utility.",
            "I can identify symptoms that call for Recovery Mode instead of a simple reset.",
        ],
        "vocab": [
            {"word": "Recovery Mode", "definition": "A special boot process used to fully reinstall ChromeOS from a USB drive when the device won't start or update normally and a Powerwash isn't enough.",
             "example": "When a Chromebook gets stuck on a black screen after a failed update, Recovery Mode is the way to reinstall ChromeOS from scratch.",
             "syllables": "ree-KUV-er-ee mode", "morphology": "Latin re- (back, again) + capere (to take, seize) form 'recovery' (taking back); 'mode' comes from Latin modus (a manner or way of doing something)."},
        ],
        "academic_vocab": {
            "word": "Prioritize",
            "definition": "To decide which of several things should be handled first, based on how important or urgent it is.",
            "syllables": "pry-OR-uh-tize",
            "morphology": "Latin prior (earlier, first) + -itize (verb-forming suffix meaning 'to make into') — literally 'to make something first.'",
            "example": "When a Chromebook won't boot, you have to prioritize trying Recovery Mode over other fixes since Powerwash isn't even reachable.",
        },
        "warm_up": "If a Powerwash can't even load because the device won't boot at all, what do you think a tech would try next?",
        "mini_lesson": [
            {"heading": "Recovery Mode vs. Powerwash", "body": "A Powerwash resets settings and data on a Chromebook that still boots and runs normally. Recovery Mode goes further: it reinstalls the ChromeOS operating system itself from an external USB drive. Techs reach for Recovery Mode when a device won't boot at all, gets stuck mid-update, or shows corrupted system errors that a simple reset can't touch. Think of Powerwash as clearing a room and Recovery Mode as rebuilding the house."},
            {"heading": "Building a Recovery Drive", "body": "Recovery media is built using the Chromebook Recovery Utility, a Chrome extension available from the Chrome Web Store, along with a USB drive of at least 8GB that will be fully erased in the process. The utility asks for the exact model number or automatically detects it, then downloads and writes the correct ChromeOS recovery image to the drive. Techs keep a small stock of ready-to-use recovery drives on hand for common models in the building."},
            {"heading": "Booting Into Recovery Mode", "body": "With the recovery USB plugged in, holding Esc and Refresh, then pressing Power, brings up the recovery screen on most Chromebook models. From there the device walks the user through reinstalling ChromeOS from the USB drive. This wipes the device completely, so it's treated as a last resort after Powerwash and basic troubleshooting have already failed."},
        ],
        "activity": {
            "title": "Build a Recovery Drive",
            "instructions": "Demonstrate building a recovery drive live using the Chromebook Recovery Utility and a spare USB drive on a lab Chromebook, narrating each screen as you go. Then have students work in small groups to write up the exact steps as a quick-reference guide for the help desk binder, as if a future Apprentice tech will need to follow it with zero prior context.",
        },
        "application": {
            "type": "realistic_fiction",
            "title": "Priya's Monday Morning Rush",
            "scenario": "It's 7:50 on a Monday and the help desk line is already five students deep. Priya, a newer Apprentice, grabs the next device: completely black screen, no response to any key, no light when plugged in to charge for a minute. Her first instinct is to reach for the Powerwash shortcut, Ctrl+Alt+Shift+R, the way she's done for glitchy sign-in screens all last week. She holds the keys at the sign-in screen, but there is no sign-in screen; the screen stays black no matter what she tries. A Level 2 tech named Marcus glances over and asks, 'Can you even get anywhere before trying that?' Priya realizes she's been assuming every dead-looking screen is the same kind of problem.",
            "task": "Explain what Priya should try instead of Powerwash, name the tool and the boot sequence she'd need, and describe the one detail in the scene that should have tipped her off earlier that Powerwash wasn't going to work.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What is the key difference between Recovery Mode and a Powerwash?", "choices": ["A. They do the exact same thing", "B. Recovery Mode reinstalls ChromeOS itself; Powerwash only resets data and settings on a working OS", "C. Powerwash requires a USB drive and Recovery Mode does not", "D. Recovery Mode only works on enrolled devices"], "answer": "B"},
                {"type": "multiple_choice", "q": "What tool is used to build a ChromeOS recovery USB drive?", "choices": ["A. Google Admin console", "B. Crucial Advisor", "C. Chromebook Recovery Utility", "D. iFixit guide"], "answer": "C"},
                {"type": "short_answer", "q": "A Chromebook is stuck on a black screen and won't respond after a failed update. Why would Recovery Mode be the right move here instead of Powerwash?", "sample_answer": "Because the device can't even boot far enough to reach settings for a Powerwash, the problem is with the operating system itself, so it needs to be fully reinstalled using Recovery Mode and a USB recovery drive."},
            ],
        },
        "exit_ticket": {"prompt": "Name one symptom that should make a tech reach for Recovery Mode instead of Powerwash."},
        "slide_bullets": [
            "Recovery Mode reinstalls ChromeOS itself",
            "Used when Powerwash isn't possible or isn't enough",
            "Build recovery media with Chromebook Recovery Utility",
            "Needs a USB drive of 8GB or more",
            "Boot sequence: Esc + Refresh + Power",
            "Last resort after basic troubleshooting fails",
        ],
    },
    {
        "day": 22,
        "unit": 2,
        "lesson_in_unit": 4,
        "title": "Enrollment Issues & Managed Devices",
        "objectives": [
            "I can explain what device enrollment means for a school-owned Chromebook.",
            "I can identify common enrollment-related tickets and how to approach them.",
            "I can use a decision tree to triage common OS-level Chromebook tickets.",
        ],
        "vocab": [
            {"word": "Enrollment", "definition": "The process of registering a Chromebook to a school's Google Admin domain so IT staff can push settings, restrictions, and apps to it remotely.",
             "example": "When a Chromebook keeps asking for a district email at setup, it's usually because the device is enrolled and expects a school account, not a personal one.",
             "syllables": "en-ROLL-ment", "morphology": "French en- (into) + rolle (a roll of paper used as a register or list) + -ment (noun-forming suffix) — literally 'the act of entering onto a list.'"},
        ],
        "academic_vocab": {
            "word": "Categorize",
            "definition": "To sort things into groups based on shared characteristics.",
            "syllables": "KAT-uh-gor-ize",
            "morphology": "Greek kategoria (an accusation, statement, or class) + -ize (verb-forming suffix) — originally about statements, now about sorting into classes.",
            "example": "Using the decision tree, you'll categorize each ticket as an enrollment problem, a boot problem, or something else entirely.",
        },
        "warm_up": "Why might a school want to control settings on hundreds of Chromebooks at once instead of letting each student set up their own device freely?",
        "mini_lesson": [
            {"heading": "What Enrollment Actually Does", "body": "Enrollment registers a Chromebook to the district's Google Admin domain, which lets IT staff push out settings, block certain apps or sites, and manage the device remotely without touching it in person. Enrolled devices usually require a school-issued account at sign-in and stay enrolled even through a Powerwash. This is different from a personal Chromebook, which has no organization managing it."},
            {"heading": "Common Enrollment Tickets", "body": "The most common enrollment tickets include a device stuck asking to enroll before it will let anyone sign in, a personal Chromebook that got accidentally enrolled to the wrong domain, and devices that need deprovisioning, removed from Google Admin, before they leave the district for good (graduating seniors, retired devices, trade-ins). Each of these needs a slightly different fix, so identifying which one you're dealing with matters before doing anything."},
            {"heading": "Looking Ahead to Asset Tracking", "body": "Every enrolled device is tied to its serial number inside the Google Admin console, which is the district's first line of inventory tracking before a device even gets a physical asset tag. Keep that connection in mind, since Week 8 of this phase goes much deeper into how serial numbers and asset tags work together to track every device in the building."},
        ],
        "activity": {
            "title": "Enrollment Troubleshooting Decision Tree",
            "instructions": "As a class, build a flowchart on the board covering common Week 5 tickets in order: won't turn on, turns on but won't boot, boots but stuck at sign-in, and stuck asking for enrollment. In small groups, students then role-play a Tier 1 phone intake call using the tree to walk a 'customer' through diagnosing which branch their problem falls under.",
        },
        "application": {
            "type": "simulation",
            "title": "The Lunch-Period Queue",
            "scenario": "It's the start of lunch period and six Chromebooks land on the help desk counter at once: (1) won't turn on at all, (2) turns on but freezes on a black screen mid-boot, (3) boots fine but is stuck asking to enroll to an unfamiliar domain, (4) boots and signs in fine but one app won't load, (5) asks for a personal Gmail account it shouldn't be asking for, (6) is completely unresponsive even to a forced restart. Lunch is 30 minutes, and past data shows enrollment-only issues take about 5 minutes each to resolve, sign-in/app issues take about 3 minutes, and no-boot or unresponsive devices take at least 15 minutes each just to begin proper diagnosis.",
            "task": "Sort all six devices into the decision-tree categories from today's lesson, estimate the total minutes needed to fully resolve all six, and decide which ones realistically get finished before lunch ends and which get a claim ticket for after school.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What does enrolling a Chromebook to a Google Admin domain allow IT staff to do?", "choices": ["A. Nothing different than an unenrolled device", "B. Push settings, restrictions, and apps to the device remotely", "C. Only change the device's serial number", "D. Prevent the device from ever being Powerwashed"], "answer": "B"},
                {"type": "multiple_choice", "q": "A graduating senior is turning in their district Chromebook for good. What needs to happen before it leaves the district's device pool?", "choices": ["A. Nothing, enrollment doesn't matter after graduation", "B. The device needs to be deprovisioned from Google Admin", "C. The device needs a new asset tag only", "D. Recovery Mode must be run first"], "answer": "B"},
                {"type": "short_answer", "q": "Explain the difference between a device that's simply broken and one that has an enrollment problem.", "sample_answer": "A broken device usually shows a hardware symptom (won't power on, cracked screen, dead port), while an enrollment problem shows up as the device booting fine but getting stuck asking for the wrong account or domain before it will let anyone sign in."},
            ],
        },
        "exit_ticket": {"prompt": "In your own words, explain what 'enrolled' means for a school Chromebook to someone who's never heard the term."},
        "slide_bullets": [
            "Enrollment = registered to district's Google Admin domain",
            "Lets IT push settings/restrictions/apps remotely",
            "Common tickets: stuck at enrollment, wrong domain, needs deprovisioning",
            "Enrollment survives a Powerwash",
            "Serial number is already tied to enrollment records",
            "Decision tree: won't turn on -> won't boot -> stuck sign-in -> enrollment",
        ],
    },
    {
        "day": 23,
        "unit": 2,
        "lesson_in_unit": 5,
        "title": "Getting Ready for Physical Repair: Tools & Safety Refresh",
        "objectives": [
            "I can identify the tools needed for Chromebook screen repair and what each one is for.",
            "I can explain what an LCD panel and a bezel are and how they fit together.",
            "I can use an iFixit guide to preview a repair before touching a device.",
        ],
        "vocab": [
            {"word": "LCD Panel", "definition": "The actual screen component inside a laptop or Chromebook that displays the image (liquid crystal display).",
             "example": "A cracked screen with the picture still visible under the damage usually still has a working LCD panel underneath a shattered outer layer.",
             "syllables": "L-C-D PAN-uhl (said as three letters, then 'panel')", "morphology": "Acronym: L = Liquid, C = Crystal, D = Display."},
            {"word": "Bezel", "definition": "The plastic frame around the screen that holds the LCD panel in place and snaps or screws into the rest of the case.",
             "example": "Before you can get to the LCD panel, you first have to carefully pop the bezel loose without cracking its plastic clips.",
             "syllables": "BEH-zul", "morphology": "From Old French 'bisel,' the slanted edge cut around a gemstone or watch glass to hold it in its setting — borrowed directly from French jewelry and clockmaking terms, no Greek/Latin root."},
        ],
        "academic_vocab": {
            "word": "Interpret",
            "definition": "To figure out the meaning of something, especially something written by someone else.",
            "syllables": "in-TER-prit",
            "morphology": "Latin inter- (between) + pres (agent, negotiator) — originally 'one who explains meaning between two parties,' like a translator.",
            "example": "Before touching a device, you'll interpret an iFixit guide's photos and warnings to understand each step correctly.",
        },
        "warm_up": "What's the difference between fixing something you've never opened before versus something you've practiced on ten times? What would you want before attempting the first kind?",
        "mini_lesson": [
            {"heading": "ESD Safety, Round Two", "body": "Phase 1 covered electrostatic discharge basics; now it's time to apply that to real Chromebook screens. Static electricity that's too small to feel can still fry an LCD panel or motherboard. Every physical repair this phase starts the same way: anti-static wrist strap on, grounded, workspace clear of loose plastic bags or synthetic fabric. This isn't optional and isn't skipped even when a repair feels quick."},
            {"heading": "Tools of the Trade", "body": "Screen and bezel repair uses a small, consistent toolkit: a plastic spudger for prying without scratching plastic, a small Phillips screwdriver, plastic pry tools or opening picks, and the anti-static wrist strap. Metal tools stay away from anything near the battery or exposed circuit boards. Keeping screws organized by step, a small tray or labeled cups works well, prevents the classic mistake of forgetting where a screw came from during reassembly."},
            {"heading": "Meet iFixit", "body": "iFixit is a real, widely used site with free step-by-step repair guides, complete with photos, for thousands of devices including most Chromebook models. This class uses actual iFixit guides for every repair lab this phase, the same way professional repair techs do. Learning to read and follow a guide you didn't write yourself is its own skill, and it's exactly what Level 2 and Level 3 techs do on the job."},
        ],
        "activity": {
            "title": "iFixit Guide Walkthrough",
            "instructions": "In pairs, have students pull up a Chromebook screen replacement guide on iFixit for a model similar to the lab devices, without touching a device yet. Ask them to list every tool the guide calls out, note any warnings or cautions it gives, and predict one step where a beginner might make a mistake. Share out predictions as a class before next class's hands-on lab.",
        },
        "application": {
            "type": "case_study",
            "title": "The YouTube Shortcut",
            "scenario": "A friend outside of class, excited about what you're learning, tries to fix a crack in their own laptop screen at home over the weekend using a random YouTube video instead of a proper guide. They use a butter knife instead of a plastic spudger to pry the bezel loose, work on a carpeted floor with no wrist strap, and toss all the screws into one pile without tracking which one came from where. Partway through, they message you a photo: a cracked corner of the bezel, one stripped screw, and a pile of parts they can no longer place back in order.",
            "task": "List the three specific mistakes in this scenario, matched to what today's lesson said the toolkit and ESD steps are for, and explain what you'd tell your friend to do differently if they attempt this repair again.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What is the LCD panel?", "choices": ["A. The plastic frame around the screen", "B. The component that actually displays the image", "C. A small circuit board for the charging port", "D. The device's serial number sticker"], "answer": "B"},
                {"type": "multiple_choice", "q": "What is the bezel?", "choices": ["A. The screen's display component", "B. The plastic frame that holds the LCD panel in place", "C. A tool used to remove screws", "D. The battery casing"], "answer": "B"},
                {"type": "short_answer", "q": "Why does the help desk use real iFixit guides instead of just relying on memory for each repair?", "sample_answer": "Different Chromebook models have different screw counts, clip locations, and steps, so following a specific guide for the exact model avoids mistakes and matches what professional repair technicians actually do on the job."},
            ],
        },
        "exit_ticket": {"prompt": "Name one tool you'll need for tomorrow's screen removal lab and what it's used for."},
        "slide_bullets": [
            "ESD safety applies to every physical repair this phase",
            "Toolkit: spudger, small screwdriver, pry tools, wrist strap",
            "LCD panel = the display; bezel = the frame around it",
            "Keep screws organized by step during teardown",
            "iFixit: real repair guides used throughout this phase",
            "Reading someone else's guide accurately is its own skill",
        ],
    },
    {
        "day": 24,
        "unit": 2,
        "lesson_in_unit": 6,
        "title": "Opening the Bezel: Screen Removal Lab, Part 1",
        "objectives": [
            "I can safely remove a Chromebook bezel following an iFixit guide.",
            "I can identify common mistakes that damage the bezel or LCD panel during removal.",
            "I can log each teardown step as I complete it.",
        ],
        "vocab": [
            {"word": "Bezel", "definition": "The plastic frame around the screen that holds the LCD panel in place and snaps or screws into the rest of the case.",
             "example": "Prying too hard on one corner of the bezel is the fastest way to snap a clip that was never actually stuck.",
             "syllables": "BEH-zul", "morphology": "From Old French 'bisel,' the slanted edge cut around a gemstone or watch glass to hold it in its setting — borrowed directly from French jewelry and clockmaking terms, no Greek/Latin root."},
            {"word": "LCD Panel", "definition": "The actual screen component inside a laptop or Chromebook that displays the image (liquid crystal display).",
             "example": "Once the bezel is off, the LCD panel is exposed and needs to be handled by its edges only.",
             "syllables": "L-C-D PAN-uhl (said as three letters, then 'panel')", "morphology": "Acronym: L = Liquid, C = Crystal, D = Display."},
        ],
        "academic_vocab": {
            "word": "Execute",
            "definition": "To carry out a plan or set of steps completely and correctly.",
            "syllables": "EK-suh-kyoot",
            "morphology": "Latin ex- (out) + sequi (to follow) — literally 'to follow out (to completion).'",
            "example": "You'll execute each step of the bezel-removal guide in order, checking it off before moving to the next.",
        },
        "warm_up": "If a plastic clip feels stuck, is more force ever the right answer? What would you try first instead?",
        "mini_lesson": [
            {"heading": "Removing the Bezel, Step by Step", "body": "Most Chromebook bezels are held on with a mix of plastic clips and a few hidden screws, sometimes under rubber feet or tape strips. The iFixit guide shows exactly where each one is for a given model. Clips get worked loose gradually with a plastic pry tool moving around the frame's edge, never forced from one spot, since forcing one corner is what snaps the plastic."},
            {"heading": "Ground First, Then Touch", "body": "Before touching anything past the bezel, wrist straps go on and get clipped to a grounded point. This is the exact moment ESD safety matters most, since the LCD panel's ribbon cable and any exposed board underneath are sensitive to static. This step never gets skipped, no matter how quick the job feels."},
            {"heading": "Levels of Trust", "body": "Right now, most students are working through this at Technician level, doing it solo but under close supervision. Full independent teardowns without any check-ins are a Level 3 Lead Tech skill, earned by demonstrating clean, careful work on labs like this one first."},
        ],
        "activity": {
            "title": "Guided Bezel Removal",
            "instructions": "Demonstrate removing the bezel on one practice Chromebook chassis first, narrating each clip and screw location from the iFixit guide. Then have pairs remove the bezel on their own practice devices, checking off each guide step as they complete it and logging any surprises (a stuck clip, a hidden screw) in a shared notes doc.",
        },
        "application": {
            "type": "real_world_problem",
            "title": "The Clip That Won't Let Go",
            "scenario": "Following the iFixit guide exactly, a student has released every visible clip around a Chromebook bezel and removed two hidden screws found under rubber feet, just as the guide described. One corner near the hinge still won't budge after three gentle attempts with the plastic pry tool, moving around the frame's edge each time like the lesson described. The student is starting to feel the pull to just tug harder or reach for a metal tool instead, since the rest of the bezel is already loose everywhere else.",
            "task": "Explain what the student should check or try next before applying more force, referencing what today's lesson said about hidden screws and gradual, all-around prying, and identify the one thing they should absolutely not do.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What's the safest way to loosen a stuck bezel clip?", "choices": ["A. Force it from one spot until it pops", "B. Work around the frame gradually with a plastic pry tool", "C. Use a metal screwdriver directly on the clip", "D. Skip it and pull the panel out anyway"], "answer": "B"},
                {"type": "multiple_choice", "q": "When should the anti-static wrist strap go on during this lab?", "choices": ["A. Only if something feels wrong later", "B. Before touching anything past the bezel", "C. Only during reassembly, not removal", "D. It's optional for bezel removal"], "answer": "B"},
                {"type": "short_answer", "q": "What's the difference between Technician-level and Lead Tech-level teardown work, based on today's lesson?", "sample_answer": "Technician level means doing the teardown solo but with close supervision and check-ins, while Lead Tech level means being trusted to do a full teardown independently, which is earned by first showing careful, consistent work at the Technician level."},
            ],
        },
        "exit_ticket": {"prompt": "Describe one moment today where going slow instead of fast paid off."},
        "slide_bullets": [
            "Bezels use a mix of clips and hidden screws",
            "Work clips loose gradually, never force one spot",
            "Wrist strap on before touching anything past the bezel",
            "Follow the iFixit guide step by step",
            "Log surprises as you go, not from memory later",
            "Technician = supervised solo work; Lead Tech = independent teardown",
        ],
    },
    {
        "day": 25,
        "unit": 2,
        "lesson_in_unit": 7,
        "title": "Screen Replacement Lab, Part 2: When Corners Get Cut",
        "objectives": [
            "I can finish installing and testing a replacement LCD panel before closing the case.",
            "I can explain the real risk behind skipping ESD grounding, even without a visible injury.",
            "I can identify what changes about my own safety habits after seeing a near-miss.",
        ],
        "vocab": [
            {"word": "LCD Panel", "definition": "The actual screen component inside a laptop or Chromebook that displays the image (liquid crystal display).",
             "example": "Jordan tests the new LCD panel before snapping the bezel back on, just in case something needs to be reseated.",
             "syllables": "L-C-D PAN-uhl (said as three letters, then 'panel')", "morphology": "Acronym: L = Liquid, C = Crystal, D = Display."},
            {"word": "Bezel", "definition": "The plastic frame around the screen that holds the LCD panel in place and snaps or screws into the rest of the case.",
             "example": "Only after the panel passes its test does the bezel go back on for good.",
             "syllables": "BEH-zul", "morphology": "From Old French 'bisel,' the slanted edge cut around a gemstone or watch glass to hold it in its setting — borrowed directly from French jewelry and clockmaking terms, no Greek/Latin root."},
        ],
        "academic_vocab": {
            "word": "Analyze",
            "definition": "To break something down into its parts to understand how or why it happened.",
            "syllables": "AN-uh-lyze",
            "morphology": "Greek ana- (up, throughout) + lyein (to loosen) — literally 'to loosen up' or take something apart.",
            "example": "After reading about Jordan's near-miss, you'll analyze exactly which safety step got skipped and why that moment mattered.",
        },
        "warm_up": "Has a small, no-harm-done mistake ever taught you more than getting away with something clean would have? What made it stick?",
        "mini_lesson": [
            {"heading": "Finishing the Install", "body": "With the old panel out, the new LCD panel seats into the frame and its ribbon cable connects to the same port the old one used. Before snapping the bezel back on, power the device on and check the display for dead pixels, color issues, or a loose connection flickering the image. Only after it passes does the bezel go back on and get clipped or screwed into place for good."},
            {"heading": "Why 'No Injury' Doesn't Mean 'No Harm'", "body": "A small static shock that startles someone but doesn't hurt them can still be serious, because the real damage often happens to the device, not the person. A static discharge that a person barely feels can be more than enough to quietly fry an LCD panel or a motherboard component, and that damage might not even show up immediately."},
            {"heading": "Today's Reading", "body": "Today's reading follows Jordan through a screen replacement lab that goes sideways after skipping ESD grounding in a hurry. As you read, pay attention to exactly what got skipped and how Sam responds, not just to the mistake itself, but to resetting expectations afterward."},
        ],
        "activity": {
            "title": "Safety Debrief Circle",
            "instructions": "After the reading, break into small groups and have each group identify the exact moment Jordan skipped a safety step, then rewrite the pre-lab safety checklist Sam should now post at the workstation. Share rewritten checklists as a class and vote on the clearest one to actually adopt for the rest of this phase's labs.",
        },
        "application": {
            "type": "realistic_fiction",
            "title": "One Dead Pixel",
            "scenario": "Before snapping the bezel back into place, a technician powers on a freshly installed LCD panel to test it first, just like today's lesson describes. The display looks almost perfect, except for a single stubborn dead pixel in the upper corner that stays black no matter what's on screen. The rest of the panel displays colors cleanly with no flicker or looseness at the ribbon connector.",
            "task": "Decide whether this repair should be closed up as finished or flagged before the bezel goes back on, and explain in one or two sentences what you'd note in this device's early repair log draft.",
        },
        "reading": {
            "type": "graphic_novel",
            "title": "Ticket #4: The Zap",
            "body": """PANEL 1: Wide shot of the help desk repair bench. Several practice Chromebooks lie open in different stages of teardown. Jordan and two other students wear anti-static wrist straps clipped to a grounding mat. Sam walks the row, checking each station.
CAPTION: Screen replacement lab. Day two.
SAM: "Strap on, clipped to the mat, every time you sit down. Even if you're just grabbing a screwdriver."

PANEL 2: Jordan glances at the clock, then at their wrist strap sitting unclipped on the table.
CAPTION: Jordan's running behind on their teardown.
JORDAN (thinking): "It's just a quick reconnect. I'll clip in after."

PANEL 3: Jordan reaches into the open chassis to reconnect the LCD ribbon cable, wrist strap still sitting on the table, unclipped.
CAPTION: One motion, no ground.

PANEL 4: A small spark jumps between Jordan's finger and the metal shielding near the connector. Jordan flinches back, dropping the spudger with a clatter.
JORDAN: "Ow— whoa!"

PANEL 5: Sam is already crossing the room, kneeling by the station, checking Jordan's hand first.
SAM: "Hey. You good? Let me see your hand."
JORDAN: "I'm fine, it just startled me."

PANEL 6: Sam looks past Jordan's hand at the open device, expression serious but not angry.
SAM: "You're fine. I'm not worried about you right now. I'm worried about that panel."

PANEL 7: Close on the LCD ribbon connector. Sam points at it without touching it yet.
SAM: "Static that small doesn't hurt people. It can absolutely kill a panel or a board, and you might not even know it happened until it fails on someone next week."

PANEL 8: Ms. Faraday appears in the doorway, having heard the commotion, arms crossed but calm.
MS. FARADAY: "Everyone okay?"
SAM: "Yeah. Small reminder about grounding. We're good."

PANEL 9: Jordan clips the wrist strap on properly this time before touching anything else, visibly more careful.
JORDAN: "Same steps every time. Even when I think I don't need them."
SAM: "That's the whole job. That's what gets you to Level 2 and keeps you there."

PANEL 10: Final wide shot, the whole bench working again, straps clipped, focused.
CAPTION: The panel tested fine. Jordan didn't skip the strap again.""",
            "questions": [
                "What specific safety step did Jordan skip, and why did they skip it in the moment?",
                "Sam says he's more worried about the panel than about Jordan. What does that tell you about why ESD safety matters, even when nobody gets physically hurt?",
                "How does Sam's response model good mentorship compared to just getting angry at a mistake?",
                "Why do you think Ms. Faraday only asked if everyone was okay instead of stepping in further?",
                "Describe a time a 'small' shortcut you took almost caused a bigger problem. What did you learn from it?",
            ],
        },
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "Before closing the bezel on a repaired screen, what should a tech do first?", "choices": ["A. Immediately snap the bezel back on to save time", "B. Power the device on and test the display for issues first", "C. Skip testing if the repair looked clean", "D. Reconnect the battery only"], "answer": "B"},
                {"type": "multiple_choice", "q": "In the reading, why was Sam more concerned about the panel than about Jordan getting hurt?", "choices": ["A. He didn't actually care about Jordan", "B. A shock too small to hurt a person can still damage sensitive electronics silently", "C. The panel was already broken before the shock", "D. He was more worried about being blamed"], "answer": "B"},
                {"type": "short_answer", "q": "What does Sam mean when he says 'same steps every time, even when I think I don't need them'?", "sample_answer": "He means safety habits like grounding only work if they're followed consistently, not just when a repair feels risky, because it's impossible to predict in the moment which 'quick' step is the one that actually causes damage."},
            ],
        },
        "exit_ticket": {"prompt": "What's one safety habit from today's lesson or reading you're committing to never skip, even when you're in a hurry?"},
        "slide_bullets": [
            "Test the new panel before closing the bezel for good",
            "A shock too small to feel can still fry electronics",
            "'No injury' doesn't mean 'no harm' happened",
            "Today's reading: Ticket #4, The Zap",
            "Good mentorship: address the habit, not just the moment",
            "Safety steps only work if they're never skipped",
        ],
    },
    {
        "day": 26,
        "unit": 2,
        "lesson_in_unit": 8,
        "title": "Hinge Repair & Reassembly Quality Check",
        "objectives": [
            "I can identify common hinge problems and how to address them during a screen repair.",
            "I can reassemble a repaired Chromebook and verify the bezel sits correctly.",
            "I can run a completed repair through a quality-check process before it's considered done.",
        ],
        "vocab": [
            {"word": "Bezel", "definition": "The plastic frame around the screen that holds the LCD panel in place and snaps or screws into the rest of the case.",
             "example": "A bezel that doesn't sit flush usually means a clip got missed during reassembly.",
             "syllables": "BEH-zul", "morphology": "From Old French 'bisel,' the slanted edge cut around a gemstone or watch glass to hold it in its setting — borrowed directly from French jewelry and clockmaking terms, no Greek/Latin root."},
        ],
        "academic_vocab": {
            "word": "Evaluate",
            "definition": "To judge the quality or condition of something using a clear set of criteria.",
            "syllables": "ee-VAL-yoo-ate",
            "morphology": "Latin ex- (out) + valere (to be strong/worth) — literally 'to draw out the worth' of something.",
            "example": "Using the quality-check list, you'll evaluate whether a finished repair is really done or just looks done.",
        },
        "warm_up": "Why might a repair that 'works' still not be considered finished until someone checks it over?",
        "mini_lesson": [
            {"heading": "Hinge Problems & Fixes", "body": "Worn or broken hinges cause a screen to flop loosely, sit at the wrong angle, or crack the surrounding plastic over time. Replacing a hinge usually means removing the bezel and sometimes the keyboard deck to access the mounting screws. Screws get snugged firmly but never overtightened, since stripped screws in plastic housing are a common and avoidable mistake."},
            {"heading": "Reassembly Done Right", "body": "During reassembly, the bezel should sit flush all the way around with no visible gaps or light leaking through the edges, and it shouldn't rattle when the device is gently shaken. Screws go back exactly where they came from, using the organized tray or labeled cups from the teardown, not wherever seems close enough."},
            {"heading": "The Quality Check Habit", "body": "A repair isn't done just because the screen turns on. Every finished repair gets a quick quality check: open and close the lid a few times to test the hinge, check the bezel for gaps, and confirm nothing rattles inside. This habit directly supports the Labs & Repair Skills portion of the grade, since sloppy reassembly on a passing repair still counts against the work."},
        ],
        "activity": {
            "title": "Final Inspection Station",
            "instructions": "Have each pair bring their repaired Chromebook from the past two labs to a quality-check station. Using a simple checklist (bezel flush, no rattle, hinge holds angle, display clean), they inspect and sign off on their own repair, then rotate to check a different pair's device as a second set of eyes, just like a real shop would do a peer quality check.",
        },
        "application": {
            "type": "simulation",
            "title": "Four Repairs, One Checklist",
            "scenario": "Four freshly reassembled Chromebooks arrive at the quality-check station with the same rubric from today's lesson: bezel gap under 1mm all around, no rattle when gently shaken, hinge holds its angle at 45, 90, and 135 degrees without drifting, and a clean display. Device A has a 2mm gap on one corner. Device B has zero gap and no rattle but the hinge slowly drifts closed on its own from 90 degrees. Device C passes every check cleanly. Device D has no gap or rattle issues but makes a faint clicking sound only when opened past 100 degrees.",
            "task": "Using the rubric, mark each of the four devices pass or fail, and for any that fail, name the most likely repair step that was done poorly based on today's lesson.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What's a common sign of a bad hinge repair?", "choices": ["A. The screen turns on normally", "B. The screen flops loosely or sits at the wrong angle", "C. The battery drains slowly", "D. The keyboard feels stiff"], "answer": "B"},
                {"type": "multiple_choice", "q": "What should a properly reassembled bezel look like?", "choices": ["A. Gaps around the edges are normal and fine", "B. Sitting flush with no visible gaps and no rattling", "C. Slightly loose so it's easy to remove again", "D. Held on with tape instead of clips"], "answer": "B"},
                {"type": "short_answer", "q": "Why does a repair still need a quality check even after the screen turns on and works?", "sample_answer": "A working screen only confirms the display itself is fine, but a sloppy reassembly can leave gaps, rattles, or a hinge that won't hold its angle, all of which matter for how the device holds up and is graded under Labs & Repair Skills."},
            ],
        },
        "exit_ticket": {"prompt": "Name one thing you'd check on a peer's finished repair before signing off on it."},
        "slide_bullets": [
            "Worn hinges cause loose or wrong-angle screens",
            "Don't overtighten screws in plastic housing",
            "Bezel should sit flush, no gaps or rattle",
            "Quality check: open/close test, gap check, shake test",
            "A working screen isn't the same as a finished repair",
            "Peer-check another team's repair for a second opinion",
        ],
    },
    {
        "day": 27,
        "unit": 2,
        "lesson_in_unit": 9,
        "title": "Battery Care & Replacement",
        "objectives": [
            "I can explain the safety concerns specific to lithium-ion Chromebook batteries.",
            "I can safely remove and replace a Chromebook battery following an iFixit guide.",
            "I can begin logging repair steps as I complete them, not after the fact.",
        ],
        "vocab": [
            {"word": "Repair Log", "definition": "A written record of what was wrong with a device, what was done to fix it, who did it, and when.",
             "example": "Even on a battery swap, jotting down the model, symptom, and part used starts building the habit of a real repair log.",
             "syllables": "ree-PAIR log", "morphology": "Latin re- (again) + parare (to make ready, prepare) form 'repair' (to make ready again); 'log' comes from an old nautical term for a ship's written voyage record."},
        ],
        "academic_vocab": {
            "word": "Mitigate",
            "definition": "To make a risk or problem less severe or dangerous.",
            "syllables": "MIT-uh-gate",
            "morphology": "Latin mitis (soft, gentle) + agere (to do/act) — literally 'to make gentle.'",
            "example": "Disconnecting the battery connector first is one way technicians mitigate the fire risk of a damaged lithium-ion battery.",
        },
        "warm_up": "Have you ever heard a warning about phone or laptop batteries catching fire or swelling up? What do you think causes that?",
        "mini_lesson": [
            {"heading": "Why Batteries Get Extra Caution", "body": "Chromebook batteries are lithium-ion, the same type that can catch fire or vent gas if punctured, bent, or crushed. Warning signs of a failing battery include a swollen case that makes the trackpad or keyboard bulge, a device that won't hold a charge, or sudden random shutdowns. A swollen battery never gets pressed flat or forced back into place; it gets carefully isolated and reported following district hazmat procedure."},
            {"heading": "Removing & Replacing Safely", "body": "Battery replacement starts with fully powering down the device, then disconnecting the battery's own connector before touching anything else inside, this removes the risk of a short while other work happens. Plastic prying tools, not metal, stay near the battery at all times. After installing the new battery, reconnect and test that it holds a charge before closing the case for good."},
            {"heading": "Start Logging Now", "body": "Professional techs don't wait until the end of a repair to remember what they did, they write it down as they go: what was replaced, why, and by whom. This phase builds toward a full lesson on writing strong repair logs, but the habit starts today. Keep a running note during this lab as an early rough draft of what a real entry looks like."},
        ],
        "activity": {
            "title": "Battery Swap Lab + Live Log",
            "instructions": "Using the iFixit guide for the lab's Chromebook model, pairs safely disconnect and replace a practice battery, testing that the new one holds a charge before closing the case. At the same time, each pair keeps a running note in a shared doc listing every step as they complete it, an early draft version of a repair log entry.",
        },
        "application": {
            "type": "real_world_problem",
            "title": "The Bulging Trackpad",
            "scenario": "A teacher brings in a Chromebook and mentions, almost as an afterthought, that the trackpad has felt 'weirdly puffy' for the past week and the device has started randomly shutting off even with battery showing charge left. Looking closer, the area under the trackpad is slightly raised compared to the rest of the case, and the keyboard deck doesn't sit quite flush anymore near that spot. The teacher asks if you can 'just pop the case open real quick and take a look.'",
            "task": "Identify what this symptom most likely is based on today's lesson, decide whether opening the case immediately is the right move, and describe the correct next steps in order, including what should never be done to a battery in this condition.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What's a warning sign of a failing lithium-ion battery?", "choices": ["A. The device charges slightly faster than usual", "B. A swollen case that bulges the keyboard or trackpad", "C. The screen brightness changes", "D. The Wi-Fi disconnects randomly"], "answer": "B"},
                {"type": "multiple_choice", "q": "What should be disconnected first when starting a battery replacement?", "choices": ["A. The keyboard ribbon cable", "B. The battery's own connector", "C. The Wi-Fi antenna", "D. The bezel clips"], "answer": "B"},
                {"type": "short_answer", "q": "Why do techs start writing a repair log entry as they work instead of waiting until the job is finished?", "sample_answer": "Writing it down as you go captures accurate details, like exact steps and part numbers, that are easy to forget or blur together by the end, which makes the final log entry more complete and trustworthy."},
            ],
        },
        "exit_ticket": {"prompt": "Write one line as if it's the start of today's repair log entry for the battery you worked on."},
        "slide_bullets": [
            "Lithium-ion batteries: fire/swelling risk if damaged",
            "Swollen battery = isolate, never force flat",
            "Disconnect the battery's own connector first",
            "Plastic tools only near the battery",
            "Test charging before closing the case",
            "Start logging steps as you go, not after",
        ],
    },
    {
        "day": 28,
        "unit": 2,
        "lesson_in_unit": 10,
        "title": "Keyboard Replacement & Ribbon Cable Care",
        "objectives": [
            "I can safely remove and replace a Chromebook keyboard following an iFixit guide.",
            "I can identify common causes of keyboard tickets.",
            "I can practice narrating repair steps clearly enough for someone else to follow.",
        ],
        "vocab": [
            {"word": "Repair Log", "definition": "A written record of what was wrong with a device, what was done to fix it, who did it, and when.",
             "example": "A keyboard swap logged with the exact cause, like liquid damage, helps the next tech spot a pattern if the same cart keeps having issues.",
             "syllables": "ree-PAIR log", "morphology": "Latin re- (again) + parare (to make ready, prepare) form 'repair' (to make ready again); 'log' comes from an old nautical term for a ship's written voyage record."},
        ],
        "academic_vocab": {
            "word": "Articulate",
            "definition": "To express something clearly and specifically, in words, so someone else understands exactly what you mean.",
            "syllables": "ar-TIK-yoo-late",
            "morphology": "Latin articulus (a small joint or connecting part) — originally about speech broken into clear, connected parts, like joints.",
            "example": "As you swap the keyboard, articulate each step out loud clearly enough that your partner could repeat it back accurately.",
        },
        "warm_up": "Ribbon cables that connect keyboards to a motherboard are thin and fragile. Why do you think techs are told to lift the connector latch instead of just pulling the cable out?",
        "mini_lesson": [
            {"heading": "What Sends Keyboards to the Bench", "body": "Common keyboard tickets include spilled liquid, missing or sticky keys, and keys that don't register at all after enough wear. Liquid damage is the trickiest, since it can look fine on the surface but corrode the ribbon connector or the board underneath over time, which is why a keyboard swap sometimes needs a second look even after the obvious fix."},
            {"heading": "Removal Without Damage", "body": "Keyboards are usually held in with screws underneath the case and connect to the motherboard through one or more ribbon cables. These connectors have a small latch that flips up to release the cable; yanking the cable straight out without releasing the latch is the single most common way to tear or damage it. Once loose, the cable should slide out easily with almost no resistance."},
            {"heading": "Narrating While You Work", "body": "Talking through each step out loud while you work isn't just for demonstrations, it forces you to slow down and notice details you might otherwise skip past on autopilot. It's also exactly what a good repair log relies on: being able to clearly describe, in words, exactly what you did and in what order."},
        ],
        "activity": {
            "title": "Keyboard Swap Relay",
            "instructions": "In pairs, one student removes and replaces a keyboard on a practice chassis using the iFixit guide while narrating every step out loud; their partner acts as an inspector, checking each ribbon-cable step for the latch-release method before letting them continue. Log the start and finish time for each swap as an early exercise in repair log habits, then switch roles.",
        },
        "application": {
            "type": "case_study",
            "title": "The Torn Connector",
            "scenario": "Running behind schedule during a timed practice swap, a Technician-level student grabs the keyboard's ribbon cable and pulls it straight out of its connector to save time, skipping the small latch entirely. The cable tears slightly at the edge and now sits loosely in the connector, making the keyboard type intermittently even after the new keyboard goes in and the old ribbon gets reused for testing. The student has to explain to their supervisor what happened before ordering a replacement ribbon cable.",
            "task": "Explain exactly what step was skipped and why it caused the tear, and write the one sentence you'd want this student to say differently next time they feel rushed during a ribbon-cable step.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What's the safest way to disconnect a keyboard ribbon cable?", "choices": ["A. Pull the cable straight out quickly", "B. Release the connector's latch first, then slide the cable out", "C. Cut the cable and replace the whole connector", "D. Twist the cable back and forth until it comes loose"], "answer": "B"},
                {"type": "multiple_choice", "q": "Why might a keyboard need a second look even after an obvious liquid spill is cleaned up?", "choices": ["A. Liquid never causes lasting damage", "B. Liquid can corrode the ribbon connector or board underneath over time", "C. The keyboard always needs replacing regardless of the spill", "D. It doesn't, cleaning it is always the complete fix"], "answer": "B"},
                {"type": "short_answer", "q": "Why does narrating a repair step out loud help build a stronger repair log habit?", "sample_answer": "Narrating forces you to put your actions into clear words in the moment, which is the same skill needed to write a specific, accurate repair log entry instead of a vague one after the fact."},
            ],
        },
        "exit_ticket": {"prompt": "Describe, in one or two sentences, the exact ribbon cable step you'd want a brand-new Apprentice to be extra careful with."},
        "slide_bullets": [
            "Common keyboard tickets: spills, missing/sticky keys, dead keys",
            "Liquid damage can hide corrosion under the surface",
            "Release the ribbon connector's latch, don't yank the cable",
            "Narrate steps out loud while working",
            "Log start/finish time as an early repair-log habit",
            "Switch roles: repair tech and inspector",
        ],
    },
    {
        "day": 29,
        "unit": 2,
        "lesson_in_unit": 11,
        "title": "Daughterboards: The Small Board With a Big Job",
        "objectives": [
            "I can explain what a daughterboard is and why it exists separately from the motherboard.",
            "I can identify common symptoms that point to a failing daughterboard.",
            "I can describe a testing plan to isolate a daughterboard problem before ordering a part.",
        ],
        "vocab": [
            {"word": "Daughterboard", "definition": "A small circuit board connected to the motherboard that handles one specific job, like the charging port or headphone jack.",
             "example": "When only the headphone jack stops working but everything else on the Chromebook runs fine, the audio daughterboard is a likely suspect.",
             "syllables": "DAW-ter-bord", "morphology": "Compound word: 'daughter' (a smaller unit branching off a larger one) + 'board' (circuit board) — named by analogy to the 'motherboard' it connects to."},
        ],
        "academic_vocab": {
            "word": "Isolate",
            "definition": "To separate one possible cause from everything else so you can test it on its own.",
            "syllables": "EYE-suh-late",
            "morphology": "Latin insula (island) — literally 'to make into an island,' i.e., to set something apart by itself.",
            "example": "Testing with a different charger and cable first helps you isolate whether the daughterboard is really the problem.",
        },
        "warm_up": "Why might it be cheaper and easier for a manufacturer to put the charging port on its own small separate board instead of building it directly into the motherboard?",
        "mini_lesson": [
            {"heading": "What a Daughterboard Does", "body": "A daughterboard is a small circuit board that branches off the main motherboard to handle one specific job, most often the charging port, the headphone jack, or sometimes a side USB port or speaker. Manufacturers build these as separate small boards because it's far cheaper and faster to replace one small failing part than to replace an entire motherboard over a single broken port."},
            {"heading": "Common Daughterboard Symptoms", "body": "Typical symptoms include a device that won't charge even though the battery and the charger both test fine on other devices, no sound from the headphone jack while internal speakers still work, or one USB port that's dead while the rest of the ports function normally. These symptoms are localized, meaning most of the device works fine except for one specific function tied to that board."},
            {"heading": "Diagnose Before You Order", "body": "Before ordering a replacement daughterboard, test with a different charger and cable to rule out those first, and check whether the symptom is isolated to just that one port or jack. This diagnostic step is exactly the kind of judgment call that separates a Level 3 Lead Tech from someone just swapping parts and hoping, and it saves the department money on parts that weren't actually the problem."},
        ],
        "activity": {
            "title": "Mystery Symptom Diagnosis",
            "instructions": "Set up station cards with symptoms like 'won't charge with any cable,' 'no sound from headphone jack only,' and 'one USB port dead.' In small groups, students decide the most likely culprit (battery, charger, daughterboard, or motherboard) for each and write out the testing steps they'd do first to confirm it before ever ordering a replacement part.",
        },
        "application": {
            "type": "real_world_problem",
            "title": "Charges Here, Not There",
            "scenario": "A student reports their Chromebook charges fine overnight at home using the charger that came with it, but never charges when plugged into the classroom charging cart's built-in USB-C cable. The battery itself tests healthy and holds a charge fine once it's actually topped up. Two other Chromebooks on the same cart slot charge normally with the same cable. A brand-new daughterboard costs the department $38 and about 20 minutes of labor to install.",
            "task": "List the tests you'd run before ordering that $38 daughterboard, in order, and explain what result from each test would actually justify replacing the daughterboard versus pointing to a different cause.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What does a daughterboard typically handle?", "choices": ["A. The device's entire operating system", "B. One specific function, like the charging port or headphone jack", "C. Wi-Fi connectivity only", "D. The LCD panel's backlight"], "answer": "B"},
                {"type": "multiple_choice", "q": "A device won't charge with any cable or charger tested, but the battery reads healthy. What's the most likely area to check?", "choices": ["A. The LCD panel", "B. The charging port daughterboard", "C. The keyboard ribbon cable", "D. The bezel clips"], "answer": "B"},
                {"type": "short_answer", "q": "Why do techs test with a different charger and cable before deciding a daughterboard is the problem?", "sample_answer": "Testing with known-good chargers and cables rules out simpler, cheaper causes first, so the tech doesn't order and install an unnecessary daughterboard when the real problem was just a bad cable or charger."},
            ],
        },
        "exit_ticket": {"prompt": "If a device has no sound from its headphone jack but the internal speakers work fine, what's your first guess and why?"},
        "slide_bullets": [
            "Daughterboard = small board handling one specific job",
            "Cheaper to replace one small board than the whole motherboard",
            "Symptoms are localized to one function or port",
            "Test with known-good cables/chargers first",
            "Diagnose before ordering a replacement part",
            "This is Level 3 Lead Tech-level judgment",
        ],
    },
    {
        "day": 30,
        "unit": 2,
        "lesson_in_unit": 12,
        "title": "Daughterboard Replacement Lab",
        "objectives": [
            "I can safely replace a daughterboard following an iFixit guide.",
            "I can test a replaced daughterboard's function before closing the case.",
            "I can write a short, accurate repair log draft for a completed repair.",
        ],
        "vocab": [
            {"word": "Daughterboard", "definition": "A small circuit board connected to the motherboard that handles one specific job, like the charging port or headphone jack.",
             "example": "Today's lab replaces a charging-port daughterboard on a practice Chromebook using the iFixit guide.",
             "syllables": "DAW-ter-bord", "morphology": "Compound word: 'daughter' (a smaller unit branching off a larger one) + 'board' (circuit board) — named by analogy to the 'motherboard' it connects to."},
        ],
        "academic_vocab": {
            "word": "Verify",
            "definition": "To check that something is true, accurate, or working correctly.",
            "syllables": "VER-uh-fy",
            "morphology": "Latin verus (true) + -ficare (to make) — literally 'to make true,' i.e., to confirm.",
            "example": "After installing the new daughterboard, you'll verify the port or jack actually works before closing the case.",
        },
        "warm_up": "Why might it help to take a photo of a ribbon cable's orientation before disconnecting it, instead of trusting yourself to remember?",
        "mini_lesson": [
            {"heading": "Safety First, Then the Swap", "body": "Just like with keyboard and battery work, daughterboard replacement starts with disconnecting the battery connector first, this removes any risk of a short while the small board is exposed. The daughterboard itself is usually held by one or two tiny screws and connects through a small ribbon cable, note its orientation, or snap a photo, before disconnecting so it goes back exactly the same way."},
            {"heading": "Reassembly & Testing", "body": "After installing the new daughterboard and reconnecting its ribbon cable, reconnect the battery and test the specific function before closing the case fully, plug in a charger if it's a charging port, or plug in headphones if it's an audio board. A repair isn't complete just because the board looks seated correctly; it's complete once the function it controls is confirmed working."},
            {"heading": "Model Variation Matters", "body": "Screw counts, board shapes, and even which side a daughterboard sits on can vary meaningfully between Chromebook models, which is exactly why this class leans on iFixit's exact, photo-based guides instead of general instructions. A guide written for the wrong model can send you down the wrong path fast."},
        ],
        "activity": {
            "title": "Guided Daughterboard Swap",
            "instructions": "Using the iFixit guide's reference photos, pairs disconnect the battery, remove and replace the practice daughterboard, and test the port or jack function before closing the chassis. Once tested and working, each pair writes a two-line repair log draft entry noting the symptom, the part replaced, and the test result.",
        },
        "application": {
            "type": "simulation",
            "title": "Reading the Meter",
            "scenario": "After installing a replacement charging-port daughterboard, a student plugs in the charger and checks the on-screen charging indicator and a USB power meter inline with the cable. A healthy charging connection on this model should show between 4.75V and 5.25V and at least 1.5A once charging begins. The meter reads 5.0V and 1.8A within ten seconds of plugging in, and the on-screen battery icon shows the little lightning bolt indicating it's charging.",
            "task": "Using the numbers from the meter, decide whether this daughterboard replacement passes the test, and explain what reading (specific voltage or amperage range) would have told you the repair still wasn't complete.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What should be disconnected before working on a daughterboard, and why?", "choices": ["A. The Wi-Fi antenna, to avoid interference", "B. The battery connector, to remove the risk of a short", "C. The bezel, because it's unrelated", "D. Nothing needs to be disconnected first"], "answer": "B"},
                {"type": "multiple_choice", "q": "When is a daughterboard replacement actually considered complete?", "choices": ["A. As soon as the board looks seated correctly", "B. Once the specific function it controls is tested and confirmed working", "C. As soon as the case is closed", "D. When the screws are back in, regardless of testing"], "answer": "B"},
                {"type": "short_answer", "q": "Why does this class use model-specific iFixit guides instead of general daughterboard replacement instructions?", "sample_answer": "Screw counts, board shapes, and layouts vary between Chromebook models, so a guide written for the wrong model could lead a tech to miss a step or damage a part that a model-specific, photo-based guide would have caught."},
            ],
        },
        "exit_ticket": {"prompt": "Write the two-line repair log draft you'd submit for today's daughterboard swap."},
        "slide_bullets": [
            "Disconnect the battery before daughterboard work",
            "Photo or note ribbon cable orientation first",
            "Reconnect and test the specific function before closing case",
            "Complete = tested and working, not just reassembled",
            "Model-specific guides matter, screw counts vary",
            "Write a short repair log draft after each repair",
        ],
    },
    {
        "day": 31,
        "unit": 2,
        "lesson_in_unit": 13,
        "title": "Internal Components Wrap-Up: Repair or Move On?",
        "objectives": [
            "I can summarize the internal repair skills built this week (battery, keyboard, daughterboard).",
            "I can explain the basic idea behind deciding whether a repair is worth doing.",
            "I can apply a simple repair-or-scrap gut-check to a sample device case.",
        ],
        "vocab": [
            {"word": "Repair-vs-Scrap", "definition": "The decision process technicians use to figure out whether fixing a device is worth the cost and time, or whether it makes more sense to scrap it for usable parts.",
             "example": "An old Chromebook needing three separate repairs might fail the repair-vs-scrap test even if each individual part is cheap.",
             "syllables": "ree-PAIR vur-sus SKRAP", "morphology": "'Repair' (Latin re- + parare, 'to make ready again') + 'vs.,' short for Latin versus (turned against); 'scrap' comes from Old Norse skrap (bits, scraps left over)."},
        ],
        "academic_vocab": {
            "word": "Assess",
            "definition": "To carefully weigh the facts of a situation in order to make a judgment or decision.",
            "syllables": "uh-SESS",
            "morphology": "Latin ad- (to) + sedere (to sit) — originally 'to sit beside' a judge, as in assessing value for taxation.",
            "example": "You'll assess whether a device is worth repairing or better off scrapped, based on cost, condition, and how common the model still is.",
        },
        "warm_up": "If a $20 part could fix an old device, is that automatically worth doing? What else might matter besides the price of the part?",
        "mini_lesson": [
            {"heading": "This Week, Recapped", "body": "This week covered three internal repairs: batteries, keyboards, and daughterboards, each with its own safety concerns and its own diagnostic questions before touching a screwdriver. Moving from shadowing these repairs to doing them solo and confidently is exactly what separates an Apprentice from a Technician, the next step up the performance ladder this course tracks."},
            {"heading": "When a Repair Stops Making Sense", "body": "Not every broken device is worth fixing. Repair-vs-scrap thinking weighs the cost of the part and the time it takes against how much useful life the device has left and whether the model is still common enough in the fleet to matter. Sometimes the smarter move is scrapping an old device for its still-good parts, like a screen, keyboard, or RAM, to keep other devices running instead."},
            {"heading": "A Quick Gut-Check", "body": "Three questions guide this call every time: is the needed part actually available and affordable, is the rest of the device otherwise in good shape, and is this model still useful enough to the district to be worth keeping in service. Week 8 goes much deeper into this decision and how it gets documented, but this is the starting framework."},
        ],
        "activity": {
            "title": "Repair or Scrap? Case Files",
            "instructions": "Give each small group a case file describing a device's age, damage, and estimated repair cost. Using the three-question gut-check, groups decide repair or scrap and present their reasoning to the class as if presenting at a real inventory review meeting.",
        },
        "application": {
            "type": "real_world_problem",
            "title": "Three Repairs or One Replacement?",
            "scenario": "A five-year-old Chromebook needs three separate fixes to be fully usable again: a $22 replacement keyboard, a $15 battery, and about 45 minutes of labor across both repairs. The model is old enough that only a handful of them are still in service in the building. A comparable refurbished replacement device costs the district $95 and would arrive fully working with no labor needed on the help desk's part.",
            "task": "Using the three-question gut-check from today's lesson (part cost/availability, overall device condition, and how useful the model still is to the fleet), decide repair or scrap for this device and justify the call in two or three sentences, as if presenting to Ms. Faraday.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What does the repair-vs-scrap decision weigh?", "choices": ["A. Only the price of the replacement part", "B. Cost and time of repair against the device's remaining usefulness", "C. Only whether the device still turns on", "D. Whether the device has ever been enrolled"], "answer": "B"},
                {"type": "multiple_choice", "q": "Why might a district scrap an old device instead of repairing it, even if the part itself is cheap?", "choices": ["A. Cheap parts are always worth using no matter what", "B. The device's model may no longer be useful enough in the fleet to justify the time", "C. Scrapping is always required by district policy", "D. Old devices can never be repaired regardless of condition"], "answer": "B"},
                {"type": "short_answer", "q": "Name the three gut-check questions used to decide repair vs. scrap.", "sample_answer": "Is the needed part available and affordable, is the rest of the device otherwise in good shape, and is the model still useful enough to the district to be worth keeping in service."},
            ],
        },
        "exit_ticket": {"prompt": "Pick one device you've worked on this week. Would you repair it or scrap it, and why?"},
        "slide_bullets": [
            "This week: batteries, keyboards, daughterboards",
            "Apprentice -> Technician: doing repairs solo and confidently",
            "Repair-vs-scrap: cost/time vs. remaining usefulness",
            "Sometimes scrapping for parts beats repairing",
            "Gut-check: part cost, device condition, model usefulness",
            "Deeper dive coming in Week 8",
        ],
    },
    {
        "day": 32,
        "unit": 2,
        "lesson_in_unit": 14,
        "title": "Serial Numbers & Asset Tags: Every Device Has an Identity",
        "objectives": [
            "I can explain what a serial number is and where to find one on a Chromebook.",
            "I can explain what an asset tag adds on top of a serial number.",
            "I can use the Crucial Advisor tool to check compatible parts for a specific device model.",
        ],
        "vocab": [
            {"word": "Serial Number", "definition": "A unique number assigned by the manufacturer that identifies one specific physical device, never duplicated on any other unit.",
             "example": "Two Chromebooks of the exact same model still have two completely different serial numbers.",
             "syllables": "SEER-ee-ul NUM-ber", "morphology": "Latin series (a row, chain, or sequence) + -al (adjective-forming suffix) — describes a number that marks one item's unique place in a sequence."},
            {"word": "Asset Tag", "definition": "A sticker or label a school district adds on top of the serial number to track a device in its own inventory system.",
             "example": "The manufacturer's serial number identifies the device to Google; the district's asset tag identifies it to us.",
             "syllables": "ASS-et tag", "morphology": "'Asset' traces to Old French assez (enough, sufficient), later meaning a valuable possession; 'tag' is a Germanic-origin word for a small label attached to an item."},
        ],
        "academic_vocab": {
            "word": "Distinguish",
            "definition": "To recognize or explain the difference between two similar things.",
            "syllables": "dih-STING-gwish",
            "morphology": "Latin di- (apart) + stinguere (to prick, mark) — literally 'to mark apart' from one another.",
            "example": "You'll distinguish what a serial number identifies versus what a district's own asset tag is used for.",
        },
        "warm_up": "If two Chromebooks are the exact same model, what's still different between them, and why would that matter for tracking?",
        "mini_lesson": [
            {"heading": "What a Serial Number Is", "body": "A serial number is a unique code assigned by the manufacturer that identifies one specific physical device, no two devices, even the same model, ever share one. It's usually printed on the bottom of the Chromebook, viewable in ChromeOS settings, and visible in the Google Admin console for enrolled devices. It's the manufacturer's way of tracking a device across its whole life."},
            {"heading": "What an Asset Tag Adds", "body": "An asset tag is the district's own sticker or number layered on top of the serial number, connecting the device to internal records like purchase date, warranty status, and which classroom or cart it's assigned to. Where the serial number identifies a device to the world, the asset tag identifies it specifically to us, and it's what shows up first in an inventory audit."},
            {"heading": "Ordering Compatible Parts: Crucial Advisor", "body": "Crucial Advisor is a real online tool that looks up compatible RAM and storage upgrades for a specific device model, so a tech can confirm exactly what to order instead of guessing. Before requesting any replacement part for internal upgrades, checking a tool like this against the exact model saves the department from ordering the wrong component."},
        ],
        "activity": {
            "title": "Tag and Track",
            "instructions": "Have students locate the serial number on their lab Chromebook (bottom label and in ChromeOS settings) and enter it, along with a mock asset tag number you provide, into a shared practice inventory spreadsheet. Then have them use the Crucial Advisor tool to look up compatible RAM or storage options for their assigned device model and record what they find.",
        },
        "application": {
            "type": "realistic_fiction",
            "title": "The Warranty Claim That Bounced Back",
            "scenario": "A tech submits a warranty claim for a Chromebook with a failed daughterboard, typing the district's asset tag number into the serial number field on the manufacturer's claim form by mistake, since both numbers were sitting on a sticky note together. Two weeks later the claim comes back rejected: 'No device found matching this serial number.' The tech spends twenty minutes trying to figure out what went wrong before realizing the two numbers got swapped, and has to resubmit the claim with the correct serial number pulled fresh from the device itself.",
            "task": "Explain, in your own words, why mixing up the serial number and the asset tag caused the claim to bounce, and describe one habit from today's lesson (like checking ChromeOS settings or the Admin console directly) that would have caught the mistake before the claim was ever submitted.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What makes a serial number different from an asset tag?", "choices": ["A. They are exactly the same thing", "B. Serial number is manufacturer-assigned and unique; asset tag is the district's own added tracking label", "C. Asset tags are assigned before serial numbers exist", "D. Only enrolled devices have serial numbers"], "answer": "B"},
                {"type": "multiple_choice", "q": "What does the Crucial Advisor tool help a tech do?", "choices": ["A. Look up compatible RAM/storage upgrades for a specific device model", "B. Build a ChromeOS recovery drive", "C. Write a repair log entry", "D. Deprovision an enrolled device"], "answer": "A"},
                {"type": "short_answer", "q": "Why does a school district add its own asset tag when a manufacturer serial number already exists?", "sample_answer": "The serial number identifies the device to the manufacturer, but the asset tag connects it to the district's own inventory records, like which classroom or cart it belongs to and its purchase and warranty history."},
            ],
        },
        "exit_ticket": {"prompt": "Where did you find your lab Chromebook's serial number, and why do you think it's placed there?"},
        "slide_bullets": [
            "Serial number = unique manufacturer ID, never duplicated",
            "Found on device bottom, in ChromeOS settings, and Admin console",
            "Asset tag = district's own inventory label on top of serial number",
            "Asset tag links to purchase, warranty, and assignment records",
            "Crucial Advisor: real tool for checking compatible RAM/storage",
            "Confirm parts before ordering, don't guess",
        ],
    },
    {
        "day": 33,
        "unit": 2,
        "lesson_in_unit": 15,
        "title": "Writing a Repair Log That Actually Helps the Next Tech",
        "objectives": [
            "I can explain why repair logs matter for accountability and for future troubleshooting.",
            "I can identify what belongs in a complete, professional repair log entry.",
            "I can rewrite a vague repair log entry into a clear, useful one.",
        ],
        "vocab": [
            {"word": "Repair Log", "definition": "A written record of what was wrong with a device, what was done to fix it, who did it, and when.",
             "example": "A repair log entry that just says 'fixed it' doesn't help the next tech at all if the same device comes back.",
             "syllables": "ree-PAIR log", "morphology": "Latin re- (again) + parare (to make ready, prepare) form 'repair' (to make ready again); 'log' comes from an old nautical term for a ship's written voyage record."},
        ],
        "academic_vocab": {
            "word": "Clarify",
            "definition": "To make something clearer or easier to understand, often by removing vague or confusing wording.",
            "syllables": "KLA-ruh-fy",
            "morphology": "Latin clarus (clear, bright) + -ficare (to make) — literally 'to make clear.'",
            "example": "You'll clarify a vague repair log entry like 'fixed it' into one that actually explains what happened and why.",
        },
        "warm_up": "If a device comes back broken a month after being 'fixed,' what information would you want from the last repair to figure out what happened?",
        "mini_lesson": [
            {"heading": "Why Repair Logs Matter", "body": "A repair log protects the tech who did the work by proving exactly what was done and by whom, helps the next person diagnose a recurring problem faster instead of starting from zero, and is often required for warranty claims and official district records. Consistent, honest logging is part of what the Professionalism & Service portion of this course's grade is actually measuring."},
            {"heading": "What Belongs in a Good Entry", "body": "A complete repair log entry includes the device's serial number and asset tag, the date, the symptom as the user described it, what the tech actually diagnosed, exactly which part or parts were replaced, the tech's name and level, and any follow-up needed. It reads like the plain-language ticket notes from Phase 1, specific and useful to a stranger reading it cold."},
            {"heading": "Common Mistakes to Avoid", "body": "The most common problems are vague entries like 'fixed it' that explain nothing, skipping the device's serial number entirely (which becomes a much bigger problem, as next week's reading shows), and recording only what was done without explaining why, which leaves the next tech guessing at the actual cause if the problem returns."},
        ],
        "activity": {
            "title": "Repair Log Rewrite",
            "instructions": "Hand out three realistic but badly written repair log entries (vague, missing serial numbers, or missing the 'why'). In pairs, students rewrite each into a complete, professional entry using today's checklist, then trade with another pair to check whether their rewrite would actually help a stranger reading it cold.",
        },
        "application": {
            "type": "case_study",
            "title": "The Entry That Said Nothing",
            "scenario": "Three weeks ago, a repair log entry for a Chromebook read only: 'Fixed it. Works now.' No serial number, no symptom, no part replaced, no tech name. This week, the same device comes back with the exact same complaint from a different student. Whoever handles the ticket this time has no idea whether the original problem was ever actually fixed, what was tried before, or whether this is a repeat failure of the same part.",
            "task": "Rewrite that vague entry into a complete, professional repair log entry using today's checklist, inventing reasonable specific details (symptom, diagnosis, part, tech name) that would have actually helped the tech handling it this week.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "Why does a repair log protect the tech who did the work?", "choices": ["A. It hides mistakes from supervisors", "B. It proves exactly what was done, by whom, and when", "C. It replaces the need for testing a repair", "D. It's only useful for warranty claims, nothing else"], "answer": "B"},
                {"type": "multiple_choice", "q": "Which of these is a problem with a repair log entry that just says 'fixed it'?", "choices": ["A. It's too long", "B. It gives the next tech no useful information if the problem returns", "C. It's technically against ChromeOS policy", "D. It always means the repair failed"], "answer": "B"},
                {"type": "short_answer", "q": "List three things that belong in a complete repair log entry.", "sample_answer": "Any three of: device serial number and asset tag, date, symptom reported, diagnosis, part(s) replaced, tech's name/level, and follow-up needed."},
            ],
        },
        "exit_ticket": {"prompt": "Rewrite this vague log entry into a better one: 'Chromebook was broken. Fixed it. Works now.'"},
        "slide_bullets": [
            "Repair logs protect techs and help the next person",
            "Required for warranty claims and district records",
            "Include: serial/asset tag, date, symptom, diagnosis, part, tech name, follow-up",
            "Avoid vague entries like 'fixed it'",
            "Never skip the serial number",
            "Explain the why, not just the what",
        ],
    },
    {
        "day": 34,
        "unit": 2,
        "lesson_in_unit": 16,
        "title": "Inventory Day: Why the Log Matters When Something Goes Missing",
        "objectives": [
            "I can explain how a school district's inventory audit cross-checks devices against records.",
            "I can identify what happens, practically, when a device isn't logged correctly.",
            "I can trace a real accountability gap back through a repair log.",
        ],
        "vocab": [
            {"word": "Repair Log", "definition": "A written record of what was wrong with a device, what was done to fix it, who did it, and when.",
             "example": "When a device goes missing, the repair log is often the only paper trail showing where it was last.",
             "syllables": "ree-PAIR log", "morphology": "Latin re- (again) + parare (to make ready, prepare) form 'repair' (to make ready again); 'log' comes from an old nautical term for a ship's written voyage record."},
            {"word": "Serial Number", "definition": "A unique number assigned by the manufacturer that identifies one specific physical device, never duplicated on any other unit.",
             "example": "A repair entry without a serial number is nearly useless for finding one specific device among hundreds.",
             "syllables": "SEER-ee-ul NUM-ber", "morphology": "Latin series (a row, chain, or sequence) + -al (adjective-forming suffix) — describes a number that marks one item's unique place in a sequence."},
        ],
        "academic_vocab": {
            "word": "Reconcile",
            "definition": "To compare two sets of records and resolve any differences between them.",
            "syllables": "REK-un-syle",
            "morphology": "Latin re- (again) + conciliare (to bring together, unite) — literally 'to bring back together.'",
            "example": "During the inventory audit, the crew has to reconcile the Google Admin console's list of devices with what's physically sitting on the cart.",
        },
        "warm_up": "If a device went missing from a school cart and nobody had written anything down about it recently, where would you even start looking?",
        "mini_lesson": [
            {"heading": "How an Inventory Audit Works", "body": "A real inventory audit cross-checks every device's asset tag and serial number against both the Google Admin console and the district's own spreadsheet or system, confirming each device is where it's supposed to be and assigned to the right cart or room. Gaps show up as devices on the list that can't be physically found, or devices found that aren't properly on the list at all."},
            {"heading": "What Happens Without a Log", "body": "When a device isn't logged correctly, there's no trail showing who last had it, why it was moved, or where it went, which turns a small oversight into a real cost for the district and a real headache for whoever has to track it down. Today's reading shows exactly how this plays out."},
            {"heading": "Reading Preview", "body": "In today's installment, the crew discovers a device missing during an inventory audit with no serial number properly logged for a recent repair. As you read, pay attention to how they trace it back, and notice every point where a simple logging habit would have prevented the problem entirely."},
        ],
        "activity": {
            "title": "Trace the Trail",
            "instructions": "After reading, have groups reconstruct the missing-device timeline from the story, identifying every point where logging the serial number properly would have prevented the confusion. Each group presents their timeline to the class, highlighting the single moment they think mattered most.",
        },
        "application": {
            "type": "simulation",
            "title": "Cart 5 Cross-Check",
            "scenario": "An inventory spreadsheet lists five devices assigned to Cart 5, each with a serial number and asset tag on record. A physical count of Cart 5 turns up only four devices, and one of the four physically present doesn't match any serial number on the spreadsheet at all.",
            "task": "Using the audit process from today's lesson, describe the exact order you'd check things in (Google Admin console, spreadsheet, recent repair log entries, sign-in sheets) to explain both the missing device and the unmatched one.",
        },
        "reading": {
            "type": "graphic_novel",
            "title": "Ticket #5: Unaccounted For",
            "body": """PANEL 1: Wide shot of the media center storage room. Carts of Chromebooks line the walls, each slot labeled. Ms. Faraday stands with a clipboard next to Sam and Jordan.
CAPTION: Quarterly inventory audit day.
MS. FARADAY: "We're cross-checking every device on Cart 3 against the spreadsheet. Should be quick."

PANEL 2: Jordan scans serial numbers with a barcode scanner while Sam checks them off on a tablet. One slot on the cart sits empty.
JORDAN: "Cart 3, slot 14 is empty. According to this it should be here."
SAM: "Check the spreadsheet again. Maybe it's just out on loan."

PANEL 3: Close on the tablet screen. The last entry for that device's row is blank where the serial number should be.
CAPTION: The last repair entry for slot 14's device: no serial number logged.
SAM (frowning): "That's a problem. No serial number means we can't even confirm which device this note is about."

PANEL 4: Sam flips back through paper repair log entries from the past month, running a finger down the page.
SAM: "Somebody did a quick keyboard fix on a Cart 3 device a few weeks back. Didn't log the serial. Didn't log where it went after."

PANEL 5: Jordan looks worried, checking their own recent entries nervously.
JORDAN: "Wasn't me, right?"
SAM: "No. But it could've been. This is exactly why we don't skip it, even on a two-minute fix."

PANEL 6: Ms. Faraday joins them, looking over the log page.
MS. FARADAY: "Who signed the desk out that day?"
SAM: "Let's check the sign-in sheet next to the log."

PANEL 7: They cross-reference the sign-in sheet with the vague log entry, narrowing down a name and a rough time.
CAPTION: Piece by piece, the trail comes back together.
SAM: "Okay. This matches a keyboard swap logged without a serial number. Let's check who it was loaned to after."

PANEL 8: They find the device in a nearby classroom, sitting on a cart that was never updated in the system, no one took it, it was just never logged back in.
JORDAN: "It's right here. It was never gone. Just never logged."

PANEL 9: Back in the storage room, Ms. Faraday updates the spreadsheet herself as Sam and Jordan watch.
MS. FARADAY: "Nothing about this was malicious. It just cost us two hours we didn't need to spend."

PANEL 10: Sam looks at Jordan directly.
SAM: "Every device. Every time. Even the two-minute fixes. This is what happens when we don't."
JORDAN: "Got it. No exceptions."

PANEL 11: Final panel, wide shot of the storage room, the cart now fully accounted for, everyone back to work.
CAPTION: Slot 14, accounted for. Log updated.""",
            "questions": [
                "What specific gap in the repair log started the whole missing-device problem?",
                "How did Sam and Jordan use the sign-in sheet together with the repair log to trace what happened?",
                "Ms. Faraday says 'nothing about this was malicious.' Why is that an important distinction from the crew treating it like someone did something wrong on purpose?",
                "How much time did the missing log entry end up costing the team, and why does that matter even though the device was never actually lost?",
                "What would you tell a new Apprentice tech to always double-check before closing out any repair, based on this story?",
            ],
        },
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What does an inventory audit cross-check devices against?", "choices": ["A. Only the manufacturer's website", "B. The Google Admin console and the district's own tracking system", "C. Nothing, it's a visual count only", "D. The student handbook"], "answer": "B"},
                {"type": "multiple_choice", "q": "In the reading, what was the root cause of the missing device confusion?", "choices": ["A. The device was stolen", "B. A repair entry was logged without the device's serial number", "C. The device was never actually assigned to Cart 3", "D. Ms. Faraday misplaced the spreadsheet"], "answer": "B"},
                {"type": "short_answer", "q": "Explain how Sam and Jordan traced the missing device back to its actual location.", "sample_answer": "They found a repair log entry missing a serial number, cross-referenced it with the sign-in sheet to figure out who had signed out the desk around that time, and used that to locate the device on a cart in a classroom where it had simply never been logged back in."},
            ],
        },
        "exit_ticket": {"prompt": "What's the one habit from today's reading you'll commit to on every repair, no matter how small?"},
        "slide_bullets": [
            "Inventory audits cross-check devices against Admin console and district records",
            "Missing logs create real accountability gaps",
            "Today's reading: Ticket #5, Unaccounted For",
            "A missing serial number can turn a small fix into hours of tracking",
            "Not malicious, just costly, and fully preventable",
            "No exceptions: log every device, every time",
        ],
    },
    {
        "day": 35,
        "unit": 2,
        "lesson_in_unit": 17,
        "title": "Repair vs. Scrap: Making the Call",
        "objectives": [
            "I can apply a full framework for deciding whether to repair or scrap a device.",
            "I can explain the concept of a 'parts donor' device.",
            "I can document a repair-vs-scrap decision in proper repair log format.",
        ],
        "vocab": [
            {"word": "Repair-vs-Scrap", "definition": "The decision process technicians use to figure out whether fixing a device is worth the cost and time, or whether it makes more sense to scrap it for usable parts.",
             "example": "The repair-vs-scrap call on an old, heavily damaged Chromebook might be to keep it only for its still-good keyboard and RAM.",
             "syllables": "ree-PAIR vur-sus SKRAP", "morphology": "'Repair' (Latin re- + parare, 'to make ready again') + 'vs.,' short for Latin versus (turned against); 'scrap' comes from Old Norse skrap (bits, scraps left over)."},
        ],
        "academic_vocab": {
            "word": "Rationale",
            "definition": "The set of reasons behind a decision, explained clearly enough for someone else to follow the thinking.",
            "syllables": "rash-uh-NAL",
            "morphology": "Latin ratio (reasoning, calculation) + -alis (adjective-forming suffix) — related to 'ratio' and 'reason.'",
            "example": "When you make a repair-vs-scrap call, you'll write the rationale behind it, not just the final decision itself.",
        },
        "warm_up": "If you had a device that would cost more in parts and time to fix than it's realistically worth to the school, what would you do with it instead of throwing it away?",
        "mini_lesson": [
            {"heading": "The Full Framework", "body": "The complete repair-vs-scrap decision weighs part cost plus labor time against the device's remaining useful life and how common that model still is across the fleet. A device needing a $15 part and ten minutes of labor is an easy repair call; a device needing three separate repairs on a model the district barely uses anymore is a much harder sell, even if each individual part is cheap."},
            {"heading": "Salvage Value", "body": "A device that isn't worth repairing itself can still be worth keeping around as a 'parts donor,' its still-good screen, keyboard, RAM, or daughterboard can go straight into a future repair instead of being ordered new. This is a real cost-saving strategy districts use, not just a fallback option."},
            {"heading": "Documenting the Decision", "body": "The repair-vs-scrap call itself gets written down too, not just the repair or the scrap action, but why that call was made. This connects the repair log and the asset tag into one full lifecycle record: what happened to a device from the day it entered the fleet to the day it was finally retired."},
        ],
        "activity": {
            "title": "The Repair-vs-Scrap Board",
            "instructions": "Set up several device folders describing condition, age, and estimated repair cost at stations around the room. Acting as Level 3 Lead Techs, students visit each station, make and justify a repair-or-scrap call, and log their decision in proper repair-log format, including their reasoning, not just their verdict.",
        },
        "application": {
            "type": "real_world_problem",
            "title": "The Parts Donor Decision",
            "scenario": "Two nearly identical old Chromebooks come in the same week. Device A needs a $30 screen and has a healthy battery, working keyboard, and good hinges otherwise. Device B needs a $30 screen, a $15 battery, and has a cracked bezel that would need a $10 replacement, and this exact model is down to only two units left in the building's fleet.",
            "task": "Using the full repair-vs-scrap framework from today's lesson, decide what to do with each device, including whether Device B should become a parts donor for Device A, and write the repair-log-style rationale you'd document for each decision.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "What does the full repair-vs-scrap framework weigh?", "choices": ["A. Only the age of the device", "B. Part cost and labor time against remaining useful life and how common the model still is", "C. Only whether the device is enrolled", "D. Only the district's overall budget for the year"], "answer": "B"},
                {"type": "multiple_choice", "q": "What is a 'parts donor' device?", "choices": ["A. A brand-new device just added to the fleet", "B. A device not worth repairing itself but kept for its still-good usable parts", "C. A device that's been fully repaired and returned to service", "D. A device that's been enrolled but never assigned"], "answer": "B"},
                {"type": "short_answer", "q": "Why does the repair-vs-scrap decision itself need to be documented, not just the repair or scrap action?", "sample_answer": "Documenting the reasoning behind the decision creates a full lifecycle record for the device, showing not just what happened to it but why, which helps with accountability and future decisions about similar devices."},
            ],
        },
        "exit_ticket": {"prompt": "Describe a device from today's activity you called 'scrap' and explain the reasoning you'd write in its log entry."},
        "slide_bullets": [
            "Weigh cost/time against remaining useful life and fleet relevance",
            "Parts donor: scrapped device kept for still-good parts",
            "Salvage saves money on future repairs",
            "Document the decision itself, not just the action",
            "Repair log + asset tag = full device lifecycle record",
            "Practice: Level 3 Lead Tech-style calls at the scrap board",
        ],
    },
    {
        "day": 36,
        "unit": 2,
        "lesson_in_unit": 18,
        "title": "Full Teardown & Rebuild: Practice Before the Real Thing",
        "objectives": [
            "I can fully disassemble and reassemble a practice Chromebook in working order.",
            "I can write a complete repair log entry documenting a full teardown and rebuild.",
            "I can plan a beginner-friendly how-to guide for a common Chromebook problem.",
        ],
        "vocab": [
            {"word": "Repair Log", "definition": "A written record of what was wrong with a device, what was done to fix it, who did it, and when.",
             "example": "Today's teardown gets logged just like a real repair, start to finish.",
             "syllables": "ree-PAIR log", "morphology": "Latin re- (again) + parare (to make ready, prepare) form 'repair' (to make ready again); 'log' comes from an old nautical term for a ship's written voyage record."},
            {"word": "Serial Number", "definition": "A unique number assigned by the manufacturer that identifies one specific physical device, never duplicated on any other unit.",
             "example": "Even a practice teardown starts by recording the device's serial number, building the habit for good.",
             "syllables": "SEER-ee-ul NUM-ber", "morphology": "Latin series (a row, chain, or sequence) + -al (adjective-forming suffix) — describes a number that marks one item's unique place in a sequence."},
            {"word": "Asset Tag", "definition": "A sticker or label a school district adds on top of the serial number to track a device in its own inventory system.",
             "example": "A real teardown would also record the asset tag, so today's practice run notes one too.",
             "syllables": "ASS-et tag", "morphology": "'Asset' traces to Old French assez (enough, sufficient), later meaning a valuable possession; 'tag' is a Germanic-origin word for a small label attached to an item."},
            {"word": "Repair-vs-Scrap", "definition": "The decision process technicians use to figure out whether fixing a device is worth the cost and time, or whether it makes more sense to scrap it for usable parts.",
             "example": "Even a practice Chromebook can prompt the question: if this were real, would it be worth this much teardown effort?",
             "syllables": "ree-PAIR vur-sus SKRAP", "morphology": "'Repair' (Latin re- + parare, 'to make ready again') + 'vs.,' short for Latin versus (turned against); 'scrap' comes from Old Norse skrap (bits, scraps left over)."},
        ],
        "academic_vocab": {
            "word": "Synthesize",
            "definition": "To combine separate pieces of knowledge or skill into one connected whole.",
            "syllables": "SIN-thuh-size",
            "morphology": "Greek syn- (together) + tithenai (to place) — literally 'to place together.'",
            "example": "Today's full teardown asks you to synthesize everything this phase covered, screens, batteries, keyboards, and daughterboards, into one complete repair.",
        },
        "warm_up": "Why do you think techs practice a full teardown on a spare device before ever being trusted to open a real student's or teacher's Chromebook?",
        "mini_lesson": [
            {"heading": "Why Practice First", "body": "Practicing a complete teardown and rebuild on a non-live practice device, not a real student's or staff member's Chromebook, mirrors exactly how Level 3 Lead Techs earn the trust to do full teardowns independently: by proving clean, careful, complete work first where a mistake costs nothing but time."},
            {"heading": "What Counts as a Full Teardown", "body": "A full teardown means removing the bezel and LCD panel, the battery, the keyboard, and the daughterboard, everything this phase has covered separately, then reassembling all of it back into full working order, start to finish, using iFixit guides as the reference throughout, exactly like every lab before this one."},
            {"heading": "The Write-Up Is Part of the Job", "body": "This teardown's repair log entry gets graded like a real one: serial number and asset tag noted, each component's removal and reinstallation documented, and any issues encountered along the way written down honestly. This ties directly into both the Labs & Repair Skills and Capstone & Portfolio categories, since a strong write-up here is genuine practice for capstone-level documentation later this year."},
        ],
        "activity": {
            "title": "Full Teardown & Rebuild Practicum",
            "instructions": "Working individually or in pairs, students fully disassemble a practice Chromebook (bezel, LCD panel, battery, keyboard, daughterboard) and reassemble it back into full working order using iFixit guides as reference throughout. Afterward, each student writes a complete repair log entry documenting the process as if handing it off to another tech. For tonight's homework, assign a short how-to write-up: a beginner-friendly guide for one common Chromebook problem covered this phase (like a Powerwash, a sticky key, or a loose bezel), simple enough for someone with zero repair experience to follow.",
        },
        "application": {
            "type": "realistic_fiction",
            "title": "Sign-Off",
            "scenario": "After finishing a full teardown and rebuild on a practice Chromebook, well past what any single lesson this phase asked for on its own, a student named Diego closes the case, powers it on, and watches it boot cleanly on the first try. He writes his repair log entry slowly, double-checking the practice serial number against what he wrote down at the very start of the teardown. Ms. Faraday reviews it, reads through his documented steps for the bezel, battery, keyboard, and daughterboard, and nods. 'That's the whole phase, right there,' she says. 'Every piece you've been doing separately, now in one repair, written down like it matters, because it does.'",
            "task": "In two or three sentences, explain which single skill from this entire phase you think was hardest to learn well enough to trust yourself with, and why finishing this full teardown feels different from any single-component lab earlier in the phase.",
        },
        "reading": None,
        "quiz": {
            "questions": [
                {"type": "multiple_choice", "q": "Why does this class practice a full teardown on a non-live device first?", "choices": ["A. Because live devices are never allowed to be repaired at school", "B. It mirrors how techs earn the trust for independent full teardowns by proving careful work first", "C. Because practice devices are more valuable than real ones", "D. It's required by the manufacturer's warranty"], "answer": "B"},
                {"type": "multiple_choice", "q": "What components together make up a 'full teardown' as covered this phase?", "choices": ["A. Only the battery", "B. Bezel/LCD panel, battery, keyboard, and daughterboard", "C. Only the keyboard and bezel", "D. Only the daughterboard and battery"], "answer": "B"},
                {"type": "short_answer", "q": "How does today's repair log write-up connect to both the Labs & Repair Skills and Capstone & Portfolio grading categories?", "sample_answer": "The hands-on teardown itself demonstrates Labs & Repair Skills, while writing a complete, professional log entry documenting it is direct practice for the kind of clear documentation students will need for their capstone portfolio later in the course."},
            ],
        },
        "exit_ticket": {"prompt": "Which single step in today's teardown would you tell a brand-new Apprentice to be most careful with, and why?"},
        "slide_bullets": [
            "Full teardown: bezel/LCD panel, battery, keyboard, daughterboard",
            "Practice on non-live devices before real ones, every time",
            "Reassemble to full working order using iFixit guides",
            "Write a complete repair log entry, serial number and asset tag included",
            "Ties to Labs & Repair Skills and Capstone & Portfolio",
            "Homework: beginner-friendly how-to for a common Chromebook problem",
            "This closes out Phase 2, ACER Chromebook Repair certification focus",
        ],
    },
]

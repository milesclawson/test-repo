"""Shared helpers and course-wide constants for Whole Foods & Nutrition.

Every student-facing string is a bilingual pair made with T(en, es).
Teacher-only notes are plain English strings.
"""


def T(en, es):
    return {"en": en, "es": es}


COURSE = {
    "title": T("Whole Foods and Nutrition", "Alimentos Integrales y Nutrición"),
    "school": "ISD 197",
    "teacher": "Beth Coleman",
    "department": "Family and Consumer Science",
    "credit": "0.5",
    "length": "1 semester · 90 days · 48 minutes",
    "cert": "YouScience Nutrition and Wellness (Exam 2001)",
}

# 8 groups of 4 at 4 tables (2 groups per table). Edit here to change class layout.
GROUP_SIZE = 4
GROUPS = 8
ROLES = [
    {"role": T("Head Chef", "Jefe de cocina"),
     "job": T("Reads the recipe aloud, keeps the group on the work plan, and handles the stove or oven.",
              "Lee la receta en voz alta, mantiene al grupo en el plan de trabajo y maneja la estufa o el horno.")},
    {"role": T("Sous Chef", "Ayudante de cocina"),
     "job": T("Measures, mixes, and prepares ingredients with the Head Chef.",
              "Mide, mezcla y prepara los ingredientes junto con el Jefe de cocina.")},
    {"role": T("Safety and Sanitation Officer", "Oficial de seguridad e higiene"),
     "job": T("Checks that everyone washes hands, keeps raw and ready-to-eat foods apart, and sanitizes surfaces.",
              "Verifica que todos se laven las manos, separa los alimentos crudos de los listos para comer y desinfecta las superficies.")},
    {"role": T("Supplies and Cleanup Manager", "Encargado de materiales y limpieza"),
     "job": T("Gets and returns equipment, washes dishes, and leads the final station check.",
              "Trae y devuelve el equipo, lava los platos y dirige la revisión final de la estación.")},
]

# Standard 48-minute shapes (minutes). Used for slides, guides, and the lesson header.
DAY_SHAPE = [(5, "Bellringer", "Actividad de inicio"),
             (12, "Direct instruction", "Instrucción directa"),
             (10, "Guided practice", "Práctica guiada"),
             (16, "Independent practice", "Práctica independiente"),
             (5, "Exit ticket", "Boleto de salida")]
LAB_SHAPE = [(5, "Bellringer and group roles", "Actividad de inicio y roles"),
             (5, "Lab brief: safety focus and work plan", "Introducción: seguridad y plan de trabajo"),
             (28, "Cook", "Cocinar"),
             (7, "Cleanup and station check", "Limpieza y revisión de la estación"),
             (3, "Exit ticket", "Boleto de salida")]

CERT_OBJECTIVES = {
    "S1.1": "Analyze food and nutrition information, including USDA Dietary Guidelines and MyPlate",
    "S1.2": "Demonstrate proper portion sizes",
    "S1.3": "Six nutrient classes, functions, and food sources",
    "S1.4": "Compare food label information",
    "S1.5": "Teen wellness goals: fads, weight management, supplements",
    "S2.1": "Components of individual and family wellness",
    "S2.2": "Geography and climate affect food selection",
    "S2.3": "Economic factors affect food selection",
    "S2.4": "Legislation and regulations on food and nutrition",
    "S2.5": "Nutritive value and cost of snacks, fast food, balanced meals",
    "S3.1": "Foodborne illness; clean, separate, cook, chill",
    "S3.2": "Safely use and maintain kitchen equipment, tools, and knives",
    "S3.3": "Prepare nutritious foods using basic methods",
    "S3.4": "Resource management: cost, work plans, collaboration",
    "S3.5": "Increase and decrease recipes by yield",
    "S4.1": "Technology and techniques in producing, processing, and storing food",
    "S4.2": "Technology to track nutrition and wellness goals",
    "S4.3": "Food marketing trends and impacts",
    "S4.4": "Careers in nutrition, food, and wellness",
}

# Plain-language support block repeated in every teacher guide lesson.
SUPPORTS = [
    "Spanish and English versions are side by side on the site; students can switch language at any time.",
    "Sentence frames and a word bank are on every guided-practice sheet for students who need writing support.",
    "Offer extended time and oral responses for exit tickets as the IEP/504 plan requires.",
    "Do not rely on color alone: every color cue in the materials is paired with a word or symbol.",
]

# Class layout and budget facts supplied by the teacher (update here, then rebuild).
BUDGET_TOTAL = 1000          # dollars, food and consumables for the whole course
BUDGET_RESERVE_PCT = 10
LAB_COUNT = 41
KITCHEN = {
    "students": 32, "tables": 4, "groups": 8, "peanut_free": True,
    "milk_machine": "Almond Cow Essentials Bundle (machine, 60 oz glass jug, jug brush)",
    "freeze_dryer": "Harvest Right Home Pro, S or M (no dedicated circuit needed, so not L or XL; confirm which)",
}

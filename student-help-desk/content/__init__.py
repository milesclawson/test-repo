"""
Student Technology Help Desk — merged content module.
Combines all 5 phase files into a single ordered `UNITS` list of
{"meta": ..., "lessons": ...} dicts, consumed by the site/workbook/slide builders.
"""
from .phase1 import PHASE_1_META, PHASE_1_LESSONS
from .phase2 import PHASE_2_META, PHASE_2_LESSONS
from .phase3 import PHASE_3_META, PHASE_3_LESSONS
from .phase4 import PHASE_4_META, PHASE_4_LESSONS
from .phase5 import PHASE_5_META, PHASE_5_LESSONS

UNITS = [
    {"meta": PHASE_1_META, "lessons": PHASE_1_LESSONS},
    {"meta": PHASE_2_META, "lessons": PHASE_2_LESSONS},
    {"meta": PHASE_3_META, "lessons": PHASE_3_LESSONS},
    {"meta": PHASE_4_META, "lessons": PHASE_4_LESSONS},
    {"meta": PHASE_5_META, "lessons": PHASE_5_LESSONS},
]

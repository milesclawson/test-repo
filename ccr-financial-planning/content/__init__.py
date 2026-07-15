"""
CCR Financial Planning — merged content module.
Combines all 8 unit files into a single ordered `UNITS` list of
{"meta": ..., "lessons": ...} dicts, consumed by the site/workbook/slide builders.
"""
from .unit1 import UNIT_1_META, UNIT_1_LESSONS
from .unit2 import UNIT_2_META, UNIT_2_LESSONS
from .unit3 import UNIT_3_META, UNIT_3_LESSONS
from .unit4 import UNIT_4_META, UNIT_4_LESSONS
from .unit5 import UNIT_5_META, UNIT_5_LESSONS
from .unit6 import UNIT_6_META, UNIT_6_LESSONS
from .unit7 import UNIT_7_META, UNIT_7_LESSONS
from .unit8 import UNIT_8_META, UNIT_8_LESSONS

UNITS = [
    {"meta": UNIT_1_META, "lessons": UNIT_1_LESSONS},
    {"meta": UNIT_2_META, "lessons": UNIT_2_LESSONS},
    {"meta": UNIT_3_META, "lessons": UNIT_3_LESSONS},
    {"meta": UNIT_4_META, "lessons": UNIT_4_LESSONS},
    {"meta": UNIT_5_META, "lessons": UNIT_5_LESSONS},
    {"meta": UNIT_6_META, "lessons": UNIT_6_LESSONS},
    {"meta": UNIT_7_META, "lessons": UNIT_7_LESSONS},
    {"meta": UNIT_8_META, "lessons": UNIT_8_LESSONS},
]

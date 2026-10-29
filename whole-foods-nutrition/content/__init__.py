"""Aggregates unit modules. Add new units by importing them and appending to UNITS."""
from .common import COURSE, ROLES, GROUP_SIZE, GROUPS, DAY_SHAPE, LAB_SHAPE, CERT_OBJECTIVES, SUPPORTS, T, BUDGET_TOTAL, BUDGET_RESERVE_PCT, LAB_COUNT, KITCHEN
from .unit01 import UNIT as UNIT01
from .unit02 import UNIT as UNIT02
from .unit03 import UNIT as UNIT03
from .unit04 import UNIT as UNIT04

UNITS = [UNIT01, UNIT02, UNIT03, UNIT04]


def _shuffle_quizzes(units):
    """Repeatably shuffle multiple-choice order so the correct answer is not always A.

    Numeric/ordered choices (every choice contains a digit) are left in order. The seed is the unit
    number and question number, so the same content always builds the same quiz.
    """
    import random
    import re
    for u in units:
        for i, q in enumerate(u["quiz"]):
            if all(re.search(r"\d", c["en"]) for c in q["choices"]):
                continue
            rng = random.Random(f"{u['number']}-{i}")
            order = list(range(len(q["choices"])))
            rng.shuffle(order)
            correct = q["choices"][q["answer"]]
            q["choices"] = [q["choices"][j] for j in order]
            q["answer"] = q["choices"].index(correct)


_shuffle_quizzes(UNITS)

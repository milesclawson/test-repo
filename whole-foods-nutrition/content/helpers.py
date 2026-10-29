"""Compact builders for unit content (Units 5 and later).

Every text argument is an (English, Español) tuple; the helpers turn them into the same T(en, es)
pairs and dict shapes that Units 1-4 write out by hand, so all builders treat them identically.
"""
from .common import T


def P(p):
    """(en, es) tuple -> T pair. A T pair passes through unchanged."""
    return p if isinstance(p, dict) else T(*p)


def V(term, term_es, definition, definition_es):
    return {"term": T(term, term_es), "definition": T(definition, definition_es)}


def Q(cert, q, choices, answer):
    return {"cert": cert, "q": P(q), "choices": [P(c) for c in choices], "answer": answer}


def RQ(q, a):
    return {"q": P(q), "answer": P(a)}


def CRIT(cert, name, high, mid, low):
    return {"cert": cert, "name": P(name), "high": P(high), "mid": P(mid), "low": P(low)}


# Standard lab pieces, worded exactly as in Units 1-4.
CP_CLEAN = T("CLEAN: Safety Officer checks hands and counter.", "LIMPIAR: el Oficial de seguridad revisa las manos y el mostrador.")
CP_ALLERGY = T("ALLERGY: Safety Officer signs the label check.", "ALERGIA: el Oficial de seguridad firma la revisión de etiquetas.")
CP_CHILL = T("CHILL: Leftovers go back within 2 hours.", "ENFRIAR: las sobras vuelven en menos de 2 horas.")
CP_STATION = T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")
CP_KNIFE = T("KNIFE: Claw grip. One cutter at a time.", "CUCHILLO: posición de garra. Un solo cortador a la vez.")
CP_COOK = T("COOK: Handles inward. Dry mitts only.", "COCINAR: mangos hacia adentro. Solo guantes secos.")

FOLLOW = T("Follow the recipe card. Your Safety Officer signs off each safety checkpoint.",
           "Sigue la tarjeta de receta. Tu Oficial de seguridad firma cada punto de control de seguridad.")
DONE_CLEAN = T("Complete cleanup and the station check.", "Completa la limpieza y la revisión de la estación.")


def _cp(cp):
    return None if cp is None else P(cp)


def recipe(title, serves, minutes, allergens, equipment, ingredients, steps, cost, allergy=None):
    """Recipe dict. Adds the standard clean + label steps at the start and cleanup at the end.

    ingredients: (qty, (unit_en, unit_es), (item_en, item_es)); steps: (en, es, checkpoint or None).
    """
    allergy = allergy or ("Read every label. Confirm peanut-free.", "Lee cada etiqueta. Confirma que sea sin cacahuate.")
    opening = [
        {"text": T("Wash hands for 20 seconds. Wash, rinse, and sanitize the counter.",
                   "Lávate las manos durante 20 segundos. Lava, enjuaga y desinfecta el mostrador."), "checkpoint": CP_CLEAN},
        {"text": P(allergy), "checkpoint": CP_ALLERGY},
    ]
    closing = [{"text": T("Wash dishes, sanitize the counter, return equipment, and call for the station check.",
                          "Lava los platos, desinfecta el mostrador, devuelve el equipo y pide la revisión de la estación."),
                "checkpoint": CP_STATION}]
    return {
        "title": P(title), "serves": serves, "active_minutes": minutes,
        "allergens": P(allergens),
        "equipment": [P(x) for x in equipment],
        "ingredients": [{"qty": q, "unit": P(u), "item": P(i)} for q, u, i in ingredients],
        "steps": opening + [{"text": T(en, es), "checkpoint": _cp(cp)} for en, es, cp in steps] + closing,
        "cost_per_group": cost,
    }


def lesson(day, title, objs, cert, vocab, bell, inst, guided, indep, exit_, mats, notes):
    """Teaching day. inst: [(heading, body)]; guided: (title, [steps]); indep: (title, [steps]); exit_: [(q, a)]."""
    return {
        "day": day, "kind": "lesson", "title": P(title), "objectives": [P(o) for o in objs],
        "cert": cert, "vocab": vocab, "bellringer": P(bell),
        "instruction": [{"heading": P(h), "body": P(b)} for h, b in inst],
        "guided": {"title": P(guided[0]), "steps": [P(s) for s in guided[1]]},
        "independent": {"kind": "activity", "title": P(indep[0]), "steps": [P(s) for s in indep[1]]},
        "exit": [RQ(q, a) for q, a in exit_],
        "teacher": {"materials": mats, "notes": notes},
    }


def lab(day, title, objs, cert, vocab, bell, brief, plan, recipe_key, cook_title, extra, exit_, mats, notes):
    """Lab day: 5-minute brief, group work plan, cook, cleanup, exit ticket."""
    return {
        "day": day, "kind": "lab", "title": P(title), "objectives": [P(o) for o in objs],
        "cert": cert, "vocab": vocab, "bellringer": P(bell),
        "instruction": [{"heading": T("Lab brief", "Introducción del laboratorio"), "body": P(brief)}],
        "guided": {"title": T("Group Work Plan", "Plan de trabajo del grupo"), "steps": [P(s) for s in plan]},
        "independent": {"kind": "lab", "recipe": recipe_key, "title": P(cook_title),
                        "steps": [FOLLOW] + [P(s) for s in extra] + [DONE_CLEAN]},
        "exit": [RQ(q, a) for q, a in exit_],
        "teacher": {"materials": mats, "notes": notes},
    }

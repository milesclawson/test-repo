"""Adds up the estimated food cost of every lab against the course budget."""
import re
from content import BUDGET_TOTAL, BUDGET_RESERVE_PCT, LAB_COUNT, GROUPS


def _dollars(s):
    m = re.search(r"\$([\d.]+)", s)
    return float(m.group(1)) if m else 0.0


def report(units, path):
    rows, total, labs = [], 0.0, 0
    for u in units:
        for les in u["lessons"]:
            r = les["independent"].get("recipe")
            if les["kind"] == "lab" and r:
                per_group = _dollars(u["recipes"][r]["cost_per_group"])
                cost = per_group * GROUPS
                total += cost
                labs += 1
                rows.append((u["number"], les["day"], u["recipes"][r]["title"]["en"], per_group, cost))
    usable = BUDGET_TOTAL * (100 - BUDGET_RESERVE_PCT) / 100
    avg = total / labs if labs else 0
    lines = ["# Food budget tracker (estimates)", "",
             f"Course budget: ${BUDGET_TOTAL:,.0f}. Reserve held back: {BUDGET_RESERVE_PCT}% (${BUDGET_TOTAL - usable:,.0f}). "
             f"Available for labs: ${usable:,.0f} across about {LAB_COUNT} labs (about ${usable / LAB_COUNT:,.2f} per lab).", "",
             "| Unit | Day | Lab recipe | Cost per group | Cost for 8 groups |", "|---|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | ${d:,.2f} | ${e:,.2f} |" for a, b, c, d, e in rows]
    left = usable - total
    lines += ["", f"**Written so far:** {labs} labs, ${total:,.2f} total, average ${avg:,.2f} per lab.",
              f"**Remaining for the other {LAB_COUNT - labs} labs:** ${left:,.2f}, about ${left / max(LAB_COUNT - labs, 1):,.2f} per lab.", "",
              "Prices are rough estimates, not quotes. Update each recipe's `cost_per_group` with current store prices."]
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return total, labs

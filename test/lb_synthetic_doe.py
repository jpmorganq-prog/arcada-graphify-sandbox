#!/usr/bin/env python3
"""Synthetic, non-production VPS screening design — NO laboratory formulation.
Illustrative BET numbers only. This is a test of trial structure and mass units.
"""
from __future__ import annotations
import csv
from itertools import product
from pathlib import Path
import sys
import numpy as np

SKILL_SCRIPTS = Path(__file__).resolve().parents[1] / ".agents/skills/experimental-design/scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
from doe_designs import two_level_factorial

def main():
    # Illustrative assumptions, not verified product BET values:
    bet_m2_g = {"R972": 100.0, "R812": 200.0}
    # 2 x 2 x 2 screening, repeated with two independently prepared batches.
    factors = {"R812_encoded": (0, 1), "area_m2_per_100g": (480.0, 600.0),
               "wax_g_per_100g": (0.5, 1.0)}
    design = two_level_factorial(factors, seed=20261025)
    expected = set(product((0.0, 1.0), (480.0, 600.0), (0.5, 1.0)))
    actual = {tuple(map(float, row)) for row in design[list(factors)].to_numpy()}
    assert len(design) == 8 and actual == expected
    rows = []
    for condition_index, row in enumerate(design.to_dict(orient="records"), start=1):
        grade = "R812" if int(row["R812_encoded"]) else "R972"
        area = float(row["area_m2_per_100g"])
        wax_g = float(row["wax_g_per_100g"])
        silica_g = area / bet_m2_g[grade]
        balance_placeholder_g = 100 - silica_g - wax_g
        assert abs((silica_g + wax_g + balance_placeholder_g) - 100.0) < 1e-10
        assert abs(silica_g * bet_m2_g[grade] - area) < 1e-10
        for batch in (1, 2):
            rows.append({
                "condition_id": f"C{condition_index:02d}",
                "independent_batch": batch,
                "grade": grade,
                "BET_assumed_m2_per_g": bet_m2_g[grade],
                "area_target_m2_per_100g": area,
                "silica_mass_g_per_100g": silica_g,
                "wax_mass_g_per_100g": wax_g,
                "other_material_placeholder_g_per_100g": balance_placeholder_g,
                "repeated_measurements_per_batch": 3,
            })
    order = np.random.default_rng(20261025).permutation(len(rows))
    ordered = [{**rows[int(i)], "random_run_order": pos} for pos,i in enumerate(order,1)]
    assert len(ordered) == 16
    assert len(set((r["condition_id"],r["independent_batch"]) for r in ordered)) == 16
    assert all(sum(r[k] for k in ("silica_mass_g_per_100g","wax_mass_g_per_100g","other_material_placeholder_g_per_100g")) == 100.0 for r in ordered)
    assert all(
        sorted([r["independent_batch"] for r in ordered if r["condition_id"] == f"C{i:02d}"]) == [1, 2]
        for i in range(1, 9)
    )
    dest = Path("out/synthetic_lb_doe.csv")
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open("w", newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(ordered[0].keys()))
        writer.writeheader(); writer.writerows(ordered)
    print("PASS VPS MODEL DOE: 8 unique conditions, 16 independent batches, randomized")
    print("PASS synthetic area equivalence and mass accounting for 100 g illustrative batch")
    print("PASS repeated measurements tracked as nested (not 48 independent replicates)")
    print(f"EXPORTED {dest}")

if __name__ == "__main__":
    main()

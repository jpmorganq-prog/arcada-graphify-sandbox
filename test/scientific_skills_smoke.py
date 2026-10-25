#!/usr/bin/env python3
"""Isolated smoke tests against vendored K-Dense source. Only synthetic inputs.
No ARCADA production data or external services are used.
"""
from __future__ import annotations
import itertools
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1] / ".agents" / "skills"
for dirname in ("experimental-design", "statistical-analysis", "uncertainty-and-units"):
    sys.path.insert(0, str(ROOT / dirname / "scripts"))

from doe_designs import two_level_factorial
from randomization import block_randomization
from assumption_checks import check_normality
from uncertainty_budget import build_budget

def check_design():
    factors = {"BET_m2_g": (100.0, 200.0), "wax_mass_pct": (0.5, 1.0)}
    a = two_level_factorial(factors, seed=42)
    b = two_level_factorial(factors, seed=42)
    actual = {tuple(row) for row in a[["BET_m2_g", "wax_mass_pct"]].to_numpy()}
    expected = set(itertools.product((100.0, 200.0), (0.5, 1.0)))
    assert len(a) == 4 and actual == expected, (len(a), actual)
    assert a.equals(b), "DOE reproducibility"
    print("PASS DOE: 2^2 = 4 unique conditions, same seed reproduced")

def check_randomization():
    schedule = block_randomization(12, arms=("control", "variant"), seed=42)
    assert schedule["arm"].value_counts().to_dict() == {"control": 6, "variant": 6}
    assert schedule.equals(block_randomization(12, arms=("control", "variant"), seed=42))
    print("PASS RANDOMIZATION: 12 positions, 6+6, reproducible")

def check_statistics():
    result = check_normality([7.0, 7.1, 6.9, 7.2, 6.8, 7.05], plot=False)
    assert result["n"] == 6 and 0.0 <= result["p_value"] <= 1.0
    assert result["test"] == "Shapiro-Wilk"
    print("PASS STATISTICS: Shapiro-Wilk finite p-value on synthetic data")

def check_uncertainty():
    result = build_budget({
        "measurand": "example length", "unit": "mm", "value": 10.0,
        "components": [
            {"label": "repeatability", "type": "B", "distribution": "normal", "value": 0.1},
            {"label": "resolution", "type": "B", "distribution": "rectangular", "value": 0.2},
        ],
    }, None)
    expected = math.sqrt(0.1**2 + (0.2 / math.sqrt(3))**2)
    assert math.isclose(result["combined_standard_uncertainty"], expected, rel_tol=1e-12)
    assert result["expanded_uncertainty"] > expected
    print(f"PASS UNCERTAINTY: combined u={expected:.9f} mm; independent formula matches")

if __name__ == "__main__":
    check_design()
    check_randomization()
    check_statistics()
    check_uncertainty()
    print("ALL 4 SMOKE TESTS PASSED")

# ARCADA — VPS Light Body: preliminary DOE proof (simulation only)

Date: 2026-10-25. Status: **synthetic design verified; no laboratory runs performed**.
Objective: verify K-Dense `experimental-design` can generate an interpretable comparison between R812 and R972 for the user's VPS Light Body project without changing any master formulation.

## Hypothesis, control and factors
A control is the **current approved Light Body formulation**, with its own verified composition and preparation process. Control must be independently prepared rather than copied from a historical measurement.

Three screening factors:
1. Silica grade: R972 / R812 (categorical; **NOT a claim of chemical equivalence**).
2. Target total BET surface area per 100 g of hypothetical material: 480 / 600 m², illustrative only.
3. Wax contribution: 0.5 / 1.0 g per 100 g, illustrative only.

The demo uses **fictional** BET(R972)=100 m²/g, BET(R812)=200 m²/g. These are not supplier specifications or values measured by ARCADA. The resulting silica mass is computed as:
`silica_g_per_100g = target_area_m2_per_100g / assumed_BET_m2_per_g`.
`other_material_placeholder` is only a balancing dummy field, **not a formulation**, and does not define Pt, Si–H, vinyl concentration or A/B mixing.

## Design and sample independence
2 × 2 × 2 = 8 conditions; prepare **two independent batches** per condition (16 batches) in randomized order, stratified by mixing day if required by schedule. For each batch, make three technical measurements, but do not treat those as three independent prepared batches. Reserve dedicated control batches and benchmark DMG Silagum Light (not included in 8 synthetic factorial conditions).

For real VPS trials, freeze and separately record A and B complete mass balances, mix ratio, sources/COA of BET, lot numbers, mixing energy, temperature, dispersion duration, degassing, storage time, cure timing and operator. Calculate actual Si–H/vinyl equivalents only with supplier-specific assay data. Prevent catalyst/Si–H cross-contact until the intended mix.

## Outputs and success conditions
Record: A/B viscosities and extrusion; Thin Edge Test; tensile/elongation; tear; detail reproduction; working/setting time; Shore A and evidence of cure. Separate instrument measurements from visual ratings. Track instrumental repeatability and independent batches.

Success for the **software test**: all 8 unique combinations, 16 independent batches, randomized order, surface-area calculation and 100 g illustrative mass accounting agree with independent assertions, and exported CSV is readable.

Success for the **future laboratory study**: prespecified acceptance bounds versus current approved Light Body and DMG Silagum Light, with confidence intervals across independent batches; acceptance bounds remain **not set** until the laboratory determines measurement error and product requirements.

## Evidence
- Source implementation: `test/lb_synthetic_doe.py`.
- CI: https://github.com/jpmorganq-prog/arcada-graphify-sandbox/actions/runs/40181944950
- Original scientific skills: K-Dense commit `593377bb048752abb0152deab9fbb1083a6087df`.

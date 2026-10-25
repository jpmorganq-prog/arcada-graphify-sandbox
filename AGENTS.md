# ARCADA — isolated scientific skills trial

This repository branch is a **test environment**, not the production ARCADA portal.

## Scope and data
- Use only synthetic or explicitly authorized test datasets.
- Never connect to ARCADA production Neon, Render, Auth0, employee accounts, corporate APIs or real recipes.
- Never alter master formulations or suggest that a screening matrix is a production recipe.
- Do not deploy or merge changes to the main branch.
- For experiments, distinguish independent **batches** from repeated measurements on the same batch.
- Treat BET values in `test/lb_synthetic_doe.py` as synthetic assumptions, not manufacturer-verified values.

## Available project-scoped skills
Use the three original K-Dense skills under `.agents/skills/` when relevant:
- `experimental-design` for randomized factorial / blocked scientific experiments.
- `statistical-analysis` for analysis and assumptions after collecting data.
- `uncertainty-and-units` for uncertainty propagation and unit checks.

Do not change these vendored files; their Git object SHAs are compared to pinned upstream commit
`593377bb048752abb0152deab9fbb1083a6087df`.

## Verifications
Run:
```bash
python test/scientific_skills_smoke.py
python test/lb_synthetic_doe.py
node test/codex_skill_discovery.mjs
```
The Codex discovery test requires the Codex CLI but does not need model authentication.
Before any further modifications: inspect the existing branch and obtain the applicable Graphify context when that index includes the code being changed.

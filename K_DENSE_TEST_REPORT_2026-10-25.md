# K-Dense Scientific Agent Skills — isolated trial (2026-10-25)

## Status
Three upstream skill directories copied verbatim into a **test-only Git branch**:
`experiment/kdense-science-skills-20261025`.
Production ARCADA, Neon, Render, employee permissions and master formulations were not changed.
This is a project-scoped skill install for a compatible Codex checkout of **this branch**; it does **not** activate the skills in all ChatGPT/Codex sessions.

## Provenance
- Original repository: https://github.com/K-Dense-AI/scientific-agent-skills
- Pinned original commit: `593377bb048752abb0152deab9fbb1083a6087df` (2026-10-19 UTC)
- Installed directories:
  - `.agents/skills/experimental-design/`
  - `.agents/skills/statistical-analysis/`
  - `.agents/skills/uncertainty-and-units/`
- 29 of 29 original file blob SHA values matched after the copy. No modifications to upstream files.

## Execution evidence
- GitHub Actions: https://github.com/jpmorganq-prog/arcada-graphify-sandbox/actions/runs/40181116307
- Runner: `ubuntu-latest`, Python 3.13, dependencies declared in `test/scientific-skills-requirements.txt`.
- Python compilation: PASS.
- Smoke cases on synthetic data: PASS for (1) factorial DOE 2^2, (2) 12-run block randomization balance, (3) Shapiro-Wilk normality diagnostic, (4) GUM component uncertainty propagation vs independent analytical formula.
- Reference uncertainty: sqrt(0.1^2 + (0.2/sqrt(3))^2) = 0.152752523 mm (synthetic).
- These are preliminary smoke checks; they are not domain validation of dental VPS formulations, ISO qualification, a malicious-code-free certification, or proof of Codex auto-discovery in the user's normal workspace.

## How to start a Codex session
Check out the **test branch**, not main, in the Codex-connected workspace:
```
git fetch origin experiment/kdense-science-skills-20261025
git switch experiment/kdense-science-skills-20261025
```
Then request: `Use experimental-design to prepare a randomized and replicated DOE on synthetic Light Body filler data, reporting independent batch units separately from repeated measurements.`
Confirm that the Codex skill discovery mechanism loads all three skills in this repository.

## Boundaries and rollback
- No API keys, production data, workflow secrets or private files needed for the tests.
- Do not merge or deploy this branch without review.
- Revert by returning the workspace to its earlier branch; delete the test branch after acceptance if no longer needed.

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


## Extended verification (2026-10-25)
- Actual Codex CLI version: **0.164.0** (verified from GitHub Actions logs).
- Actual Codex app-server `initialize` succeeded, then `skills/list` with `forceReload=true` returned **all three project-scoped skills** with expected paths and without scan errors.
- This test deliberately did **not** call `thread/start` or `turn/start`; no LLM inference or account authorization was used.
- Additional generated synthetic Light Body plan: 8 conditions, 2 independently prepared batches per condition, 16 total batches, 3 repeat measurements linked to each batch. Illustrative BET values are never claimed to be source-verified.
- Proof run: https://github.com/jpmorganq-prog/arcada-graphify-sandbox/actions/runs/40181944950
- Executable source: `test/codex_skill_discovery.mjs`, `test/lb_synthetic_doe.py`.
- Experiment assumptions and acceptance plan: `VPS_LB_SYNTHETIC_TEST_PLAN_2026-10-25.md`.
- `AGENTS.md` limits Codex agents in this branch to synthetic test data.
- GitHub CI now pins Codex CLI 0.164.0 and cancels redundant concurrent branch builds.

### Remaining limitations
- Skill discovery is **not** proof that a signed-in user's Codex model selected/executed each skill as an agent in the user's personal Codex workspace. This connector currently offers no action to switch the user's hosted Codex workspace or perform an authenticated model turn.
- Graphify's indexed default-branch graph does not include this trial branch; do not describe it as validating the newly copied skills.
- Neither this test nor the K-Dense documentation establishes real product improvements or a validated VPS formulation.
- Working ARCADA portal, `main`, Neon, Render, Auth0 and real recipes were left unchanged.

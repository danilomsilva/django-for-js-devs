# Writing Plan

Phased breakdown of `0-initiative.md` into executable work. Each phase ends with a stop-and-review point per the working agreement — small PRs, one chapter/step at a time.

## Phase 0 — Scaffold (this session)

- [ ] `0-initiative.md` (this brief)
- [ ] `1-writing-plan.md` (this file)
- [ ] `CLAUDE.md` — standing rules for AI-assisted sessions in this repo
- [ ] `README.md` — purpose, audience, how to read, versions, AI disclosure, TOC
- [ ] `LICENSE` (MIT) + `LICENSE-CONTENT` (CC BY 4.0)
- [ ] `CREDITS.md` (seed with Django, DRF, and any other sources already referenced)
- [ ] `CONTRIBUTING.md` — style rules, PR checklist, how to suggest fixes
- [ ] `docs/_template.md` — chapter template
- [ ] `.gitignore` for Python/uv/Node artifacts
- [ ] Push to `origin/main`

## Phase 1 — Runnable example project

- [ ] `examples/` — minimal Django + DRF project scaffolded with `uv`
- [ ] `examples/pyproject.toml` pinned to verified current Django LTS / DRF / Python versions
- [ ] `docker-compose.yml` for Postgres (local dev)
- [ ] One passing test (pytest-django)
- [ ] `.github/workflows/ci.yml` — ruff check + ruff format --check + pytest with Postgres service container
- [ ] Confirm CI is green on a PR

## Phase 2 — Chapter 0 (Intro) draft

- [ ] Draft `docs/00-intro.md` using the template: who it's for, how to read it, setup with `uv`, Postgres via Docker
- [ ] Verify install/setup steps actually run end-to-end
- [ ] Add "Further reading & credits"
- [ ] **Stop for author review** — end of first-session deliverables

## Phase 3 — Part 1: Mindset (✅ core)

- [ ] Ch. 1 — Python survival kit
- [ ] Ch. 2 — Django philosophy
- One PR per chapter; author runs code + reviews before merge.

## Phase 4 — Part 2: Core Django (✅ core)

- [ ] Ch. 3 — Project anatomy
- [ ] Ch. 4 — Request lifecycle
- [ ] Ch. 5 — URLs & views
- [ ] Ch. 6 — Models & ORM
- [ ] Ch. 7 — Migrations
- [ ] Ch. 8 — Admin
- [ ] Ch. 9 — Settings & environments
- Each chapter grows the same `examples/` project incrementally — no throwaway example apps.

## Phase 5 — Part 3: APIs for React (✅ core, plus two ⏳)

- [ ] Ch. 10 — DRF intro
- [ ] Ch. 11 — Serializers
- [ ] Ch. 12 — Auth
- [ ] Ch. 13 — Permissions
- [ ] Ch. 14 — Pagination, filtering, ordering
- [ ] Ch. 17 — Dev setup React ↔ Django
- [ ] Ch. 15 — Errors & validation (⏳, only after all ✅ chapters across all parts are done, unless author asks sooner)
- [ ] Ch. 16 — Typed contracts (⏳, same condition)

## Phase 6 — Part 4: Data & Postgres

- [ ] Ch. 19 — N+1 queries (✅)
- [ ] Ch. 18 — Postgres with Django (⏳)
- [ ] Ch. 20 — Transactions (⏳)

## Phase 7 — Part 5: Quality & ops (all ⏳)

- [ ] Ch. 21 — Testing
- [ ] Ch. 22 — Tooling
- [ ] Ch. 23 — Background tasks
- [ ] Ch. 24 — Deploy
- [ ] Ch. 25 — Observability

## Phase 8 — Appendix (✅ core)

- [ ] Cheat sheet (the JS-anchor table)
- [ ] Glossary
- [ ] Full resource list

## Phase 9 — Capstone (⏳, blocked)

- Do not start. Idea to be defined later, with explicit author sign-off, only after all ✅ and requested ⏳ chapters are complete.

## Sequencing rules

- ✅ chapters always come before ⏳ chapters, across the whole plan — not just within a part — unless the author explicitly asks to jump ahead.
- One chapter or scaffold step per PR.
- No new dependency or chapter-plan change without asking first.
- Every Django code example lives in `examples/` and must pass CI before the chapter referencing it is merged.

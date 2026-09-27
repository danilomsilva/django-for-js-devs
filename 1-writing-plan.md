# Writing Plan

Phased breakdown of `0-initiative.md` into executable work. Each phase ends with a stop-and-review point per the working agreement — small PRs, one chapter/step at a time.

## Phase 0 — Scaffold (this session) ✅ done

- [x] `0-initiative.md` (this brief)
- [x] `1-writing-plan.md` (this file)
- [x] `CLAUDE.md` — standing rules for AI-assisted sessions in this repo
- [x] `README.md` — purpose, audience, how to read, versions, AI disclosure, TOC
- [x] `LICENSE` (MIT) + `LICENSE-CONTENT` (CC BY 4.0)
- [x] `CREDITS.md` (seed with Django, DRF, and any other sources already referenced)
- [x] `CONTRIBUTING.md` — style rules, PR checklist, how to suggest fixes
- [x] `docs/_template.md` — chapter template
- [x] `.gitignore` for Python/uv/Node artifacts
- [x] Push to `origin/main`

## Phase 1 — Runnable example project ✅ done

- [x] `examples/` — minimal Django + DRF project scaffolded with `uv`
- [x] `examples/pyproject.toml` pinned to verified current Django LTS / DRF / Python versions
- [x] `docker-compose.yml` for Postgres (local dev)
- [x] One passing test (pytest-django) — 3 tests, passing locally (SQLite) and in CI (Postgres)
- [x] `.github/workflows/ci.yml` — ruff check + ruff format --check + pytest with Postgres service container
- [x] Confirm CI is green — verified on push to main (run 36326831866)

## Phase 2 — Chapter 0 (Intro) draft ✅ done

- [x] Draft `docs/00-intro.md` using the template: who it's for, how to read it, setup with `uv`, Postgres via Docker
- [x] Verify install/setup steps actually run end-to-end (`uv sync`, `migrate`, `pytest` all verified; Postgres path verified via CI since local Docker Desktop wasn't running this session)
- [x] Add "Further reading & credits"
- Author granted autonomy through Phase 8 — continuing without stopping here.

## Phase 3 — Part 1: Mindset (✅ core) ✅ done

- [x] Ch. 1 — Python survival kit
- [x] Ch. 2 — Django philosophy

## Phase 4 — Part 2: Core Django (✅ core) ✅ done

- [x] Ch. 3 — Project anatomy
- [x] Ch. 4 — Request lifecycle (added `greetings/middleware.py`)
- [x] Ch. 5 — URLs & views (added `ping` FBV alongside the `GreetingViewSet` CBV)
- [x] Ch. 6 — Models & ORM (added `GreetingCategory` + FK relation)
- [x] Ch. 7 — Migrations (references the two real migrations generated above)
- [x] Ch. 8 — Admin (registered both models with list_display/list_filter)
- [x] Ch. 9 — Settings & environments
- Each chapter grew the same `examples/` project incrementally — no throwaway example apps. 6/6 tests passing, ruff clean.

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

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

## Phase 5 — Part 3: APIs for React (✅ core, plus two ⏳) ✅ done

- [x] Ch. 10 — DRF intro
- [x] Ch. 11 — Serializers (added `validate_message`)
- [x] Ch. 12 — Auth (added token auth: `rest_framework.authtoken`, `whoami`)
- [x] Ch. 13 — Permissions (added `IsStaffOrReadOnly`)
- [x] Ch. 14 — Pagination, filtering, ordering (added `django-filter`, pagination, ordering)
- [x] Ch. 17 — Dev setup React ↔ Django (added `django-cors-headers`)
- [x] Ch. 15 — Errors & validation (⏳)
- [x] Ch. 16 — Typed contracts (⏳, added drf-spectacular + OpenAPI schema endpoint)

## Phase 6 — Part 4: Data & Postgres ✅ done

- [x] Ch. 19 — N+1 queries (✅, added `select_related` + `django_assert_num_queries` test)
- [x] Ch. 18 — Postgres with Django (⏳, has one `> ⚠️ Verify:` flag — no `JSONField`/index in `examples/` yet to test against)
- [x] Ch. 20 — Transactions (⏳, added `services.py` with `@transaction.atomic`)

## Phase 7 — Part 5: Quality & ops (all ⏳) ✅ done

- [x] Ch. 21 — Testing (names the pytest-django/APIClient patterns already used throughout `examples/`)
- [x] Ch. 22 — Tooling (ruff already enforced since Phase 1; mypy/pre-commit flagged as `> ⚠️ Verify:`, not added)
- [x] Ch. 23 — Background tasks (⏳, conceptual — Celery not added to `examples/`, flagged with `> ⚠️ Verify:`; would need a Redis broker)
- [x] Ch. 24 — Deploy (⏳, conceptual — Gunicorn/Dockerfile shape described, not added to `examples/`, flagged with `> ⚠️ Verify:`)
- [x] Ch. 25 — Observability (⏳, conceptual — LOGGING/Sentry not added to `examples/`, flagged with `> ⚠️ Verify:`)

## Phase 8 — Appendix (✅ core) ✅ done

- [x] Cheat sheet (the JS-anchor table, linked back to every chapter)
- [x] Glossary
- [x] Full resource list

**All of Phases 0–8 are now complete.** Every ✅ core chapter and every ⏳ chapter from the original plan is written. Only Phase 9 (capstone) remains, and it stays blocked per §13 of `0-initiative.md` and the standing rule in `CLAUDE.md` — do not start it without explicit author sign-off.

## Phase 9 — Capstone (⏳, blocked)

- Do not start. Idea to be defined later, with explicit author sign-off, only after all ✅ and requested ⏳ chapters are complete.

## Sequencing rules

- ✅ chapters always come before ⏳ chapters, across the whole plan — not just within a part — unless the author explicitly asks to jump ahead.
- One chapter or scaffold step per PR.
- No new dependency or chapter-plan change without asking first.
- Every Django code example lives in `examples/` and must pass CI before the chapter referencing it is merged.

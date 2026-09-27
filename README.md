# Django for JS Devs

A free, open-source guide that teaches Django to JavaScript/TypeScript developers — by explaining every Django concept through the JS tools you already know.

## Who this is for

You're comfortable with **React** on the frontend, you've built or worked on **Node.js** backends, and now you need to work with Django — but every Django resource out there assumes you're a Python beginner, a general programming beginner, or a Django dev learning React. This guide assumes none of that. It assumes you already know how to build a web app; it's here to map Django's world onto the one you already have a mental model for.

## How to read it

- Start at [`docs/00-intro.md`](docs/00-intro.md) and follow the chapter order — later chapters build on earlier ones and link back when they do.
- Each chapter is short (5–10 minutes) and follows the same shape: TL;DR → mental model → "if you know JS" comparison → the Django way → gotchas → check-yourself questions → further reading. See [`docs/_template.md`](docs/_template.md) for the exact structure.
- Every Django code example lives in [`examples/`](examples/), a single Django + DRF project that grows chapter by chapter. It's runnable and tested — clone the repo and follow along in [`docs/00-intro.md`](docs/00-intro.md) to set it up.
- Claims about versions or "most popular JS tool" are verified against current sources; anything the author couldn't verify is flagged inline with `> ⚠️ Verify:` rather than stated as fact.

## Versions used in this guide

- **Django 5.2 (LTS)**
- **Django REST Framework 3.17**
- **Python 3.12**
- **PostgreSQL** (via Docker for local dev)
- **uv** for Python dependency management

`examples/pyproject.toml` is the source of truth if these drift — check it if a version here looks stale.

## Table of contents

See the full chapter plan in [`1-writing-plan.md`](1-writing-plan.md). Chapters are published as they're written; ✅-marked chapters in the plan are written before ⏳-marked ones.

- **Part 0 — Intro:** [00 — Intro](docs/00-intro.md) ✅
- **Part 1 — Mindset:** 01 — Python survival kit · 02 — Django philosophy
- **Part 2 — Core Django:** 03 — Project anatomy · 04 — Request lifecycle · 05 — URLs & views · 06 — Models & ORM · 07 — Migrations · 08 — Admin · 09 — Settings & environments
- **Part 3 — APIs for React:** 10 — DRF intro · 11 — Serializers · 12 — Auth · 13 — Permissions · 14 — Pagination, filtering, ordering · 15 — Errors & validation · 16 — Typed contracts · 17 — Dev setup React ↔ Django
- **Part 4 — Data & Postgres:** 18 — Postgres with Django · 19 — N+1 queries · 20 — Transactions
- **Part 5 — Quality & ops:** 21 — Testing · 22 — Tooling · 23 — Background tasks · 24 — Deploy · 25 — Observability
- **Appendix:** JS↔Django cheat sheet · Glossary · Resource list

Chapters not yet linked above haven't been written yet — check back, or see the plan for status.

## AI disclosure

This guide is **AI-assisted and human-reviewed**. Drafts are produced with AI assistance, then run, tested, and reviewed by the author before merging. If you spot something inaccurate or unclear, please open an issue or PR — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

- Written content (`docs/`) is licensed under [CC BY 4.0](LICENSE-CONTENT).
- Code (`examples/`) is licensed under [MIT](LICENSE).

See [`CREDITS.md`](CREDITS.md) for every project and source referenced.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

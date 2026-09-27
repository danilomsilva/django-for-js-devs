# Initiative: Django for JS Devs

> Working brief derived from the author's handoff. This is the source of truth for scope, structure, and constraints. See `1-writing-plan.md` for how the work is sequenced, and `CLAUDE.md` for the standing rules every session in this repo must follow.

## 1. What this is

A free, open-source guide that teaches Django to JavaScript/TypeScript developers by anchoring every Django concept to the closest, most popular JS equivalent. Published as a GitHub repo, no paywall, no docs site for now.

- **Repo:** `django-for-js-devs` (github.com/danilomsilva/django-for-js-devs) — already created, remote configured.
- **Author/owner:** Danilo M. Silva.

## 2. Audience

JS/TS developers who know React and Node.js, but have little or no Python/Django experience. Written for JS developers generally — no tailoring to one person's employer, stack, or projects.

## 3. Core principles

1. **Macro first** — mental model and "where things live" per chapter; depth is linked, not inlined.
2. **JS anchor for every concept** — always explain via the most popular JS equivalent (§6 of the original brief; canonical table lives in `docs/_template.md` usage and the Appendix cheat sheet once written).
3. **Short and scannable** — bullets, tables, side-by-side code, no walls of text.
4. **Runnable and tested** — every Django snippet in `examples/` runs and is covered by CI.
5. **Accurate and current** — verify versions/APIs/"most popular" claims against current official sources, not memory. Flag unverifiable claims with `> ⚠️ Verify:` instead of guessing.
6. **Credit the community** — link to official docs, credit projects/authors, never copy text verbatim.
7. **Honest about AI** — README discloses the content is AI-assisted and human-reviewed.

## 4. Licensing

| Asset | License |
|---|---|
| Written content (`docs/`) | CC BY 4.0 |
| Code (`examples/`) | MIT |

`CREDITS.md` tracks every referenced project/doc/article with links and licenses. Each chapter ends with "Further reading & credits."

## 5. Repo structure

```
django-for-js-devs/
├── README.md
├── LICENSE                 # MIT (code)
├── LICENSE-CONTENT          # CC BY 4.0 (docs)
├── CREDITS.md
├── CONTRIBUTING.md
├── CLAUDE.md               # standing rules for AI-assisted work in this repo
├── 0-initiative.md         # this file
├── 1-writing-plan.md       # phased plan
├── docs/
│   ├── _template.md
│   ├── 00-intro.md
│   └── ...
├── examples/                # one runnable Django project, grown chapter by chapter
│   ├── pyproject.toml        # managed with uv
│   └── ...
└── .github/workflows/        # CI: lint + test examples/
```

## 6. Versions (verify before locking in)

- Latest Django LTS (check djangoproject.com/download).
- Current stable Django REST Framework.
- Current Python 3.x supported by that Django version.
- PostgreSQL for local dev, via Docker.

## 7. Chapter plan status

See the full chapter table from the original handoff — kept intact as the backlog. Priority order: all ✅ (core) chapters before any ⏳ chapters, unless the author asks otherwise. The capstone (ch. 26) is not started; its idea is not yet defined.

## 8. Working agreement

- Small PRs: one chapter or one scaffold step per PR.
- Flow: draft → author runs the code and reviews → revise → merge.
- Ask before adding new dependencies or changing the chapter plan.
- Never mention a specific company, employer, or the author's personal projects.
- Never start the capstone without explicit sign-off.
- Never copy text verbatim from docs, books, or articles — paraphrase and link.

## 9. First-session deliverables (from the handoff, for reference)

1. Scaffold repo structure, license files, `CREDITS.md`, `CONTRIBUTING.md`.
2. `README.md` (purpose, audience, how to read, versions, AI disclosure, TOC).
3. `docs/_template.md`.
4. `examples/` — minimal Django + DRF project via `uv`, Postgres via `docker-compose.yml`, one passing test.
5. CI set up and green.
6. Draft Chapter 0 (Intro) only.
7. Stop for review.

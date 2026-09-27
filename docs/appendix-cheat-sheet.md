# Appendix — JS ↔ Django cheat sheet

Ok, you've been through the whole guide now — this page is the reference you come back to, not something to read start to finish. It's the same anchor table from `0-initiative.md`, expanded with a link back to the chapter that actually explains each row.

| Django / Python concept | Primary JS anchor | Also mention | Chapter |
|---|---|---|---|
| pip / uv, `pyproject.toml` | npm, `package.json` | pnpm | [00 — Intro](00-intro.md) |
| Virtual env | `node_modules` (per project) | nvm | [00 — Intro](00-intro.md) |
| Python syntax | JS/TS syntax equivalents | — | [01 — Python survival kit](01-python-survival-kit.md) |
| Django (batteries included) | Express (minimal) | Next.js / NestJS (opinionated) | [02 — Django philosophy](02-django-philosophy.md) |
| Project vs apps | Express app vs feature modules | NestJS modules | [03 — Project anatomy](03-project-anatomy.md) |
| Middleware | Express middleware | — | [04 — Request lifecycle](04-request-lifecycle.md) |
| `urls.py` | Express Router | Next.js route handlers | [05 — URLs & views](05-urls-and-views.md) |
| Views / class-based views | Express route handlers | NestJS controllers | [05 — URLs & views](05-urls-and-views.md) |
| Models + ORM / QuerySets | Prisma schema + client | Drizzle | [06 — Models & ORM](06-models-and-orm.md) |
| Migrations | `prisma migrate` | drizzle-kit | [07 — Migrations](07-migrations.md) |
| Django Admin | Prisma Studio (DB browser) | AdminJS (full admin panel) | [08 — Admin](08-admin.md) |
| `settings.py` + env vars | `dotenv` / `.env` | — | [09 — Settings & environments](09-settings-and-environments.md) |
| DRF intro | Express + Router for REST APIs | NestJS | [10 — DRF intro](10-drf-intro.md) |
| DRF Serializers | Zod | — | [11 — Serializers](11-serializers.md) |
| Auth (sessions, CSRF, tokens) | Passport.js | Auth.js, Better Auth | [12 — Auth](12-auth.md) |
| Permissions | Auth middleware / guards | NestJS guards | [13 — Permissions](13-permissions.md) |
| Pagination / filtering | Query params + ORM | TanStack Table (client side) | [14 — Pagination, filtering, ordering](14-pagination-filtering-ordering.md) |
| Errors & validation | Zod errors + React Hook Form | — | [15 — Errors & validation](15-errors-and-validation.md) |
| OpenAPI (drf-spectacular) | openapi-typescript | Orval, tRPC (JS-only alternative) | [16 — Typed contracts](16-typed-contracts.md) |
| Dev setup (CORS, proxy) | Vite config, MSW | — | [17 — Dev setup React ↔ Django](17-dev-setup-react-django.md) |
| Postgres-specific fields | Prisma + Postgres | — | [18 — Postgres with Django](18-postgres-with-django.md) |
| `select_related` / `prefetch_related` | Prisma `include` | — | [19 — N+1 queries](19-n-plus-1-queries.md) |
| `transaction.atomic` | `prisma.$transaction` | — | [20 — Transactions](20-transactions.md) |
| pytest + pytest-django | Vitest / Jest | Supertest | [21 — Testing](21-testing.md) |
| ruff | ESLint + Prettier | Biome | [22 — Tooling](22-tooling.md) |
| Celery | BullMQ | — | [23 — Background tasks](23-background-tasks.md) |
| Gunicorn / Uvicorn | Node HTTP server + PM2 | — | [24 — Deploy](24-deploy.md) |
| Logging / error tracking | winston/pino, Sentry | Same tools, Python SDKs | [25 — Observability](25-observability.md) |

## Quick command reference

The commands you've actually run throughout this guide, in one place:

```bash
# Setup (chapter 0)
uv sync
docker compose up -d
uv run python manage.py migrate

# Everyday development
uv run python manage.py runserver
uv run python manage.py makemigrations <app>   # chapter 7
uv run python manage.py createsuperuser         # chapter 8

# Quality (chapters 21-22)
uv run pytest
uv run ruff check .
uv run ruff format .
```

## Further reading & credits

- See each linked chapter's own "Further reading & credits" section, and [`CREDITS.md`](../CREDITS.md) for the full source list.

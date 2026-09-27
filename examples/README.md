# examples/

The single runnable Django + DRF project referenced throughout `docs/`. It grows chapter by chapter — no throwaway example apps.

## Setup

```bash
cd examples
uv sync
cp .env.example .env
docker compose up -d      # Postgres
uv run python manage.py migrate
uv run python manage.py runserver
```

## Running tests

```bash
uv run pytest
```

Tests default to a fast in-memory SQLite database (`config/settings_test.py`) so they run without Docker. CI (`.github/workflows/ci.yml`) runs the same suite against a real Postgres service container using `config.settings`, which is what `manage.py` uses too.

## Linting

```bash
uv run ruff check .
uv run ruff format --check .
```

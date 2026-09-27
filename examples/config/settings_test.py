"""Test-only settings: swap Postgres for local SQLite so `pytest` runs fast
without requiring Docker. CI still runs the full suite against a real
Postgres service container using config.settings (see .github/workflows/ci.yml).
"""

from .settings import *  # noqa: F401,F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

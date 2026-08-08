"""
Alembic Migration Environment

TODO:
- Import your Base metadata from app.core.database
- Import all models so Alembic can detect them
- Configure the migration context to use your DATABASE_URL
- Support both online and offline migration modes

Hints:
    - target_metadata = Base.metadata
    - Import models: from app.models import *  (so all tables are registered)
    - For async: use run_async_migrations() pattern
"""

from alembic import context

# TODO: Set target_metadata = Base.metadata
target_metadata = None


def run_migrations_offline():
    """Run migrations in 'offline' mode — generates SQL scripts without DB connection."""
    pass


def run_migrations_online():
    """Run migrations in 'online' mode — connects to DB and applies changes."""
    pass


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

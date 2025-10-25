from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# 1️⃣ Load environment variables from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# 2️⃣ Access Alembic Config object
config = context.config

# 3️⃣ Inject DATABASE_URL into Alembic configuration
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
else:
    raise RuntimeError("DATABASE_URL not found in .env file")

# 4️⃣ Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 5️⃣ Import your SQLAlchemy Base metadata
# (Alembic will scan these models for changes)
from app.database import Base
target_metadata = Base.metadata

# 6️⃣ Define how migrations run (offline vs online)
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# 7️⃣ Entry point
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

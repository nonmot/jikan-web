import os
from contextlib import contextmanager
from pathlib import Path

from jikan.db import reset_session_context_factory, set_session_context_factory
from sqlmodel import Session, create_engine

from app.logging import logger

db_path = os.getenv("JIKAN_DB_PATH")
if db_path is None:
    logger.warning("'JIKAN_DB_PATH' is not set.")
    home_dir = Path.home()
    db_path = f"{home_dir}/.jikan/database.db"


def create_db_session_context() -> None:
    engine = create_engine(f"sqlite:///{db_path}")

    @contextmanager
    def _session_context():
        with Session(engine) as session:
            yield session

    set_session_context_factory(_session_context)


def reset_db_session_context() -> None:
    reset_session_context_factory()

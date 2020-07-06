from typing import Generator

from app.database.session import SessiongLocal


def get_db() -> Generator:
    try:
        db = SessiongLocal()
        yield db
    finally:
        db.close()

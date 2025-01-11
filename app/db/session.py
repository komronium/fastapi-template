from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    url=str(settings.DATABASE_URL),
    pool_pre_ping=True,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    echo=settings.DEBUG
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from ..core.config import settings


_engine: Optional[AsyncEngine] = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        url = settings.db_url or "postgresql+asyncpg://user:pass@localhost:5432/finmind"
        _engine = create_async_engine(url, future=True)
    return _engine


"""
Database Connection & Session Management

Sets up SQLAlchemy async engine and session factory.

TODO:
- Create async engine using create_async_engine(DATABASE_URL)
- Create async session factory using async_sessionmaker
- Create Base class for models using DeclarativeBase
- Create a `get_db()` async generator dependency for FastAPI:
    async def get_db() -> AsyncGenerator[AsyncSession, None]:
        async with async_session() as session:
            yield session
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


# TODO: Create engine and session factory
# engine = create_async_engine(settings.DATABASE_URL)
# async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    """FastAPI dependency that yields a database session.

    Usage in route:
        @router.get("/example")
        async def example(db: AsyncSession = Depends(get_db)):
            ...

    Hints:
        - Use `async with async_session() as session`
        - yield the session so FastAPI manages its lifecycle
    """
    pass

"""
Company Service

Business logic for company management and watchlists.

TODO: Implement each function. Called by the companies API routes.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


async def search_companies(db: AsyncSession, query: str = "", skip: int = 0, limit: int = 20):
    """Search companies by ticker or name.

    Args:
        db: Database session.
        query: Search string (matched against ticker and name with ILIKE).
        skip: Pagination offset.
        limit: Max results to return.

    Returns:
        Tuple of (list[Company], total_count).

    Hints:
        - Use `Company.ticker.ilike(f"%{query}%")` for fuzzy matching
        - Also search Company.name
        - Use `select(func.count()).select_from(Company)` for total
    """
    pass


async def get_company_by_id(db: AsyncSession, company_id: UUID):
    """Get a single company by ID with its financial data.

    Returns:
        Company model instance or None.
    """
    pass


async def create_company(db: AsyncSession, ticker: str, name: str, sector: str | None = None, industry: str | None = None):
    """Create a new company entry.

    Returns:
        The created Company instance.

    Raises:
        ValueError: If ticker already exists.

    Hints:
        - After creating, trigger a Celery task to scrape initial data:
          `scrape_company_data.delay(str(company.id), ticker)`
    """
    pass


async def get_user_watchlist(db: AsyncSession, user_id: UUID):
    """Get all companies in a user's watchlist.

    Returns:
        list[Company] — the companies the user is watching.

    Hints:
        - Join Watchlist with Company
        - Filter by user_id
    """
    pass


async def add_to_watchlist(db: AsyncSession, user_id: UUID, company_id: UUID):
    """Add a company to the user's watchlist.

    Raises:
        ValueError: If already in watchlist or company doesn't exist.
    """
    pass


async def remove_from_watchlist(db: AsyncSession, user_id: UUID, company_id: UUID):
    """Remove a company from the user's watchlist.

    Raises:
        ValueError: If not in watchlist.
    """
    pass

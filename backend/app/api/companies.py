"""
Companies API Routes

Manage companies and user watchlists.

Endpoints:
    GET    /api/companies          — Search/list companies
    GET    /api/companies/{id}     — Get company details
    POST   /api/companies          — Add a new company (triggers initial scrape)
    GET    /api/companies/watchlist — Get user's watchlist
    POST   /api/companies/watchlist/{company_id} — Add company to watchlist
    DELETE /api/companies/watchlist/{company_id} — Remove from watchlist
"""

from fastapi import APIRouter, Depends
from uuid import UUID

router = APIRouter(prefix="/api/companies", tags=["companies"])


@router.get("/")
async def list_companies():
    """Search and list companies.

    Query params: q (search string), skip (int), limit (int)
    Response: CompanyList

    Hints:
        - Search by ticker OR name using ILIKE
        - Default limit=20, max limit=100
        - Return total count for pagination
    """
    pass


@router.get("/watchlist")
async def get_watchlist():
    """Get the current user's watchlist with latest financial summaries.

    Response: list[CompanyResponse] (with nested financial summary)

    Hints:
        - Requires authentication (Depends(get_current_user))
        - Join with latest financial_data to include summary metrics
    """
    pass


@router.post("/watchlist/{company_id}")
async def add_to_watchlist(company_id: UUID):
    """Add a company to the user's watchlist.

    Response: {"message": "Added to watchlist"}

    Hints:
        - Check company exists → 404 if not
        - Check not already in watchlist → 400 if duplicate
        - Create Watchlist entry
    """
    pass


@router.delete("/watchlist/{company_id}")
async def remove_from_watchlist(company_id: UUID):
    """Remove a company from the user's watchlist.

    Response: {"message": "Removed from watchlist"}
    """
    pass


@router.get("/{company_id}")
async def get_company(company_id: UUID):
    """Get detailed company info with financial data.

    Response: CompanyResponse with latest financial data

    Hints:
        - Include recent financial_data entries
        - 404 if company not found
    """
    pass


@router.post("/")
async def create_company():
    """Add a new company to track.

    Request body: CompanyCreate (ticker, name, sector, industry)
    Response: CompanyResponse

    Hints:
        - Check if ticker already exists → 400 if so
        - Create company in DB
        - Trigger an async Celery task to scrape initial data
        - Return 201 with the new company
    """
    pass

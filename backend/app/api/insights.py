"""
Insights API Routes

Generate and retrieve AI-powered insights from financial data.

Endpoints:
    GET  /api/insights/{company_id}          — Get AI-generated insights for a company
    GET  /api/insights/{company_id}/financial — Get raw financial data
    POST /api/insights/{company_id}/generate  — Trigger fresh insight generation
"""

from fastapi import APIRouter, Depends
from uuid import UUID

router = APIRouter(prefix="/api/insights", tags=["insights"])


@router.get("/{company_id}")
async def get_insights(company_id: UUID):
    """Get AI-generated insights for a company.

    Response: InsightResponse (summary, key_metrics, trends)

    Hints:
        - Call insight_service.get_or_generate_insights(db, company_id)
        - Cache results in Redis (TTL: 1 hour) to avoid redundant AI calls
        - Return cached version if available and fresh
    """
    pass


@router.get("/{company_id}/financial")
async def get_financial_data(company_id: UUID):
    """Get raw financial data for a company.

    Query params: data_type (str, optional), period (str, optional)
    Response: list[FinancialDataResponse]

    Hints:
        - Filter by data_type if provided (e.g., "income_statement")
        - Order by date descending
        - Default to last 8 quarters
    """
    pass


@router.post("/{company_id}/generate")
async def generate_insights(company_id: UUID):
    """Trigger fresh insight generation for a company.

    Response: InsightResponse

    Hints:
        - Fetch latest financial data from DB
        - Send to AI service to generate narrative insights
        - Store/cache the result
        - This is an expensive operation — consider rate limiting
    """
    pass

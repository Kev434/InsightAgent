"""
Financial Data Schemas (Pydantic)

Request/response models for financial data endpoints.

TODO:
- FinancialDataResponse: id, company_id, data_type, period, date, metrics (dict), source, created_at
- InsightRequest: company_id (UUID), question (str | None)
- InsightResponse: company_id, ticker, summary (str), key_metrics (dict), trends (list[dict])
    - trends example: [{"metric": "revenue", "direction": "up", "change_pct": 12.5}]
- FinancialSummary: ticker, name, latest_price (float | None), revenue (float | None),
    net_income (float | None), pe_ratio (float | None)
"""

from pydantic import BaseModel


class FinancialDataResponse(BaseModel):
    """Schema for raw financial data in API responses."""
    pass


class InsightRequest(BaseModel):
    """Schema for requesting AI-generated insights about a company."""
    pass


class InsightResponse(BaseModel):
    """Schema for AI-generated insight results."""
    pass


class FinancialSummary(BaseModel):
    """Condensed financial overview for dashboard cards."""
    pass

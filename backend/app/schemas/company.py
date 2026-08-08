"""
Company Schemas (Pydantic)

Request/response models for company-related endpoints.

TODO:
- CompanyCreate: ticker (str), name (str), sector (str | None), industry (str | None)
- CompanyResponse: id, ticker, name, sector, industry, description, created_at
    - from_attributes=True for ORM
- CompanySearchQuery: query (str) — for searching companies by name or ticker
- CompanyList: companies (list[CompanyResponse]), total (int)
"""

from pydantic import BaseModel


class CompanyCreate(BaseModel):
    """Schema for adding a new company."""
    pass


class CompanyResponse(BaseModel):
    """Schema for company data in API responses."""
    pass


class CompanySearchQuery(BaseModel):
    """Schema for company search parameters."""
    pass


class CompanyList(BaseModel):
    """Paginated list of companies."""
    pass

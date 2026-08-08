"""
Financial Data Model

Stores scraped financial data points for companies.

TODO:
- Define the `financial_data` table with these columns:
    - id: UUID, primary key
    - company_id: UUID, ForeignKey("companies.id"), not null, indexed
    - data_type: String, not null (e.g., "income_statement", "balance_sheet", "stock_price")
    - period: String, not null (e.g., "2024-Q1", "2024-annual")
    - date: Date, not null
    - metrics: JSON, not null (flexible dict for different financial metrics)
        Example for income_statement:
        {"revenue": 94836000000, "net_income": 23636000000, "eps": 1.53}
        Example for stock_price:
        {"open": 150.0, "close": 155.0, "high": 156.0, "low": 149.0, "volume": 5000000}
    - source: String, nullable (e.g., "sec_edgar", "yahoo_finance")
    - raw_filing_url: String, nullable (link to original source)
    - created_at: DateTime, default=utcnow
- Add relationships:
    - company: relationship("Company", back_populates="financial_data")
- Add unique constraint on (company_id, data_type, period)
"""

from app.core.database import Base


class FinancialData(Base):
    __tablename__ = "financial_data"

    # TODO: Define columns
    pass

"""
Company Model

Represents a publicly traded company that can be tracked.

TODO:
- Define the `companies` table with these columns:
    - id: UUID, primary key
    - ticker: String(10), unique, not null, indexed (e.g., "AAPL")
    - name: String, not null (e.g., "Apple Inc.")
    - sector: String, nullable (e.g., "Technology")
    - industry: String, nullable
    - cik: String, nullable (SEC Central Index Key)
    - description: Text, nullable
    - created_at: DateTime, default=utcnow
    - updated_at: DateTime, onupdate=utcnow
- Add relationships:
    - financial_data: relationship("FinancialData", back_populates="company")
    - watchlists: relationship("Watchlist", back_populates="company")
"""

from app.core.database import Base


class Company(Base):
    __tablename__ = "companies"

    # TODO: Define columns
    pass

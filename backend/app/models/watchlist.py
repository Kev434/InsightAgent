"""
Watchlist Model

Maps users to companies they're tracking.

TODO:
- Define the `watchlists` table with these columns:
    - id: UUID, primary key
    - user_id: UUID, ForeignKey("users.id"), not null, indexed
    - company_id: UUID, ForeignKey("companies.id"), not null, indexed
    - added_at: DateTime, default=utcnow
- Add unique constraint on (user_id, company_id) — user can't watch same company twice
- Add relationships:
    - user: relationship("User", back_populates="watchlists")
    - company: relationship("Company", back_populates="watchlists")
"""

from app.core.database import Base


class Watchlist(Base):
    __tablename__ = "watchlists"

    # TODO: Define columns
    pass

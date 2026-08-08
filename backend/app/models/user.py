"""
User Model

Represents a registered user in the system.

TODO:
- Define the `users` table with these columns:
    - id: UUID, primary key, default=uuid4
    - email: String, unique, not null, indexed
    - hashed_password: String, not null
    - full_name: String, nullable
    - is_active: Boolean, default=True
    - created_at: DateTime, default=utcnow
    - updated_at: DateTime, onupdate=utcnow
- Add relationships:
    - watchlists: relationship("Watchlist", back_populates="user")
    - chat_messages: relationship("ChatMessage", back_populates="user")
"""

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    # TODO: Define columns
    pass

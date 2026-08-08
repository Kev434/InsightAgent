"""
Chat History Model

Stores conversation messages between users and the AI agent.

TODO:
- Define the `chat_messages` table with these columns:
    - id: UUID, primary key
    - user_id: UUID, ForeignKey("users.id"), not null, indexed
    - role: String, not null (either "user" or "assistant")
    - content: Text, not null
    - company_id: UUID, ForeignKey("companies.id"), nullable
        (if the message is about a specific company)
    - created_at: DateTime, default=utcnow
- Add relationships:
    - user: relationship("User", back_populates="chat_messages")
"""

from app.core.database import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    # TODO: Define columns
    pass

"""
Chat Schemas (Pydantic)

Request/response models for the AI chat feature.

TODO:
- ChatMessageRequest: content (str), company_id (UUID | None)
    - company_id is optional; if provided, the AI focuses on that company's data
- ChatMessageResponse: id, role ("user" | "assistant"), content, company_id, created_at
- ChatHistory: messages (list[ChatMessageResponse])
"""

from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    """Schema for sending a message to the AI agent."""
    pass


class ChatMessageResponse(BaseModel):
    """Schema for a single chat message in responses."""
    pass


class ChatHistory(BaseModel):
    """Schema for a list of chat messages."""
    pass

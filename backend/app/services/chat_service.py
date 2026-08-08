"""
Chat Service

Business logic for the AI chat agent.

TODO: Implement each function. Called by the chat API routes.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


async def process_message(db: AsyncSession, user_id: UUID, content: str, company_id: UUID | None = None):
    """Process a user message and generate AI response.

    Args:
        db: Database session.
        user_id: The authenticated user's ID.
        content: The user's message text.
        company_id: Optional company to focus the conversation on.

    Returns:
        ChatMessageResponse for the assistant's reply.

    Steps:
    1. Save user message to chat_messages table
    2. Load recent chat history (last 20 messages for this user)
    3. If company_id is provided:
       a. Fetch company info from DB
       b. Fetch recent financial data for that company
       c. Include as context in the AI prompt
    4. Build the system prompt (see SYSTEM_PROMPT below)
    5. Call AI service with chat history + context
    6. Save assistant response to chat_messages table
    7. Return the assistant's ChatMessageResponse
    """
    pass


async def get_chat_history(db: AsyncSession, user_id: UUID, limit: int = 50, company_id: UUID | None = None):
    """Retrieve chat history for a user.

    Args:
        db: Database session.
        user_id: The user's ID.
        limit: Max messages to return.
        company_id: Optional filter by company.

    Returns:
        list[ChatMessage] ordered by created_at ascending.
    """
    pass


# System prompt for the AI agent — customize this!
SYSTEM_PROMPT = """You are InsightAgent, an AI financial analyst assistant. You help users
understand company financial data, market trends, and investment insights.

Your capabilities:
- Analyze income statements, balance sheets, and cash flow data
- Identify trends in revenue, profitability, and growth
- Compare companies and sectors
- Explain financial metrics in plain language
- Provide data-driven insights (NOT investment advice)

Rules:
- Always base your analysis on the provided data
- Be specific — cite numbers and percentages
- If you don't have data to answer a question, say so
- Never give investment advice or recommendations to buy/sell
- Be concise but thorough

{context}
"""

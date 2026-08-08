"""
Chat API Routes

Conversational AI interface for exploring financial data.

Endpoints:
    POST /api/chat              — Send a message to the AI agent
    GET  /api/chat/history      — Get chat history
    WS   /api/chat/ws           — WebSocket for real-time chat (stretch goal)
"""

from fastapi import APIRouter, Depends, WebSocket

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("/")
async def send_message():
    """Send a message to the AI financial analyst agent.

    Request body: ChatMessageRequest (content, company_id?)
    Response: ChatMessageResponse

    Steps:
    1. Save user message to chat_messages table
    2. Load recent chat history (last 20 messages) for context
    3. If company_id provided, fetch that company's financial data
    4. Build prompt with financial context + chat history
    5. Call AI service (Claude/OpenAI) to generate response
    6. Save assistant message to chat_messages table
    7. Return the assistant's response

    Hints:
        - Use chat_service.process_message(db, user, message)
        - The AI should have access to the company's financial data as context
    """
    pass


@router.get("/history")
async def get_chat_history():
    """Get the user's chat history.

    Query params: limit (int, default=50), company_id (UUID, optional)
    Response: ChatHistory

    Hints:
        - Filter by company_id if provided
        - Order by created_at ascending (oldest first)
        - Requires authentication
    """
    pass


@router.websocket("/ws")
async def chat_websocket(websocket: WebSocket):
    """WebSocket endpoint for real-time streaming chat.

    This is a stretch goal — implement the REST endpoint first.

    Flow:
    1. Accept WebSocket connection
    2. Authenticate via token in query params
    3. Loop: receive message → stream AI response tokens back
    4. Handle disconnect gracefully

    Hints:
        - Use `await websocket.accept()`
        - Authenticate: token = websocket.query_params.get("token")
        - Stream response chunks with `await websocket.send_text(chunk)`
    """
    pass

/**
 * AI Chat Page
 *
 * Conversational interface for exploring financial data with the AI agent.
 *
 * TODO:
 * - Chat message list (scrollable, auto-scroll to bottom)
 * - Message input with send button
 * - Company selector dropdown (optional — focus chat on a specific company)
 * - Load chat history from GET /api/chat/history
 * - Send messages via POST /api/chat
 * - Display AI responses with markdown rendering
 * - Loading indicator while AI is generating
 *
 * Stretch goal: WebSocket for streaming responses
 *
 * Layout:
 * ┌──────────────────────────────────────────────┐
 * │  AI Financial Analyst    [Company: All ▼]    │
 * ├──────────────────────────────────────────────┤
 * │                                              │
 * │  User: What's Apple's revenue trend?         │
 * │                                              │
 * │  AI: Apple's revenue has grown 12% YoY...    │
 * │      Key highlights:                         │
 * │      - Q1 2024: $94.8B (+2.1% QoQ)          │
 * │      - Services segment: fastest growing...  │
 * │                                              │
 * │  User: Compare it to Microsoft               │
 * │                                              │
 * │  AI: Comparing AAPL vs MSFT...               │
 * │                                              │
 * ├──────────────────────────────────────────────┤
 * │  [Type your message...              ] [Send] │
 * └──────────────────────────────────────────────┘
 */

export default function ChatPage() {
  // TODO: Implement chat interface
  return (
    <main>
      <h1>AI Financial Analyst</h1>
      <div>{/* Chat messages */}</div>
      <form>{/* Message input + send button */}</form>
    </main>
  );
}

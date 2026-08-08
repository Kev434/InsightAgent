/**
 * useChat Hook
 *
 * Manages chat state and communication with the AI agent.
 *
 * TODO:
 * - Provide `messages` state (list of chat messages)
 * - Provide `isGenerating` state (true while AI is responding)
 * - Provide functions:
 *   - sendMessage(content, companyId?) → POST /api/chat
 *   - loadHistory(companyId?) → GET /api/chat/history
 *   - clearMessages() → reset local state
 * - Auto-load history on mount
 * - Optimistically add user message to list before API response
 *
 * Returns:
 *   { messages, isGenerating, sendMessage, loadHistory, clearMessages }
 */

export function useChat() {
  // TODO: Implement chat hook
  return {
    messages: [],
    isGenerating: false,
    sendMessage: async (content: string, companyId?: string) => {},
    loadHistory: async (companyId?: string) => {},
    clearMessages: () => {},
  };
}

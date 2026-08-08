/**
 * ChatMessage Component
 *
 * Renders a single chat message bubble.
 *
 * Props:
 * - role: "user" | "assistant"
 * - content: string (may contain markdown)
 * - timestamp: string
 *
 * TODO:
 * - User messages: right-aligned, blue background
 * - Assistant messages: left-aligned, gray background
 * - Render markdown in assistant messages (bold, lists, code blocks)
 * - Show timestamp below the message
 * - Avatar/icon for assistant messages
 */

interface ChatMessageProps {
  role: "user" | "assistant";
  content: string;
  timestamp: string;
}

export default function ChatMessage({ role, content, timestamp }: ChatMessageProps) {
  // TODO: Implement message bubble
  return (
    <div>
      <strong>{role}:</strong> {content}
    </div>
  );
}

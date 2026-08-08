/**
 * Sidebar Component
 *
 * Navigation sidebar for the application.
 *
 * TODO:
 * - Logo/brand at the top
 * - Navigation links:
 *   - Dashboard (/)
 *   - AI Chat (/chat)
 *   - Settings (stretch goal)
 * - Highlight active route
 * - User info + logout button at the bottom
 * - Collapsible on mobile
 */

export default function Sidebar() {
  // TODO: Implement sidebar navigation
  return (
    <aside>
      <nav>
        <ul>
          <li><a href="/">Dashboard</a></li>
          <li><a href="/chat">AI Chat</a></li>
        </ul>
      </nav>
    </aside>
  );
}

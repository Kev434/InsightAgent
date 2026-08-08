/**
 * Home / Dashboard Page
 *
 * This is the main dashboard page users see after logging in.
 *
 * TODO:
 * - Redirect to /login if not authenticated
 * - Display user's watchlist as cards (CompanyCard component)
 * - Each card shows: ticker, name, latest price, price change, mini chart
 * - "Add Company" button that opens a search modal
 * - Summary stats at the top (total companies tracked, market overview)
 *
 * Layout:
 * ┌─────────────────────────────────────────────┐
 * │  Header (logo, user menu)                   │
 * ├──────────┬──────────────────────────────────┤
 * │          │  Summary Stats Row               │
 * │ Sidebar  │  ┌──────┐ ┌──────┐ ┌──────┐     │
 * │          │  │ Card │ │ Card │ │ Card │     │
 * │ - Dashboard│ └──────┘ └──────┘ └──────┘     │
 * │ - Chat   │  ┌──────┐ ┌──────┐ ┌──────┐     │
 * │ - Settings│ │ Card │ │ Card │ │ + Add│     │
 * │          │  └──────┘ └──────┘ └──────┘     │
 * └──────────┴──────────────────────────────────┘
 */

export default function DashboardPage() {
  // TODO: Implement dashboard
  return (
    <main>
      <h1>InsightAgent Dashboard</h1>
      <p>Your financial insights, powered by AI.</p>
    </main>
  );
}

/**
 * Company Detail Page
 *
 * Shows detailed financial data and AI insights for a single company.
 *
 * TODO:
 * - Fetch company data from GET /api/companies/{id}
 * - Fetch insights from GET /api/insights/{id}
 * - Display:
 *   - Company header (name, ticker, sector, current price)
 *   - Stock price chart (line chart using Recharts)
 *   - Financial metrics table (revenue, net income, EPS over time)
 *   - AI Insights section (narrative summary, key metrics, trends)
 *   - "Refresh Data" button → POST /api/insights/{id}/generate
 *   - "Chat about this company" button → opens chat with company context
 *
 * Layout:
 * ┌──────────────────────────────────────────────┐
 * │  AAPL - Apple Inc.          $178.50 (+1.3%)  │
 * ├──────────────────────────────────────────────┤
 * │  [Stock Price Chart - 1Y line chart]         │
 * ├─────────────────────┬────────────────────────┤
 * │  Financial Metrics   │  AI Insights          │
 * │  ┌─────────────────┐ │  "Apple's revenue..." │
 * │  │ Revenue  | $94B │ │  Key: Revenue +12%    │
 * │  │ Income   | $23B │ │  Trend: Growing       │
 * │  └─────────────────┘ │                       │
 * └─────────────────────┴────────────────────────┘
 */

export default function CompanyDetailPage({
  params,
}: {
  params: { id: string };
}) {
  // TODO: Implement company detail view
  return (
    <main>
      <h1>Company Detail: {params.id}</h1>
    </main>
  );
}

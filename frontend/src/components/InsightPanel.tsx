/**
 * InsightPanel Component
 *
 * Displays AI-generated insights for a company.
 *
 * Props:
 * - insights: { summary, key_metrics, trends }
 * - isLoading: boolean
 * - onRefresh: () => void
 *
 * TODO:
 * - Summary section: rendered as paragraphs
 * - Key Metrics: displayed as highlighted stat cards
 * - Trends: list with directional arrows (↑ green, ↓ red)
 * - "Refresh Insights" button that calls onRefresh
 * - Loading skeleton while generating
 */

interface InsightPanelProps {
  insights?: {
    summary: string;
    key_metrics: Record<string, number | string>;
    trends: Array<{
      metric: string;
      direction: "up" | "down" | "flat";
      change_pct: number;
    }>;
  };
  isLoading: boolean;
  onRefresh: () => void;
}

export default function InsightPanel({ insights, isLoading, onRefresh }: InsightPanelProps) {
  // TODO: Implement insight display
  return (
    <div>
      <h3>AI Insights</h3>
      {isLoading ? <p>Generating insights...</p> : <p>{insights?.summary}</p>}
    </div>
  );
}

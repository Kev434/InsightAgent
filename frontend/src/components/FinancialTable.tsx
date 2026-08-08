/**
 * FinancialTable Component
 *
 * Displays financial metrics in a table format.
 *
 * Props:
 * - data: Array of financial records with period and metrics
 * - dataType: "income_statement" | "balance_sheet" | "stock_price"
 *
 * TODO:
 * - Render a table with periods as columns and metrics as rows
 * - Format numbers (abbreviate millions/billions, add $ prefix)
 * - Highlight positive/negative changes with color
 * - Allow sorting by period
 *
 * Example layout:
 * ┌─────────────┬──────────┬──────────┬──────────┐
 * │ Metric      │ Q1 2024  │ Q4 2023  │ Q3 2023  │
 * ├─────────────┼──────────┼──────────┼──────────┤
 * │ Revenue     │ $94.8B   │ $119.6B  │ $89.5B   │
 * │ Net Income  │ $23.6B   │ $33.9B   │ $22.9B   │
 * │ EPS         │ $1.53    │ $2.18    │ $1.46    │
 * └─────────────┴──────────┴──────────┴──────────┘
 */

interface FinancialTableProps {
  data: Array<{
    period: string;
    metrics: Record<string, number>;
  }>;
  dataType: string;
}

export default function FinancialTable({ data, dataType }: FinancialTableProps) {
  // TODO: Implement table
  return (
    <div>
      <p>Financial table placeholder — {dataType}</p>
    </div>
  );
}

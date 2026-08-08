/**
 * StockChart Component
 *
 * Displays a stock price chart using Recharts.
 *
 * Props:
 * - data: Array of { date, close, volume } objects
 * - period: "1mo" | "3mo" | "6mo" | "1y" | "5y"
 *
 * TODO:
 * - Line chart for closing prices (primary)
 * - Optional bar chart overlay for volume
 * - Period selector buttons (1M, 3M, 6M, 1Y, 5Y)
 * - Tooltip showing date, price, volume on hover
 * - Responsive container
 *
 * Hints:
 * - Use Recharts: LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer
 * - Format dates on X-axis (e.g., "Jan 24")
 * - Format prices with $ and commas
 */

interface StockChartProps {
  data: Array<{
    date: string;
    close: number;
    volume?: number;
  }>;
  period?: string;
}

export default function StockChart({ data, period = "1y" }: StockChartProps) {
  // TODO: Implement chart with Recharts
  return (
    <div>
      <p>Stock chart placeholder — {data.length} data points</p>
    </div>
  );
}

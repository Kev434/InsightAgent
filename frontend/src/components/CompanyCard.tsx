/**
 * CompanyCard Component
 *
 * Displays a summary card for a company in the dashboard watchlist.
 *
 * Props:
 * - company: { id, ticker, name, sector }
 * - financials?: { price, change, change_percent, revenue }
 *
 * TODO:
 * - Display ticker (large, bold), company name, sector
 * - Show current price and price change (green if +, red if -)
 * - Mini sparkline chart of recent prices (optional, use Recharts)
 * - Click navigates to /company/{id}
 * - "Remove from watchlist" button (X icon in corner)
 */

interface CompanyCardProps {
  company: {
    id: string;
    ticker: string;
    name: string;
    sector?: string;
  };
  financials?: {
    price: number;
    change: number;
    change_percent: number;
  };
}

export default function CompanyCard({ company, financials }: CompanyCardProps) {
  // TODO: Implement card UI
  return (
    <div>
      <h3>{company.ticker}</h3>
      <p>{company.name}</p>
    </div>
  );
}

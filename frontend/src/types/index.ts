/**
 * TypeScript Type Definitions
 *
 * Shared types that match the backend Pydantic schemas.
 * Keep these in sync with backend/app/schemas/*.py
 */

export interface User {
  id: string;
  email: string;
  full_name: string | null;
  is_active: boolean;
  created_at: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface Company {
  id: string;
  ticker: string;
  name: string;
  sector: string | null;
  industry: string | null;
  description: string | null;
  created_at: string;
}

export interface FinancialData {
  id: string;
  company_id: string;
  data_type: string;
  period: string;
  date: string;
  metrics: Record<string, number>;
  source: string | null;
  created_at: string;
}

export interface Insight {
  company_id: string;
  ticker: string;
  summary: string;
  key_metrics: Record<string, number | string>;
  trends: Trend[];
}

export interface Trend {
  metric: string;
  direction: "up" | "down" | "flat";
  change_pct: number;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  company_id: string | null;
  created_at: string;
}

export interface FinancialSummary {
  ticker: string;
  name: string;
  latest_price: number | null;
  revenue: number | null;
  net_income: number | null;
  pe_ratio: number | null;
}

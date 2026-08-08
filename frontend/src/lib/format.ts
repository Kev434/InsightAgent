/**
 * Formatting Utilities
 *
 * Helper functions for formatting numbers, dates, and currencies.
 *
 * TODO: Implement each function.
 */

export function formatCurrency(value: number): string {
  /**
   * Format a number as USD currency.
   * Examples: 1234.56 → "$1,234.56", 1500000000 → "$1.5B"
   *
   * Hints:
   * - Use Intl.NumberFormat for basic formatting
   * - For large numbers, abbreviate: K (thousands), M (millions), B (billions), T (trillions)
   */
  return "";
}

export function formatPercent(value: number): string {
  /**
   * Format a number as percentage.
   * Examples: 0.1234 → "12.34%", -0.05 → "-5.00%"
   */
  return "";
}

export function formatDate(dateString: string): string {
  /**
   * Format an ISO date string for display.
   * Examples: "2024-01-15" → "Jan 15, 2024"
   */
  return "";
}

export function formatLargeNumber(value: number): string {
  /**
   * Abbreviate large numbers.
   * Examples: 94836000000 → "94.8B", 1500000 → "1.5M"
   */
  return "";
}

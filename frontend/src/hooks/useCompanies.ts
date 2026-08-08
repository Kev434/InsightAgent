/**
 * useCompanies Hook
 *
 * Fetches and manages company/watchlist data.
 *
 * TODO:
 * - Provide `watchlist` state (list of companies user is tracking)
 * - Provide `searchResults` state for company search
 * - Provide functions:
 *   - fetchWatchlist() → GET /api/companies/watchlist
 *   - searchCompanies(query) → GET /api/companies?q={query}
 *   - addToWatchlist(companyId) → POST /api/companies/watchlist/{id}
 *   - removeFromWatchlist(companyId) → DELETE /api/companies/watchlist/{id}
 * - Auto-fetch watchlist on mount
 *
 * Returns:
 *   { watchlist, searchResults, isLoading, fetchWatchlist, searchCompanies, addToWatchlist, removeFromWatchlist }
 */

export function useCompanies() {
  // TODO: Implement companies hook
  return {
    watchlist: [],
    searchResults: [],
    isLoading: true,
    fetchWatchlist: async () => {},
    searchCompanies: async (query: string) => {},
    addToWatchlist: async (companyId: string) => {},
    removeFromWatchlist: async (companyId: string) => {},
  };
}

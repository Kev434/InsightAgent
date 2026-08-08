/**
 * API Client
 *
 * Centralized HTTP client for backend API calls.
 *
 * TODO:
 * - Create an axios instance with baseURL and default headers
 * - Add request interceptor to attach JWT token from localStorage
 * - Add response interceptor to handle 401 (redirect to /login)
 * - Export typed API functions for each endpoint:
 *
 *   Auth:
 *   - api.auth.login(email, password) → POST /api/auth/login
 *   - api.auth.register(email, password, fullName) → POST /api/auth/register
 *   - api.auth.getMe() → GET /api/auth/me
 *
 *   Companies:
 *   - api.companies.list(query?, skip?, limit?) → GET /api/companies
 *   - api.companies.get(id) → GET /api/companies/{id}
 *   - api.companies.create(data) → POST /api/companies
 *   - api.companies.getWatchlist() → GET /api/companies/watchlist
 *   - api.companies.addToWatchlist(id) → POST /api/companies/watchlist/{id}
 *   - api.companies.removeFromWatchlist(id) → DELETE /api/companies/watchlist/{id}
 *
 *   Insights:
 *   - api.insights.get(companyId) → GET /api/insights/{id}
 *   - api.insights.getFinancials(companyId) → GET /api/insights/{id}/financial
 *   - api.insights.generate(companyId) → POST /api/insights/{id}/generate
 *
 *   Chat:
 *   - api.chat.send(content, companyId?) → POST /api/chat
 *   - api.chat.getHistory(limit?, companyId?) → GET /api/chat/history
 *
 * Hints:
 *   import axios from "axios";
 *   const client = axios.create({ baseURL: "/api" });
 *   client.interceptors.request.use(config => {
 *     const token = localStorage.getItem("token");
 *     if (token) config.headers.Authorization = `Bearer ${token}`;
 *     return config;
 *   });
 */

import axios from "axios";

const client = axios.create({
  baseURL: "/api",
});

// TODO: Add interceptors and export API functions

export default client;

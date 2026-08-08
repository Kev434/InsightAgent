/**
 * useAuth Hook
 *
 * Manages authentication state across the app.
 *
 * TODO:
 * - Store JWT token in localStorage
 * - Provide login(email, password) function
 * - Provide register(email, password, fullName) function
 * - Provide logout() function (clear token, redirect to /login)
 * - Provide `user` state (null if not logged in)
 * - On mount, check for existing token and fetch user profile (GET /api/auth/me)
 * - Provide `isLoading` state for initial auth check
 *
 * Returns:
 *   { user, isLoading, login, register, logout }
 *
 * Hints:
 * - Use React.useState and React.useEffect
 * - Store token: localStorage.setItem("token", token)
 * - Set axios default header: axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
 * - Consider using React Context for app-wide auth state
 */

export function useAuth() {
  // TODO: Implement auth hook
  return {
    user: null,
    isLoading: true,
    login: async (email: string, password: string) => {},
    register: async (email: string, password: string, fullName?: string) => {},
    logout: () => {},
  };
}

"""
Companies API Tests

TODO: Implement tests for company CRUD and watchlist operations.

Test cases to implement:
- test_list_companies: GET /api/companies → 200, returns paginated list
- test_search_companies: GET /api/companies?q=apple → filtered results
- test_create_company: POST /api/companies → 201
- test_create_duplicate_ticker: POST with existing ticker → 400
- test_get_company: GET /api/companies/{id} → 200
- test_get_company_not_found: GET /api/companies/{bad_id} → 404
- test_add_to_watchlist: POST /api/companies/watchlist/{id} → 200
- test_get_watchlist: GET /api/companies/watchlist → user's watchlist
- test_remove_from_watchlist: DELETE /api/companies/watchlist/{id} → 200
"""

import pytest


class TestListCompanies:
    async def test_list_companies(self):
        pass

    async def test_search_companies(self):
        pass


class TestCompanyCrud:
    async def test_create_company(self):
        pass

    async def test_get_company(self):
        pass


class TestWatchlist:
    async def test_add_to_watchlist(self):
        pass

    async def test_get_watchlist(self):
        pass

    async def test_remove_from_watchlist(self):
        pass

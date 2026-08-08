"""
Test Configuration & Fixtures

TODO:
- Set up a test database (use SQLite in-memory or test PostgreSQL)
- Create fixtures for:
    - test_db: AsyncSession connected to test database
    - test_client: httpx.AsyncClient with the FastAPI app
    - test_user: A pre-created user for authenticated tests
    - auth_headers: Authorization headers with a valid JWT

Hints:
    - Use pytest-asyncio for async test support
    - Override the get_db dependency to use the test database
    - Create tables with Base.metadata.create_all() in setup
    - Drop tables in teardown

Example:
    @pytest.fixture
    async def test_client(test_db):
        app.dependency_overrides[get_db] = lambda: test_db
        async with httpx.AsyncClient(app=app, base_url="http://test") as client:
            yield client
"""

import pytest

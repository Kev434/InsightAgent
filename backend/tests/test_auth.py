"""
Auth API Tests

TODO: Implement tests for registration, login, and profile endpoints.

Test cases to implement:
- test_register_success: Register with valid data → 201, returns user
- test_register_duplicate_email: Register same email twice → 400
- test_register_weak_password: Password too short → 422
- test_login_success: Login with correct credentials → 200, returns token
- test_login_wrong_password: Login with wrong password → 401
- test_login_nonexistent_email: Login with unknown email → 401
- test_get_me_authenticated: GET /api/auth/me with valid token → 200
- test_get_me_no_token: GET /api/auth/me without token → 401
"""

import pytest


class TestRegister:
    async def test_register_success(self):
        """POST /api/auth/register with valid data returns 201 and user info."""
        pass

    async def test_register_duplicate_email(self):
        """POST /api/auth/register with existing email returns 400."""
        pass


class TestLogin:
    async def test_login_success(self):
        """POST /api/auth/login with correct credentials returns JWT token."""
        pass

    async def test_login_wrong_password(self):
        """POST /api/auth/login with wrong password returns 401."""
        pass


class TestGetMe:
    async def test_get_me_authenticated(self):
        """GET /api/auth/me with valid token returns user profile."""
        pass

    async def test_get_me_no_token(self):
        """GET /api/auth/me without token returns 401."""
        pass

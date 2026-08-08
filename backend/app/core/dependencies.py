"""
Shared FastAPI Dependencies

Reusable dependency functions injected into route handlers.

TODO:
- Create `get_current_user(token, db)` dependency:
    - Extract token from Authorization header (OAuth2PasswordBearer)
    - Decode JWT to get user_id
    - Query DB for the user
    - Raise 401 if not found
    - Return the User model instance
"""

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Extract and validate the current user from the JWT token.

    Args:
        token: JWT from the Authorization header (injected by OAuth2PasswordBearer).

    Returns:
        The User model instance for the authenticated user.

    Raises:
        HTTPException(401) if token is invalid or user not found.

    Hints:
        - Call decode_access_token(token) to get payload
        - Extract user_id from payload["sub"]
        - Query the database for the user
        - Also inject `db: AsyncSession = Depends(get_db)`
    """
    pass

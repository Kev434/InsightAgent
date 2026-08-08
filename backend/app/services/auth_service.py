"""
Auth Service

Business logic for user registration and authentication.

TODO: Implement each function. These are called by the auth API routes.
"""

from sqlalchemy.ext.asyncio import AsyncSession


async def register_user(db: AsyncSession, email: str, password: str, full_name: str | None = None):
    """Register a new user.

    Args:
        db: Database session.
        email: User's email address.
        password: Plaintext password (will be hashed).
        full_name: Optional display name.

    Returns:
        The created User model instance.

    Raises:
        ValueError: If email already exists.

    Steps:
    1. Query DB to check if email is taken
    2. Hash the password using security.hash_password()
    3. Create a User instance and add to DB
    4. Commit and refresh
    5. Return the user
    """
    pass


async def authenticate_user(db: AsyncSession, email: str, password: str):
    """Authenticate a user by email and password.

    Args:
        db: Database session.
        email: User's email.
        password: Plaintext password to verify.

    Returns:
        The User model instance if credentials are valid.

    Raises:
        ValueError: If email not found or password incorrect.

    Steps:
    1. Query user by email
    2. Verify password with security.verify_password()
    3. Return user if valid, raise if not
    """
    pass

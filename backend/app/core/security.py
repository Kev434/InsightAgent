"""
Authentication & Security Utilities

Handles password hashing and JWT token creation/verification.

TODO:
- Create password hashing functions using passlib with bcrypt:
    - hash_password(password: str) -> str
    - verify_password(plain: str, hashed: str) -> bool
- Create JWT token functions using python-jose:
    - create_access_token(data: dict) -> str
        - Encode user_id into JWT with expiration
    - decode_access_token(token: str) -> dict
        - Decode and validate JWT, raise HTTPException if invalid
"""

from datetime import datetime, timedelta


def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt.

    Args:
        password: The plaintext password to hash.

    Returns:
        The bcrypt-hashed password string.
    """
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a bcrypt hash.

    Args:
        plain_password: The plaintext password to check.
        hashed_password: The stored bcrypt hash.

    Returns:
        True if the password matches, False otherwise.
    """
    pass


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create a JWT access token.

    Args:
        data: Payload dict — should include {"sub": user_id}.
        expires_delta: Optional custom expiration time.

    Returns:
        Encoded JWT string.

    Hints:
        - Use jose.jwt.encode()
        - Add "exp" claim using datetime.utcnow() + expires_delta
        - Get SECRET_KEY and ALGORITHM from settings
    """
    pass


def decode_access_token(token: str) -> dict:
    """Decode and validate a JWT access token.

    Args:
        token: The JWT string to decode.

    Returns:
        The decoded payload dict.

    Raises:
        HTTPException(401) if token is invalid or expired.

    Hints:
        - Use jose.jwt.decode()
        - Catch JWTError and raise HTTPException
    """
    pass

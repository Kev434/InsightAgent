"""
Auth API Routes

Handles user registration and login.

Endpoints:
    POST /api/auth/register  — Create a new user account
    POST /api/auth/login     — Login and receive JWT token
    GET  /api/auth/me        — Get current user profile

TODO:
- Implement each endpoint using the corresponding service functions
- Use Depends(get_db) for database sessions
- Use Depends(get_current_user) for protected routes
"""

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register")
async def register():
    """Register a new user.

    Request body: UserCreate (email, password, full_name)
    Response: UserResponse

    Steps:
    1. Check if email already exists → 400 if so
    2. Hash the password
    3. Create User in DB
    4. Return UserResponse

    Hints:
        - Use auth_service.register_user(db, user_data)
        - Return status_code=201 on success
    """
    pass


@router.post("/login")
async def login():
    """Authenticate user and return JWT token.

    Request body: UserLogin (email, password)
    Response: TokenResponse (access_token, token_type)

    Steps:
    1. Find user by email → 401 if not found
    2. Verify password → 401 if wrong
    3. Create JWT with user.id as subject
    4. Return TokenResponse

    Hints:
        - Use OAuth2PasswordRequestForm for standard OAuth2 login
        - Use auth_service.authenticate_user(db, email, password)
    """
    pass


@router.get("/me")
async def get_me():
    """Get current authenticated user's profile.

    Response: UserResponse

    Hints:
        - Use Depends(get_current_user) to get the user
        - Simply return the user as UserResponse
    """
    pass

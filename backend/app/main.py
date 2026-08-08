"""
InsightAgent — FastAPI Application Entry Point

This is the main file that creates and configures the FastAPI application.

TODO:
- Create the FastAPI app instance
- Include all API routers (auth, companies, insights, chat)
- Add CORS middleware (allow frontend origin)
- Add a startup event to verify DB connection
- Add a health check endpoint at GET /health
"""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Factory function to create and configure the FastAPI application.

    Steps:
    1. Instantiate FastAPI with title="InsightAgent API"
    2. Add CORSMiddleware (allow origins: ["http://localhost:3000"])
    3. Include routers from app.api with appropriate prefixes:
       - auth_router    → /api/auth
       - companies_router → /api/companies
       - insights_router  → /api/insights
       - chat_router      → /api/chat
    4. Return the app
    """
    pass


app = create_app()

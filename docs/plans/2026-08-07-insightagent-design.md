# InsightAgent — Design Document

## Overview
AI-powered multi-tenant SaaS platform that scrapes company financial data (SEC filings, stock prices), processes it through ETL pipelines, and lets users explore insights via a dashboard and conversational AI agent.

## Architecture
- **Backend**: FastAPI (Python), Celery workers, PostgreSQL, Redis
- **Frontend**: Next.js (React), Recharts, TailwindCSS
- **AI**: Claude/OpenAI API for chat and insight generation
- **Data Sources**: SEC EDGAR API, Yahoo Finance

## Data Flow
1. User adds a company (by ticker) to their watchlist
2. Celery task triggers ETL pipeline for that company
3. Pipeline: Extract (SEC + Yahoo) → Transform (normalize) → Load (PostgreSQL)
4. Dashboard displays financial data with charts and tables
5. AI generates narrative insights from the stored data
6. User can chat with AI agent about any company's financials

## Database Schema
- `users` — Authentication and profiles
- `companies` — Tracked companies (ticker, name, sector)
- `financial_data` — Scraped financial metrics (JSON metrics column)
- `watchlists` — User ↔ Company many-to-many
- `chat_messages` — Conversation history

## API Endpoints
- `POST /api/auth/register` — User registration
- `POST /api/auth/login` — JWT authentication
- `GET /api/auth/me` — Current user profile
- `GET /api/companies` — Search/list companies
- `GET/POST /api/companies/watchlist` — Manage watchlist
- `GET /api/insights/{company_id}` — AI-generated insights
- `POST /api/chat` — Send message to AI agent

## Implementation Order
1. Core setup (config, database, models, migrations)
2. Auth (register, login, JWT)
3. Company CRUD + watchlist
4. SEC EDGAR scraper
5. Yahoo Finance scraper
6. ETL pipeline
7. Celery worker setup
8. Insights generation (AI)
9. Chat agent
10. Frontend dashboard
11. Frontend company detail page
12. Frontend chat page

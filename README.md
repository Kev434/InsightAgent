# InsightAgent

AI-powered SaaS platform that scrapes company financial data, processes it through data pipelines, and generates meaningful insights via a dashboard and conversational AI agent.

## Tech Stack

### Backend
- **FastAPI** — REST API + WebSocket for AI chat
- **Celery** — Background task queue for scraping & ETL
- **PostgreSQL** — Relational database for users, companies, financial data
- **Redis** — Caching, job queues, rate limiting
- **SQLAlchemy** — ORM for database models
- **Alembic** — Database migrations

### Frontend
- **Next.js** (React) — Dashboard UI
- **Recharts** — Data visualization / charts
- **TailwindCSS** — Styling

### AI
- **Claude API / OpenAI API** — Powers the conversational AI agent
- **LangChain** (optional) — For RAG and context management

### Data Sources
- **SEC EDGAR API** — Company filings (10-K, 10-Q, 8-K)
- **Yahoo Finance** — Stock prices, market data
- **News APIs** — Financial news and sentiment

## Project Structure

```
insight-agent/
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── api/             # API route handlers
│   │   ├── core/            # Config, security, dependencies
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Business logic
│   │   ├── scrapers/        # Data scraping modules
│   │   ├── pipelines/       # ETL pipeline processors
│   │   ├── ai/              # AI agent logic
│   │   └── workers/         # Celery task definitions
│   ├── alembic/             # Database migrations
│   ├── tests/               # Backend tests
│   └── requirements.txt
├── frontend/                # Next.js application
│   ├── src/
│   │   ├── app/             # Next.js app router pages
│   │   ├── components/      # React components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── lib/             # Utility functions & API client
│   │   └── types/           # TypeScript type definitions
│   └── package.json
├── docker-compose.yml       # Local dev environment
└── docs/                    # Documentation & design docs
```

## Getting Started

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your API keys
3. Run `docker-compose up` to start PostgreSQL and Redis
4. Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
5. Frontend: `cd frontend && npm install && npm run dev`

## License

MIT

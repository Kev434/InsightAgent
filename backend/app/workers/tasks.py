"""
Celery Tasks

Background tasks for scraping and data processing.

TODO: Implement each task. These run asynchronously in Celery workers.

To run the worker:
    celery -A app.workers.celery_app worker --loglevel=info

To run the beat scheduler (for periodic tasks):
    celery -A app.workers.celery_app beat --loglevel=info
"""


def scrape_company_data(company_id: str, ticker: str):
    """Celery task: Run the full ETL pipeline for a company.

    This is triggered when:
    - A new company is added
    - A user manually requests a data refresh
    - The periodic beat schedule fires

    Args:
        company_id: UUID string of the company.
        ticker: Stock ticker symbol.

    Steps:
    1. Create a new DB session (can't reuse FastAPI's)
    2. Call etl.run_pipeline(db, company_id, ticker)
    3. Log results
    4. Close session

    Hints:
        - Decorate with @celery_app.task
        - Use synchronous DB session here (not async)
          since Celery workers don't use asyncio by default
        - Or use `asgiref.sync.async_to_sync` to call async functions
    """
    pass


def refresh_all_companies():
    """Celery task: Refresh data for all tracked companies.

    Called on a schedule (e.g., daily at midnight).

    Steps:
    1. Query all companies from DB
    2. For each company, dispatch scrape_company_data.delay(id, ticker)
    3. This fans out the work across multiple workers

    Hints:
        - Decorate with @celery_app.task
        - Configure in beat_schedule:
          celery_app.conf.beat_schedule = {
              "refresh-all-daily": {
                  "task": "app.workers.tasks.refresh_all_companies",
                  "schedule": crontab(hour=0, minute=0),
              }
          }
    """
    pass


def generate_company_insights(company_id: str):
    """Celery task: Generate AI insights for a company.

    Can be triggered after new data is scraped, or on demand.

    Steps:
    1. Fetch company and financial data from DB
    2. Call insight_service.generate_insights()
    3. Cache result in Redis
    """
    pass

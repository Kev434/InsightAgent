"""
ETL Pipeline

Extract → Transform → Load pipeline for financial data.

This is the core data engineering piece of the project. The pipeline:
1. EXTRACT: Scrape raw data from SEC EDGAR and Yahoo Finance
2. TRANSFORM: Clean, normalize, and structure the data
3. LOAD: Store processed data in PostgreSQL

TODO: Implement each function.
"""

from sqlalchemy.ext.asyncio import AsyncSession


async def run_pipeline(db: AsyncSession, company_id: str, ticker: str):
    """Run the full ETL pipeline for a company.

    This is the main orchestrator function. Called by Celery workers.

    Args:
        db: Database session.
        company_id: UUID of the company in the DB.
        ticker: Stock ticker symbol.

    Steps:
    1. Extract SEC filing data → extract_sec_data(ticker)
    2. Extract stock price data → extract_stock_data(ticker)
    3. Transform SEC data → transform_financial_statements(raw_sec_data)
    4. Transform stock data → transform_stock_prices(raw_stock_data)
    5. Load all transformed data → load_financial_data(db, company_id, transformed_data)
    6. Update company profile info if needed

    Returns:
        Dict summary: {"records_processed": int, "errors": list[str]}
    """
    pass


async def extract_sec_data(ticker: str) -> dict:
    """Extract raw financial data from SEC EDGAR.

    Returns:
        Raw API response dict with filing data and XBRL financials.

    Hints:
        - Call sec_edgar.get_company_cik(ticker)
        - Call sec_edgar.get_company_financials(cik)
        - Handle case where CIK is not found
    """
    pass


async def extract_stock_data(ticker: str) -> dict:
    """Extract stock price data from Yahoo Finance.

    Returns:
        Raw price history and current quote data.

    Hints:
        - Call yahoo_finance.get_stock_price(ticker)
        - Call yahoo_finance.get_stock_history(ticker, period="2y")
    """
    pass


def transform_financial_statements(raw_data: dict) -> list[dict]:
    """Transform raw SEC XBRL data into structured financial records.

    Args:
        raw_data: Raw XBRL API response.

    Returns:
        List of dicts ready for DB insertion:
        [
            {
                "data_type": "income_statement",
                "period": "2024-Q1",
                "date": "2024-03-31",
                "metrics": {"revenue": 94836000000, "net_income": 23636000000, ...},
                "source": "sec_edgar"
            },
            ...
        ]

    Hints:
        - Group XBRL data points by fiscal period
        - Normalize metric names (XBRL tags → friendly names)
        - Handle missing data gracefully (some companies report differently)
        - Deduplicate periods
    """
    pass


def transform_stock_prices(raw_data: dict) -> list[dict]:
    """Transform raw stock price data into structured records.

    Args:
        raw_data: Raw Yahoo Finance response.

    Returns:
        List of dicts ready for DB insertion:
        [
            {
                "data_type": "stock_price",
                "period": "2024-01-02",
                "date": "2024-01-02",
                "metrics": {"open": 150.0, "close": 155.0, "high": 156.0, "low": 149.0, "volume": 5000000},
                "source": "yahoo_finance"
            },
            ...
        ]
    """
    pass


async def load_financial_data(db: AsyncSession, company_id: str, records: list[dict]):
    """Load transformed financial records into the database.

    Args:
        db: Database session.
        company_id: UUID of the company.
        records: List of transformed data dicts.

    Hints:
        - Use upsert logic: if record for same (company_id, data_type, period) exists, update it
        - Batch insert for performance
        - Commit after all records are inserted
    """
    pass

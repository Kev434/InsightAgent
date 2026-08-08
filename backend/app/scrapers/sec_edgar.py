"""
SEC EDGAR Scraper

Fetches company filings (10-K, 10-Q, 8-K) from the SEC EDGAR API.

SEC EDGAR API docs: https://www.sec.gov/edgar/sec-api-documentation
- Free, no API key needed
- Requires a User-Agent header: "YourName your@email.com"
- Rate limit: 10 requests/second

TODO: Implement each function using httpx for HTTP requests.
"""

import httpx

# SEC EDGAR base URLs
EDGAR_BASE_URL = "https://efts.sec.gov/LATEST"
EDGAR_SUBMISSIONS_URL = "https://data.sec.gov/submissions"
EDGAR_COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts"


async def get_company_cik(ticker: str) -> str | None:
    """Look up a company's CIK (Central Index Key) by ticker symbol.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL").

    Returns:
        CIK string (zero-padded to 10 digits) or None if not found.

    Hints:
        - GET https://efts.sec.gov/LATEST/search-index?q={ticker}&dateRange=custom&startdt=2024-01-01
        - Or use the company tickers JSON:
          GET https://www.sec.gov/files/company_tickers.json
        - Set User-Agent header from settings.SEC_USER_AGENT
    """
    pass


async def get_company_filings(cik: str, filing_type: str = "10-K", count: int = 10) -> list[dict]:
    """Fetch recent filings for a company from EDGAR.

    Args:
        cik: Company CIK number.
        filing_type: Type of filing ("10-K", "10-Q", "8-K").
        count: Number of recent filings to fetch.

    Returns:
        List of filing dicts with keys: accession_number, filing_date, primary_document_url.

    Hints:
        - GET https://data.sec.gov/submissions/CIK{cik}.json
        - Response includes recent filings in `recentFilings`
        - Filter by form type
    """
    pass


async def get_company_financials(cik: str) -> dict:
    """Fetch structured financial data (XBRL) for a company.

    Args:
        cik: Company CIK number.

    Returns:
        Dict of financial metrics extracted from XBRL data:
        {
            "revenue": [{"period": "2024-Q1", "value": 94836000000}, ...],
            "net_income": [{"period": "2024-Q1", "value": 23636000000}, ...],
            "total_assets": [...],
            "total_liabilities": [...],
            "eps": [...]
        }

    Hints:
        - GET https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json
        - Navigate: response["facts"]["us-gaap"]
        - Key XBRL tags:
            Revenue: "Revenues" or "RevenueFromContractWithCustomerExcludingAssessedTax"
            Net Income: "NetIncomeLoss"
            Total Assets: "Assets"
            EPS: "EarningsPerShareBasic"
        - Each tag has "units" → "USD" → list of data points with "val", "end", "fp" (fiscal period)
    """
    pass

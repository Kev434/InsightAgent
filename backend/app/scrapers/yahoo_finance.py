"""
Yahoo Finance Scraper

Fetches stock price data and market info.

NOTE: Yahoo Finance does not have an official free API. Options:
- Use the `yfinance` Python library (wraps Yahoo Finance)
- Use Yahoo Finance v8 API (unofficial, may break)
- Use Alpha Vantage or Finnhub as alternatives

For this project, we'll use httpx to call Yahoo Finance's public endpoints.

TODO: Implement each function.
"""

import httpx


async def get_stock_price(ticker: str) -> dict | None:
    """Get current/latest stock price for a ticker.

    Args:
        ticker: Stock symbol (e.g., "AAPL").

    Returns:
        Dict with current price data:
        {
            "ticker": "AAPL",
            "price": 178.50,
            "change": 2.30,
            "change_percent": 1.31,
            "volume": 52340000,
            "market_cap": 2780000000000,
            "pe_ratio": 28.5,
            "52w_high": 199.62,
            "52w_low": 124.17
        }
        Returns None if ticker not found.

    Hints:
        - Consider using `yfinance` library: `pip install yfinance`
        - Alternative: Yahoo Finance v8 quote endpoint
          GET https://query1.finance.yahoo.com/v8/finance/chart/{ticker}
        - Parse the response JSON carefully
    """
    pass


async def get_stock_history(ticker: str, period: str = "1y", interval: str = "1d") -> list[dict]:
    """Get historical stock price data.

    Args:
        ticker: Stock symbol.
        period: Time period ("1mo", "3mo", "6mo", "1y", "5y").
        interval: Data interval ("1d", "1wk", "1mo").

    Returns:
        List of price points:
        [
            {"date": "2024-01-02", "open": 150.0, "close": 155.0, "high": 156.0, "low": 149.0, "volume": 5000000},
            ...
        ]

    Hints:
        - Yahoo Finance chart API:
          GET https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range={period}&interval={interval}
        - Response structure: result[0]["indicators"]["quote"][0] has OHLCV arrays
        - Timestamps in result[0]["timestamp"] (Unix epoch)
    """
    pass


async def get_company_profile(ticker: str) -> dict | None:
    """Get company profile/overview information.

    Args:
        ticker: Stock symbol.

    Returns:
        Dict with company info:
        {
            "name": "Apple Inc.",
            "sector": "Technology",
            "industry": "Consumer Electronics",
            "description": "Apple Inc. designs, manufactures...",
            "employees": 164000,
            "website": "https://www.apple.com"
        }
    """
    pass

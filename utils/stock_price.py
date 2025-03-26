import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_price(ticker):
    """
    Fetch real-time stock price data using yfinance
    """
    try:
        stock = yf.Ticker(ticker)
        # Get historical data for the last 5 days
        hist = stock.history(period="5d")
        
        if hist.empty:
            return {"price": None, "trend": "unknown", "error": "No data available"}
        
        current_price = float(hist['Close'].iloc[-1])
        previous_price = float(hist['Close'].iloc[-2])
        
        # Determine trend
        trend = "up" if current_price > previous_price else "down"
        
        return {
            "price": round(current_price, 2),
            "trend": trend,
            "volume": int(hist['Volume'].iloc[-1]),
            "high": round(float(hist['High'].iloc[-1]), 2),
            "low": round(float(hist['Low'].iloc[-1]), 2)
        }
    except Exception as e:
        return {"price": None, "trend": "unknown", "error": str(e)} 
import yfinance as yf
import pandas as pd

def get_tickers():
    return pd.read_csv("data/tickers.csv")["Symbol"].tolist()

def fetch_all_data(timeframe):
    tickers = get_tickers()
    all_data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            if timeframe == "1d":
                df = stock.history(period="2y", interval="1d")
            elif timeframe == "1h":
                df = stock.history(period="20d", interval="1h")
            elif timeframe == "5m":
                df = stock.history(period="2d", interval="5m")
            df["Ticker"] = ticker
            df["Timeframe"] = timeframe
            all_data.append(df.reset_index())
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
    return pd.concat(all_data)

# src/fetch_prices.py

import yfinance as yf
import datetime

# Choose your demo stocks
TICKERS = ['AAPL', 'TSLA', 'INFY']

def fetch_latest_prices(tickers):
    now = datetime.datetime.now()
    results = []
    for symbol in tickers:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1m")
        if not data.empty:
            latest = data.tail(1)
            price = latest['Close'].values[0]
            timestamp = latest.index[-1].to_pydatetime()
            results.append({'symbol': symbol, 'datetime': timestamp, 'price': price})
            print(f"{symbol} @ {timestamp}: {price}")
        else:
            print(f"No data for {symbol}")
    return results

if __name__ == '__main__':
    fetch_latest_prices(TICKERS)

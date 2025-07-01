# Stock Sentiment Dashboard

A real-time dashboard for live stock prices, news, and sentiment analytics.

## Features
- Live stock prices for selected companies
- News headline fetching and sentiment analysis
- Interactive Streamlit dashboard
- Automated data pipeline

## Tech Stack
- Python, Streamlit, PostgreSQL, yfinance, Hugging Face Transformers

## Setup

1. Clone the repo:
    ```
    git clone https://github.com/<your-username>/stock-sentiment-dashboard.git
    cd stock-sentiment-dashboard
    ```

2. Setup virtual environment and install requirements:
    ```
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Edit `src/fetch_prices.py` and `src/fetch_news.py` to configure your stocks and API keys.

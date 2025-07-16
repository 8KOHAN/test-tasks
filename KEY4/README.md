# SP500 Data Loader

A Python-based pipeline to **fetch**, **measure**, and **store** historical stock data from Yahoo Finance for selected S&P 500 companies. Data is saved to a PostgreSQL database with support for multiple timeframes (`1d`, `1h`, `5m`).

---

## Features

- Pulls historical stock data using `yfinance`
- Supports three timeframes:
  - Daily (`1d`)
  - Hourly (`1h`)
  - Intraday 5-minute (`5m`)
- Stores data in a PostgreSQL table (`stock_data`)
- Measures fetch time per timeframe
- Easily configurable via `.env` file
- Modular script structure with CLI entry point

---

## Tech Stack

- **Python**
- `yfinance`, `pandas`, `psycopg2`, `dotenv`
- **PostgreSQL**

---

## Directory Structure
```bash
SP500_DATA_LOADER/
├── data/
│ └── tickers.csv
├── ddl/
│ └── structure.sql
├── scripts/
│ ├── main.py
│ ├── fetch_data.py
│ ├── save_to_db.py
│ └── measure_perf.py
├── requirements.txt
├── .gitignore
├── README.md

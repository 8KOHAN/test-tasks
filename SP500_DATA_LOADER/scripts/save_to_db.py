import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def save_data_to_db(df, timeframe):
    conn = psycopg2.connect(os.getenv("DB_URI"))
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO stock_data (ticker, timeframe, datetime, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (row["Ticker"], row["Timeframe"], row["Datetime"], row["Open"], row["High"],
              row["Low"], row["Close"], row["Volume"]))
    conn.commit()
    cur.close()
    conn.close()

CREATE TABLE IF NOT EXISTS stock_data (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    timeframe VARCHAR(10) NOT NULL,
    datetime TIMESTAMP NOT NULL,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT
);

CREATE INDEX IF NOT EXISTS idx_stock_data_main ON stock_data (ticker, timeframe, datetime);

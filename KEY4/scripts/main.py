from fetch_data import fetch_all_data
from save_to_db import save_data_to_db
from measure_perf import measure_time

if __name__ == "__main__":
    for timeframe in ["1d", "1h", "5m"]:
        data, duration = measure_time(fetch_all_data, timeframe)
        save_data_to_db(data, timeframe)
        print(f"[{timeframe}] Time: {duration:.2f} сек")

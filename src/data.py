from pathlib import Path

import pandas as pd
import yaml
import yfinance as yf

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def load_config(config_path: Path = CONFIG_PATH) -> dict:
    """Load project configuration from a YAML file."""
    with config_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def download_market_data(
    ticker: str,
    start_date: str,
    end_date: str,
    interval: str = "1d",
) -> pd.DataFrame:
    """Download historical market data from Yahoo Finance.

    Args:
        ticker: Financial asset symbol, for example "SPY".
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format.
        interval: Data frequency, for example "1d".

    Returns:
        A DataFrame indexed by date with one column per price field.
    """
    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval=interval,
        auto_adjust=True,
        progress=False,
    )

    if data is None or data.empty:
        raise ValueError(f"No market data was downloaded for {ticker}.")

    # Recent yfinance versions return two-level columns even for one ticker.
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data.columns.name = None

    return data


def validate_market_data(data: pd.DataFrame) -> None:
    """Run basic integrity checks and raise ValueError if any fails."""
    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if not data.index.is_monotonic_increasing:
        raise ValueError("Dates are not sorted in ascending order.")
    if data.index.has_duplicates:
        raise ValueError("Duplicate dates found.")
    if (data["Close"] <= 0).any():
        raise ValueError("Non-positive closing prices found.")


def save_market_data(data: pd.DataFrame, file_path: Path) -> None:
    """Save market data to a CSV file, creating folders if needed."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(file_path, index=True)


def main() -> None:
    """Download the asset defined in config.yaml and save it to data/raw."""
    settings = load_config()["data"]
    ticker = settings["ticker"]
    interval = settings["interval"]

    data = download_market_data(
        ticker=ticker,
        start_date=settings["start_date"],
        end_date=settings["end_date"],
        interval=interval,
    )
    validate_market_data(data)

    file_path = RAW_DATA_DIR / f"{ticker}_{interval}.csv"
    save_market_data(data, file_path)

    print(f"{ticker}: {len(data)} rows, {data.index.min().date()} to {data.index.max().date()}")
    print(f"Missing values per column:\n{data.isna().sum()}")
    print(f"Saved to {file_path}")


if __name__ == "__main__":
    main()

import pandas as pd


REQUIRED_COLUMNS = {
    "student_id",
    "timestamp",
    "event_type",
    "resource",
    "score",
}


def load_logs(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

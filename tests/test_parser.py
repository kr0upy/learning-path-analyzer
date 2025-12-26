import pandas as pd
import pytest
from src.parser import load_logs


def test_load_logs_valid(tmp_path):
    file = tmp_path / "logs.csv"
    file.write_text(
        "student_id,timestamp,event_type,resource,score\n"
        "1,2024-01-01 10:00,login,system,\n"
    )

    df = load_logs(file)
    assert isinstance(df, pd.DataFrame)
    assert "event_type" in df.columns


def test_load_logs_missing_column(tmp_path):
    file = tmp_path / "logs.csv"
    file.write_text("student_id,timestamp\n1,2024-01-01 10:00\n")

    with pytest.raises(ValueError):
        load_logs(file)

import pandas as pd
from src.analysis import (
    aggregate_student_activity,
    activity_score_correlation,
)


def sample_df():
    return pd.DataFrame(
        {
            "student_id": [1, 1, 2, 2],
            "event_type": [
                "quiz_attempt",
                "assignment_submission",
                "quiz_attempt",
                "forum_post",
            ],
            "score": [80, 90, 95, None],
        }
    )


def test_aggregate_student_activity():
    df = sample_df()
    agg = aggregate_student_activity(df)

    assert "quiz_attempt" in agg.columns
    assert "avg_score" in agg.columns
    assert agg.loc[1, "avg_score"] == 85


def test_activity_score_correlation():
    df = sample_df()
    agg = aggregate_student_activity(df)
    corr = activity_score_correlation(agg)

    assert isinstance(corr, pd.Series)

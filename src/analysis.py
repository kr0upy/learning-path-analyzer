import pandas as pd


def aggregate_student_activity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate activity counts and average score per student.
    """
    activity_counts = (
        df.groupby(["student_id", "event_type"])
        .size()
        .unstack(fill_value=0)
    )

    avg_scores = (
        df.dropna(subset=["score"])
        .groupby("student_id")["score"]
        .mean()
        .rename("avg_score")
    )

    result = activity_counts.join(avg_scores, how="left")
    return result


def activity_score_correlation(aggregated_df: pd.DataFrame) -> pd.Series:
    """
    Compute correlation between activity types and average score.
    """
    numeric_df = aggregated_df.dropna(subset=["avg_score"])
    correlations = numeric_df.corr()["avg_score"].drop("avg_score")
    return correlations

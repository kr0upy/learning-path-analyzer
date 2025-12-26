import matplotlib.pyplot as plt
import pandas as pd


def plot_activity_distribution(aggregated_df: pd.DataFrame, output_path: str):
    """
    Bar chart of average activity counts per student.
    """
    activity_cols = aggregated_df.drop(columns=["avg_score"], errors="ignore")

    means = activity_cols.mean()
    plt.figure()
    means.plot(kind="bar")
    plt.title("Average Activity Count per Student")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_activity_score_correlation(
    correlations: pd.Series, output_path: str
):
    """
    Bar chart of correlation between activity types and avg score.
    """
    plt.figure()
    correlations.plot(kind="bar")
    plt.title("Correlation Between Activity Types and Performance")
    plt.ylabel("Correlation")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

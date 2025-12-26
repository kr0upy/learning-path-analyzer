from pathlib import Path
import pandas as pd

from src.analysis import (
    aggregate_student_activity,
    activity_score_correlation,
)
from src.recommender import generate_recommendations
from src.visualization import (
    plot_activity_distribution,
    plot_activity_score_correlation,
)


def generate_report(df: pd.DataFrame, output_dir: str):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    aggregated = aggregate_student_activity(df)
    correlations = activity_score_correlation(aggregated)
    recommendations = generate_recommendations(correlations)

    activity_plot = output_path / "activity_distribution.png"
    corr_plot = output_path / "activity_correlation.png"

    plot_activity_distribution(aggregated, activity_plot)
    plot_activity_score_correlation(correlations, corr_plot)

    report_md = output_path / "latest_report.md"

    with report_md.open("w", encoding="utf-8") as f:
        f.write("# 📊 Learning Path Analysis Report\n\n")

        f.write("## 🔍 Activity–Performance Correlation\n\n")
        f.write(correlations.to_frame("correlation").to_markdown())
        f.write("\n\n")

        f.write("## 💡 Recommendations\n\n")
        for rec in recommendations:
            f.write(f"- {rec}\n")

        f.write("\n## 📈 Visualizations\n\n")
        f.write("![Activity Distribution](activity_distribution.png)\n\n")
        f.write("![Activity Correlation](activity_correlation.png)\n")

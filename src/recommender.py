import pandas as pd


def generate_recommendations(correlations: pd.Series) -> list[str]:
    """
    Generate human-readable recommendations
    based on activity-performance correlations.
    """
    recommendations = []

    for activity, corr in correlations.items():
        if corr > 0.3:
            recommendations.append(
                f"Increasing '{activity}' activity is strongly "
                f"associated with better performance (corr={corr:.2f})."
            )
        elif corr > 0.1:
            recommendations.append(
                f"'{activity}' shows a mild positive impact on performance "
                f"(corr={corr:.2f})."
            )
        elif corr < -0.1:
            recommendations.append(
                f"High '{activity}' activity may negatively affect performance "
                f"(corr={corr:.2f})."
            )

    if not recommendations:
        recommendations.append(
            "No strong correlations found. Consider collecting more data."
        )

    return recommendations

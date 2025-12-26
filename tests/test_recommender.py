import pandas as pd
from src.recommender import generate_recommendations


def test_generate_recommendations():
    correlations = pd.Series(
        {
            "quiz_attempt": 0.45,
            "forum_post": 0.15,
            "login": -0.05,
        }
    )

    recs = generate_recommendations(correlations)

    assert isinstance(recs, list)
    assert len(recs) >= 2
    assert any("quiz_attempt" in r for r in recs)

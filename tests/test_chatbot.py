import pandas as pd

from GenAI.chartbot import try_rule_based_answer


def test_rule_based_assistant_handles_top_city_query():
    df = pd.DataFrame(
        {
            "city": ["Mumbai", "Delhi", "Mumbai", "Bengaluru"],
            "crime_description": ["Theft", "Theft", "Assault", "Fraud"],
        }
    )

    result, explanation = try_rule_based_answer("Which city has the highest crime?", df)

    assert isinstance(result, pd.Series)
    assert result.index[0] == "Mumbai"
    assert "city" in explanation.lower()

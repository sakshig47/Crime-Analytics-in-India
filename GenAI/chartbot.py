import pandas as pd

from GenAI.llm import client
from GenAI.prompt import SYSTEM_PROMPT

df = pd.read_csv("cleaned_crime_dataset.csv")


def ask_ai(question):
    """
    Takes a natural language question, asks the LLM to generate pandas
    code against `df`, executes it, then asks the LLM to explain the
    result in plain language.

    Returns (result, explanation) on success.
    Raises a RuntimeError with a user-friendly message on failure.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )
    except Exception as e:
        raise RuntimeError(f"Could not reach the AI model: {e}")

    code = response.choices[0].message.content

    code = code.replace("```python", "").replace("```", "").strip()

    local_scope = {"df": df.copy()}

    try:
        exec(code, {}, local_scope)
        result = local_scope["result"]
    except Exception as e:
        raise RuntimeError(
            f"The generated code failed to run.\n\nCode:\n{code}\n\nError: {e}"
        )

    try:
        explanation = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Explain the result in simple business language.",
                },
                {
                    "role": "user",
                    "content": f"""
Question:

{question}

Result:

{result}
""",
                },
            ],
        )
        explanation_text = explanation.choices[0].message.content
    except Exception as e:
        explanation_text = f"(Could not generate explanation: {e})"

    return result, explanation_text
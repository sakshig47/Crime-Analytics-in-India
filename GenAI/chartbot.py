import pandas as pd

from groq import Groq

from GenAI.llm import client
from GenAI.prompt import SYSTEM_PROMPT

df = pd.read_csv("cleaned_crime_dataset.csv")


def ask_ai(question):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":question
            }
        ],
        temperature=0
    )

    code = response.choices[0].message.content

    code = code.replace("```python","")
    code = code.replace("```","")

    local_scope = {"df": df}

    exec(code, {}, local_scope)

    result = local_scope["result"]

    explanation = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":"Explain the result in simple business language."
            },
            {
                "role":"user",
                "content":f"""
Question:

{question}

Result:

{result}
"""
            }
        ]
    )

    return result, explanation.choices[0].message.content
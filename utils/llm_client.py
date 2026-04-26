import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(prompt, user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"]
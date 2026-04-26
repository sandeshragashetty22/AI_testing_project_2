import json
import pandas as pd
from utils.llm_client import get_response
from evaluator.metrics import keyword_score, forbidden_penalty, tone_score


def evaluate(prompt_file):
    with open(prompt_file) as f:
        prompt = f.read()

    with open("dataset/golden_dataset.json") as f:
        dataset = json.load(f)

    results = []

    for test in dataset:
        response = get_response(prompt, test["input"])

        k_score = keyword_score(response, test["expected_keywords"])
        f_penalty = forbidden_penalty(response, test["forbidden_keywords"])
        t_score = tone_score(response)

        final_score = k_score + t_score - f_penalty

        results.append({
            "input": test["input"],
            "response": response,
            "keyword_score": k_score,
            "tone_score": t_score,
            "penalty": f_penalty,
            "final_score": final_score
        })

    df = pd.DataFrame(results)
    return df.to_csv(f"results/{prompt_file.split('/')[-1]}.csv", index=False)

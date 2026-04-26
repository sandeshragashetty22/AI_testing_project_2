from evaluator import *
from evaluator.evaluator import evaluate

THRESHOLD = 1.5


def test_prompt_regression():
    v1_results = evaluate("prompts/v1.txt")
    v2_results = evaluate("prompts/v2.txt")

    v1_avg = v1_results["final_score"].mean()
    v2_avg = v2_results["final_score"].mean()

    assert v2_avg >= v1_avg - 0.2, "Regression detected in v2"


def test_prompt_v3_failure():
    v1_results = evaluate("prompts/v1.txt")
    v3_results = evaluate("prompts/v3.txt")

    v1_avg = v1_results["final_score"].mean()
    v3_avg = v3_results["final_score"].mean()

    assert v3_avg >= v1_avg - 0.2, "v3 caused regression"
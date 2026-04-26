import pandas as pd
import matplotlib.pyplot as plt

v1 = pd.read_csv("results/v1.txt.csv")
v2 = pd.read_csv("results/v2.txt.csv")
v3 = pd.read_csv("results/v3.txt.csv")

scores = [
    v1["final_score"].mean(),
    v2["final_score"].mean(),
    v3["final_score"].mean()
]

labels = ["v1", "v2", "v3"]

plt.bar(labels, scores)
plt.title("Prompt Performance Comparison")
plt.xlabel("Prompt Version")
plt.ylabel("Score")

plt.show()
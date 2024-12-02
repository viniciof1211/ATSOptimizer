import numpy as np
import pandas as pd

# Assumed percentile data for candidates
percentiles = {
    "Candidate": ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Your Resume"],
    "Percentile": [55, 60, 70, 75, 90],  # Assume your updated resume is in the 90th percentile
}

# Convert percentiles to scores assuming a linear distribution (e.g., max score = 100)
percentile_to_score = lambda p: (p / 100) * 100
scores = [percentile_to_score(p) for p in percentiles["Percentile"]]

# Calculate statistics for Z-score
mean_score = np.mean(scores)
std_dev = np.std(scores)

# Z-score calculation
z_scores = [(score - mean_score) / std_dev for score in scores]

# Create a DataFrame
data = pd.DataFrame({
    "Candidate": percentiles["Candidate"],
    "Percentile": percentiles["Percentile"],
    "Score": scores,
    "Z-Score": z_scores
})

# Save this data to an Excel file
excel_path = "/mnt/data/Resume_Score_Comparison.xlsx"
data.to_excel(excel_path, index=False)

import matplotlib.pyplot as plt

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(data["Candidate"], data["Score"], alpha=0.7, label="Scores")
plt.axhline(mean_score, color="red", linestyle="--", label="Mean Score")

for idx, row in data.iterrows():
    plt.text(idx, row["Score"] + 2, f"{row['Percentile']}%", ha="center")

plt.title("Resume Match Scores and Percentiles")
plt.xlabel("Candidates")
plt.ylabel("Score")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
chart_path = "/mnt/data/Resume_Score_Comparison_Chart.png"
plt.savefig(chart_path)

excel_path, chart_path
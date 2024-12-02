# Redefine necessary imports for numerical and visualization tasks
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Recalculate scores and statistics for the new dataset
new_extended_scores = [percentile_to_score(p) for p in new_extended_percentiles]
new_mean_score = np.mean(new_extended_scores)
new_std_dev = np.std(new_extended_scores)
new_extended_z_scores = [(score - new_mean_score) / new_std_dev for score in new_extended_scores]

# Create a new DataFrame for the updated data
new_extended_data = pd.DataFrame({
    "Candidate": new_extended_candidates,
    "Percentile": new_extended_percentiles,
    "Score": new_extended_scores,
    "Z-Score": new_extended_z_scores
})

# Save the updated data to an Excel file
new_extended_excel_path = "/mnt/data/New_Extended_Resume_Score_Comparison.xlsx"
new_extended_data.to_excel(new_extended_excel_path, index=False)

# Generate updated visualizations
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Bar chart for scores and percentiles
axs[0].bar(new_extended_data["Candidate"], new_extended_data["Score"], alpha=0.7, label="Scores")
axs[0].plot(new_extended_data["Candidate"], new_extended_data["Percentile"], marker="o", color="orange", label="Percentile Trend")
axs[0].axhline(new_mean_score, color="red", linestyle="--", label="Mean Score")
axs[0].set_title("Updated Resume Match Scores and Percentiles")
axs[0].set_ylabel("Scores / Percentiles")
axs[0].legend()
axs[0].grid(axis="y", linestyle="--", alpha=0.7)

# Line chart for Z-scores
axs[1].plot(new_extended_data["Candidate"], new_extended_data["Z-Score"], marker="o", label="Z-Score", color="green")
axs[1].axhline(0, color="red", linestyle="--", label="Mean Z-Score")
axs[1].set_title("Updated Z-Score Analysis")
axs[1].set_ylabel("Z-Score")
axs[1].legend()
axs[1].grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
new_chart_combo_path = "/mnt/data/Updated_Complex_Resume_Score_Comparison_Charts.png"
plt.savefig(new_chart_combo_path)

new_extended_excel_path, new_chart_combo_path

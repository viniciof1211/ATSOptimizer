import matplotlib.pyplot as plt

# Refine Z-Score analysis with worst-case and best-case percentiles
worst_case_percentile = 50  # Assuming worst-case for a candidate's resume match
best_case_percentile = 95   # Assuming best-case scenario for your resume

# Extend dataset with additional cases
extended_percentiles = percentiles["Percentile"] + [worst_case_percentile, best_case_percentile]
extended_candidates = percentiles["Candidate"] + ["Worst Case", "Best Case"]
extended_scores = [percentile_to_score(p) for p in extended_percentiles]
extended_mean = np.mean(extended_scores)
extended_std_dev = np.std(extended_scores)
extended_z_scores = [(score - extended_mean) / extended_std_dev for score in extended_scores]

# Create a DataFrame for the extended data
extended_data = pd.DataFrame({
    "Candidate": extended_candidates,
    "Percentile": extended_percentiles,
    "Score": extended_scores,
    "Z-Score": extended_z_scores
})

# Save the extended data to an Excel file
extended_excel_path = "/mnt/data/Extended_Resume_Score_Comparison.xlsx"
extended_data.to_excel(extended_excel_path, index=False)

# Generate visualizations
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Bar chart for scores and percentiles
axs[0].bar(extended_data["Candidate"], extended_data["Score"], alpha=0.7, label="Scores")
axs[0].plot(extended_data["Candidate"], extended_data["Percentile"], marker="o", color="orange", label="Percentile Trend")
axs[0].axhline(extended_mean, color="red", linestyle="--", label="Mean Score")
axs[0].set_title("Resume Match Scores and Percentiles")
axs[0].set_ylabel("Scores / Percentiles")
axs[0].legend()
axs[0].grid(axis="y", linestyle="--", alpha=0.7)

# Line chart for Z-scores
axs[1].plot(extended_data["Candidate"], extended_data["Z-Score"], marker="o", label="Z-Score", color="green")
axs[1].axhline(0, color="red", linestyle="--", label="Mean Z-Score")
axs[1].set_title("Z-Score Analysis")
axs[1].set_ylabel("Z-Score")
axs[1].legend()
axs[1].grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
chart_combo_path = "/mnt/data/Complex_Resume_Score_Comparison_Charts.png"
plt.savefig(chart_combo_path)

extended_excel_path, chart_combo_path

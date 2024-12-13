# Create a detailed keyword optimization matrix based on simulated data
keyword_matrix = pd.DataFrame({
    "Keyword": jd_keywords,
    "Current Density": resume_df[jd_keywords].iloc[0],
    "Recommended Density (90th Percentile)": [8, 9, 8, 7, 6, 6, 7, 8, 8, 6, 6, 7]
})

# Add a column suggesting action for optimization
keyword_matrix["Action Required"] = keyword_matrix.apply(
    lambda row: "Increase" if row["Current Density"] < row["Recommended Density (90th Percentile)"] else "Maintain",
    axis=1
)

# Display the optimization matrix
import ace_tools as tools; tools.display_dataframe_to_user(name="Keyword Optimization Matrix", dataframe=keyword_matrix)

# Statistical analysis summary
statistical_summary = {
    "Resume Total Matches": resume_df["Total Matches"].iloc[0],
    "Competitor Mean Matches": mean_matches,
    "Resume Percentile": competitor_df.loc[competitor_df["Candidate"] == "Vinicio Flores (Best Match)", "Percentile"].iloc[0]
}

statistical_summary

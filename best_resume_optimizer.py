import pandas as pd
import numpy as np
from scipy.stats import poisson, norm, zscore
import matplotlib.pyplot as plt
from docx import Document

resumes_text = {""}
keyword_results = [""][""]
# Extract Solutions Architect resume for optimization
solutions_architect_text = resumes_text["Solutions Architect"]

# Missing and underrepresented keywords
missing_keywords = keyword_results["Solutions Architect"]["missing"]
density = keyword_results["Solutions Architect"]["density"]

# Create a mapping for missing and underrepresented keywords for natural placement
missing_keywords = list(missing_keywords)
underrepresented_keywords = {k: v for k, v in density.items() if v < 2}  # Less than 2 occurrences

# Areas to improve - custom suggestions
suggestions = []
optimized_resume = solutions_architect_text

# Add missing keywords in relevant sections (manually decide for clarity)
optimized_resume += "\n\n### Additions to Strengthen ATS Optimization ###\n"
for keyword in missing_keywords:
    suggestions.append(f"Consider adding '{keyword}' to align more with the job requirements.")
    optimized_resume += f"- Include '{keyword}' naturally in sections discussing {keyword}-related tasks.\n"

# Highlight underrepresented keywords
for keyword in underrepresented_keywords:
    suggestions.append(f"Increase the frequency of '{keyword}' slightly in relevant contexts.")

# Add to suggestions list
formatted_suggestions = "\n".join(suggestions)

# ATS formatting improvements: Remove non-standard bullet points, add clear headings, and simplify text
optimized_resume = optimized_resume.replace("•", "-")  # Standardize bullet points
optimized_resume = optimized_resume.replace("💼 LinkedIn Profile", "LinkedIn: <your link here>")
optimized_resume = optimized_resume.replace("🌐 Professional Blog", "Blog: <your link here>")

# Present optimized content and suggestions to the user
tools.display_dataframe_to_user("Keyword Optimization Suggestions", pd.DataFrame({
    "Keyword": missing_keywords + list(underrepresented_keywords.keys()),
    "Type": ["Missing"] * len(missing_keywords) + ["Underrepresented"] * len(underrepresented_keywords),
    "Suggestions": suggestions[:len(missing_keywords) + len(underrepresented_keywords)]
}))

optimized_resume[:1500]  # Preview of optimized resume

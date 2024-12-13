import pandas as pd
import numpy as np
from scipy.stats import poisson, norm, zscore
import matplotlib.pyplot as plt
from docx import Document
from tabulate import tabulate
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from pdfminer.high_level import extract_text
import functools
import re

# Load the resumes
file_paths = {
    "Data Architect": "Vinicio Flores Data Architect Resume.docx",
    "Solutions Architect": "Vinicio Solutions Architect Resume CV.docx",
    "AWS Resume": "Vinicio Flores AWS Resume.docx"
}

resumes = {name: Document(path) for name, path in file_paths.items()}

# Load the job description into a text variable
job_description = """
Python Developer (GCP/AWS Experience)
About Us
The Website Design Agency Ltd. (TWDA) is a London-based digital agency at the forefront of innovation. We are building 
Savvy, an AI-driven platform designed to process input documents, extract relevant data, analyse it using advanced AI models, 
and generate output documents efficiently. This is an exciting opportunity to contribute to a groundbreaking platform leveraging 
cutting-edge tools like LangChain for building intelligent and adaptable systems.

Role Overview
We are looking for a talented Python Developer with experience in Google Cloud Platform (GCP) or Amazon Web Services (AWS) dashboards. 
A key focus of this role is working with LangChain to build and integrate AI capabilities for seamless document processing, data extraction, 
and analysis workflows. If you have a passion for Python development, cloud technologies, and AI-driven tools, we want to hear from you.

Key Responsibilities
- Design, develop, and implement features for the Savvy platform using Python.
- Leverage GCP or AWS to create scalable, efficient cloud-based solutions.
- Integrate and utilise LangChain to build and manage AI-driven workflows.
- Develop systems for document processing, data extraction, and analysis using AI models and training data.
- Generate structured output documents based on AI analysis results.
- Debug, optimise, and improve platform performance.
- Collaborate with a multidisciplinary team to meet project requirements and timelines.

Skills and Qualifications
Essential:
- Strong proficiency in Python for application and AI development.
- Hands-on experience with GCP or AWS, including dashboards and services.
- Familiarity with LangChain and its integration into AI systems.
- Experience with document data extraction and AI-based analysis workflows.
- Understanding of AI concepts, including model integration and training data usage.
- Strong analytical and problem-solving skills.

Desirable:
- Experience with AI frameworks (e.g., TensorFlow, PyTorch, Scikit-learn).
- Knowledge of document processing libraries (e.g., Tesseract, OpenCV, or PDF libraries).
- Familiarity with APIs, containerisation (Docker), and orchestration tools (Kubernetes).
- Prior experience deploying AI-driven platforms in production environments.
"""

# Function to extract text from resumes
def extract_text(doc):
    return " ".join([p.text for p in doc.paragraphs])

# Extract text from resumes
resumes_text = {name: extract_text(doc) for name, doc in resumes.items()}

# Analyze keyword presence, absence, and density
def keyword_analysis(resume_text, job_description):
    jd_keywords = set(job_description.lower().split())
    resume_keywords = set(resume_text.lower().split())
    matched = jd_keywords.intersection(resume_keywords)
    missing = jd_keywords - matched
    total_keywords = len(jd_keywords)
    match_rate = len(matched) / total_keywords
    density = {word: resume_text.lower().split().count(word) for word in matched}
    return {
        "matched": matched,
        "missing": missing,
        "match_rate": match_rate,
        "density": density
    }

# Perform keyword analysis for each resume
keyword_results = {
    name: keyword_analysis(text, job_description) for name, text in resumes_text.items()
}

# Poisson distribution: Competing candidates
lambda_poisson = 13  # average number of applications
poisson_distribution = poisson.pmf(range(0, 21), lambda_poisson)

# Statistical comparison
candidates = 145
z_scores = {
    name: (keyword_results[name]['match_rate'] - np.mean([keyword_results[n]['match_rate'] for n in keyword_results])) /
          np.std([keyword_results[n]['match_rate'] for n in keyword_results])
    for name in keyword_results
}
percentiles = {name: norm.cdf(z) * 100 for name, z in z_scores.items()}

# Display summary statistics
summary_stats = pd.DataFrame({
    "Resume": list(keyword_results.keys()),
    "Match Rate": [result['match_rate'] for result in keyword_results.values()],
    "Z-Score": list(z_scores.values()),
    "Percentile": list(percentiles.values())
})

# Generate visualizations
# Bar chart for match rates
plt.figure(figsize=(10, 6))
plt.bar(summary_stats["Resume"], summary_stats["Match Rate"], alpha=0.7)
plt.title("Keyword Match Rates per Resume")
plt.xlabel("Resume")
plt.ylabel("Match Rate")
plt.show()

# Pie chart for skill distribution in one resume (Data Architect as example)
example_density = keyword_results["Data Architect"]['density']
labels, sizes = zip(*example_density.items())
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Skill Distribution in Data Architect Resume")
plt.show()

# Display the summary statistics for user
import ace_tools as tools; tools.display_dataframe_to_user("Summary Statistics of Resumes", summary_stats)

summary_stats

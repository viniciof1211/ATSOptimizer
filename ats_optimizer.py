
# Importing Required Libraries
import numpy as np
import pandas as pd
from scipy.stats import poisson
from docx import Document
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from tabulate import tabulate
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from pdfminer.high_level import extract_text
import re

class ATSAnalysis:
    def __init__(self, jd_text, resume_text, num_candidates):
        self.jd_text = jd_text
        self.resume_text = resume_text
        self.num_candidates = num_candidates
        self.jd_tokens = None
        self.resume_tokens = None
        self.match_score = 0
        self.mean_score = 0
        self.percentile = 0
        self.keyword_density = {}
        self.replacement_suggestions = {}

    def tokenize(self, text):
        """Tokenizes and cleans the input text."""
        return re.sub(r"[^\w\s]", "", text.lower()).split()

    def calculate_keyword_match(self):
        """Calculates the keyword match score between the job description and the resume."""
        from collections import Counter
        self.jd_tokens = Counter(self.tokenize(self.jd_text))
        self.resume_tokens = Counter(self.tokenize(self.resume_text))
        common_tokens = self.jd_tokens & self.resume_tokens
        self.match_score = sum(common_tokens.values())
        self.mean_score = self.match_score  # Using match_score as the mean for simplicity
        return self.match_score

    def calculate_percentile(self):
        """Calculates the percentile rank using Poisson distribution."""
        self.percentile = poisson.cdf(self.match_score, self.mean_score) * 100
        return self.percentile

    def generate_poisson_distribution(self):
        """Generates the Poisson distribution data."""
        x = np.arange(0, self.match_score + 10)
        probabilities = poisson.pmf(x, self.mean_score)
        return x, probabilities

    def calculate_keyword_density(self):
        """Calculates the keyword density and suggestions for improvement."""
        vectorizer = TfidfVectorizer()
        jd_vocab = vectorizer.fit([self.jd_text]).vocabulary_
        for word, count in self.jd_tokens.items():
            recurrence = self.resume_tokens.get(word, 0)
            self.keyword_density[word] = {
                "Required": count,
                "In Resume": recurrence,
                "Improve": max(0, count - recurrence)
            }
        return self.keyword_density

    def detect_replacement_suggestions(self):
        """Detect lines in the resume for replacement suggestions."""
        lines = self.resume_text.splitlines()
        for word, data in self.keyword_density.items():
            if data["Improve"] > 0:
                for i, line in enumerate(lines):
                    if word in line.lower():
                        self.replacement_suggestions[word] = {
                            "Line": line.strip(),
                            "Suggestion": f"Include the keyword '{word}' {data['Improve']} more times."
                        }
                        break
        return self.replacement_suggestions

    def save_to_excel(self, file_path, x, probabilities):
        """Saves the analysis results to an Excel file."""
        wb = Workbook()
        ws = wb.active
        ws.title = "Poisson Analysis"

        ws.append(["Keyword Match Score", "Probability"])
        for score, prob in zip(x, probabilities):
            ws.append([score, prob])

        chart = BarChart()
        data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(x) + 1)
        categories = Reference(ws, min_col=1, min_row=2, max_row=len(x) + 1)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        chart.title = "Poisson Distribution"
        chart.x_axis.title = "Keyword Match Score"
        chart.y_axis.title = "Probability"
        ws.add_chart(chart, "E2")

        wb.save(file_path)
        return file_path

    def print_results(self):
        """Prints keyword density and replacement suggestions to stdout."""
        print("\nKeyword Density Table:")
        print(tabulate(
            [(word, data["Required"], data["In Resume"], data["Improve"]) 
             for word, data in self.keyword_density.items()],
            headers=["Keyword", "Required", "In Resume", "Improve"],
            tablefmt="grid"
        ))

        print("\nReplacement Suggestions:")
        for word, suggestion in self.replacement_suggestions.items():
            print(f"\nKeyword: {word}")
            print(f"Line: {suggestion['Line']}")
            print(f"Suggestion: {suggestion['Suggestion']}")

# Helper Functions
def read_text_file(file_path):
    """Reads text from a .txt file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_docx_file(file_path):
    """Reads text from a .docx file."""
    doc = Document(file_path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])

# Main Program
if __name__ == "__main__":
    # File paths for input files
    jd_file = "job_description.txt"  # Replace with your JD text file path
    resume_file = "resume.docx"      # Replace with your resume .docx file path

    # Read contents from files
    jd_text = read_text_file(jd_file)
    resume_text = read_docx_file(resume_file)
    num_candidates = 11

    # Perform analysis
    analysis = ATSAnalysis(jd_text, resume_text, num_candidates)
    match_score = analysis.calculate_keyword_match()
    percentile = analysis.calculate_percentile()
    x, probabilities = analysis.generate_poisson_distribution()
    keyword_density = analysis.calculate_keyword_density()
    replacement_suggestions = analysis.detect_replacement_suggestions()

    # Save to Excel
    excel_file = analysis.save_to_excel("ATS_Poisson_Analysis.xlsx", x, probabilities)

    # Print Results
    analysis.print_results()
    print(f"\nMatch Score: {match_score}")
    print(f"Percentile: {percentile}%")
    print(f"Results saved to {excel_file}")

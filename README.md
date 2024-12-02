# ATSOptimizer

**Optimize your resume's ATS performance with Poisson-powered insights!**

ATSOptimizer is a Python-based application designed to enhance resume compatibility with Applicant Tracking Systems (ATS). Leveraging advanced keyword analysis and Poisson distribution, the tool evaluates and ranks resumes against job descriptions. It provides precise percentile scoring, actionable keyword optimization insights, and data visualization to maximize job matching potential. Hiring processes usually follow a Poisson statistical distribution, so this tool provides you also with the fixes you must perform to your resume so you can be on top of the percentile - above 90th n-tile - in order to be picked up by HR and passed to the hiring manager and team, instead of being lost into the mythical HR-dark hole of forgetness.

---

## Features

- **Keyword Analysis**: Automatically identify and match relevant keywords and their density (recurrence) between resumes and job descriptions.
- **Poisson Distribution**: Visualizes the ranking of resumes among candidates.
- **Percentile Scoring**: Rank resumes using Poisson distribution to calculate their ATS compatibility percentile.
- **Data Visualization**: Generate visual insights with charts and graphs for better decision-making.
- **Customizable Reports**: Export analysis results to Excel files, complete with interactive charts.
- **Support for Multiple Formats**: Analyze `.txt` and `.docx` files seamlessly.
- **Replacement Suggestions**: Detects lines in the resume that need improvement and suggests updates.
- **Excel Reports**: Generates detailed Excel reports for further analysis on how your resume application compares against a "n" number of applicants (if you have LinkedIn Premium you have visibility of this variable, if not then you can always "guess").

---

## Installation

Follow these steps to set up ATSOptimizer on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ATSOptimizer.git
   cd ATSOptimizer
   ```
**Install Dependencies:** Ensure you have Python 3.7+ installed. Then, run:

   ```bash
   pip install numpy pandas scipy matplotlib sklearn python-docx openpyxl tabulate
   ```
**Verify Installation:** Test the setup by running the example code in the repository.

## Usage

### Input Requirements

- Job Description: A .txt file containing the job description.
- Resume: A .docx file with your resume content.

### Running the Program
Place your job description (job_description.txt) and resume (resume.docx) in the working directory.

### Run the script:

   ```bash
    python ats_optimizer.py
   ```
### Outputs:

**Match Score:** Numerical evaluation of keyword alignment.
**Percentile:** Ranking among other resumes.
**Excel File:** ATS_Poisson_Analysis.xlsx with detailed results.
**Graph:** Visual Poisson distribution of resume scores.

#### Example Console Output
   ```bash
    Match Score: 85
    Percentile: 92.7%
    Results saved to ATS_Poisson_Analysis.xlsx

    Keyword Density Table:
    +----------+----------+-----------------+------------------+
    | Keyword                 | Required | In Resume | Improve |
    +----------+----------+-----------+------------------------+
    | salesforce integration  | 8        | 5         | 3       |
    | sales                   | 6        | 4         | 2       |
    +----------+----------+-----------+------------------------+
    
    Replacement Suggestions:
    Keyword: salesforce integration
    Line: Expert in Salesforce solutions and implementations.
    Suggestion: Include the keyword 'salesforce integration' 3 more times.

   ```

**Excel Output:** A bar chart showing the Poisson distribution of resume scores.

## Contributing
We welcome contributions from the community! To contribute:

- Fork the repository.
- Create a feature branch:
   ``` bash
   git checkout -b feature-name
   ```
- Commit your changes:
   ```bash
   git commit -m "Description of feature"
   ```
- Push your changes:

  ```bash
    git push origin feature-name
   ```
  
- Open a Pull Request.

## License
This project is licensed under the MIT License. See LICENSE for details.

## Caveats

To calculate a **Z-score** for your updated resume against the scores of four other candidates, 
first need the match scores for each candidate in the competition. 
A Z-score measures how far a data point (your resume's score compared against the keywords in the job description of your choice) 
is from the mean of the dataset in terms of standard deviations.

### Steps:

1. **Data Requirements**:
   - Gather the match scores for all candidates, including your updated resume.
   - Calculate the mean and standard deviation of these scores.

2. **Calculate the Z-Score**:
   $$ Z = \frac{X - \mu}{\sigma} $$

   - \( X \): Your match score.
   - \( \mu \): Mean score of all candidates.
   - \( \sigma \): Standard deviation of the scores.

3. **Visualize Data**:
   - Create an Excel chart comparing match scores and percentiles.
  
4. **Inputs Needed:**
- Provide the match scores for the four other candidates and your updated resume. 
- If scores are unknown, we can assume mock data to demonstrate the process. 

### Feel free to customize further based on your preferences or additional features! Let me know if you'd like any changes

## License
This project is licensed under the **MIT License**.

--- 
This Python script (s) and `README.md` ensure a comprehensive ATS optimization tool ready for integration into any standalone environment, including VS 2022.

# Hospital Data Analysis

This repository contains a focused, reproducible, and simple analysis of hospital patient data using only `numpy`, `pandas`, and `matplotlib`.

## Repository Contents

- `hospital.csv` — Primary dataset used for the analysis (comma-separated CSV).
- `hospital_analysis.ipynb` — Single Jupyter Notebook performing the full analysis (imports, in-memory cleaning, basic statistics, and plots).

## Dataset Overview

Expected columns (case-insensitive, with minor whitespace trimmed):

- `Patient_ID` — Unique identifier for the patient
- `Age` — Patient age (numeric)
- `Gender` — Categorical (e.g., Male/Female/Other)
- `Condition` — Primary diagnosis/condition
- `Medication` — Medications prescribed
- `Admission_Date` — Admission date (day-first format expected)
- `Discharge_Date` — Discharge date (day-first format expected)
- `Patient_State` — State or region of residence
- `Year_of_Admission` — Year (numeric)
- `Length_of_Stay` — Length of stay in days (numeric)
- `Readmission` — Yes/No indicator
- `Outcome` — e.g., Recovered/Deceased/Other
- `Satisfaction` — Satisfaction score (numeric)
- `Insurance_Claimed` — Yes/No indicator
- `Total_Cost` — Numeric cost value (currency-free)

If column names differ by whitespace or capitalization, the notebook strips and normalizes them at load time.

## Goals of the Analysis

The `hospital_analysis.ipynb` notebook performs a short, easy-to-follow exploration that:

- Loads `hospital.csv` into a `pandas` DataFrame.
- Cleans data in memory only (no files are overwritten): trims column names, converts numeric columns, parses dates, standardizes Yes/No fields, and reports missing values.
- Presents the first 10 rows and basic `df.info()` / `df.describe()` statistics.
- Performs simple analyses on financials, demographics, and length-of-stay:
  - Summary statistics for `Total_Cost` and top conditions by average cost.
  - `Age` distribution and `Gender` counts.
  - Distribution and top conditions by average `Length_of_Stay`.
- Visualizes results with concise `matplotlib` charts: bar charts and histograms with labels for quick interpretation.

## Requirements

- Python 3.10+ (or a compatible Python 3 environment)
- Jupyter Notebook or JupyterLab
- Python packages: `pandas`, `numpy`, `matplotlib`

Install required packages with:

```bash
python -m pip install pandas numpy matplotlib
```

## How to Run

1. Open this folder in VS Code, Jupyter Notebook, or JupyterLab.
2. Launch Jupyter and open `hospital_analysis.ipynb`.
3. Run the notebook cells top-to-bottom. The notebook is ordered to:
   - import libraries
   - read `hospital.csv`
   - clean data in memory and display `df.head(10)`
   - print basic info and simple statistics
   - produce labeled plots summarizing key findings

Notes:

- The notebook strictly uses `numpy`, `pandas`, and `matplotlib` per the project constraints.

## Concise Findings (from the notebook)

- Data cleaning identifies and reports missing or malformed numeric/date values and coerces them where possible.
- Financial: `Total_Cost` summary (mean, median, min, max) and top conditions by average cost are computed and displayed.
- Demographics: `Age` distribution and `Gender` counts are shown; these inform simple subgroup cost and stay comparisons.
- Length of stay: distribution and top conditions by average `Length_of_Stay` are reported.
- Visualizations include bar charts for gender distribution and top conditions by cost, plus histograms for age and length of stay.

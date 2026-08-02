# Hospital Data Analysis Project

This repository contains Jupyter notebooks for exploring and analyzing hospital patient data using Python.

## Project Structure

- `hospital .csv` - The main dataset used for analysis.
- `hospitalDataOverview.ipynb` - Overview notebook with dataset loading and summary statistics.
- `hospital_demographics.ipynb` - Analysis of patient demographics, conditions, and outcomes.
- `hospital_financial_analysis.ipynb` - Cost, length-of-stay, satisfaction, insurance, and readmission analysis.
- `hospital_geographic_analysis.ipynb` - Time-series and geographic analysis, including monthly admissions and state-level condition heatmaps.
- `HospitalAnalysisIndex.ipynb` - Index notebook linking to the separate analysis notebooks.
- `Practice/` - Additional practice files and data used during development.

## Requirements

- Python 3.10+ (or compatible Python 3 environment)
- Jupyter Notebook / JupyterLab
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Install dependencies with:

```bash
python -m pip install pandas numpy matplotlib seaborn
```

## How to Use

1. Open the project folder in VS Code or Jupyter.
2. Launch Jupyter Notebook or JupyterLab.
3. Open `hospitalDataOverview.ipynb` for an initial dataset summary.
4. Open the other notebooks for more focused analyses:
   - `hospital_demographics.ipynb`
   - `hospital_financial_analysis.ipynb`
   - `hospital_geographic_analysis.ipynb`

## Notes

- If notebook execution fails, ensure the required packages are installed and the selected interpreter has access to them.
- Outputs are saved in the notebook files and will render on GitHub when pushed.

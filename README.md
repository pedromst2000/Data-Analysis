# :bar_chart: Data-Analysis

---

## :clipboard: Table of Contents

- :dart: [Overview](#dart-overview)
- :hammer_and_wrench: [Tech Stack](#hammer_and_wrench-tech-stack)
- :file_folder: [Projects](#file_folder-projects)
  - :one: [Demographic Data Analyzer](#one-demographic-data-analyzer) [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/15xuljB270NIhQLyMZ5QuTt3NzKquTwVh?usp=sharing)
  - :two: [Mean, Variance & Standard Deviation Calculator](#two-mean-variance--standard-deviation-calculator) [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1ooFNF91BcRPpAoUn5GG9XC2DP5pCbF2j?usp=sharing)
  - :three: [Medical Data Visualizer](#three-medical-data-visualizer) [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1BNXvU_Oo1JyjWUWsbqBgWM_extGZxASv?usp=sharing)
  - :four: [Page View Time Series Visualizer](#four-page-view-time-series-visualizer) [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1D3AmrdbC_KKsOqiYy0wchc4knCBAGyjK?usp=sharing)
  - :five: [Sea Level Predictor](#five-sea-level-predictor) [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1BuHFw4mfcI6Kly0gG6GbT7Fv9JFPF6i9?usp=sharing)
- :rocket: [Getting Started](#rocket-getting-started)

---

## :dart: Overview

A collection of **Python data analysis and visualization projects** demonstrating core data science techniques:

- **Statistical computation** — matrix operations, descriptive statistics, linear regression
- **Exploratory data analysis (EDA)** — trends, distributions, seasonality, correlations, forecasting
- **Data visualization** — line charts, bar plots, box plots, heatmaps, scatter plots, time-series plots
- **Data cleaning & preprocessing** — outlier removal, categorical encoding, feature engineering
- **Predictive modeling** — trend analysis, extrapolation, linear regression forecasting

**Notebooks** are hosted in **Google Colab** for interactive exploration with inline visualizations. **Python scripts** provide production-ready implementations with unit tests and command-line execution.

---

## :hammer_and_wrench: Tech Stack

| Category             | Tools & Libraries                                       |
| -------------------- | ------------------------------------------------------- |
| **Language**         | Python 3.7+                                             |
| **Data Handling**    | pandas, NumPy                                           |
| **Visualization**    | Matplotlib, Seaborn, pandas.plotting                    |
| **Statistics**       | SciPy (linregress, pearsonr, stats)                     |
| **Machine Learning** | scikit-learn (sklearn)                                  |
| **Testing**          | Unit tests (unittest)                                   |
| **Environment**      | Jupyter Notebook, Google Colab, IDE (VS Code)           |

---

## :file_folder: Projects

### :one: Demographic Data Analyzer

<div align="center">

**US Census Income & Demographics Analyzer**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/15xuljB270NIhQLyMZ5QuTt3NzKquTwVh?usp=sharing)

</div>

Analyzes demographic and income patterns from the [UCI Adult Census Income dataset](https://archive.ics.uci.edu/ml/datasets/Adult) — answering key questions on socioeconomic disparities, education premiums, and workforce demographics.

**Key Features:**

- :globe_with_meridians: Race distribution count across the full dataset
- :man: Average age of male respondents
- :books: Percentage of respondents with Bachelor's degree or higher
- :moneybag: Income differential by education level (higher vs lower education)
- :stopwatch: Minimum work hours + income rate for minimum-hour workers
- :earth_americas: Country with highest high-earner proportion & top occupation for high earners from India

**Key Findings:**

- :white_check_mark: **Education premium:** Higher education respondents earn >50K at **~4.2× higher rate** than lower education
- :white_check_mark: **Race skew:** Dataset heavily skewed toward White respondents (~27,000 of 32,561); Black and Asian populations underrepresented
- :white_check_mark: **Class imbalance:** Only **~24% earn >50K** — binary outcome is imbalanced, important for classification models
- :white_check_mark: **Age factor:** Average age of >50K earners is ~44 years; strong correlation with experience and seniority
- :white_check_mark: **Gender patterns:** Male respondents average age ~40; female respondents average ~38 — consistent with historical workforce trends
- :white_check_mark: **Geographic insight:** India ranks among top countries with >50K earners despite small sample size — likely selection bias (skilled professionals)

---

### :two: Mean, Variance & Standard Deviation Calculator

<div align="center">

**Statistical Calculator for 3×3 Matrix Operations**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1ooFNF91BcRPpAoUn5GG9XC2DP5pCbF2j?usp=sharing)

</div>

Computes mean, variance, standard deviation, max, min, and sum on a list of 9 numbers reshaped into a 3×3 matrix — along columns, rows, and the flattened array.

**Key Features:**

- :white_check_mark: Input validation — raises `ValueError` if input is not exactly 9 elements
- :white_check_mark: Results computed along axis 0 (columns), axis 1 (rows), and flattened
- :white_check_mark: Visualizations: heatmap + bar charts per statistical measure

**Output Format:**

```python
{
    'mean':               [axis_0_list, axis_1_list, flattened_value],
    'variance':           [axis_0_list, axis_1_list, flattened_value],
    'standard deviation': [axis_0_list, axis_1_list, flattened_value],
    'max':                [axis_0_list, axis_1_list, flattened_value],
    'min':                [axis_0_list, axis_1_list, flattened_value],
    'sum':                [axis_0_list, axis_1_list, flattened_value]
}
```

---

### :three: Medical Data Visualizer

<div align="center">

**Cardiovascular Disease Risk Analysis & Data Visualization**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1BNXvU_Oo1JyjWUWsbqBgWM_extGZxASv?usp=sharing)

</div>

Analyzes the [Kaggle Cardiovascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) (70,000 patients) to explore relationships between lifestyle factors, biomarkers, and cardiovascular disease risk through exploratory data analysis and statistical visualization.

**Key Features:**

- :bar_chart: Categorical plot — count of categorical variables (active, smoke, alcohol, cholesterol, glucose, BMI) stratified by CVD status
- :fire: Correlation heatmap — Pearson correlation matrix with upper triangle masked for clarity
- :chart_with_upwards_trend: Feature correlation rankings — horizontal bar chart showing which features correlate strongest with CVD
- :dart: Age & BMI group analysis — CVD prevalence by age group and BMI category
- :syringe: Biomarker distributions — cholesterol and glucose normalization (binary: normal vs elevated)
- :abacus: Feature engineering — BMI calculation from weight/height, categorical binning for age and BMI groups
- :medical_symbol: Data cleaning — removes physiologically impossible values (e.g., DBP > SBP), outliers beyond 2.5–97.5 percentiles

**Key Findings:**

- :white_check_mark: **Balanced binary outcome:** 50/50 split between CVD/non-CVD — excellent for supervised learning without class resampling
- :white_check_mark: **Lifestyle factors paradox:** Activity, smoking, alcohol show ~0 correlation with CVD — may indicate dataset bias or confounding variables
- :white_check_mark: **Real physiological drivers:** Systolic BP (r≈+0.4), cholesterol (r≈+0.3), age (r≈+0.2) are strongest CVD predictors
- :white_check_mark: **Age-BMI interaction:** Overweight prevalence increases with age; BMI categories show age-dependent CVD risk
- :white_check_mark: **Data quality:** Absence of impossible values (DBP > SBP); outliers removed conservatively (2.5–97.5 percentile)

---

### :four: Page View Time Series Visualizer

<div align="center">

**freeCodeCamp Forum Daily Traffic Analysis (2016–2019)**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1D3AmrdbC_KKsOqiYy0wchc4knCBAGyjK?usp=sharing)

</div>

Visualizes and analyzes **1,238 days** of freeCodeCamp.org forum page views — revealing growth trends, seasonal patterns, and distribution shifts across a 3.5-year period. Data is cleaned by removing the top/bottom **2.5%** of outliers.

**Key Features:**

- :chart_with_upwards_trend: **Line plot:** Tracks daily page views with clear visibility of growth trajectory and spike events
- :bar_chart: **Grouped bar chart:** Average monthly views by year — reveals seasonal patterns and year-over-year comparison
- :package: **Box plots:** Dual side-by-side plots showing year-wise trend (upward distribution shift) and month-wise seasonality (October–November peaks)
- :repeat: **Rolling mean analysis:** 30-day centred rolling average isolates the long-term trend from daily noise
- :clipboard: **Statistical outlier documentation:** Box plots display IQR-based outlier dots with full transparency on data quality

**Key Findings:**

- :white_check_mark: **Explosive growth:** Forum traffic grew **~3.3× from 2016 to 2019** (mean daily views: ~30K → ~100K)
- :white_check_mark: **Acceleration phase:** Clear growth acceleration begins in **late 2018** — detected via 30-day rolling mean inflection
- :white_check_mark: **Academic seasonality:** January–February and October–November show consistently elevated activity; June–August show dips — suggests student/educator-driven traffic
- :white_check_mark: **Improving consistency:** 2019 shows narrower gap between mean and max values — traffic became more stable, fewer extreme spikes relative to baseline
- :white_check_mark: **Statistical outliers present:** Even after 2.5% quantile removal, box plots reveal IQR-based outliers — genuine exceptional traffic days, especially in peak months
- :white_check_mark: **Partial-year caveat:** 2016 data begins in May (not January) — full-year comparison with 2017–2019 requires interpretation care

---

### :five: Sea Level Predictor

<div align="center">

**Global Sea Level Rise Analysis & 2050 Forecasting**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1BuHFw4mfcI6Kly0gG6GbT7Fv9JFPF6i9?usp=sharing)

</div>

Analyzes **172 years** of global average sea level measurements (1880–present) from NOAA/CSIRO data — predicting sea level rise through 2050 using linear regression across two distinct time windows.

**Key Features:**

- :bar_chart: **Scatter plot** — Visualizes historical sea level observations with clear temporal trends
- :chart_with_upwards_trend: **Long-term regression (1880–present)** — Establishes baseline 140-year trend slope and projects through 2050
- :rocket: **Recent trend regression (2000–present)** — Captures acceleration phase by fitting recent 20+ years separately, revealing steeper rise rate
- :crystal_ball: **Dual forecasts** — Compares pessimistic (recent trend) vs. conservative (full history) scenarios for 2050 predictions
- :triangular_ruler: **Statistical metrics** — Reports slope (inches/year) and y-intercept for both regression models
- :dart: **Annotated visualization** — Line labels display slope values for easy interpretation

**Key Findings:**

- :white_check_mark: **Accelerating rise:** Recent sea level rise rate (~0.13 in/year) significantly exceeds long-term average (~0.06 in/year) — 2.2× acceleration detected
- :white_check_mark: **2050 projections:** Conservative model predicts ~14.5 inches rise from 1880 baseline; recent-trend model projects ~20+ inches — wide range reflects climate uncertainty
- :white_check_mark: **Inflection point:** Acceleration becomes evident after year 2000, aligning with intensified climate change impacts
- :white_check_mark: **Linear extrapolation limits:** Assumes constant rates; actual sea level rise may be nonlinear due to ice sheet collapse, thermal expansion acceleration
- :white_check_mark: **Data quality:** CSIRO Adjusted Sea Level provides satellite-era continuity with pre-satellite tide gauge records

---

## :rocket: Getting Started

### Prerequisites

Ensure **Python 3.7 or later** is installed:

```bash
python --version
```

### Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/pedromst2000/Data-Analysis.git
   cd Data-Analysis
   ```

2. **Navigate to a project folder:**
   ```bash
   cd <project-folder>
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > **📌 Dependency Pinning:** `requirements.txt` files pin specific versions to ensure reproducibility across projects. If installation fails, install packages individually:
   >
   > ```bash
   > pip install pandas numpy matplotlib seaborn scipy
   > ```

   > **Note:**: You only need to install dependencies if you want to run the Python scripts. The Jupyter notebooks can read all necessary libraries from the Colab environment or Kernel without additional setup.

### Running Projects

Each project is fully self-contained. Run the main script to execute the analysis and display unit test results:

```bash
python main.py
```

Output includes:

- ✅ Function results (statistics, aggregations, visualizations)
- ✅ Unit test pass/fail status with detailed assertions

---

<div align="center">

[:arrow_up: Back to Top](#bar_chart-data-analysis)

</div>

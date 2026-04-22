# 📊 Data-Analysis

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#️-tech-stack)
- [Projects](#-projects)
- [Getting Started](#-getting-started)

---

## 🎯 Overview

A collection of **Python data analysis and visualization projects** demonstrating core data science techniques:

- **Statistical computation** — matrix operations, descriptive statistics
- **Exploratory data analysis (EDA)** — trends, distributions, seasonality, correlations
- **Data visualization** — line charts, bar plots, box plots, heatmaps, scatter plots
- **Data cleaning & preprocessing** — outlier removal, categorical encoding, feature engineering

**Notebooks** are hosted in **Google Colab** for interactive exploration with inline visualizations. **Python scripts** provide production-ready implementations with unit tests and command-line execution.

---

## 🛠️ Tech Stack

| Category          | Tools & Libraries                       |
| ----------------- | --------------------------------------- |
| **Language**      | Python 3.7+                             |
| **Data Handling** | pandas, NumPy                           |
| **Visualization** | Matplotlib, Seaborn, pandas.plotting    |
| **Testing**       | Unit tests (unittest)                   |
| **Environment**   | Jupyter Notebook, Google Colab, VS Code |

---

## 📁 Projects

### 1️⃣ Demographic Data Analyzer

<div align="center">

**US Census Income & Demographics Analyzer**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/15xuljB270NIhQLyMZ5QuTt3NzKquTwVh?usp=sharing)

</div>

Analyzes demographic and income patterns from the [UCI Adult Census Income dataset](https://archive.ics.uci.edu/ml/datasets/Adult) — answering key questions on socioeconomic disparities, education premiums, and workforce demographics.

**Key Features:**

- 🌍 Race distribution count across the full dataset
- 👨 Average age of male respondents
- 🎓 Percentage of respondents with Bachelor's degree or higher
- 💰 Income differential by education level (higher vs lower education)
- ⏱️ Minimum work hours + income rate for minimum-hour workers
- 🗺️ Country with highest high-earner proportion & top occupation for high earners from India

**Key Findings:**

- ✅ **Education premium:** Higher education respondents earn >50K at **~4.2× higher rate** than lower education
- ✅ **Race skew:** Dataset heavily skewed toward White respondents (~27,000 of 32,561); Black and Asian populations underrepresented
- ✅ **Class imbalance:** Only **~24% earn >50K** — binary outcome is imbalanced, important for classification models
- ✅ **Age factor:** Average age of >50K earners is ~44 years; strong correlation with experience and seniority
- ✅ **Gender patterns:** Male respondents average age ~40; female respondents average ~38 — consistent with historical workforce trends
- ✅ **Geographic insight:** India ranks among top countries with >50K earners despite small sample size — likely selection bias (skilled professionals)

---

### 2️⃣ Mean, Variance & Standard Deviation Calculator

<div align="center">

**Statistical Calculator for 3×3 Matrix Operations**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1ooFNF91BcRPpAoUn5GG9XC2DP5pCbF2j?usp=sharing)

</div>

Computes mean, variance, standard deviation, max, min, and sum on a list of 9 numbers reshaped into a 3×3 matrix — along columns, rows, and the flattened array.

**Key Features:**

- ✅ Input validation — raises `ValueError` if input is not exactly 9 elements
- ✅ Results computed along axis 0 (columns), axis 1 (rows), and flattened
- ✅ Visualizations: heatmap + bar charts per statistical measure

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

### 3️⃣ Medical Data Visualizer

<div align="center">

**Cardiovascular Disease Risk Analysis & Data Visualization**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1BNXvU_Oo1JyjWUWsbqBgWM_extGZxASv?usp=sharing)

</div>

Analyzes the [Kaggle Cardiovascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) (70,000 patients) to explore relationships between lifestyle factors, biomarkers, and cardiovascular disease risk through exploratory data analysis and statistical visualization.

**Key Features:**

- 📊 Categorical plot — count of categorical variables (active, smoke, alcohol, cholesterol, glucose, BMI) stratified by CVD status
- 🔥 Correlation heatmap — Pearson correlation matrix with upper triangle masked for clarity
- 📈 Feature correlation rankings — horizontal bar chart showing which features correlate strongest with CVD
- 🎯 Age & BMI group analysis — CVD prevalence by age group and BMI category
- 💉 Biomarker distributions — cholesterol and glucose normalization (binary: normal vs elevated)
- 🧮 Feature engineering — BMI calculation from weight/height, categorical binning for age and BMI groups
- ⚕️ Data cleaning — removes physiologically impossible values (e.g., DBP > SBP), outliers beyond 2.5–97.5 percentiles

**Key Findings:**

- ✅ **Balanced binary outcome:** 50/50 split between CVD/non-CVD — excellent for supervised learning without class resampling
- ✅ **Lifestyle factors paradox:** Activity, smoking, alcohol show ~0 correlation with CVD — may indicate dataset bias or confounding variables
- ✅ **Real physiological drivers:** Systolic BP (r≈+0.4), cholesterol (r≈+0.3), age (r≈+0.2) are strongest CVD predictors
- ✅ **Age-BMI interaction:** Overweight prevalence increases with age; BMI categories show age-dependent CVD risk
- ✅ **Data quality:** Absence of impossible values (DBP > SBP); outliers removed conservatively (2.5–97.5 percentile)

---

### 4️⃣ Page View Time Series Visualizer

<div align="center">

**freeCodeCamp Forum Daily Traffic Analysis (2016–2019)**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/1D3AmrdbC_KKsOqiYy0wchc4knCBAGyjK?usp=sharing)

</div>

Visualizes and analyzes **1,238 days** of freeCodeCamp.org forum page views — revealing growth trends, seasonal patterns, and distribution shifts across a 3.5-year period. Data is cleaned by removing the top/bottom **2.5%** of outliers.

**Key Features:**

- 📈 **Line plot:** Tracks daily page views with clear visibility of growth trajectory and spike events
- 📊 **Grouped bar chart:** Average monthly views by year — reveals seasonal patterns and year-over-year comparison
- 📦 **Box plots:** Dual side-by-side plots showing year-wise trend (upward distribution shift) and month-wise seasonality (October–November peaks)
- 🔄 **Rolling mean analysis:** 30-day centred rolling average isolates the long-term trend from daily noise
- 📋 **Statistical outlier documentation:** Box plots display IQR-based outlier dots with full transparency on data quality

**Key Findings:**

- ✅ **Explosive growth:** Forum traffic grew **~3.3× from 2016 to 2019** (mean daily views: ~30K → ~100K)
- ✅ **Acceleration phase:** Clear growth acceleration begins in **late 2018** — detected via 30-day rolling mean inflection
- ✅ **Academic seasonality:** January–February and October–November show consistently elevated activity; June–August show dips — suggests student/educator-driven traffic
- ✅ **Improving consistency:** 2019 shows narrower gap between mean and max values — traffic became more stable, fewer extreme spikes relative to baseline
- ✅ **Statistical outliers present:** Even after 2.5% quantile removal, box plots reveal IQR-based outliers — genuine exceptional traffic days, especially in peak months
- ✅ **Partial-year caveat:** 2016 data begins in May (not January) — full-year comparison with 2017–2019 requires interpretation care

---

## 🚀 Getting Started

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
   > **📌 Dependency Pinning:** `requirements.txt` files pin specific versions (e.g., `pandas==1.5.3`, `numpy==2.2.5`). If installation fails, install packages individually:
   >
   > ```bash
   > pip install pandas numpy matplotlib seaborn
   > ```

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

[⬆️ Back to Top](#-data-analysis)

</div>

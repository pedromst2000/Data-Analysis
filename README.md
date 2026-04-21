# 📊 Data-Analysis

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#️-tech-stack)
- [Projects](#-projects)
- [Getting Started](#-getting-started)

---

## 🎯 Overview

A collection of Python data analysis projects covering statistical computation, demographic analysis, and data visualization.

**Notebooks** are hosted in **Google Colab** for interactive exploration with inline visualizations. **Python scripts** contain the core logic for imports, testing, and running from the command line.

---

## 🛠️ Tech Stack

| Category          | Tools                                   |
| ----------------- | --------------------------------------- |
| **Language**      | Python 3.x                              |
| **Data**          | NumPy, pandas                           |
| **Visualization** | Matplotlib, Seaborn                     |
| **Environment**   | Jupyter Notebook, Google Colab, VS Code |

---

## 📁 Projects

### 1️⃣ Demographic Data Analyzer

<div align="center">

**US Census Income & Demographics Analyzer**

[![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-blue?logo=google-colab&style=flat-square)](https://colab.research.google.com/drive/15xuljB270NIhQLyMZ5QuTt3NzKquTwVh?usp=sharing)

</div>

Analyzes US Census data to answer specific socioeconomic questions across income, education, occupation, and country of origin.

**Key Features:**

- 🌍 Race distribution count across the full dataset
- 👨 Average age of male respondents
- 🎓 Percentage of respondents holding a Bachelor's degree
- 💰 % earning >50K split by education level (higher vs lower education)
- ⏱️ Minimum weekly work hours + % of those minimum-hour workers earning >50K
- 🗺️ Country with the highest proportion of >50K earners & top occupation for high earners in India

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

## 🚀 Getting Started

### Prerequisites

**Python 3.7+** is required:

```bash
python --version
```

### Running the Projects

Each project is self-contained. Navigate to its folder, install dependencies, then run `main.py`:

```bash
cd <project-folder>
pip install -r requirements.txt
python main.py
```

`python main.py` prints both the **function output** and the **unit test results**.

> **⚠️ Note on `requirements.txt`:** Dependencies are pinned (e.g. `pandas==1.5.3`, `numpy==2.2.5`). If installation fails due to version conflicts, install direcrly with pip as shown below:
>
> ```bash
> pip install pandas   # demographic-data-analyzer
> pip install numpy    # mean-variance-standard-deviation-calculator
> ```

---

<div align="center">

### [⬆️ Back to Top](#-data-analysis)

</div>

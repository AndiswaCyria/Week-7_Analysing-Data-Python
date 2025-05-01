#  Wine Quality Data Analysis

## Overview

This project is a Python-based data analysis and visualization assignment using the **Wine Quality - Red Wine** dataset. The objective is to:

- Load and explore the dataset.
- Perform basic data analysis.
- Visualize the data using various chart types.

The analysis was done using `pandas` for data manipulation, `matplotlib` and `seaborn` for data visualization.

---

## Dataset

- **Name:** Wine Quality - Red Wine Dataset
- **File:** `winequality-red.csv`
- **Source:** UCI Machine Learning Repository

The dataset contains physicochemical tests of red wine samples from the Portuguese "Vinho Verde" region. Each row represents a wine sample, and includes columns such as:

- `fixed acidity`
- `volatile acidity`
- `citric acid`
- `residual sugar`
- `chlorides`
- `free sulfur dioxide`
- `total sulfur dioxide`
- `density`
- `pH`
- `sulphates`
- `alcohol`
- `quality` (score between 0 and 10)

---

## Tasks Completed

###  Task 1: Load and Explore the Dataset

- Loaded the dataset with `pandas`.
- Displayed the first few rows using `.head()`.
- Checked data types and missing values.
- Cleaned the data by removing any missing entries.

### Task 2: Basic Data Analysis

- Computed basic statistics using `.describe()`.
- Grouped by the `quality` column to find mean values across groups.
- Identified patterns and trends (e.g., higher alcohol content tends to correlate with better quality).

###  Task 3: Data Visualization

Created the following charts:

1. **Line Chart:**  
   *Shows the average alcohol content across different wine quality scores.*

2. **Bar Chart:**  
   *Compares average volatile acidity across wine quality scores.*

3. **Histogram:**  
   *Displays the distribution of alcohol content.*

4. **Scatter Plot:**  
   *Visualizes the relationship between alcohol content and density, color-coded by wine quality.*

Each chart is fully customized with titles, axis labels, and legends for clarity.

---

## How to Run

**Install Dependencies:**

```bash
pip install pandas matplotlib seaborn

# 📊 Netflix Data Cleaning & Exploratory Data Analysis

## 📌 Project Overview

This project focuses on cleaning and preprocessing the **Netflix Titles** dataset using **Python** and **Pandas**. The goal is to prepare the raw dataset for analysis by handling missing values, correcting data types, and standardizing inconsistent data. After cleaning, exploratory data analysis (EDA) is performed using **Matplotlib** to visualize important trends.

---

## 🎯 Objectives

* Inspect the dataset using `head()`, `info()`, and `describe()`.
* Identify and handle missing values column by column.
* Fix mixed-type columns (e.g., `duration` stored as `"90 min"` or `"3 Seasons"`).
* Convert date columns into proper datetime format.
* Export the cleaned dataset to a new CSV file.
* Create visualizations to better understand the dataset.

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* Matplotlib

---

## 📂 Project Structure

```text
Netflix-Data-Cleaning/
│
├── netflix_titles.csv          # Original dataset
├── cleaned_netflix_titles.csv  # Cleaned dataset
├── data_cleaning.ipynb         # Jupyter Notebook
├── README.md                   # Project documentation
```

---

## 🔧 Data Cleaning Steps

### 1. Dataset Inspection

* Displayed the first few records using `head()`
* Checked column names and data types using `info()`
* Generated descriptive statistics using `describe()`

### 2. Missing Value Handling

* Identified missing values in every column.
* Filled categorical missing values with `"Unknown"` or the mode where appropriate.
* Removed rows with essential missing information.

### 3. Mixed-Type Column Cleaning

The `duration` column contained values such as:

* `90 min`
* `120 min`
* `1 Season`
* `3 Seasons`

The numeric value and unit were separated into:

* `duration_value`
* `duration_unit`

making the data easier to analyze.

### 4. Date Parsing

Converted the `date_added` column into a proper datetime format using Pandas.

### 5. Export

Saved the cleaned dataset as:

```text
cleaned_netflix_titles.csv
```

---

## 📈 Visualizations

The project includes the following charts:

* Missing Values by Column
* Movies vs TV Shows
* Content Rating Distribution
* Top 10 Producing Countries
* Movies vs TV Shows (Pie Chart)
* Titles Added Per Year
* Movie Duration Distribution

---

## 📊 Key Findings

* Successfully cleaned missing and inconsistent values.
* Standardized the `duration` column by separating numeric values from units.
* Converted date columns into datetime objects for time-based analysis.
* Produced several visualizations that provide insights into the Netflix catalog.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd Netflix-Data-Cleaning
```

3. Install the required libraries:

```bash
pip install pandas matplotlib
```

4. Launch Jupyter Notebook:

```bash
jupyter notebook
```

5. Open `data_cleaning.ipynb` and run all cells.

---

## 📷 Sample Output

The notebook generates:

* A cleaned dataset (`cleaned_netflix_titles.csv`)
* Multiple charts for exploratory data analysis
* Summary statistics and data quality checks

---

## 📚 Learning Outcomes

Through this project, you will learn how to:

* Clean real-world datasets using Pandas.
* Handle missing values effectively.
* Work with mixed-format columns.
* Parse and manipulate datetime data.
* Create meaningful visualizations with Matplotlib.
* Export cleaned data for further analysis.

---
project url
https://roadmap.sh/projects/cleaning-netflix-dataset
-----

## 👨‍💻 Author

**Aditya**

---

## 📄 License

This project is intended for educational and learning purposes.

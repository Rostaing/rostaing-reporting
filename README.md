## 📊 Rostaing Reporting (RR) - Your Automated Data Analysis Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Pandas-brightgreen.svg)](https://pandas.pydata.org/)
[![Dependencies](Rostaing Report)](https://pypi.org/project/rostaing-report/)

**Rostaing Reporting** is a powerful and intuitive web application built with Python and Streamlit. It automates the tedious process of exploratory data analysis (EDA). Simply upload your data file, and let the application generate detailed reports, visualizations, and statistical tests in just a few clicks.

Say goodbye to repetitive Jupyter notebooks and hello to interactive and efficient analysis!

## 🚀 Key Features

*   **📤 Multi-Format Data Loading:** Easily import your data from `.csv`, `.xlsx` (Excel), or `.json` files.
*   **📈 Automated Exploratory Data Analysis (EDA):** Generate a comprehensive report that includes:
    *   Data overview (number of variables, observations, missing values).
    *   Detailed analysis for each variable (distribution, key statistics, etc.).
    *   Interaction and correlation analysis between variables.
*   **📊 Interactive Data Interface:** View your data in a full table or through a paginated system for better performance on large datasets.
*   **🔬 On-Demand Statistical Tests:** Perform complex statistical tests without writing a single line of code:
    *   **Chi-squared Test (χ²):** To test the independence between two categorical variables.
    *   **Kolmogorov-Smirnov Test (K-S):** To compare a variable's distribution to a normal distribution.
    *   **Mann-Whitney U Test:** To compare the distributions of two independent groups.
    *   **Normality Test (Shapiro-Wilk):** To check if a variable follows a normal distribution.
*   **📥 Easy Export:**
    *   Download the full analysis report in **HTML** format.
    *   Export the current dashboard view as **PNG** or **PDF** for your presentations.
    *   Download the statistical test results in **CSV** format.
*   **🧹 Clean and Reusable Interface:** A "Clear and restart" button allows you to reset the application for a new analysis.

## 🛠️ Technologies Used

*   **Backend & Logic:** Python
*   **Web Interface:** Streamlit
*   **Data Manipulation:** Pandas, Numpy
*   **Statistical Tests:** Scipy
*   **Excel File Reading:** openpyxl
*   **Report Generation:** rostaing-report

## ⚙️ Installation and Launch

Follow these steps to run the project on your local machine.

### 1. Prerequisites

*   [Python 3.8+](https://www.python.org/downloads/)
*   `pip` (usually included with Python)
*   [Git](https://git-scm.com/downloads)

### 2. Installation Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Rostaing/rostaing-reporting.git
    cd rostaing-reporting
    ```

2.  **Create a virtual environment (recommended):**
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the dependencies:**
    Create a `requirements.txt` file in the root of your project with the following content, then run the command.

    **`requirements.txt`**
    ```
    numpy>=1.23.1
    pandas>=2.0.1
    rostaing_report>=0.1.2
    streamlit>=1.36.0
    openpyxl>=3.1.2
    scipy>=1.11.2
    ```

    **Installation command:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Launching the application

Once the dependencies are installed, launch the application with the following command (assuming your main file is named `app.py`):

```bash
streamlit run app.py
```
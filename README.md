# 📈 Earnings Surprise Trading Analytics

## 🚀 Live Dashboard

[https://YOUR-STREAMLIT-APP.streamlit.app](https://event-driven-equity-market-analytics-f4n8mkdll5vnscsajghrfp.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?logo=numpy)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-purple?logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📌 Project Overview

This project analyzes the relationship between earnings surprises and post-earnings stock returns. The objective is to understand whether companies that outperform analyst expectations generate abnormal returns and to evaluate the performance of a simple earnings-based trading strategy.

The project combines financial data analysis, exploratory analytics, risk metrics, and interactive visualization to provide insights into market reactions following earnings announcements.

---

# 🎯 Objectives

- Analyze earnings surprise patterns across companies.
- Study stock returns after earnings announcements.
- Categorize earnings events into different surprise levels.
- Evaluate trading opportunities based on earnings surprises.
- Measure strategy performance using risk-adjusted metrics.
- Build an interactive dashboard for exploratory analysis.

---

# 🔄 Project Workflow

```text
Data Collection
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Exploratory Data Analysis
       ↓
Statistical Analysis
       ↓
Risk Metrics Calculation
       ↓
Strategy Performance Evaluation
       ↓
Interactive Dashboard Development
```

---

# 📂 Project Structure

```text
Earnings-Surprise-Analytics/
│
├── app.py
├── Earnings_Surprise_Analysis.ipynb
├── powerbi_earnings_dashboard.csv
├── requirements.txt
├── README.md
└── outputs/
```

---

# 📊 Dataset Features

| Variable | Description |
|------------|-------------|
| Symbol | Stock ticker |
| Earnings Date | Earnings announcement date |
| Reported EPS | Actual EPS reported |
| Surprise(%) | Earnings surprise percentage |
| Return_1D_% | One-day return |
| Return_5D_% | Five-day return |
| Return_30D_% | Thirty-day return |
| Surprise_Category | Earnings event category |

---

# ⚙ Methodology

## 1. Data Collection

Historical earnings data and stock returns were collected and consolidated into a structured dataset.

---

## 2. Feature Engineering

Generated:

- One-Day Return
- Five-Day Return
- Thirty-Day Return
- Earnings Surprise Categories

Categories include:

- Strong Beat
- Beat
- In-Line
- Miss
- Strong Miss

---

## 3. Exploratory Data Analysis

Performed:

- Distribution analysis
- Category-wise return analysis
- Scatter plots
- Box plots
- Outlier detection

---

## 4. Statistical Analysis

Studied:

- Relationship between earnings surprises and returns.
- Average returns across holding periods.
- Correlation between variables.

---

## 5. Trading Strategy Analysis

Evaluated:

- Top-performing earnings events
- Return distributions
- Risk vs reward characteristics

---

## 6. Risk Analytics

Calculated:

### Annualized Volatility

Measures return variability.

### Sharpe Ratio

Measures risk-adjusted performance.

### Maximum Drawdown

Measures worst portfolio decline.

### Equity Curve

Tracks cumulative growth.

### Drawdown Curve

Visualizes portfolio declines over time.

---

# 📈 Dashboard Features

## Executive Summary

- KPI Cards
- Average Return Analysis

## Earnings Analysis

- Earnings Category Distribution
- Scatter Plot
- Category Return Analysis

## Trading Strategy

- Top Earnings Surprises
- Top Returns
- Box Plot Analysis

## Risk Analytics

- Heatmap
- Histogram
- Bubble Chart
- Treemap
- Equity Curve
- Drawdown Curve
- Correlation Matrix

## Interactive Components

- Sidebar Filters
- Symbol Search
- Dataset Viewer
- Download Dataset

---

# 🛠 Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly
- Matplotlib
- Seaborn

### Dashboard

- Streamlit

### Development Environment

- VS Code
- Jupyter Notebook

### Version Control

- GitHub

---

# 📊 Key Insights

- Positive earnings surprises generally resulted in superior short-term returns.
- Strong Beat stocks delivered the highest average performance.
- Return distributions exhibited several high-performing outliers.
- Strategy volatility remained moderate.
- Drawdowns were manageable.
- Earnings surprises showed a positive correlation with subsequent returns.

---

# 🚀 Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/earnings-surprise-trading-analytics.git
```

Navigate to project directory:

```bash
cd earnings-surprise-trading-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run dashboard:

```bash
streamlit run app.py
```

---

# 📋 Requirements

- Python 3.10+
- Streamlit
- Plotly
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 🔮 Future Enhancements

- Real-time earnings data integration
- Event Study methodology
- Sector-wise analysis
- Machine Learning return prediction
- Portfolio optimization
- FRM-based risk models
- Advanced performance metrics

---

# 👨‍💻 Author

## Ansh Saboo

B.Tech Information Technology

Interested in:

- FinTech
- Data Analytics
- Quantitative Finance
- Financial Risk Management
- Investment Analytics

---

⭐ If you found this project useful, consider giving the repository a star.

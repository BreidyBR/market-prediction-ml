# Market Prediction ML

## Project Overview

This project investigates whether machine learning models can predict the next-day price direction of the SPY ETF, which tracks the S&P 500, using publicly available historical market data.

The primary objective is to develop a reproducible end-to-end data science pipeline that applies proper time-series validation, compares predictive models against simple baselines, and evaluates their performance through realistic backtesting.

This project is intended for educational and portfolio purposes. It does not provide financial advice or support real-money trading.

## Research Question

Can machine learning models predict whether SPY will close higher or lower on the next trading day more accurately than simple baseline models?

## Project Objectives

- Collect and explore historical financial market data.
- Develop technical indicators using historical price and volume information.
- Implement baseline models for performance comparison.
- Train and evaluate multiple machine learning algorithms.
- Apply walk-forward validation to prevent look-ahead bias.
- Perform backtesting that includes transaction costs and slippage.
- Evaluate model performance across different market conditions.
- Test the pipeline on additional financial assets.
- Document results, limitations, and reproducibility procedures.

## Success Criteria

The project will be evaluated based on:

1. **Predictive performance:** Compare classification metrics against baseline models.
2. **Temporal validation:** Ensure that training and evaluation respect chronological order.
3. **Data integrity:** Prevent data leakage from future observations.
4. **Backtesting:** Evaluate simulated strategies after transaction costs and slippage.
5. **Robustness:** Examine performance across different periods and financial assets.
6. **Reproducibility:** Provide documented dependencies, configurations, and execution procedures.

A model outperforming its baselines is not guaranteed. Results that show no predictive advantage will also be documented.

## Technology Stack

- **Language:** Python
- **Data Collection:** yfinance
- **Data Processing:** pandas, NumPy
- **Visualization:** Matplotlib
- **Machine Learning:** scikit-learn (planned)
- **Version Control:** Git and GitHub
- **Development Environment:** Visual Studio Code

Additional dependencies will be introduced as needed.

## Project Status

**Phase 1 — Project Setup**

The repository structure, Python environment, dependencies, and initial configuration have been prepared.

The next stage focuses on historical market data collection and exploratory data analysis.

## Disclaimer

This project is developed exclusively for educational and research purposes. Historical performance does not guarantee future results. No real-money trading will be conducted.
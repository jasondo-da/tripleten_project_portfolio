# A/B Test Analysis

## Table of Contents
- [Goal](#goal)
- [Introduction](#introduction)
- [Analysis Outline](#analysis-outline)
- [Results](#results)
- [A/B Test Analysis Jupyter Notebook](#a/b-test-analysis-jupyter-notebook)
- [Hypotheses US Raw Data CSV](#hypotheses-us-raw-data-csv)
- [Orders US Raw Data CSV](#orders-us-raw-data-csv)
- [Visits US Raw Data CSV](#visits-us-raw-data-csv)

### Goal: 

The project goal is to analyze the online performance of the e-commerce platform and generate new ideas on how to increase sales revenue. To test our new ideas, we will perform an A/B test on the online landing page to see if a different web page would perform better than the current web page.

### Introduction: 

This project is focused on two parts: analyzing a list of potential hypotheses and initiating an A/B test to find the hypothesis that can best help boost company revenue. The first dataset includes various hypotheses and their rating in reach, impact, confidence, and effort. The second dataset includes transaction IDs, visitor IDs, revenue accumulated, and other relevant information. Completing this project includes pre-processing data, calculating both ICE and RICE rating methods, A/B testing, and creating visuals of the results.

### Analysis Outline: 

• Performed web page, online traffic, and customer analysis using pandas, numpy, stats, and matplotlib libraries in python.

• Tested hypotheses and made statistical calculations on web page performance.

• Made fact based reccomendations to assist company executives on web page performance.

### Results: 

The end data supported that the alternative hypothesis (H1) is the better web page based on the statistical significance difference between groups A and B.


## A/B Test Analysis Jupyter Notebook

A/B Test Analysis project in Jupyter Notebook.

Code: [A/B Test Analysis](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2010%20%20-%20AB%20Test/abtest_project.ipynb)


## Hypotheses US Raw Data CSV
The hypotheses data carries several different hypotheses and their various levels of effectiveness if implemented.

Code: [Hypotheses US Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2010%20%20-%20AB%20Test/hypotheses_us.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| Hypotheses | brief descriptions of the hypotheses |
| Reach | user reach, on a scale of one to ten |
| Impact | impact on users, on a scale of one to ten |
| Confidence | confidence in the hypothesis, on a scale of one to ten |
| Effort | the resources required to test a hypothesis, on a scale of one to ten (The higher the Effort value, the more resource-intensive the test) |


## Orders US Raw Data CSV
The orders us table contains data related each transactions made.

Code: [Orders US Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2010%20%20-%20AB%20Test/orders_us.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| transactionId | order identifier |
| visitorId | identifier of the user who placed the order |
| date | of the order |
| revenue | from the order |
| group | the A/B test group that the user belongs to |


## Visits US Raw Data CSV
The visits us table contains data from each visitor.

Code: [Visits US Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2010%20%20-%20AB%20Test/visits_us.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| date | date |
| group | A/B test group |
| visits | the number of visits on the date specified in the A/B test group specified |

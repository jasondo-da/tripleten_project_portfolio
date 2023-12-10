# Yandex.Afisha Marketing Expense Analysis 

Goal: Analyze the marketing expenses for Yandex.Afisha and find methods to optimize it. 

Introduction: As an intern for Yandex.Afisha's analytical department our first task is to help optimize the marketing expenses. Yandex.Afisha will allow access to server logs for the visits from June 2017 through May 2018, a large file of all the orders, and marketing expense statistics. The project involves data cleaning, data analysis, business analysis, cohort analysis, and data visualization.

Analysis Outline: 

Products

• Grouped users by various timeframes (daily, weekly, monthly) to find the total number of users for that period.

• Calculate the session frequency of daily users.

• Calculate the length of each user session.

• Create monthly cohorts and calculate the user retention rate for every cohort.

Sales

• Analyze the conversion timeframe from a customer’s first visit and their first purchase.

• Calculate the total number of orders made each month for each monthly cohort.

• Calculate the average purchase size for each monthly cohort.

• Calculate the long-term value of each monthly cohort.

Marketing

• Calculate the overall, per source, and overtime of marketing cost spent.

• Calculate customer acquisition cost from each of the sources.

• Calculate the return on marketing investment on each monthly cohort.

Results: Based on the sample data, the ideal solution would be to allocate more of the marketing budget to the sources that were used to acquire the summer 17' cohorts and the September 17' cohort since those cohorts had the highest long term return on marketing investment.


## Table of Contents
- [Yandex.Afisha Marketing Expense Analysis Jupyter Notebook](#yandex.afisha=marketing-expense-analysis-jupyter-notebook)
- [Visits Log Raw Data CSV](#visits-log-raw-data-csv)
- [Orders Log Raw Data CSV](#orders-log-raw-data-csv)
- [Costs Raw Data CSV](#costs-raw-data-csv)

<a name="headers"/>


## Yandex.Afisha Marketing Expense Analysis Jupyter Notebook
Yandex.Afisha Marketing Expense Analysis project in Jupyter Notebook.

Code: [Jupyter Notebook](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%209%20-%20Yandex/yandex_afisha.ipynb)



## Visits Log Raw Data CSV
The visits table are server logs with data on website visits.
(All dates in this table are in YYYY-MM-DD format)

Code: [Visits Log Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%209%20-%20Yandex/visits_log_us.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| Uid | user's unique identifier |
| Device | user's device |
| Start Ts | session start date and time |
| End Ts | session end date and time |
| Source Id | identifier of the ad source the user came from |


## Orders Log Raw Data CSV
The orders table consists of data on orders.

Code: [Orders Log Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%209%20-%20Yandex/orders_log_us.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| Uid | unique identifier of the user making an order |
| Buy Ts | order date and time |
| Revenue | Yandex.Afisha's revenue from the order |


## Costs Raw Data CSV
The costs table is made of data on marketing expenses.

Code: [Costs Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%209%20-%20Yandex/costs_us.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| source_id | ad source identifier |
| dt | date |
| costs | expenses on this ad source on this day |

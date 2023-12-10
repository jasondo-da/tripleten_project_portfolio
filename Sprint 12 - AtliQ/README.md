# AtliQ Hardware Customer Analysis

Goal: The goal of our analysis for AtliQ Hardware is to perform a customer analysis on their current clients and find a way to improve customer orders and grow the customer base. This analysis will only be performed on the sample database provided.

Introduction: As a junior analyst for a third-party consulting agency, our client AtliQ Hardware is interested in learning more about their customers and is asking for a customer analysis. AtliQ Hardware has provided us with a backup of their database in the SQLite format. AtliQ Hardware has also restricted the ability to load the whole database to CSV. The backup database includes data on customers, products, gross prices, monthly sales, and other relevant information. Completing this project includes connecting to the database, cleaning data, pre-processing data, exploratory data analysis (EDA), and creating visuals for the discovered results.

Analysis Outline: 

• Assess the data to find the largest customers by gross profit and sales volume.

• Use value_counts to find where these businesses reside and identify other similar potential customers.

• Count and group the products by popularity and by quality variant.

• Count and analyze which transaction is the most preferred.

• Make recommendations on which platform is most advantageous to sell on.

• Make recommendations of other popular products that other customers have frequently purchased.

Results: Discovered our customers' shopping habits regarding product preferences and made recommendations on areas of improvement such as which countries to target and to put more emphasis on the e-commerce side of the business. 

## Table of Contents
- [Jupyter Notebook](#jupyter-notebook)
- [AtliQ Database](#atliq-database)

<a name="headers"/>


## Jupyter Notebook
AtliQ Hardware Customer Analysis project in Jupyter Notebook.

Code: [AtliQ Hardware Customer Analysis](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2012%20-%20AtliQ/atliq_customer_analysis.ipynb)


## AtliQ Database
AtliQ Hardware has provided us with a backup of their database in the SQLite format, no CSV files will be provided, and the company has also restricted your ability to load the whole database to CSV. (The atliq_db.sqlite3 provided file was not included due to limited upload size on GitHub)

| SQLite Tables | Table Description |
| :------------- | :------------ |
| dim_customer | contains customer-related data |
| dim_product | contains product-related data |
| fact_pre_discount | contains pre-invoice deductions information for each product |
| fact_manufacturing_cost | contains the cost incurred in the production of each product |
| fact_gross_price | contains gross price information for each product |
| fact_sales_monthly | contains monthly sales data for each product. |

# Instacart Exploratory Data Analysis

Goal: The objectivce is to  first clean the data and then prepare a report that gives insight into the behavior and shopping habits of Instacart customers from 2017.

Introduction: Using a modified version of Instacart 2017 data, this project is a test to see if we can clean all the errors and process the data of the modified Instacart data. The database includes Instacart orders, products, departments, and other important information. To complete this project will require high attention to detail during the cleaning and pre-processing segment of the project and a deep understanding of the data to accurately report customer behavior through easy-to-read visuals.

Analysis Outline: 

Part A

• Verify that values in the 'order_hour_of_day' columns in the orders table are in ranges from 0 to 23 and 'order_dow' ranges from 0 to 6.

• Create a plot that shows how many people place orders for each hour of the day.

• Create a plot that shows what day of the week people shop for groceries.

• Create a plot that shows how long people wait until they place their next order.

Part B

• Displayed the difference in 'order_hour_of_day' distributions on Wednesdays and Saturdays using histograms.

• Plotted the distribution for the number of total orders that customers make.

• List the top 20 products that are most frequently ordered.

Part C

• Calculated how large each customer's cart size is per order.

• List of the top 20 items that are reordered most frequently by our customers.

Results: Discovered our customers' shopping habits from purchase frequency to most popular sold products to highest store traffic periods.

## Table of Contents
- [Instacart Exploratory Data Analysis Jupyter Notebook](#instacart-exploratory-data-analysis-jupyter-notebook)
- [Instacart Orders Raw Data CSV](#instacart-orders-raw-data-csv)
- [Products Raw Data CSV](#products-raw-data-csv)
- [Order Products Raw Data CSV](#order=products-raw-data-csv)
- [Aisles Raw Data CSV](#aisles-raw-data-csv)
- [Departments Raw Data CSV](#departments-raw-data-csv)

<a name="headers"/>


## Instacart Exploratory Data Analysis Jupyter Notebook
Instacart Exploratory Data Analysis project in Jupyter Notebook.

Code: [Instacart Exploratory Data Analysis](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%207%20-%20insta_project/insta_cart_eda.ipynb)


## Instacart Orders Raw Data CSV
The instacart orders table holdss every order made on the Instacart app.

Code: [Instacart Orders Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%207%20-%20insta_project/instacart_orders.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| order_id | ID number that uniquely identifies each order |
| user_id | ID number that uniquely identifies each customer account |
| order_number | the number of times this customer has placed an order |
| order_dow | day of the week that the order placed (which day is 0 is uncertain) |
| order_hour_of_day | hour of the day that the order was placed |
| days_since_prior_order | number of days since this customer placed their previous order |


## Products Raw Data CSV
The products tables contains a unique product that customers can buy.

Code: [Products Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%207%20-%20insta_project/products.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| product_id | ID number that uniquely identifies each product |
| product_name | name of the product |
| aisle_id | ID number that uniquely identifies each grocery aisle category |
| department_id | ID number that uniquely identifies each grocery department category |


## Order Products Raw Data CSV
The order products table entries displays an item placed in an order. (The order_products.csv file was not included due to limited upload size on GitHub)

Code: ---------------- 

| Column Name | Column Description |
| :------------- | :------------ |
| order_id | ID number that uniquely identifies each order |
| product_id | ID number that uniquely identifies each product |
| add_to_cart_order | the sequential order in which each item was placed in the cart |
| reordered | 0 if the customer has never ordered this product before, 1 if they have |


## Aisles Raw Data CSV
The aisles table contains the aisle names and IDs.

Code: [Aisles Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%207%20-%20insta_project/aisles.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| aisle_id | ID number that uniquely identifies each grocery aisle category |
| aisle | name of the aisle |


## Departments Raw Data CSV
The departments table contains the department names and IDs.

Code: [Departments Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%207%20-%20insta_project/departments.csv)

| Column Name | Column Description |
| :------------- | :------------ |
| department_id | ID number that uniquely identifies each grocery department category |
| department | name of the department |

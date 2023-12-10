# Megaline Mobile Carrier Machine Learning Model

Goal: The project goal is to develop a model with the highest possible accuracy for our client Megaline a popular mobile carrier. For this project, our client is expecting an accuracy threshold of at least 0.75.

Introduction: Megaline wants to develop a model that would analyze subscribers' behavior and recommend one of Megaline's newer plans: Smart or Ultra. Megaline gave permission to access the behavioral database about subscribers who have already switched to the new plans. This database includes calls, minutes called, messages sent, and other important information. To complete our goals, we developed a model with the highest possible accuracy. To do that we are going to split the sample data into a training set, a validation set, and a test set and input these data sets into various models to find the model with the highest accuracy score.

Analysis Outline: 

• Used pandas, sklearn, and matplotlib libraries to create machine learning models

• Split the sample data into a training set, a validation set, and a test set

• Investigated the quality of different models by changing hyperparameters of each model

• Checked the quality of the model using the test set

• Sanity checked each model type

Results: The model we have built with the highest accuracy would be the random forest model. This is to be expected as the random forest model usually has the highest accuracy score when compared to the other model types.

## Table of Contents
- [Jupyter Notebook](#jupyter-notebook)
- [User Behavior Raw Data CSV](#user-behavior-raw-data-csv)

<a name="headers"/>


## Jupyter Notebook
Megaline Mobile Carrier Machine Learning project in Jupyter Notebook.

Code: [Megaline Mobile Carrier Machine Learning Model](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2011%20-%20Machine%20Learning/megaline_project.ipynb)


## User Behavior Raw Data CSV
AtliQ Hardware has provided us with a backup of their database in the SQLite format, no CSV files will be provided, and the company has also restricted your ability to load the whole database to CSV. (The atliq_db.sqlite3 provided file was not included due to limited upload size on GitHub)

| Code | [User Behavior Raw Data CSV](https://github.com/jasondo-da/tripleten_project_portfolio/blob/main/Sprint%2011%20-%20Machine%20Learning/users_behavior.csv) |
| :------------- | :------------ |
| сalls | number of calls |
| minutes | total call duration in minutes |
| messages | number of text messages |
| mb_used | internet traffic used in MB |
| is_ultra | plan for the current month (Ultra - 1, Smart - 0) |

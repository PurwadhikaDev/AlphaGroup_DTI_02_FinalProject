<h1 style="font-weight:bold"> Bank Telemarketing Marketing Campaign </h1>

DTIDS-0206 Alpha Team Final Project  
Created By: Davis Sebastian, Sean Kristian Anderson

## Overview

![Portugal GPD Growth](https://raw.githubusercontent.com/seanka/Python-BankTelemarketing-MachineLearning/master/Resources/Images/portugal_gdp.png)

Portugal, a country located in Europe seems to have negative GDP growth from 2007 before it sinks in 2009. Which was the worst GDP growth this country ever encountered since twenty years ago. Negative GDP growth, for context is marked with higher unemployment rate, lower personal income and lower retail or wholesale sales.

However, a portuguese banking institution conducted a telemarketing campaign in 2008 to 2010. Term deposit is a type of deposit that specify the maturity date. Despite the benefits of term deposit such as minimum risk, this campaign results in a disappointment and didn't work as well as expected. Which could be affected by the economical struggle that Portugal encountered. This campaign however, returns the number of customer that actually open a term deposit account for only around 10% of the total customer contacted. Therefore, this institution wasted many resources and efforts while trying to convince customers to open a deposit account.

## Business Problem Statement

Direct marketing, is a marketing strategy that reaching out potential customers directly via phone calls, emails, etc. Although this strategy requires low cost, it has many drawbacks includes irritates customer, time consuming, limited reaches. Typically, this method has a low conversion rate despite all the effort marketing team had put in this method. In addition without proper prediction such as no initial screening before performing the call, the wasted effort becomes worse.

Despite the drawbacks from direct telemarketing strategy, the effectiveness of this method can be increased using machine learning. The model have a goal to increase the institution benefit by predicting the likelihood of customers open a term deposit account while reducing its expenses by avoiding unnecessary calls. Allowing them to secure as many term deposits as quickly as possible for operational purposes. In addition, this model will also introduce a stronger bank customer relationship by minimizing the disturbance for them. Later on, this model should be the guidelines for the marketing team before performing the calls in order to yield efficient campaigns.

## Project Outline

### 1. Business Problem Understanding

Understanding the overall business, problem encountered and suggested solutions.

### 2. Data Understanding

Dive towards the data, and import required libraries to support the machine learning development.

### 3. Exploratory Data Analysis (EDA)

Data exploration using visualization graphs to discover insights, patterns, and interrelation. Which could provide strong reasoning for any method or approches done for the next sections.

### 4. Data Preprocessing

Handle the raw dataset including duplicated value, missing value, and outliers to obtain better overall accuracy since these values could negatively affects the process of machine learning training.

### 5. Feature Engineering

Handle engineering against the features included in the dataset which includes encoding and scaling before passing the data into the machine learning model.

### 6. Modeling

Exploration towards difference machine learning model, data approaches, and hyperparameter to obtain the best fit results. Analysis on each benchmark methods and its utilization on the business approaches.

### 7. Conclusion and Recommendation

Conclusion or summary in business perspective and for the machine learning model. Recommendation in actionable actions that can be done by stakeholders to increase the business profit or advanced machine learning development in the future to achieve better overall accuracy.

### 8. Model Export

Going through the overall machine learning workflow, and export the model into .pkl extension file. Exported model is used for the dashboard to create new prediction using custom features inputted by user.

## Navigating through Notebook

The final jupyter notebook work is located under **Notebook/Notebook.ipynb**. For easier navigation, Table Of Content (TOC) is provided within the notebook under the heading section. Each entry in the TOC is linked to its corresponding section-simply click on desired entry to jump directly to that section.

## Dashboard

Dashboards are included in this project to assist the understanding of the machine learning workflow.

### Tableau

The [Tableau Dashboard](https://public.tableau.com/shared/PWTMNY9SW?:display_count=n&:origin=viz_share_link) includes sections on the Business Problem, Explanatory Data Analysis (EDA), Model Performance, Conclusion, and Recommendation. Attached image below is the screenshot of the provided tableau dashboard. Simply click on the tab inside the blue section to navigates through the dashboard.

![Tableau Home](https://raw.githubusercontent.com/seanka/Python-BankTelemarketing-MachineLearning/master/Resources/Images/tableau_home.png)

![Tableau Business Problem](https://raw.githubusercontent.com/seanka/Python-BankTelemarketing-MachineLearning/master/Resources/Images/tableau_02.png)

![Tableau Metric Evaluation](https://raw.githubusercontent.com/seanka/Python-BankTelemarketing-MachineLearning/master/Resources/Images/tableau_03.png)

### Streamlit

The [Streamlit Dashboard](http://194.59.165.17:1010) allows user to input custom data for predictions. It provides insights into data preprocessing, feature engineering, oversampling, and the prediction process. This dashboard provides two ways to input features, single and batch input.

To make a single prediction, follow these steps below:

![Streamlit Single Input](https://raw.githubusercontent.com/seanka/Python-BankTelemarketing-MachineLearning/master/Resources/Images/streamlit_single_input.png)

1. Open the dashboard link using any browser.
2. Under the yellow section, make sure to select the "Single Input" tab.
3. Input the features in the provided form under the purple section, ensure that every field has been inputted properly. Click the "Predict Single Outcome" button in the bottom of the form.
4. The result of the prediction located on the right side under the blue section. Which includes the summary of the prediction and the feature importance using SHAP.

To make a batch prediction, follow these steps below:

![Streamlit Batch Input](https://raw.githubusercontent.com/seanka/Python-BankTelemarketing-MachineLearning/master/Resources/Images/streamlit_batch_input.png)

1. Open the dashboard link using any browser.
2. Under the yellow section, make sure to select the "Batch Input" tab.
3. Prepare a CSV file containing records to be predicted, follow this [example file](./Dataset/bank_marketing_test_data.csv) as the guide for the CSV format.
4. Drag and drop or click the "Browse files" button to import the prepared CSV. Click the "Predict Batch Outcome" button.
5. The result of the prediction located on the right side under the blue section. Which includes the summary of the prediction and the feature importance using SHAP.

## Project Directory

- **Dataset/**
  - **bank-additional-full.csv** : raw dataset.
  - **bank_marketing_test_data.csv** : 20 records of randomized dataset for dashboard testing.
- **Models/**
  - **final_model.pkl** : exported machine learning workflow model, including data preprocessing, feature engineering, oversampling, and prediction using lightgbm model.
- **Notebook/**
  - **Notebook.ipynb**: final jupyter notebook.
- **Resources/** : additional resources required for the machine learning dashboard.

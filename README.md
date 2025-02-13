# Big Data Project

## Overview

This repository contains the code and documentation for the **Big Data Project**. The goal of this project is to process, analyze, and visualize large e-commerce datasets. Due to GitHub's file size limitations (100 MB), the dataset has been uploaded to Google Drive. You can access the dataset from the provided link below.

## Access the Data

Due to the large size of the dataset, it exceeds the file upload limits for GitHub. Therefore, the dataset has been uploaded to Google Drive, and you can access it by clicking the link below:

[Click here to access the dataset](https://drive.google.com/drive/folders/1H7aVBOKv5rx4fMdd-Bj87lok0any3Y17?usp=drive_link)

### Files Included in the Dataset:

- **bigdatasate.csv**: The raw e-commerce dataset containing sales, product, and customer information.
- **cleaned_data.csv**: The cleaned and pre-processed data ready for analysis.

## Project Workflow

This project follows the following phases:

### 1. Data Extraction and Preprocessing
The dataset is first extracted and cleaned to handle missing values, incorrect data types, and ensure it is ready for analysis. The following steps are included in the cleaning process:
- Removal of duplicate rows.
- Conversion of columns to appropriate data types (e.g., date fields).
- Handling missing data with suitable strategies like imputation or removal.

### 2. Data Analysis and Transformation
The cleaned dataset is then analyzed to identify key metrics such as sales trends, customer segmentation, and product performance. Key transformations include:
- Calculating metrics like total sales, average order value, and customer lifetime value.
- Segmenting customers based on purchase behavior.
- Aggregating sales data by product category, region, or time period.

### 3. Data Loading to PostgreSQL
The cleaned and transformed data is loaded into a PostgreSQL database for storage and further analysis. You can interact with the database using SQL queries or BI tools such as Power BI or Tableau.

## How to Use the Project

Follow the steps below to run the project and analyze the dataset.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/tarikdabot/big-data.git
cd big-data

[![Python Application Test with Github Actions - Polars Project Su Zhang](https://github.com/nogibjj/Su_Zhang_Polars_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Su_Zhang_Polars_Project/actions/workflows/cicd.yml)

# Su Zhang Polars Project - IDS706 Week 3 Assignment
This project aims to analyze a dataset on patients' healthcare records, which includes patient age, gender, blood type, medical condition, billing amount, medication etc. Please note that these data are not real-world data and are just for descriptive data practice. This project primarily used **Polars** and **Matplotlib** packages to analyze the distribution of billing amount, summary statistics (mean, median, max, standard variation) of billing amount, and age. This project also showcased the distribution of subcategories in tables for the categorical variables, such as blood type, medical condition, admission type, and test results. 

# Source of data: 
https://www.kaggle.com/datasets/prasad22/healthcare-dataset/data

# Project Structure
- Makefile: Build automation commands: in this project, commands mainly include install, format, lint, and test.
- requirements.txt: Specify Python dependencies needed for this project and for this project, added packages of polars and matplotlib.
- main.py: Main application script to read the input data and create functions to print out first few rows of dataset, summarize the key statistics, build histogram for specific data category
- test_main.py: Tests if the functions defined in main.py work normally
- README.me: Project documentation to offer an overview of the project
- github actions: Describes the steps and jobs that GitHub should run automatically. In this project, this includes installing dependencies and packages, lint, format, and test.
- devcontainer: Set up a development environment in Github Codespace, and Dockerfile to define the base environment (such as what tools and libraries are installed)
- healthcare_dataset.csv: Input dataset on patients healthcare records
- Billing_Amount_Hist.png: Output histogram graph demonstrating the distribution of billing amount
- Data_Summary.pdf: Output pdf generated from Jupyter Notebook to showcase the analysis output

# Descriptive Statistics and Visualizations
<img width="329" alt="Screen Shot 2024-09-22 at 2 19 25 AM" src="https://github.com/user-attachments/assets/fd7201e7-75a1-48e9-90b3-49fa14445942">

![Billing Amount](./Billing_Amount_Hist.png)

# Profiler Comparison
<img width="519" alt="Screen Shot 2024-09-22 at 2 18 06 AM" src="https://github.com/user-attachments/assets/9acada48-ee8e-4f0c-95a3-d6cafb075fed">
<img width="536" alt="Screen Shot 2024-09-22 at 2 18 22 AM" src="https://github.com/user-attachments/assets/23a6322a-844d-447f-b42f-26def695c268">

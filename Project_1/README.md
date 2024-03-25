# Project Name: Data Scientist Project1

## Overview
This repository contains a comprehensive exploration of an automobile dataset and the development of predictive models for pricing. It encompasses various stages of the data science workflow, from exploratory data analysis (EDA) to model building and deployment. The primary objective is to extract valuable insights from the data and create accurate price prediction models.

## Files and Components

1. **Mladenova_Data_Scientist_Project1.ipynb**
   - Jupyter Notebook presenting detailed EDA, preprocessing steps, key visualizations, and the development of predictive models for pricing. It offers a comprehensive view of the data analysis process and model comparisons.

2. **Mladenova_Data_Scientist_Project1_Multiple_Correspondence_Analysis_(MCA).Rmd / .html**
   - R Markdown file and its HTML output showcasing the application of Multiple Correspondence Analysis (MCA) on the dataset. This analysis provides deeper insights into categorical variables and their relationships.

3. **Mladenova_Data_Scientist_Project1_RR_model_web_app.py**
   - Python script for a user-friendly web application built with Streamlit. The application allows users to input key data points related to automobiles and receive predicted prices based on the trained models.

4. **Mladenova_Data_Scientist_Project1_Large_Language_Model_(LLM).ipynb**
   - Jupyter Notebook demonstrating the usage of Large Language Model (LLM) to train data and generate new rows. This illustrates an innovative approach to data augmentation and model enhancement.

5. **Automobile_data.csv**
   - The original dataset obtained from Kaggle, containing diverse automobile-related attributes for analysis.

6. **ad.csv**
   - Processed dataset derived after thorough preprocessing steps, ready for model training and evaluation.

7. **Mladenova_Data_Scientist_Project1_ridge_regression_model.pkl**
   - Pickle file storing the trained Ridge Regression model, which serves as the backend for the web application's price prediction functionality.


## Usage Instructions
- Start exploring the project by reviewing the EDA, preprocessing, and model building steps in the Jupyter Notebooks.
- Gain insights into categorical variables using the MCA analysis.
- Experience the model's predictions interactively through the web application developed with Streamlit.
	### Running the Streamlit Web Application
To run the `Mladenova_Data_Scientist_Project1_RR_model_web_app.py` file and launch the Streamlit web application, execute the following command in your terminal or command prompt:

```bash
streamlit run Mladenova_Data_Scientist_Project1_RR_model_web_app.py
```
- Experiment with the LLM approach for data augmentation and model refinement.
	### Note for Mladenova_Data_Scientist_Project1_Large_Language_Model_(LLM).ipynb
Please, note that the Mladenova_BP_Data_Scientist_Technical_Assessment_LLM.ipynb notebook is an example notebook. To run it, you will need to provide your actual API key and ensure that the required data is available. Modify the code within the notebook accordingly to incorporate your API key and data source.

## Dependencies
Ensure all necessary dependencies listed in the `requirements.txt` file are installed before running the scripts or notebooks.

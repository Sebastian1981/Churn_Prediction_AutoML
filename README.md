# Churn_Prediction_AutoML
This project aims to implement a customer churn model using auto-ml including the model development, model explainability/fairness and model deployment. To get the code running, set up e.g. a conda environment using the packages in the requirement.txt file.
## Step #1 - Model Development
Run the notebooks in the following order:
- "step_01_overview.ipynb"
- "step_02_exploratory_data_analysis.ipynb"
- "step_03_model_training.ipynb"
Details on what the notebooks exactly do are provided in the notebooks itself.
## Step #2 - Model Explainability and Model Fairness
Run the notebooks in the following order:
- "step_04_model_explainability.ipynb"
- "step_05_model_fairness.ipynb"
Details on what the notebooks exactly do are provided in the notebooks itself.
## Step #3 - Model Deployment
- run "step_06_web_api.ipynb" to create a fast-api python script and dockerize it
- use docker desktop to explore the app
## Step #4 - Model Monitoring
- model performance and data drifts are monitored using the mlflow package: from the terminal simply run $mlflow ui 
 

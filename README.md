# Problem statment1: German credit score 
#teammates: Group 7 Gunda Venkatanaga Manikumar,Swathi Surampudi



This repository contains code which demonstrates ML-Ops using a `FastAPI` application which predicts the Risk by using the German Score dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/)

## Running Instructions
- Used the assignment1 Credit_scorer as a reference for reading the dataset
- utilised the assigmnet Ml-ops_iris to make necessary changes in the code for the ci/cd pipelines  workflow
- utilised assignment of explainability instructions to do the explainability of the gernman dataset
- Install dependencies using `pip3 install requirements.txt`
- Run application using `python3 main.py`
- Run tests using `pytest`

## CI/CD
- `build` (test) for all the pull requests
- `build` (test) and `upload_zip` for all pushes

## Assignment Tasks
API, MLOps, Usage of rule based and ML models, Visualization, Explainability
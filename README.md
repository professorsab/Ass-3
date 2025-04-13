# wine-quality-prediction
# Wine Quality Prediction Models

This repository contains various regression models trained on the Wine Quality dataset:

- Linear Regression
- Polynomial Regression (Degree 2)
- Ridge Regression (L2 Regularization)
- Lasso Regression (L1 Regularization)
- Custom implementations of Batch GD, SGD, and Mini-Batch GD

## How to Use

Load models with `joblib.load('model_name.pkl')` or load thetas with `numpy.load('theta.npy')`.

# -*- coding: utf-8 -*-
"""Lightgbm Model 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PLyCBwJOBxvJw_tqwIO7WRp8HrfXEuZ0
"""

# Commented out IPython magic to ensure Python compatibility.
# Basic Imports 
import numpy as np
import pandas as pd
# Plotting 
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
# %matplotlib inline

# Preprocessing
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
# Metrics 
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ML Models
import lightgbm as lgb
from lightgbm import LGBMRegressor 
import xgboost as xg 
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.linear_model import LinearRegression

# Ignore Warnings 
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv("Model 2.csv")

dataset.head(5)

# Split into features (X) and target (y)
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=14)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.model_selection import cross_val_score

cv_scores = []

##% evaluateRegressor
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_scor
def evaluateRegressor(true,predicted,message = "Test set"):
    RMSE = mean_squared_error(true,predicted,squared = False)
    R_squared = r2_score(true,predicted)
    print(message)
    print("RMSE:", RMSE)
    print("R-squared:", R_squared)

##% Initial Models
# import lightgbm as lgb


LGBMReg = lgb.LGBMRegressor(random_state=0).fit(X_train, y_train)

# Evaluate the performance of the model on a separate test set
y_pred = LGBMReg.predict(X_test)
test_score = mean_squared_error(y_test, y_pred)


print('Test score:', test_score)

# Predict on the training and testing data
y_train_pred = LGBMReg.predict(X_train)
y_test_pred = LGBMReg.predict(X_test)
# Calculate the training and testing error metrics
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
nse_train = 1 - mean_squared_error(y_train, y_train_pred) / np.var(y_train)
r2_train = r2_score(y_train, y_train_pred)
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
nse_test = 1 - mean_squared_error(y_test, y_test_pred) / np.var(y_test)
r2_test = r2_score(y_test, y_test_pred)

print("LightGBM Regressor:")
print("Train RMSE: {:.4f}".format(rmse_train))
print("Train NSE : {:.4f}".format(nse_train))
print("Train R^2 : {:.4f}".format(r2_train))
print("Test RMSE : {:.4f}".format(rmse_test))
print("Test NSE  : {:.4f}".format(nse_test))
print("Test R^2  : {:.4f}".format(r2_test))

pd.DataFrame(y_train).to_csv('/content/actualTrain.csv', index=False, header=False)
pd.DataFrame(y_train_pred).to_csv('/content/predictTrain.csv', index=False, header=False)
pd.DataFrame(y_test).to_csv('/content/actualTest.csv', index=False, header=False)
pd.DataFrame(y_test_pred).to_csv('/content/predictTest.csv', index=False, header=False)


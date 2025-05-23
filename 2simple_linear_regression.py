# -*- coding: utf-8 -*-
"""2simple_linear_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VDJyyeNw3-Wpe-XI53hfcsEjiWyaSZgz

# Simple Linear Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

#LinearRegression is the class from the scikitlearn library and then linear_model module
from sklearn.linear_model import LinearRegression
#Creating the instance(object) of the class, here regressor is the instance/object
regressor = LinearRegression()
#Here fit() is the method of the class LinearRegression
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""

#Predicting the salary for the test set
#y_test contains the real salary, whereas the y_pred contains the predicted salary
y_pred = regressor.predict(X_test)

"""## Visualising the Training set results"""

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Test set results"""

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""##Making a single prediction (for example the salary of an employee with 12 years of experience)"""

print(regressor.predict([[12]]))

"""Therefore, our model predicts that the salary of an employee with 12 years of experience is $ 138967,5.

Important note: Notice that the value of the feature (12 years) was input in a double pair of square brackets. That's because the "predict" method always expects a 2D array as the format of its inputs. And putting 12 into a double pair of square brackets makes the input exactly a 2D array. Simply put:

12→scalar

[12]→1D array

[[12]]→2D array
"""


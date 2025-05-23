# -*- coding: utf-8 -*-
"""1data_preprocessing_tools.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13IvIV-xaKrgBkDtNrbnFZGo_igbW_kq5

# Data Preprocessing Tools

## Importing the libraries
"""

import numpy as np # Helps in working with arrays
import matplotlib.pyplot as plt #Plotting charts
import pandas as pd #Importing data and also the making of matrix

"""## Importing the dataset"""

dataset = pd.read_csv('Data.csv')
#iloc is locate indexes, and : means everything(range), and [rows, columns],
#lower bound values are included and upper bound are not
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

"""## Taking care of missing data"""

from sklearn.impute import SimpleImputer
#sklearn is scikitlearn
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
#nan is missing or empty value
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)

"""## Encoding categorical data

### Encoding the Independent Variable
"""

#Something like .compose/.preprocessing is called modules
#One hot encoding is used to transform the non numerical columns into the numberical rows,
#here for this dataset we'd countries(3) column with string, so they got converted to the 1's and 0's.
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""### Encoding the Dependent Variable"""

# this is same as above, but this is just for the dependent variable, here the target column with true and false.
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

"""## Splitting the dataset into the Training set and Test set"""

#0.2 is 20%, so the rest is training set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

print(X_train)

print(X_test)

print(y_train)

print(y_test)

"""## Feature Scaling"""

# To avoid some features to be dominated by the others, not applied to all the models
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)

print(X_test)
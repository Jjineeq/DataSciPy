from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 
 
diabetes = datasets.load_diabetes()
regr = linear_model.LinearRegression() 

X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target,
                                                    test_size = 0.2) 
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)

print("평균제곱 오차(MSE): ",mean_squared_error(y_test, y_pred))
print(y_pred)
print(y_test)


from data_preprocessing import X_train, X_test, y_train, y_test
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import config as cfg
import dvc.api

#Read params
params=dvc.api.params_show()
degrees = params['polyreg']['degrees']

#Performing the regression
poly_r2=[]
for element in degrees:

    poly_model = PolynomialFeatures(degree=element)

    poly_x_values = poly_model.fit_transform(X_train.values)
    poly_model.fit(poly_x_values, y_train)

    regression_model = LinearRegression()
    regression_model.fit(poly_x_values, y_train)

    poly_X_values = poly_model.fit_transform(X_test.values)
    y_pred = regression_model.predict(poly_X_values)

    r2_1=r2_score(y_train, regression_model.predict(poly_x_values))
    r2_2=r2_score(y_test, y_pred)

    poly_r2.append([element,r2_1, r2_2])

np.save(cfg.POLYREGPATH, poly_r2)
from data_preprocessing import X_train, X_test, y_train, y_test
import config as cfg
from statsmodels.formula.api import ols
import pandas as pd
from sklearn.metrics import r2_score
import numpy as np

#Create the model
model = ols('suicide_number ~ population + C(gender) + C(age_group) + C(country) + gdp_per_capita', data=pd.concat([X_train, y_train], axis=1))
fitted_model = model.fit()

#Predict values
y_pred = fitted_model.predict(X_test)

#Calculate r2 for train and test sets
ols_r2_1=fitted_model.rsquared
ols_r2_2=r2_score(y_test, y_pred)

#Save results as an array
Y=np.array([ols_r2_1, ols_r2_2])
np.save(cfg.OLSREGPATH, Y)
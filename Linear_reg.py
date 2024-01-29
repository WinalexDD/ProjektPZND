from sklearn.linear_model import LinearRegression
from data_preprocessing import X_train, X_test, y_train, y_test
from sklearn.metrics import r2_score
import config as cfg
import numpy as np

#Create the model
model = LinearRegression()
model.fit(X_train, y_train)

#Calculate r2 for train and test sets
r2_train=r2_score(y_train, model.predict(X_train))
r2_test=r2_score(y_test, model.predict(X_test))

#Save results as an array
results=np.array([r2_train, r2_test])
np.save(cfg.LINREGPATH, results)
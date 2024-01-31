import numpy as np
import config as cfg
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Get data
data = np.load(cfg.PROCESSEDDATAPATH + '.npy', allow_pickle=True)
X_train, X_test, y_train, y_test = data[0], data[1], data[2], data[3]

# Create the model
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate r2 for train and test sets
r2_train = r2_score(y_train, model.predict(X_train))
r2_test = r2_score(y_test, model.predict(X_test))

# Save results as an array
results = np.array([r2_train, r2_test])
np.save(cfg.LINREGPATH, results)

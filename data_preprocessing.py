import data_clearing
import config as cfg
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import dvc.api

# Read params
params = dvc.api.params_show()
null_threshold = params['Datapick']['null_threshold']
country_name = params['Datapick']['country_name']
year = params['Datapick']['year']
random_state = params['Datapick']['random_state']
test_size = params['Datapick']['test_size']

# Get Data
dataframe = pd.read_csv(cfg.DATA_PATH)
dataframe = data_clearing.column_adapt(dataframe)
dataframe = data_clearing.check_null(dataframe, null_threshold)

# Save this dataframe for plotting
dataframe.to_csv(cfg.DATA_FOR_PLOT)

# Check if we want more selective data
if country_name:
    dataframe = data_clearing.custom_country(dataframe, country_name)
if year != 0:
    dataframe = data_clearing.custom_year(dataframe, year)

# Change categorical values to numerical
for name in data_clearing.num_vs_cat(dataframe)[0]:
    dataframe[str(name)].replace(dataframe[str(name)].unique(),
                                 list(range(len(dataframe[str(name)].unique()))), inplace=True)

# Divide dataset into train and test sets
X = dataframe.drop(['suicide_number'], axis=1)
y = dataframe['suicide_number']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Save final dataset for regression
np.save(cfg.PROCESSED_DATA_PATH, np.array([X_train, X_test, y_train, y_test], dtype=object))

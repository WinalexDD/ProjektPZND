import data_clearing
import config as cfg
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import dvc.api

#Read params
params=dvc.api.params_show()
null_threshold = params['Datapick']['null_threshold']
country_name = params['Datapick']['country_name']
year = params['Datapick']['year']
random_state= params['Datapick']['random_state']

#Getting Data
dataframe=pd.read_csv(cfg.DATAPATH)
dataframe=data_clearing.column_adapt(dataframe)
dataframe=data_clearing.check_null(dataframe, null_threshold)

#Checking if we want more selective data
if country_name:
    dataframe = data_clearing.custom_country(dataframe, country_name)
if year != 0:
    dataframe = data_clearing.custom_year(dataframe, year)

#Changing categorical values to numerical
for name in data_clearing.num_vs_cat(dataframe)[0]:
    dataframe[str(name)].replace(dataframe[str(name)].unique(),list(range(len(dataframe[str(name)].unique()))), inplace=True)

#Diving dataset for train and test sets
X = dataframe.drop(['suicide_number'], axis =1)
y = dataframe['suicide_number']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=random_state)

#Saving updating dataset
np.save(cfg.PROCESSEDDATAPATH, np.array([X_train, X_test, y_train, y_test], dtype=object))
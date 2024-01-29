import data_clearing
import config
import pandas as pd
import dvc.api


#Read params
params=dvc.api.params_show()
null_threshold = params['Datapick']['null_threshold']
country_name = params['Datapick']['country_name']
year = params['Datapick']['year']

#Getting Data
dataframe=pd.read_csv(config.DATAPATH)
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















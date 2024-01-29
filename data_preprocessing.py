import data_clearing
import config
import pandas as pd

null_threshold=1000
country_name=''
year=0

#Getting Data
dataframe=pd.read_csv(config.DATAPATH)
dataframe=data_clearing.column_adapt(dataframe)
dataframe=data_clearing.check_null(dataframe, null_threshold)

#Checking if we want more selective data
if country_name:
    dataframe = data_clearing.custom_country(dataframe, country_name)
if year != 0:
    dataframe = data_clearing.custom_year(dataframe, year)













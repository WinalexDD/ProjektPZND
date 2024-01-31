import numpy as np
import pandas as pd
import config as cfg
from tabulate import tabulate
import dvc.api

#Read params
params = dvc.api.params_show()
country_name = params['Datapick']['country_name']
year = params['Datapick']['year']

#Load saved results
linreg=np.load(cfg.LINREGPATH + '.npy')
olsreg=np.load(cfg.OLSREGPATH + '.npy')
polyreg=np.load(cfg.POLYREGPATH + '.npy')

#Create dataframe to present results
dataframe=pd.DataFrame(data={'Linear Regression': linreg, 'OLS Model': olsreg}, index=['r2 on train-set', 'r2 on test-set'])
for number in range(len(polyreg)):
    dataframe.insert(2+number, "Polymional Regression degree " + str(int(polyreg[number][0])), [polyreg[number][1], polyreg[number][2]])

#Save the dataframe as csv
dataframe.to_csv(cfg.RESULTPATH)

#Prepare the titles of columns
table_titles=list(dataframe.keys())
if country_name and year != 0:
    table_titles.insert(0, "country&year=" + str(country_name)+ " " + str(year))
elif year != 0:
    table_titles.insert(0, "year=" + str(year))
elif country_name:
    table_titles.insert(0, "country=" + str(country_name))
else:
    table_titles.insert(0, "All data")

# Print and save the table with results
table=tabulate(dataframe, headers=table_titles, tablefmt='psql')
print(table)
with open(cfg.TABLEPATH, 'w') as f:
    f.write(tabulate(table))
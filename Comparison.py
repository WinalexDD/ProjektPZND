import numpy as np
import pandas as pd
import config as cfg
from tabulate import tabulate

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

#Print the dataframe with results
print(tabulate(dataframe, headers='keys', tablefmt='psql'))
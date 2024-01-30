from data_visualization import *
from data_clearing import *
import pandas as pd
import dvc.api

#Load Data
result_dataframe=pd.read_csv(cfg.RESULTPATH)
dataframe=pd.read_csv(cfg.DATAFORPLOT)

#Read params
params=dvc.api.params_show()
variable1 = params['plotting']['scatter_plot_var1']
variable2 = params['plotting']['scatter_plot_var2']

#Check if params meet the conditions
for var in [variable1, variable2]:
    if not type(var) is str:
        raise TypeError("Only strings are allowed")
    if var not in num_vs_cat(dataframe)[1]:
        raise TypeError("Variables need to be numerical")

#Do the plotting
characteristics_chart(dataframe)
heat_map(dataframe)
scatter_plot(dataframe,variable1,variable2)
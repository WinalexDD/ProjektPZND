from data_visualization import *
from data_clearing import *
import pandas as pd
import dvc.api
import config as cfg

#Load Data
dataframe=pd.read_csv(cfg.DATAFORPLOT, index_col=0)

#Read params
params=dvc.api.params_show()
variable1 = params['plotting']['scatter_plot_var1']
variable2 = params['plotting']['scatter_plot_var2']
variable3 = params['plotting']['histogram_var']
bins = params['plotting']['histogram_bins']

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
histogram(dataframe, variable3, bins)
time_series_plot(dataframe)
import matplotlib.pyplot as plt
from pandas.plotting import table
import config as cfg
import seaborn as sb

from data_preprocessing import dataframe
def characteristics_chart(dataframe):
    "Function that creates a table of statistical features of our cleared data and saves it in folder for data visualization"

    desc = dataframe.describe()
    plot = plt.subplot(111, frame_on=False)
    plot.xaxis.set_visible(False)
    plot.yaxis.set_visible(False)
    table(plot, desc, loc='center')

    plt.savefig(cfg.DIAGRAMPATH + '\desc_plot.png')
    plt.close()

def heat_map(dataframe):
    "Function that creates a heatmap of correlations in our data"

    fig, ax = plt.subplots(figsize=(12, 10))
    corr = dataframe.corr()
    sb.heatmap(corr, cmap="Blues", annot=True, ax=ax)
    fig.savefig(cfg.DIAGRAMPATH+r"\heat_map.png")


def scatter_plot(dataframe, variable1:str, variable2:str):
    "Function that creates a scatter plot of two chosen variables"

    plt.figure(figsize=(12,7))
    plt.scatter(dataframe[variable1],dataframe[variable2])
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.savefig(cfg.DIAGRAMPATH+'\scatter_plot('+ variable1 +','+ variable2 + ').png')
    plt.close()

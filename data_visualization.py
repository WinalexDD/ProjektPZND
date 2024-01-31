import matplotlib.pyplot as plt
from pandas.plotting import table
import config as cfg
import seaborn as sb


def characteristics_chart(dataframe):
    """Function that creates a table of statistical features of our cleared data and saves it in folder for data
    visualization"""

    desc = dataframe.describe()
    plot = plt.subplot(frame_on=False)
    plot.xaxis.set_visible(False)
    plot.yaxis.set_visible(False)
    table(plot, desc, loc='center')

    plt.savefig(cfg.DIAGRAM_PATH + r'\desc_plot.png')
    plt.close()


def heat_map(dataframe):
    """Function that creates a heatmap of correlations in our data"""

    fig, ax = plt.subplots(figsize=(12, 10))
    corr = dataframe.corr()
    sb.heatmap(corr, cmap="Blues", annot=True, ax=ax)
    fig.savefig(cfg.DIAGRAM_PATH + r"\heat_map.png")
    plt.close()


def scatter_plot(dataframe, variable1: str, variable2: str):
    """Function that creates a scatter plot of two chosen variables"""

    plt.figure(figsize=(12,7))
    plt.scatter(dataframe[variable1],dataframe[variable2])
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.savefig(cfg.DIAGRAM_PATH + r'\scatter_plot.png')
    plt.close()


def histogram(dataframe, variable3: str, bins: int):
    """Function that creates a histogram of a chosen variable with customize bins"""

    plt.hist(dataframe[variable3], bins=bins)
    plt.xlabel(variable3)
    plt.ylabel("Amount")
    plt.savefig(cfg.DIAGRAM_PATH + r"\histogram.png")
    plt.close()


def time_series_plot(dataframe):
    """Function that creates a plot of number of suicides over the years"""

    plt.figure(figsize=(20, 10))
    sb.pointplot(x='year', y='suicide_number', data=dataframe)
    plt.xlabel('year')
    plt.ylabel('number of suicides')
    plt.savefig(cfg.DIAGRAM_PATH + r"\time_series_plot.png")
    plt.close()

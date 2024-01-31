def column_adapt(dataframe):
    """Function that drops columns that will not be useful for our project and renames the rest for better clarity"""

    dataframe.drop(["country-year", "suicides/100k pop", " gdp_for_year ($) ", "generation"], axis=1, inplace=True)
    dataframe.columns = ["country", "year", "gender", "age_group",
                         "suicide_number", "population", "hdi", "gdp_per_capita"]
    return dataframe


def check_null(dataframe, threshold):
    """Function that checks whether any of our data contains NaNs, and removes the columns if they have more NaNs
    than given threshold"""

    isnull = dataframe.isnull().sum()
    for i in range(len(isnull)):
        if isnull[i] > threshold:
            dataframe.drop([dataframe.columns[i]], axis=1, inplace=True)
    return dataframe


def custom_country(dataframe, country: str):
    """Function that picks our data only for specified country"""

    filtered_dataframe = dataframe[dataframe['country'] == country]
    return filtered_dataframe


def custom_year(dataframe, year: int):
    """Function that picks our data only for specified year"""

    filtered_dataframe = dataframe[dataframe['year'] == year]
    return filtered_dataframe


def num_vs_cat(dataframe):
    """Function that separates our columns by type of data they contain, either numerical or categorical"""

    categorical = []
    numerical = []
    for i in range(len(dataframe.columns)):
        if dataframe.dtypes[i] == 'object':
            categorical.append(dataframe.columns[i])
        else:
            numerical.append(dataframe.columns[i])
    return categorical, numerical

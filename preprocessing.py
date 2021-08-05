import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

def read_data(datasheet):
    dataframe = pd.read_csv(
        datasheet, 
        parse_dates = {'time': ['year', 'month', 'day', 'hour']}, 
        date_parser = lambda year, month, day, hour : 
            pd.to_datetime(year+' '+month+' '+day) 
            + pd.to_timedelta(hour+'hour', unit='hours'),
        index_col = 'time',
        ).drop('No', axis=1)

    return dataframe


def clean_data(dataframe):
    # select the numerical part of the dataframe
    num_df = dataframe.select_dtypes(include=["number"])
    numerical_columns = num_df.columns

    # detect outliers based on rolling standard deviation
    rolling = num_df.rolling(window=20)
    dataframe[numerical_columns] = num_df.mask((num_df - rolling.mean()).abs() > (3 * rolling.std()))

    # fill null values in numerical data with rolling mean and ite
    dataframe[numerical_columns] = dataframe[numerical_columns].fillna(num_df.rolling(20,min_periods=1).mean())
    dataframe[numerical_columns] = dataframe[numerical_columns].interpolate(method='bfill')

    # select the non numerical part of the dataframe and fill nan wtih previous value
    str_df = dataframe.select_dtypes(exclude=["number"])
    string_columns = str_df.columns
    dataframe[string_columns] = dataframe[string_columns].fillna(method='ffill')

    # print(dataframe.isnull().sum())
    return dataframe

def preprocess(datafram):
    pass 

if __name__ == '__main__':
    datasheet = 'datasheets/Air_Quality/PRSA_Data_Aotizhongxin_20130301-20170228.csv'
    clean_data(datasheet)
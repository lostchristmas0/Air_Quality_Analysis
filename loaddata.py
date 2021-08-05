import sqlalchemy as sa
import pandas as pd
from preprocessing import clean_data, read_data
import pymysql, os

def create_database():
    sqlEngine = sa.create_engine('mysql+pymysql://root:@127.0.0.1/airquality', pool_recycle=3600)
    dbConnection = sqlEngine.connect()

    dataset_directory = 'datasheets/Air_Quality/'
    datasheets = os.listdir(dataset_directory)
    dataframe = pd.DataFrame()
    for file in datasheets:
        dataframe = pd.concat([dataframe, read_data(dataset_directory+file)])
    dataframe = clean_data(dataframe)
    print(dataframe.head())
    print(dataframe.isnull().sum())

    try:
        frame = dataframe.to_sql('airdata', dbConnection, if_exists='fail')
    except ValueError:
        print('table already exists')
        pass
    finally:
        dbConnection.close()

create_database()
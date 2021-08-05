import sqlalchemy as sa
import pymysql
import os, sys
import pandas as pd        

def main():
    sqlEngine = sa.create_engine('mysql+pymysql://root:@127.0.0.1/airquality', pool_recycle=3600)
    dbConnection = sqlEngine.connect()

    try:
        sql = """
            select time 
            from airdata 
            where station = 'Gucheng' and time < '2014-01-01 00:00:00'
                and SO2 > 
                    all(
                        select avg(SO2) 
                        from airdata 
                        where station = 'Gucheng' and time < '2014-01-01 00:00:00'
                        )
        """
        new_frame = pd.read_sql(
            sql,
            dbConnection
        )
        print(new_frame)
    finally:
        dbConnection.close()

if __name__ == '__main__':
    main()
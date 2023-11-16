import pandas as pd
from sqlalchemy import create_engine
import time
from api import db_params


class PG_api:
    def __init__(self, db_params):
        host, login, password, database = db_params()
        self.host = host
        self.login = login
        self.password = password
        self.database = database
        self.engine = create_engine(f'postgresql+psycopg2://{self.login}:{self.password}@{self.host}/{self.database}')

    def lead_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            print(start)
            res = func(*args, **kwargs)
            end = time.time()
            result = end - start
            print(f'Время выполнения: {result}')
            return result
        return wrapper
    
    @lead_time
    def create_table(self, df, dbname):
        df.to_sql(dbname, self.engine, index=False)
    
    @lead_time
    def delete_from_table(self, table_name, value):
        query = f"DELETE FROM {table_name} WHERE {value}"
        with self.engine.begin() as connection:
            connection.execute(query)
    
    @lead_time
    def truncate_table(self, name):
        query = f"TRUNCATE TABLE {name}"
        with self.engine.begin() as connection:
            connection.execute(query)
    
    @lead_time
    def read_sql(self, query):
        df = pd.read_sql_query(query, self.engine)
        print(df)
        return df
    
    @lead_time
    def insert_sql(self, db, name, mode):
        db.to_sql(name, self.engine, if_exists=mode, index=False)
    
    @lead_time
    def execute(self, query):
        with self.engine.begin() as connection:
            res = connection.execute(query)
            return res


api = PG_api(db_params)
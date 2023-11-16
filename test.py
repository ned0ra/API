from main import PG_api
from api import db_params
import pandas as pd

api = PG_api(db_params=db_params)

    #create table
# df = pd.DataFrame({"id": [1, 2, 3, 4], "Juice": ["Banana", "Tomato", "Strawberry","Pineapple"]})
# api.create_table(df, "juice")

    #delete from table
# api.delete_from_table('juice', 'id=4')

    # truncate table
# api.truncate_table('juice')

    #read sql
# data=api.read_sql('SELECT * FROM juice')
# print(data)

    #insert sql
# values=pd.DataFrame({"id":[4],"Juice":"Pineapple"})
# api.insert_sql(values,"juice",mode="append")

    # execute
# query = "SELECT * FROM juice"
# api.execute(query=query)
# data = api.read_sql(query=query)
# print(data)

import pandas as pd
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.project1
collection = db.project1
#records = collection.find()
print(collection)
for record in collection.find().limit(1):
    print(record)
cursor = collection.find()

    # Expand the cursor and construct the DataFrame
#df =  pd.DataFrame(list(cursor))
df =  pd.DataFrame(list(collection.find()))
print(df.head())
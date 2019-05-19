from pymongo import MongoClient
try:
    conn = MongoClient()
    print('connected Succesfully')
except:
    print('Couldn\'t connect')

db = conn.code

# Created or Switched to collection names: my_gfg_collection
collection = db.mycode
lang=""
title =""
code = ""
# Insert Data
def insert_code(title , lang , code):
    collection.insert({'title' : title,'lang' : lang,'code' : code})
    print("Data inserted with title ", title)

insert_code('HIii','cpp','hello world')

# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)
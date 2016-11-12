import sys
import pymongo
from pymongo import MongoClient

connection=MongoClient("mongodb://localhost")

db=connection.test
users=db.users

doc={'firstname':"Dilip",'lastname':"Dwarak"}
print (doc)
print ("About to insert the document")

try:
    users.insert_one(doc)
except Exception as e:
     print("Insert failed:", e)

print(doc)
print("Inserting again")

try:
    users.insert_one(doc)
except Exception as e:
    print("Second insert failed:",e)

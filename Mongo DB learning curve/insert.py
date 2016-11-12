import sys
import pymongo
from pymongo import MongoClient


#establish a connection to the database
connection=MongoClient("mongodb://localhost")
 

#get a handle to the school database
db=connection.school
people=db.people

def insert():
    print "insert, reporting for duty"

dilip={"name":"Dilip Dwarak","company":"KSU","interests":['gaming','reading']}
pradyumna={"_id":"dwarak","name":"Pradyumna Dwarak","company":"KSU","interests":['programming','debating']}

try:
    people.insert(dilip)
    people.insert(pradyumna)
except:
    print "Unexpected error:",sys.exc_info()[0]

print (dilip)
print (pradyumna)

insert()
	
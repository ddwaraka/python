import sys
import pymongo
from pymongo import MongoClient


#establish a connection to the database
connection=MongoClient("mongodb://localhost")
 

#get a handle to the school database
db=connection.school
scores=db.scores

#def find():
print "Find, reporting for duty"
query={'type':'exam', 'score':{'$gt':50,'$lt':70}}
     
try:
    iter = scores.find(query)
except:
    print "Unexpected error", sys.exc_info()[0]
     
sanity=0
for doc in iter:
    print doc
    sanity +=1
    if (sanity>10):
        break
import sys
import pymongo
from pymongo import MongoClient


#establish a connection to the database
connection=MongoClient("mongodb://localhost")
 

db=connection.school
scores=db.scores

def find():
    print "find, reporting for duty"
    query = {}
    try:
        cursor=scores.find(query).sort('student_id',pymongo.ASCENDING).skip(4).limit(1)
    except:
	    print "Unexpected error:", sys.exec_info()[0]
    
    for doc in cursor:
	    print doc
		
find()
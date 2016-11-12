import sys 
import json
import urllib2
import pymongo
from pymongo import MongoClient

#connect to mongo
connection=MongoClient("mongodb://localhost")

#get a handle to the reddit database
db=connection.reddit
stories=db.stories

def find():
    print "find, reporting for duty"
    query = {'title':{'$regex':'NASA'}}
    projection={'title':1,'id':0}

    try:
        iter=scores.find(query, projection)

    except:
        print "Unexpected error:", sys.exec_info()[0]

    sanity=0
    for doc in iter:
        print doc
        sanity+=1
        if (sanity>10):
	        break
    print doc	   

find()
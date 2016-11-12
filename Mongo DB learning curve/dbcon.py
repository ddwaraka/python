import sys
import pymongo
from pymongo import MongoClient


#establish a connection to the database
connection=MongoClient("mongodb://localhost")
 

#get a handle to the school database
db=connection.school
scores=db.scores

def find():
   print "Find, reporting for duty"
   query={'type':'exam'}

   try:
       cursor=scores.find(query)
	
   except:
       print "Unexpected Error:", sys.exc_info()[0]
	
   sanity=0
   for doc in cursor:
       print doc
       sanity +=1
       if (sanity >10):
           break

def find_one():
    print "find one, reporting for duty"
    query ={'student_id':10}   #Single quote is compulsory
    
    try:
        doc=scores.find_one(query)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        
    print doc
    
find() #Specify whuch function you want to call
import datetime
import sys
import pymongo
from pymongo import MongoClient


#establish a connection to the database
connection=MongoClient("mongodb://localhost")

def remove_review_date():
    print "\n\nremoving all review dates"
	
	#get a handle to the school database
    db=connection.school
    scores=db.scores
    try:
	    scores.update({},{'$unset':{'review_date':1}},multi=True)
    except:
	    print "Unexpected error:", sys.exc_info()[0]
 
def using_save():
      
	  #get a handle to the school db
	  db=connection.school
	  scores=db.scores
	  
	  print "updating record using save"
	  
	  try:
	      #get the doc
		  score=scores.find_one({'student_id':1,'type':'homework'})
		  print "before:", score
		  
		  #add a review date
		  score['review date']=datetime.datetime.utcnow()
		  
		  #update the record with convenience method
		  scores.save(score)
		  score=scores.find_one({'student_id':1,'type':'homework'})
		  print "after",score
	  except:
	      print "Unexpected error:", sys.exc_info()[0]
	      raise
		  
#performs wholesale replacement of document
def using_update():
    print "updating record using update"
	#get a handle to the school database
    db=connection.school
    scores=db.scores
	
    try:
	    #get the doc
	    score=scores.find_one({'student_id':1,'type':'homework'})
	    print "before:",score
		
		#add a review date
	    score['reviewdate']=datetime.datetime.utcnow()
		
		#update the record with update. Noth that there is an _id but DB is ok with that
		#because it matches what was there
	    scores.update({'student_id':1,'type':'homework'},score)
		
	    score=scores.find_one({'student_id':1,'type':'homework'})
	    print "after:", score
    except:
	    print "Unexpected error:", sys.exc_info()[0]
	    raise

def using_set():
    print "updating reccord using set"
	#get a handle to the school database
    db=connection.school
    scores=db.sccores
	
    try:
	    #get the doc
		score=scores.find_one({'student_id':1,'type':'homework'})
		print "before:", score
		
		#update using set
		scores.update({'student_id':1, 'type':'homework'},
		{'$set':{'review_date':datetime.datetime.utcnow()}})
		
		score=scores.find_one({'student_id':1,'type':'homework'})
		print "after",score
    except:
	    print "Unexpected error:",sys.exc_info()[0]
		
remove_review_date()
using_save()
remove_review_date()
using_update()
remove_review_date()
using_set()

	
		
	
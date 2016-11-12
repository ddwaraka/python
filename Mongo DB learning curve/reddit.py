import json
import urllib2
import pymongo
from pymongo import MongoClient

#connect to mongo
connection=MongoClient("mongodb://localhost")

#get a handle to the reddit database
db=connection.reddit #creating the DB called Reddit
stories=db.stories #creating the collection called stories

#get the reddit homepage
reddit_page=urllib2.urlopen("https://www.reddit.com/r/technology/.json")

#parse the json into python objects
parsed=json.loads(reddit_page.read())

#iterate through every news item on the page
for item in parsed['data']['children']:
                stories.insert(item['data'])
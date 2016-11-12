import pymongo
from pymongo import MongoClient
import sys

class User:
    def __init__(self, db):
	    self.db=db
	    self.users=self.db.users

    #Validate User
    def validate_login(self, username, password):
        user = None
        try:
            user = self.users.find_one({'_id': username})
        except:
            print "Username not found"	
        
        if user is None:
            print "User not in database"
            return None
        
        try:
            pas = self.users.find_one({'password':password})

            if pas['password'] != password:
                print "Password does not match"
                return False
            else:
                return True
        except:
            return False
        
        
    #Creates a new user in the collection
    def add_user(self, username, password, email):
        user={'_id':username, 'password':password, 'email':email}
        print self, username, password, email
        #print user._id, user.password, user.email
        try:
            self.users.insert(user)
        except pymongo.errors.OperationFailure:
            print "Error"
        except pymongo.errors.DuplicateKeyError as e:
            print "Username is already taken"
        #except pymongo.errors.DuplicateKeyError as e:
            #print "Email id is already in use. Please login"
            return False
        
        return True

    def find_tasks(self,username):
        print username
        data = self.users.find({'_id':username},{"tasks":1,"_id":0})
        return data
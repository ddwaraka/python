import pymongo
import userdata
import bottle
from bottle import run
from bottle import get, put, post, request, template
from bottle import static_file


username = ""
#HomePage
@bottle.route('/')
def home_page():
	return bottle.template('home')


#Login Page
@bottle.route('/login')
def login():
	return bottle.template('login', dict(username="", password="",login_error=""))



#*************************************************#
#Processing the Login Request 
#This section is under concstruction
@bottle.post('/login')
def process_login():
    global username

    username=bottle.request.forms.get("username")
    password=bottle.request.forms.get("password")

    print "user submitted", username, "pass: ", password

    user_record=users.validate_login(username, password)
    if user_record:
        bottle.redirect("/welcome")
    else:
        bottle.redirect("/wrong")

#New User Register Page
@bottle.get('/new')
def new():
	return bottle.template('new', dict(username="", password="", pass1_error="", email="", uname_error="", email_error="", pass2_error=""))

#Process Signing Up
@bottle.post('/new')
def process_new():  
	global username
	email = bottle.request.forms.get("email")
	username = bottle.request.forms.get("username")
	password = bottle.request.forms.get("password")
	verify = bottle.request.forms.get("verify")
	print email, username, password
	users.add_user(username, password, email)
	bottle.redirect("/welcome")
   
 
@bottle.route('/welcome')
def welcome():
	#return
	global username
	return bottle.template('welcome',{'username':username})
	
@bottle.route('/listview')
def listview():
    global tasks,username
    data=users.find_tasks(username)
    for i in data:
        print i['tasks']
        return bottle.template('listview',{'username':username, 'tasks':i['tasks']})
		
@get('/static/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='static')

@bottle.route('/logout')
def logout():
	return bottle.template('logout')
	
@bottle.route('/wrong')
def wrong():
	return bottle.template('wrong')

@bottle.route('/delete')
def delete():
	return bottle.template('delete')
	
#About Me Page
@bottle.route('/about')
def about():
	return bottle.template('about')

@bottle.route('/newpost')
def newpost():
	return bottle.template('newpost')






connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.blog

users = userdata.User(database)
#sessions = sessionDAO.SessionDAO(database)


bottle.debug(True)
run(reloader=True)
bottle.run(host='localhost',port=8080)
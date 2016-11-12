import bottle 
from bottle import run

@bottle.route('/')
def home_page():
	return "<html><title></title><body>Hello World!\n</body></html>"
	
@bottle.route('/testpage')
def test_page():
	return("This is a Test Page")

	
bottle.debug(True)
run(reloader=True)
bottle.run(host='localhost',port=8080)
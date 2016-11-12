import bottle
from bottle import run

@bottle.route('/')
def home_page():
    mythings=['apple','orange','banana','peach']
    return bottle.template('hello_world', username="Dilip", things=mythings)
	 
@bottle.route('/page2')
def sec_page():
    mythings2=['laptop','PS4','smartphone']
    return bottle.template('hello_world', username="Dilip", things=mythings2)


bottle.debug(True)
run(reloader=True)
bottle.run(host='localhost',port=8080)
											 
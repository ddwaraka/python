import bottle
from bottle import run

@bottle.route('/')
def home_page():
    mythings=['apple','orange','banana','peach']
    return bottle.template('fruitsel', username="Dilip", things=mythings)
    

@bottle.post('/favourite_fruit')
def favourite_fruit():
    fruit=bottle.request.forms.get("fruit")
    if (fruit==None or fruit==""):
        fruit="No fruit Selected"
    
    return bottle.template('fruit_selection.tpl',{'fruit':fruit})
     

bottle.debug(True)
run(reloader=True)
bottle.run(host='localhost',port=8080)
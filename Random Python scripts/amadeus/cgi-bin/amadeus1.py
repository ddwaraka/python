
from amadeus import Flights
import cgi, cgitb

form = cgi.FieldStorage()

origin = form.getvalue('origin')
destination = form.getvalue('destination')
departure_date = form.getvalue('date')
max_price = form.getvalue('max_price')



flights=Flights('as954p7KMzRYH5WN6JBAUz3Z04zkGDQH')
resp = flights.inspiration_search(origin='origin', 
destination='destination', departure_date='date', 
max_price='max_price') 
print resp
   
   
   

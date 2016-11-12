
from amadeus import Flights
import cgi, cgitb
import bottle



'''origin = form.getvalue('origin')
destination = form.getvalue('destination')
departure_date = form.getvalue('date')'''
max_price = form.getvalue('max_price')

print ("content-type:text/html \r\n\r\n")
print ('<HTML>')
print ('<HEAD>')
print ('<TITLE>SAMPLE CGI PROGRAM</TITLE>')
print ('</HEAD>')
print ('<BODY>')


flights=Flights('as954p7KMzRYH5WN6JBAUz3Z04zkGDQH')
resp = flights.inspiration_search(origin='origin', 
destination='destination', departure_date='date', 
max_price='max_price') 
print resp

print "Hello World %s"%max_price
print ('</BODY>')
print ('</HTML'>)
   
   
   

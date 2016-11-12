
from amadeus import Flights
import cgi, cgitb

first_name=form.getvalue('first_name')
last_name=form.getvalue('last_name')

print ("content-type:text/html \r\n\r\n")
print ('<HTML>')
print ('<HEAD>')
print ('<TITLE>SAMPLE CGI PROGRAM</TITLE>')
print ('</HEAD>')
print ('<BODY>')
print (first_name, last_name)
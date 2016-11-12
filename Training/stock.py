import re
import urllib2
from bs4 import BeautifulSoup
import requests
import smtplib



company_url = urllib2.urlopen('http://money.rediff.com/companies/Gvk-Power-Infrastructure-Ltd/15130101?src=gain_lose').read()

#[^>] means "match any character that ISN'T >"
#and there's a * after it, so [^>]* means "Match any character not > zero or more times."
#Then you have another literal >, which is matched.
#Then you have ([^<]*]) which means "match anything not < zero or more times and put it into a group."
price = float(re.search('<span id="ltpid"[^>]*>([^<]*)', company_url).group(1))

print price


#Using a HTML Parser

#.content gets text of the page
html = requests.get('http://money.rediff.com/companies/Tata-Motors-Ltd/10510008').content

#For debugging only
#print html
#Calling the BS on html
soup = BeautifulSoup(html, "html.parser")
rate = float(soup.find(id='ltpid').get_text())
print rate


#content = str(price) + "\n" + str(rate)

#mail = smtplib.SMTP('smtp.gmail.com', 587)

#mail.ehlo()

#mail.starttls()

#mail.login('sample@email.com', 'password')

#mail.sendmail('sample@email.com','receiver@email.com', content)

#mail.close()
import smtplib

subject = "Hello!"

body = "This message was sent with Python's smtplib."

message = 'Subject: %s\n\n%s' % (subject, text)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('email', 'password')
server.sendmail('sender_email', 'reciever_email', message)
server.quit()


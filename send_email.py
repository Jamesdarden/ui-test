import smtplib
#from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Sender's Gmail account
sender_email = "<sender_email>"
sender_password = "<sender_password>"

#Receiver's Gmail account
reciever_email = "<reciever_email>"

#Message
message = MIMEText("This is a message body")

#Subject
subject = "This is a message subject"

#Connect to SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

#Start TLS (Transport Layer Security)
smtp_server.starttls()

#Login to Gmail
smtp_server.login(sender_email, sender_password)

#Send email
smtp_server.sendmail(sender_email, reciever_email, message.as_string())

#Terminate session
smtp_server.quit()
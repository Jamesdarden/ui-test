import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()



port = 465  # For SSL
password =  os.environ.get('password')

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "developementlocaltesting@gmail.com"  # Enter your address
receiver_email = "jamesdardenjr@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("developementlocaltesting@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
    

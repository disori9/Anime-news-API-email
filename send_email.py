import smtplib
import ssl
import os

def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465

    username = "violetori99@gmail.com"
    receiver = username
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()

    message_local = user_message

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_local)
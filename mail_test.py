import smtplib
from email.message import EmailMessage

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv("sendgrid.env")

message = Mail(
    from_email='stefan.scheible@kurz-fischer.com',
    to_emails='stefan.scheible@kurz-fischer.com',
    subject='Sending!!!',
    html_content='Why does it not work')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
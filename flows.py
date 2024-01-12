from prefect import flow, task, serve
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




print(os.getenv("SMTP_PASSWORD"))

print("WHO CAN SEE THIS?")

@flow(log_prints=True)
def notify_people(people="Walter"):
    print("Hello from the flow")
    print(people)
    print("Goodbye")


@flow(log_prints=True)
def send_a_mail(people="Walter"):
    print("Hello from send_a_mail")
    # Replace these with your details
    sender_email = "alarm.svantek@kurz-fischer.de"
    sender_password = "kfnum@alarm7"
    receiver_email = "stefan.scheible@kurz-fischer.com"

    server = "syscp3.webhosting-franken.de"

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Test mail from Python"

    # The body and the attachments for the mail
    message.attach(MIMEText("Hello, this is a test email sent from Python!", 'plain'))

    # Create SMTP session for sending the mail
    try:
        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 25)
        # server.starttls()  # Enable security
        server.login(sender_email, sender_password)  # Login with mail_id and password
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email successfully sent to", receiver_email)
    except Exception as e:
        print("Error: unable to send email")
        print("Exception: ", e)
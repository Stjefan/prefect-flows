from prefect import flow, task, serve
# import os
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage



@flow(log_prints=True)
def notify_people(people="Walter"):
    print("Hello from the flow")
    print(people)
    print("Goodbye")



@flow(log_prints=True)
def send_a_mail(people="Walter"):
    print("Hello from send_a_mail")
    msg = EmailMessage()
    msg.set_content("Hello!")

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f'The contents'
    msg['From'] = "python-mail@kurz-fischer.de"
    msg['To'] = "st.scheible@gmail.com"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP("syscp3.webhosting-franken.de", 25)
    s.login("alarm.svantek@kurz-fischer.de","kfnum@alarm7")
    s.send_message(msg)
    s.quit()
    print("Goodbye")
    # Set up the MIME
    

if __name__ == "__main__":
    send_a_mail()
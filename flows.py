from prefect import flow, task, serve
# import os
import smtplib
from email.message import EmailMessage



@flow(log_prints=True)
def notify_people(people="Walter"):
    print("Hello from the flow")
    print(people)
    print("Goodbye")



@flow(log_prints=True)
def send_a_mail(people="Walter"):
    print("Hello from send_a_mail")

    receiver_email = "stefan.scheible@kurz-fischer.com"
    port = 25
    host = "syscp3.webhosting-franken.de"
    server = smtplib.SMTP(host, port)
    sender_email = "alarm.svantek@kurz-fischer.de"
    sender_password = "kfnum@alarm7"

    msg = EmailMessage()
    msg["Subject"] = "Hello from prefect"
    msg.set_content("From a flow")
    msg["From"] = sender_email
    msg["To"] = receiver_email
    
    
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    # Replace these with your details
    


    print("Goodbye")

    # Set up the MIME
    

if __name__ == "__main__":
    send_a_mail()
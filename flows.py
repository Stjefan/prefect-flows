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
    print("Goodbye")
    # Set up the MIME
    

if __name__ == "__main__":
    send_a_mail()
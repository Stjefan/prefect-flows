from prefect import flow, task, serve
import os


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
    print("Goodbye")

    # Set up the MIME
    

if __name__ == "__main__":
    send_a_mail()
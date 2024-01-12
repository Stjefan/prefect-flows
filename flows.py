from prefect import flow, task, serve

@flow(log_prints=True)
def notify_people(people="Walter"):
    print("Hello from the flow")
    print(people)
    print("Goodbye")
from prefect import flow, task, serve

@flow(log_prints=True)
def notify_people(people="Walter"):
    print("Hello from the flow")
    print(people)
    print("Goodbye")

if __name__ == "__main__":
    serve(notify_people.to_deployment(name="my-first-deployment",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *"))
        
    
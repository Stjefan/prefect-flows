from prefect import flow, task, serve



if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/Stjefan/prefect-flows.git",
        entrypoint="flows_and_more.py:notify_people",
    ).deploy(name="my-first-deployment",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *")
        
    
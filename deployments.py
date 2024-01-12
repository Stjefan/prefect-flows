from prefect import flow, task, serve



if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/Stjefan/prefect-flows.git",
        entrypoint="flows.py:notify_people",
    ).deploy(name="my-first-deployment",
        work_pool_name="my-managed-pool",
        # cron="0 1 * * *"
        )
    
    flow.from_source(
        source="https://github.com/Stjefan/prefect-flows.git",
        entrypoint="flows.py:send_a_mail",
    ).deploy(name="my-first-deployment",
        work_pool_name="my-managed-pool",
        )
    
    flow.from_source(
        source="https://github.com/discdiver/demos.git",
        entrypoint="my_gh_workflow.py:repo_info",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-managed-pool",
    )

        
    
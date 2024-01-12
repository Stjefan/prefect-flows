from prefect import flow, task, serve


@flow(log_prints=True)
def random_flow(repo_name: str = "PrefectHQ/prefect"):
    print("Just a random_flow")
    pass
    


if __name__ == "__main__":
    random_flow.from_source(
        source="https://github.com/Stjefan/prefect-flows.git",
        entrypoint="flows.py:notify_people",
    ).deploy(name="foo-azure",
        work_pool_name="my-managed-pool",
        cron="* * * * *"
        )
    
    # random_flow.from_source(
    #     source="https://github.com/Stjefan/prefect-flows.git",
    #     entrypoint="flows.py:send_a_mail",
    # ).deploy(name="bar",
    #     work_pool_name="my-managed-pool",

        
    #     )
    
    # random_flow.from_source(
    #     source="https://github.com/discdiver/demos.git",
    #     entrypoint="my_gh_workflow.py:repo_info",
    # ).deploy(
    #     name="baz",
    #     work_pool_name="my-managed-pool",
    # )

        
    
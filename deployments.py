from prefect import flow, task, serve
from prefect.deployments import DeploymentImage



### Somehow st.scheible@gmail.com is broken, use st.scheible+prefect@gmail.com

@flow(log_prints=True)
def random_flow(repo_name: str = "PrefectHQ/prefect"):
    print("Just a random_flow")
    pass
    


if __name__ == "__main__":
    random_flow.from_source(
        source="https://github.com/Stjefan/prefect-flows.git",
        entrypoint="flows.py:send_a_mail",
    ).deploy(name="deploy-again",
        work_pool_name="aci-work-pool",
        # cron="*/15 * * * *"
        )
    
    # random_flow.from_source(
    #     source="https://github.com/Stjefan/prefect-flows.git",
    #     entrypoint="pandas_flow.py:fun",
        
        
    # ).deploy(name="we-check-pandas",
    #     work_pool_name="work-pool-docker",
    #     image=DeploymentImage(
    #         name="my_second_image",
    #         tag="deploy-guide-1",
    #         dockerfile="Dockerfile"
    # ),
    # push=False,
        
    #     cron="* * * * *",
        
    #     )
    
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

        
    
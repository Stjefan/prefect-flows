import numpy as np

import pandas as pd
from prefect import flow, task, serve
import os
from prefect.blocks.system import Secret



@flow(log_prints=True)
def not_too_long():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(os.getenv("POSTGRES_CS"))
    print(df)
    secret_block = Secret.load("secret-connectionstring")
    print(secret_block.get())
    print("Hello from the flow")


import numpy as np

# import pandas as pd
from prefect import flow, task, serve

@flow(log_prints=True)
def fun():
    print(np.random.randn(6, 4))
    # dates = pd.date_range("20130101", periods=6)
    # df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print("...")
FROM prefecthq/prefect:2-latest


COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
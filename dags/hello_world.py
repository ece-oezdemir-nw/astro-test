"""
hello_world
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
import pandas as pd
import pendulum


@aql.dataframe(task_id="python_1")
def python_1_func():
    from airflow.decorators import dag, task
    from datetime import datetime
    
    @task
    def hello_world():
        print("Hello World")
    
    @dag(
        dag_id='hello_world',
        start_date=datetime(2023, 1, 1),
        schedule_interval='@daily',
        catchup=False,
        default_args={'owner': 'airflow', 'retries': 1},
    )
    def hello_world_dag():
        hello_world_task = hello_world()
    
    hello_world_dag()

default_args={
    "owner": "ece.oezdemir@new-work.se,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2025-03-14", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "ece.oezdemir@new-work.se": "mailto:ece.oezdemir@new-work.se",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cm7vpp9790phl01prbv7fjxpq/cloud-ide/cm833k6ig100w01id2fit528c/cm88wvaxp118x01meuyu5i21x",
    },
)
def hello_world():
    python_1 = python_1_func()

dag_obj = hello_world()

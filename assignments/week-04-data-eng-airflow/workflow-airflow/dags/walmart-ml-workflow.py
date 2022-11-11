from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

# instantiates a directed acyclic graph
with DAG(
    'walmart-ml-workflow',
    default_args={
        'owner': 'Flora Xu', # YOUR NAME HERE
        'depends_on_past': False,
        'email': ['flora@fourthbrain.ai'], # YOUR EMAIL HERE
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        },
    description='A simple Machine Learning workflow for Walmart Sales',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 8, 27), 
    tags=['walmart', 'ml', 'workflow'] # OPTIONAL: tags
) as dag:

    # instantiate tasks using Operators.
    # BashOperator defines tasks that execute bash scripts. In this case, we run Python scripts for each task.
    get_store_data = BashOperator(
        task_id='get_store_data',
        bash_command='python3 ~/airflow/scripts/get_store_data.py',
    )
    train = BashOperator(
        task_id='train',
        depends_on_past=False,
        bash_command='python3 ~/airflow/scripts/train.py',
        retries=3,
    )

    # sets the ordering of the DAG. The >> directs the 2nd task to run after the 1st task. This means that
    # get the store data first, then train.
    get_store_data >> train 
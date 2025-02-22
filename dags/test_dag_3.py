import time
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator


def extract():
    time.sleep(10)

def transform():
    time.sleep(10)

def load():
    time.sleep(10)


with DAG(
    dag_id='testing-dag-3',
    start_date=days_ago(n=0),
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract-task',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform-task',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=transform
    )


extract_task >> transform_task >> load_task
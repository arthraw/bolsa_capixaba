from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG
import datetime
from src.ingestion.load_data_from_web import load_data

dag_name = "bolsacapixaba"
dag = DAG(
    dag_id=dag_name,
    dag_display_name="bolsa capixaba ETL",
    start_date=datetime.datetime(2025, 5, 3),
    schedule=None,
    catchup=False,
)

with dag:
    # Extract all csv's of bolsa capixaba posted in public ES government website
    extract_raw_data_from_web = PythonOperator(
        task_id="extract_raw_data_from_web",
        python_callable=load_data,
        dag=dag,
    )
    # Refine and clean all data
    clean_data = BashOperator(
        task_id="clean_data",
        bash_command='spark-submit /opt/airflow/src/processing/process_data.py',
        dag=dag
    )

    extract_raw_data_from_web >> clean_data
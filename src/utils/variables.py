import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/opt/airflow/.env")

# env variables
url = os.getenv('BOLSA_CAPIXABA_URL')
storage_account_name = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
storage_account_key = os.getenv('# AZURE_STORAGE_ACCOUNT_KEY')
container_name = os.getenv('AZURE_CONTAINER_NAME')



# paths variables
src = os.path.join(os.getcwd(), '..')
root = os.path.abspath(os.path.join(src, '..'))

# Use in local windows tests
# bronze_path = os.path.join(root,'data','bronze')
# silver_path = os.path.join(root,'data','silver')
# gold_path = os.path.join(root,'data','gold')
# log_path = os.path.join(root,'logs', 'bolsa_capixaba.log')

# Use in airflow container
bronze_path = '/opt/airflow/data/bronze'
silver_path = '/opt/airflow/data/silver'
gold_path = '/opt/airflow/data/gold'
log_path = '/opt/airflow/logs/bolsa_capixaba.log'

# Azure paths
bronze_lake_output_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/bronze"
silver_lake_output_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/silver"
gold_lake_output_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/gold"

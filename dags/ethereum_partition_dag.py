from __future__ import print_function
import logging

from airflow.models import Variable
from ethereumetl_airflow.build_partition_dag import build_partition_dag

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Build Airflow DAG for Ethereum partitioning
DAG = build_partition_dag(
    dag_id="ethereum_partition_dag",
    partitioned_project_id="blockchain-etl-internal",
    partitioned_dataset_name="crypto_ethereum_partitioned",
    public_project_id="bigquery-public-data",
    public_dataset_name="crypto_ethereum",
    load_dag_id="ethereum_load_dag",
    notification_emails=Variable.get("notification_emails", default_var=None),
    schedule_interval="30 9 * * *"
)
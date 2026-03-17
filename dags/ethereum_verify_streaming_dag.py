from __future__ import print_function
import logging

from ethereumetl_airflow.build_verify_streaming_dag import build_verify_streaming_dag
from ethereumetl_airflow.variables import read_verify_streaming_dag_vars

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Airflow detects DAGs only if both "airflow" and "DAG" appear in the file
dag_config = read_verify_streaming_dag_vars(
    var_prefix="ethereum_",
    max_lag_in_minutes=10
)

DAG = build_verify_streaming_dag(
    dag_id="ethereum_verify_streaming_dag",
    **dag_config
)
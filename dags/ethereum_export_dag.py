from __future__ import print_function

from ethereumetl_airflow.build_export_dag import build_export_dag
from ethereumetl_airflow.variables import read_export_dag_vars

DAG = build_export_dag(
    dag_id='eth_export_dag',
    **read_export_dag_vars(
        var_prefix='ethereum_',
        export_schedule_interval='0 6 * * *',
        export_start_date='2016-01-01',
        export_max_workers=8,
        export_batch_size=20,
        export_retries=3,
    )
)
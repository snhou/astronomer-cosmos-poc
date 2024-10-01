from pathlib import Path
from cosmos import ExecutionConfig

jaffle_shop_path = Path("/opt/airflow/dbt/jaffle_shop")
dbt_executable = Path("/opt/airflow/dbt")

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable)
)

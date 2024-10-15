import pytest
from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.utils.state import State

@pytest.fixture
def dagbag():
    return DagBag()

def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="simple_task_group")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) > 0

def test_dag_structure(dagbag):
    dag = dagbag.get_dag(dag_id="simple_task_group")
    task_ids = [task.task_id for task in dag.tasks]
    assert "post_dbt" in task_ids
    assert "final_dbt" in task_ids

def test_task_dependencies(dagbag):
    dag = dagbag.get_dag(dag_id="simple_task_group")
    assert dag.task_dict["post_dbt"].downstream_task_ids == {"final_dbt"}

def test_execute_dag(dagbag):
    dag = dagbag.get_dag(dag_id="simple_task_group")
    execution_date = days_ago(1)
    dag.clear(start_date=execution_date, end_date=execution_date)
    dag_run = dag.create_dagrun(
        run_id=f"test_execute_dag_{execution_date.isoformat()}",
        execution_date=execution_date,
        start_date=execution_date,
        state=State.RUNNING,
        external_trigger=False,
    )
    dag_run.run()
    assert dag_run.state == State.SUCCESS
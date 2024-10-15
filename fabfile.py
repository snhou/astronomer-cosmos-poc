import os
from fabric import Connection, task

@task
def staging(ctx):
    with Connection(
        "YOUR SERVER IP",
        user="YOUR USER NAEM",
        connect_kwargs={"key_filename":os.environ['KEY_PATH']}
    ) as conn:
        with conn.cd("/airflow"):
            conn.run("git pull origin main --rebase")
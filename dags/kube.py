from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'runai',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['itay@run.ai'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'runai_job',
    default_args=default_args,
    schedule_interval=timedelta(minutes=10))

resources = {
  limits: {
    nvidia.com/gpu: 1
  }
}

job = KubernetesPodOperator(namespace='default',
                          image="gcr.io/run-ai-lab/quickstart",
                          labels={"project": "airflow"},
                          name="train1",
                          task_id="train1",
                          get_logs=True,
                          schedulername: "runai-scheduler",
                          resources: resources,
                          dag=dag
                          )




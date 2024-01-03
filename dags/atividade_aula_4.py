import pendulum
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

with DAG(
            'atividade_aula_4',
            start_date=pendulum.today('UTC').add(days=-1),
            schedule_interval='@daily'
) as dag:
    
    def cumprimentos():
        print('Boas-vindas ao Airflow')

    tarefa = PythonOperator(
        task_id = 'cumprimentos',
        python_callable=cumprimentos
    )
import pendulum
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# definindo o DAG
with DAG(
            'atividade_aula_4',
            start_date=pendulum.today('UTC').add(days=-1),
            schedule_interval='@daily'
) as dag:
    
    # para definir uma tarefa com PythonOperator é necessário criar uma função
    def cumprimentos():
        print('Boas-vindas ao Airflow')

    tarefa = PythonOperator(
        # operador precisa de pelo menos dois parâmetros para funcionamento
        task_id = 'cumprimentos',
        python_callable=cumprimentos
    )
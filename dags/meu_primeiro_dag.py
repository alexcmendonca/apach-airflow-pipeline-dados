from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

# especificando os parâmetros principais do DAG
with DAG(
    'meu_primeiro_dag', 
    start_date=days_ago(2),
    schedule_interval='@daily'
) as dag:

    # tarefa com EmptyOperator será avaliada pelo scheduler mas não será executada
    tarefa_1 = EmptyOperator(task_id = 'tarefa_1')
    tarefa_2 = EmptyOperator(task_id = 'tarefa_2')
    tarefa_3 = EmptyOperator(task_id = 'tarefa_3')
    # tarefa com BashOperator executa um script ou comando bash
    tarefa_4 = BashOperator(
        task_id = 'cria_pasta',
        bash_command='mkdir -p "/home/alexmend/Documents/airflow/pasta={{data_interval_end}}"'
    )
    # definindo o fluxo de execução das tarefas
    tarefa_1 >> [tarefa_2, tarefa_3]
    tarefa_3 >> tarefa_4
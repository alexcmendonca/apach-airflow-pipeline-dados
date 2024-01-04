from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
import os
from dotenv import load_dotenv
import pendulum
from os.path import join
import pandas as pd

# definição do DAG e criação das tarefas
with DAG(
    'dados_climaticos',
    # definindo data específica com biblioteca pendulum
    start_date=pendulum.datetime(2023, 12, 3, tz='UTC'),

    # utilizando uma cron expression para definir período de tempo mais complexo
    schedule_interval='0 0 * * 1', #executar toda segunda feira
) as dag:
    
    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        # definindo nome da pasta com a data formatada através do strftime()
        bash_command='mkdir -p "/home/alexmend/Documents/airflow/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    # utilizando variável na função com JinjaTemplates
    def extrair_dados(data_interval_end):

        load_dotenv()

        city = 'Boston'
        key = os.getenv('key')

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                    f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')
    
        dados = pd.read_csv(URL)

        # Definindo diretório e criando uma pasta
        file_path = f'/home/alexmend/Documents/airflow/semana={data_interval_end}/'

        # Salvar arquivos em csv
        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperatura.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')


    tarefa_2 = PythonOperator(
        task_id = 'extrair_dados',
        python_callable = extrair_dados,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    tarefa_1 >> tarefa_2
# Gerenciando um Pipeline de Dados com Apache Airflow

## 💡Objetivos
Desenvolver um pipeline de dados automatizado dedicado à obtenção da previsão do tempo para a cidade de Boston nos próximos 7 dias. O pipeline será responsável por extrair essas informações de uma API confiável, armazenando-as de maneira eficiente e programada para execução regular em um dia determinado. O propósito principal dessa iniciativa é fornecer à cidade de Boston dados precisos e atualizados sobre as condições climáticas futuras, permitindo que ela organize a programação de passeios de maneira mais informada e adequada às condições meteorológicas esperadas.


## 🖥️Desafios do Projeto
Este projeto consiste em aprofundar os conhecimentos sobre Apache Airflow, poderosa ferramenta de orquestração de fluxos, visando entender seus conceitos fundamentais, componentes arquitetônicos e recursos essenciais. Instalar o Airflow, explorar sua interface e compreender o papel crucial dos conceitos como DAGs, tasks e operators na criação, agendamento e monitoramento de pipelines de dados e fluxos de trabalho de forma programática.

###### Imagem 1: Arquitetura do Airflow (Crédito da imagem: Alura)
<img src="/assets/img/img_arquitetura_dag.png">

## 📄Desenvolvimento de Competências:
|Atividades|Realizadas |
|----------|-----------|
| Utilizar uma API com dados climáticos | Extrair dados da previsão do tempo |
| Criar uma pasta utilizando Python | Salvar os arquivos extraídos em csv |
| Diferenciar DAGs, Tasks e Operators | Listar quais são os principais componentes do Airflow |
| Arquitetura do Airflow | Instalar o Python 3.9 no Ubuntu |
| Criar e ativar um ambiente virtual | Instalar o Airflow |
| Executar o Airflow localmente | Navegar pela interface do Airflow |
| Criar seu primeiro DAG | Instanciar tarefas utilizando o EmptyOperator |
| Desenvolver tarefas utilizando o BashOperator | Utilizar os Jinja Templates |
| Criar um DAG mais complexo | Utilizar as CRON Expressions para definir um intervalo de agendamento |
| Criar tarefas utilizando o PythonOperator | Desenvolver um DAG que extrai dados da previsão do tempo |

## 🗂️Organização dos Arquivos
- Pasta dags: A pasta de DAGs deve ser denominada como "dags" para que o Apache Airflow possa identificar adequadamente o local onde estamos criando esses fluxos de trabalho. É nesse diretório específico que os arquivos contendo o desenvolvimento de cada DAG devem ser salvos;
- Pasta semana: É um diretório semanal criado por meio de um DAG para armazenar os dados extraídos da previsão do tempo correspondentes à semana de execução.

## 🎞️Imagens do Projeto

###### Imagem 2: Inicialização Apache Airflow
<img src="/assets/img/img_start_airflow.png">

###### Imagem 3: Interface Airflow
<img src="/assets/img/img_dag.png">

###### Imagem 4: Visualização gráfica de um DAG e suas dependências
<img src="/assets/img/img_graph.png">


## 🔍Referências
- [Alura](https://www.alura.com.br/)

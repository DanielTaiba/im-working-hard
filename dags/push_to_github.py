from src import git
from src.utils import createReadMe
from datetime import timedelta

from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

import logging

default_args = {
  'owner':'airflow',
  'depends_on_past': False,
  'email':['hola@example.com'],
  'email_on_failure':False,
  'email_on_retry':False,
  'retries':1,
  'retry_delay':timedelta(minutes=5),
}

def extract_transform():
  createReadMe('Timbuktu')
  logging.info("create readme")



def save():
  git().pushToGithub(filename='README.md',repo='Im-working-hard',branch='main')
  logging.info('push to github')


with DAG(
  'first',
  default_args=default_args,
  description='A simple tutorial DAG',
  schedule_interval=timedelta(days=1),
  start_date=days_ago(1),
  tags=['first']
) as dag:
  init_task = PythonOperator(task_id='scrape',python_callable=extract_transform)

  save_task = PythonOperator(task_id='save',python_callable=save)

  init_task >> save_task
#!/bin/bash

#create dir
if [ ! -d $(pwd)/airflow ];
  then
  exec mkdir $(pwd)/airflow
  exec cp ./dags ./airflow/dags
fi

#add environment variables
export AIRFLOW__CORE__LOAD__EXAMPLES=false
export AIRFLOW_HOME=$(pwd)/airflow


#install airflow
#AIRFLOW_VERSION=2.2.4
#PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
#pip install "apache-airflow[celery]==2.2.4" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
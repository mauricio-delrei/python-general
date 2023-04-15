## Instalação Monitoramento com Mensagem no Canal do Slack.

python3.8 -m venv env
source env/bin/activate

## Instalar Pacotes para Monitoramento.

pip3 install slackclient
pip install slackclient
pip3 install requests
pip install requests

##Instalar driver MySQL

pip3 uninstall pymysql
pip3 install pymysql

## Instalar Kafka connector

pip3 install kafka-python

## Instalar Flask

pip3 install flask


## Execução:
python3 exception/monitoramento.py
from prefect import flow
import logging

@flow
def hello_world():
    logging.info("Hello World! Rodando a cada 30 minutos 🚀")
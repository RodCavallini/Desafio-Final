import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime
from plyer import notification 
import requests


def get_url(url):
    response = requests.get(url)  

    if response.status_code == 200:
        data_json = response.json()
        notification.notify(
        title='SUCESSO',
        message='Base carregada com sucesso',
        app_name='API',
        timeout=10 )
        return data_json
    else:
        notification.notify(
        title='ERRO',
        message='Erro ao carregar base de dados',
        app_name='API',
        timeout=10 )


def tabelas_bd():

    conn = sqlite3.connect('coderhouse.db')

    # Executar uma consulta que retorna as informações do esquema do banco de dados
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    schema = pd.read_sql_query(query, conn)

    conn.close()

    return schema

def salva_bd(df, nome_tabela):
    
    conn = sqlite3.connect('coderhouse.db')

    # Escrever o DataFrame na tabela 'nome_tabela'
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

    conn.close()

    return True

def carrega_bd(nome_tabela):
    conn = sqlite3.connect('coderhouse.db')

    # Executar uma consulta SELECT na tabela 'produtos' e converter em um DataFrame
    query = f"SELECT * FROM {nome_tabela}"
    df = pd.read_sql(query, conn)

    conn.close()

    return df
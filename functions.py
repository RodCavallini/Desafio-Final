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
        message=f'Base carregada com sucesso',
        app_name='API',
        timeout=10 )
        return data_json

    else:
        notification.notify(
        title='ERRO',
        message=f'Erro ao carregar base de dados',
        app_name='API',
        timeout=10 )
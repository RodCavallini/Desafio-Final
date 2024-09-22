### Projeto Final Python CoderHouse
Projeto Final de conclusão do curso de Python da plataforma CoderHouse.

Este projeto foi desenvolvido como parte do curso de Python da CoderHouse, Turma 6400 por Rodrigo Cavallini.

### Descrição do Projeto 🚀
O projeto consiste na extração de APIS públicas e salvar em um banco de dados para consulta. 

### Funcionalidades 🛠️
Extração de dados de APIs públicas.
Tratamento e manipulação dos dados coletados.
Armazenamento dos dados em banco de dados SQLite.
Notificação de sucesso ou falha na extração e tratamento dos dados.

### Bibliotecas Necessárias 📚
* import pandas as pd
* import sqlite3
* from datetime import datetime
* from plyer import notification 
* import requests
* import functions as f (Arquivo .py com as funções utilizadas)

### Endpoints utilizados:
* Bancos: https://brasilapi.com.br/api/banks/v1
* Pix : https://brasilapi.com.br/api/pix/v1/participants/
* Corretoras : https://brasilapi.com.br/api/cvm/corretoras/v1

Ambiente Virtual 🌐

Criar ambiente:
virtualenv nome_do_ambiente

Ativar ambiente virtual:
.\nome_do_ambiente\Scripts\Activate.ps1

Verificar se o ambiente está ativado:
Get-Command python

Instalação das bibliotecas através do arquivo requirements: 

pip install -r requeriments.txt

### Tratamento e Manipulação dos Dados 🛠️
* Renomeando de colunas:
Coluna "nome_social" na tabela corretoras renomeada para "nome"

* Covertendo tipos de dados:
Coluna "inicio_operacao" na tabela Pix alterada para Data

* Melhorando valores ausentes:
Exclusão de 2 linhas na tabela Bancos e alteração de valores "NAN" para "0" na coluna CODE.

* Armazenamento dos dados em bancos de dados SQLite:
Função : salva_bd(df, nome_tabela) no aqruivo funcitions.py



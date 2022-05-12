#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset
# 

# In[3]:


# PASSO 1

import pandas as pd
import plotly.express as px
database = pd.read_csv("telecom_users.csv")
# PASSO 2

database = database.drop("Unnamed: 0", axis=1) #Colunas = 1 | linhas = 0
#display(database)

# database.to_csv("teste.csv") exportar a tabela modificada para csv

# PASSO 3

#Converte os valores da coluna TotalGasto para numéricos
# errors="coerce" significa que caso algum dado dê erro, deixe-o vazio
database["TotalGasto"] = pd.to_numeric(database["TotalGasto"], errors="coerce") 

#Excluir colunas COM TODOS os valores vazios = "all"
# Dropna analisa a base de dados e exclui de forma inteligente valores vazios
database = database.dropna(how="all", axis=1)

# Excluir linhas com ALGUNS valores vazios = "any"
database = database.dropna(how="any", axis=0)

#print(database.info()) #database.info() retorna informações sobre a tabela

# Passo 4

#print(database["Churn"].value_counts())
#print(database["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #Retorna em porcentagem

# Passo 5
# Instale potly para gerar graficos

#Para cada coluna da base de dados, criar 1 gráfico
#Criar gráfico
for column in database.columns:
    if column == "IDCliente" or column == "Churn":
        continue
    grafico = px.histogram(database, x=column, color="Churn")
    grafico.update_layout(bargap=0.1)
    grafico.show()


# In[ ]:





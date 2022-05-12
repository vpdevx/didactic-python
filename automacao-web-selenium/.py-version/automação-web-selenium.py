#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[ ]:


#!pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

browser = webdriver.Edge()

#DOLAR
browser.get("https://www.google.com.br")
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(dolar)
#EURO
browser.get("https://www.google.com.br")
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


#OURO
browser.get("https://www.melhorcambio.com/ouro-hoje")
ouro = browser.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(",",".")

default_database = pd.read_excel("Produtos.xlsx")
#atualizar a cotação de acordo com a moeda, preço de compra e preço de venda
default_database.loc[default_database["Moeda"] == "Dólar", "Cotação"] = float(dolar)
default_database.loc[default_database["Moeda"] == "Euro", "Cotação"] = float(euro)
default_database.loc[default_database["Moeda"] == "Ouro", "Cotação"] = float(ouro)

default_database["Preço de Compra"] = default_database["Preço Original"] * default_database["Cotação"]
default_database["Preço de Venda"] = default_database["Preço de Compra"] * default_database["Margem"]
display(default_database)

default_database.to_excel("Novos produtos.xlsx", index=False)
pd.write_csv("teste.csv")
browser.quit()


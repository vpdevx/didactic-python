#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Aula 1 automação de processos

#Instalação do pyautogui e pyperclip
get_ipython().system('pip install pyautogui')
get_ipython().system('pip install pyperclip')


# In[ ]:


import pyautogui
import pyperclip
import time
import pandas as pd #Ler planilhas
import datetime

#pyperclip permite escrever texto com caracteres especiais
#pyautogui.hotkey() -> conjunto de teclas
#pyautogui.write() -> escrever um texto
#pyautogui.press() -> apertar uma tecla

#pyautogui.PAUSE -> pausa de 1 segundo entre os comandos
pyautogui.PAUSE = 1

#Descobrir posição do mouse na tela
#time.sleep(3)
#pyautogui.position()

#Open a new browser tab 
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
#pyautogui.write("hltv.org")
pyautogui.press("enter")

#pausa o código neste momento
time.sleep(3)
pyautogui.click(x=346, y=287, clicks=2) #Clica na pasta
time.sleep(3)
pyautogui.click(x=392, y=350) #Seleciona o arquivo
pyautogui.click(x=1162, y=174) #Clica nos três pontos
pyautogui.click(x=922, y=541) #Realiza o download do arquivo



table = pd.read_excel(r"C:\Users\Vini\Downloads\Vendas - Dez.xlsx") #Substitua pelo caminho do arquivo na SUA máquina.
#display(table)

#Calculos
faturamento = table["Valor Final"].sum()

quantidade = table["Quantidade"].sum()

pyautogui.hotkey("ctrl", "t")

pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=82, y=174)

time.sleep(2)

pyautogui.write("zoboomafoo011@gmail.com")

pyautogui.press(["tab", "tab"])

strDate = str(datetime.date.today())

assunto = "Relatório de vendas " + strDate 

pyperclip.copy(assunto)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

texto = f"""

Prezados,

    segue o faturamento e quantidades referentes a data {strDate}
    O faturamento foi de {faturamento:,.2f}
    A quantidade foi de {quantidade:,}

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl","enter")


# In[ ]:


#time.sleep(3)
#pyautogui.position() descobrir posição do mouse


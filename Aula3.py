import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

# Passo 1: Pegar Cotação do Dólar
navegador.get("http://www.google.com/")
navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")\
    .send_keys("cotação dolar")
navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")\
    .send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]")\
    .get_attribute("data-value")
print(cotacao_dolar)
cotacao_dolar = "{:.2f}".format(float(cotacao_dolar))
print(cotacao_dolar)

# Passo 2: Pegar Cotação do Euro
navegador.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")\
    .clear()
navegador.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")\
    .send_keys("cotação euro")
navegador.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")\
    .send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]")\
    .get_attribute("data-value")
print(cotacao_euro)
cotacao_euro = "{:.2f}".format(float(cotacao_euro))
print(cotacao_euro)

# Passo 3: Pegar Cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div/input[2]").get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)

# Fechar o navegador
navegador.quit()

# Passo 4: Importar a Lista de Produtos
diretorio = (r"C:\Users\Gabriel\Documents\Programação\Hashtag\Aula 3").replace(os.sep, '/')
dir2 = diretorio+("/Produtos.xlsx")
tabela = pd.read_excel(dir2)
print(tabela)

# Alterar Valores da Tabela
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# Conferir Resultado
print(tabela)

# Exportando a nova planilha Excel
tabela.to_excel(diretorio+"/Produtos Novo.xlsx", index = False)
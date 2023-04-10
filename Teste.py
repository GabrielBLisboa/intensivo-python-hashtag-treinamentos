import os

lista = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda x:x+2, lista)))

import pandas as pd
diretorio = r"C:\Users\Gabriel\Documents\Programação\Hashtag\Aula 3"
dir2 = diretorio.replace(os.sep, '/')+("/Produtos.xlsx")
tabela = pd.read_excel(dir2)
print(tabela)
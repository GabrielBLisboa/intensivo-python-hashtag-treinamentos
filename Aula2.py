import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'png'
#import plotly.graph_objects as go
import seaborn as sns
from IPython.display import display

df = pd.read_csv("C:/Users/Gabriel/Documents/Programação/Python/Hashtag - Intensivo Python/Aula 2")
df = df.drop(["Unnamed: 0"], axis=1)
display(df)
print(df.info())

#Transformar coluna que deveria ser número e está como texto em número
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")

#Remover a coluna que está 100% vazia
df = df.dropna(how='all', axis=1)

#Remover linha que tem um item vazio
df = df.dropna()

display(df)
print(df.info())

display(df['Churn'].value_counts())
display(df["Churn"].value_counts(normalize=True).map('{:.1%}'.format))

for coluna in df:
    if coluna != "IDCliente":
        #criar a figura
        fig = px.histogram(df, x=coluna, color="Churn")
        #exibir a figura
        #fig.write_image("figure.png", engine="kaleido")
        fig.show()
        display(df.pivot_table(index="Churn", columns=coluna, aggfunc="count")["IDCliente"])
        sns.pairplot(df)
        plt.show()
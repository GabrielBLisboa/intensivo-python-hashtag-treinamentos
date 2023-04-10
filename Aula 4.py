import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split



# Buscar o Arquivo
diretorio = (r"C:\Users\Gabriel\Documents\Programação\Hashtag\Aula 4").replace(os.sep, '/')
dir2 = diretorio+("/advertising.csv")
df = pd.read_csv(dir2)
print(df.info())

sns.pairplot(df)
plt.show()
sns.heatmap(df.corr(), cmap = "Wistia", annot=True)
plt.show()

x = df.drop("Vendas", axis=1)
y = df["Vendas"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=1)

# Treino de AI
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

rf_reg = RandomForestRegressor()
rf_reg.fit(x_train, y_train)

# Teste AI
test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

# Indicadores da Regressão Linear
r2_lin = metrics.r2_score(y_test, test_pred_lin)
rmse_lin = np.sqrt(metrics.mean_squared_error(y_test, test_pred_lin))
print(f"R² da Regressão Linear: {r2_lin}")
print(f"RSME da Regressão Linear: {rmse_lin}")

# Indicadores da Random Forest
r2_rf = metrics.r2_score(y_test, test_pred_rf)
rmse_rf = np.sqrt(metrics.mean_squared_error(y_test, test_pred_rf))
print(f"R² da Regressão Linear: {r2_rf}")
print(f"RSME da Regressão Linear: {rmse_rf}")

# Análise de Confiabilidade

df_resultado = pd.DataFrame()
#df_resultado.index = x_test
df_resultado["y_teste"] = y_test
df_resultado["y_previsao_rf"] = test_pred_rf
df_resultado["y_previsao_lin"] = test_pred_lin
df_resultado = df_resultado.reset_index(drop=True)
fig = plt.figure(figsize=(15,5))
sns.lineplot(data=df_resultado)
plt.show()
print(df_resultado)

importancia_features = pd.DataFrame(rf_reg.feature_importances_, x_train.columns)
plt.figure(figsize=(5,5))
sns.barplot(x=importancia_features.index, y=importancia_features[0])
plt.show()
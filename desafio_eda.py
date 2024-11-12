import pandas as pd  
import matplotlib.pyplot as plt
from scipy.stats import zscore
import numpy as np

df_netflix = pd.read_csv('./datasets_desafio/netflix daily top 10.csv')

# Tipos de Dados Disponíveis
data_types = df_netflix.dtypes
print(f'\nOs tipos de dados são:\n{data_types}')

# Período da análise feita
df_netflix['As of'] = pd.to_datetime(df_netflix['As of'])

first_day = df_netflix['As of'].min()
last_day = df_netflix['As of'].max()
period = (last_day - first_day).days

print(f'\nPeríodo de Análise: {period} dias')

#Tamanho da base de dados
print(f'\nA base de dados tem dimensões de {df_netflix.shape}, ou seja {df_netflix.shape[0]*df_netflix.shape[1]} valores\n')

#Verificar dados nulos
print(df_netflix.isna().sum())
print(f'\nExistem valores nulos somente na coluna Netflix Exclusive, e são {df_netflix['Netflix Exclusive'].isna().sum()} dados nulos')

#Outliers
fig1, ax1 = plt.subplots() 
df_netflix.plot.box(ax=ax1)
plt.show()

#Outliers em Rank
fig2, ax2 = plt.subplots()
df_netflix['Rank'].plot.box(ax=ax2)
plt.show()

z = np.abs(zscore(df_netflix['Rank']))
print('\nNão existem outliers na variável Rank' if len(df_netflix[z > 3]) == 0 else f'\nExistem {len(z)} outliers na variável Rank')

#Outliers em Days In Top 10
fig3, ax3 = plt.subplots()
df_netflix['Days In Top 10'].plot.hist(ax=ax3)
plt.show()

q1_DaysInTop10 = df_netflix['Days In Top 10'].quantile(0.25)
q3_DaysInTop10 = df_netflix['Days In Top 10'].quantile(0.75)
iqr_DaysInTop10 = q3_DaysInTop10 - q1_DaysInTop10
LimInf_DaysInTop10 = q1_DaysInTop10 - 1.5*iqr_DaysInTop10
LimSup_DaysInTop10 = q3_DaysInTop10 + 1.5*iqr_DaysInTop10
outliers_DaysInTop10 = df_netflix[(df_netflix['Days In Top 10'] < LimInf_DaysInTop10) | (df_netflix['Days In Top 10'] > LimSup_DaysInTop10)]
print(f'\nExistem: {len(outliers_DaysInTop10)} outliers na variável Days In Top 10')

#Outliers em Viewership Score
fig4, ax4 = plt.subplots()
df_netflix['Viewership Score'].plot.hist(ax=ax4)
plt.show()

q1_ViewershipScore = df_netflix['Viewership Score'].quantile(0.25)
q3_ViewershipScore = df_netflix['Viewership Score'].quantile(0.75)
iqr_ViewershipScore = q3_ViewershipScore - q1_ViewershipScore
LimInf_ViewershipScore = q1_ViewershipScore - 1.5*iqr_ViewershipScore
LimSup_ViewershipScore = q3_ViewershipScore + 1.5*iqr_ViewershipScore
outliers_ViewershipScore = df_netflix[(df_netflix['Viewership Score'] < LimInf_ViewershipScore) | (df_netflix['Viewership Score'] > LimSup_ViewershipScore)]
print(f'\nExistem: {len(outliers_ViewershipScore)} outliers na variável Viewership Score')

# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

# Obtendo a média
df_faturamento = pd.DataFrame.from_dict(dict_faturamento)
media = df_faturamento.valor.mean()
print(f'A média de vendas foi de: {media}')

# Trocando o tipo de variável das 'data_ref' no DataFrame
print(f'{df_faturamento.info()}\n')
df_faturamento['data_ref'] = pd.to_datetime(df_faturamento['data_ref'])
print(f'{df_faturamento.info()}\n')

# Plot dos gráficos
df_faturamento.sort_values('data_ref').plot.bar(x='data_ref', y='valor')
plt.show()

df_faturamento.sort_values('data_ref').plot.line(x='data_ref',y='valor')
plt.show()

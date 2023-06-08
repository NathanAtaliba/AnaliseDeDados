# PANDAS DIVIDIDO EM SERIES(1D), DATAFRAMES(2D+)
import pandas as pd
import numpy as np

# CRIANDO UMA SERIES
# PANDAS TRABALHA COM INDICES CUSTOMIZAVEIS
series1 = pd.Series({'a': 10, 'b': 20, 'c': 30})
series2 = pd.Series({'a': 10, 'c': 20, 'd': 30})
print(series1.values + series2.values)
print(series1.add(series2, fill_value=0))


# CONDICIONAL NO PANDAS
print(series1[series1 > 25])
# SLICING NA SERIES
print(series1[['b', 'c']])
# CRIANDO UM DATAFRAME
df = pd.read_csv('paises.csv', delimiter=';')
print(df.columns[1]) # pegando apenas a coluna 1
print(df[['Country', 'Birthrate', 'Deathrate']])

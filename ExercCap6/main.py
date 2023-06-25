import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ds1 = pd.read_csv('paises.csv', delimiter=';')
ds2 = pd.read_csv('space.csv', delimiter=';')

# 1)
USA = ds2[ds2['Location'].str.contains('USA')] #USA
USA = USA['Company Name'].unique()
USA = len(USA)
china = ds2[ds2['Location'].str.contains('China')] #China
china = china['Company Name'].unique()
china = len(china)
categorias = ['USA', 'China']
valores = [USA, china]
# TRAÇANDO O GRAFICO DE BARRAS
plt.bar(range(len(categorias)), valores, color=['red', 'green'])
plt.xlabel('Paises')
plt.ylabel('Qtd')
plt.title('Qtd de Empresas Espaciais')
plt.xticks(range(len(categorias)), categorias)
plt.show()

# 2)
region = ds1[ds1['Region'].str.contains('NORTHERN AMERICA                   ')]
dados1 = region['Birthrate']
print(dados1)
dados2 = region['Deathrate']
print(dados2)
x = region['Country'].values
plt.xlabel('NORTHERN AMERICA COUNTRY')
plt.ylabel('(BIRTHRATE,DEATHRATE) VALUES')
plt.plot(x, dados1.values, 'r-', x, dados2.values, 'g-')
plt.show()












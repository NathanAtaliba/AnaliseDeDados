import numpy as np
'''
np.random.seed(10)
mtz = np.random.randint(1, 10, 16).reshape(4, 4)
print(mtz)
#CONDICIONAIS DO NUMPY
print(mtz % 2 == 1)#Extraindo Trues e Falses
print(mtz[mtz % 2 == 1]) #Extraindo os numeros impares]
print(mtz[mtz >= 3]) #Extraindo os numeros maiores ou iguais a 3
'''
'''
#MANIPULANDO TEXTOS COM SUBPACOTE CHAR
arr = np.array(['Mateus',' Vinix', 'Leticia','Raphael','Livia','Nathan'])
print(np.char.find(arr, 'ia') > 0) #PROCURANDO IA NA PALAVRA
cond = np.char.find(arr, 'ia') > 0
print(arr[cond]) #
'''
#TRABALHANDO COM DATA SETS
dataset = np.loadtxt('space.csv',
                     delimiter=';',
                     dtype=str,
                     encoding='utf-8')

#VISUALIZANDO APENAS AS COLUNAS DO DATASET
dataset[0,:] #ANALISANDO AS COLUNAS

#EXTRAINDO APENAS AS EMPRESAS QUE JA FIZERAM
print(dataset[1:, 1])


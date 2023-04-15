#Exercicios
import numpy as np
#1)CRIE UM ARRAY DE FLOATS  COM 10 ELEMENTOS POSITIVO E NEGATIVO, ENTRE 0 E 1
np.random.seed(5)
arr = np.random.randn(10)
arrayMultiplicado = arr*100 #ARRAY COM VALORES MULTIPLICADO
arrayInteiro = arrayMultiplicado.round() #ARRAY INTEIRO
print(arr)
print('primeiro array multiplicada por 100 com numero inteiro', arrayInteiro)

#2)CRIE UMA MATRIZ 4X4 FORMADA POR NÚMEROS ALEATORIOS INTEIROS ENTRE 1 E 50
np.random.seed(10)
arr2 = np.random.randint(1, 50, 16).reshape(4, 4)
print('Array 4x4: ', arr2)

#3)MOSTRE O RESULTADO DA MÉDIA DE CADA LINHA E CADA COLUNA DA MATRIZ GERADA PELA QUESTAO 2, APRESENTE O  MAIOR VALOR DAS MEDIAS PARA LINHAS E TAMBEM PARA COLUNAS.

print('Media das colunas: ', arr2.mean(axis=0))
print('Media das linhas: ', arr2.mean(axis=1))
#4)MOSTRE  A QUANTIDADE  DE APARIÇÕES DE CADA UM DOS NÚMEROS NA MESMA.
print('Numero / quantidade que aparece:', np.unique(arr2, return_counts=True))
print('Numeros que aparecem 2 vezes ', np.unique(return_counts=True))


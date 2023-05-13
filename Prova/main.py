import numpy as np

ds = np.loadtxt('artists_v2.csv',
                delimiter=',',
                dtype=str,
                encoding='UTF-8'
                )

#1)
print(ds[0, :])
#colunaa 1
estadoUnido = ds[:, 1]
porcentagem = np.unique(estadoUnido, return_counts=True)
total = np.size(ds[1:, 1]) #TOTAL DE PAISES
#print(total)
#print(porcentagem) #ACHEI O VALOR DE ESTADOS UNIDOS (79)
print('1) Porcentagem de artistas que são deste pais é: ', 79/total*100, '%')
########################################################################################
#2)
#PROFESSOR AO MEU VER TINHA QUE USAR ALGUM COMANDO QUE PEGARIA A STRING '-present' E PROCURAR NO DATA SET COM O COMANDO ds[ds[1:2]== '-present'], MAS NÃO SEI QUAL COMANDO É.
period_active = ds[1:, 2]
contagem = period_active[period_active.astype(str) == '-present']
print(contagem)
procura = np.unique(period_active, return_counts=True)
print('2) Numero de artistas que não estão em atividade: ', procura)

########################################################################################
#3)
year = ds[1:, 3]
nome = ds[1:, 0]
pais = ds[1:, 1]
#print(year[92]) #DESCOBRI O ANO MAIOR ANALISANDO O ARRAY
print('3) ''nome: ', nome[92], 'pais:', pais[92])
########################################################################################
#4)
#ANALISAR A COLUNA SALES
sales = ds[:11, 6]
nomes = ds[:11, 0]
print('4) BANNER:')
for i in range(1, 11):
    print('{} lugar, nome: {}'.format(i, nomes[i]))

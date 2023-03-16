# COLEÇOES DO PYTHON
# 1 - TUPLA
#COLEÇÃO IMUTAVEL(NÃO PODE MUDAR ELEMENTOS)
'''
nomes = ('Goku','Vegeta', 'Gohan','trunks')
print(nomes)
'''
# 2 - LISTAS
#COLÇÃO MUTAVEL(PODE MUDAR ELEMENTOS)
'''
nomes = ['Goku','Vegeta', 'Gohan','trunks']
nomes.append('Kuririn') #INSERT DE DADOS
nomes[0] = 'Kuririn' #UPDATE DE DADOS
nomes.pop(3) #DELETA O 3 ELEMENTO
nomes.remove('Vegeta') #DELETE DE DADOS
print(nomes[1:3]) #De 1(inclusivo) a 3(exclusivo) 
print(nomes)
'''
# CONJUNTOS
# NÃO GUARDA INDICE
# NÃO GUARDA ELEMENTOS REPETIDOS
nomes = {'Goku','Vegeta', 'Gohan','trunks'}
nomes.add('Piccolo') #INSERT DE DADOS
nomes.remove('Trunks') #DELETE DE DADOS
print(nomes)


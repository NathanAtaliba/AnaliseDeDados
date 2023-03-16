'''
# COLEÇOES DO PYTHON
# 1 - TUPLA
#COLEÇÃO IMUTAVEL(NÃO PODE MUDAR ELEMENTOS)
nomes = ('Goku','Vegeta', 'Gohan','trunks')
print(nomes)
'''

'''
# 2 - LISTAS
#COLÇÃO MUTAVEL(PODE MUDAR ELEMENTOS)
nomes = ['Goku','Vegeta', 'Gohan','trunks']
nomes.append('Kuririn') #INSERT DE DADOS
nomes[0] = 'Kuririn' #UPDATE DE DADOS
nomes.pop(3) #DELETA O 3 ELEMENTO
nomes.remove('Vegeta') #DELETE DE DADOS
print(nomes[1:3]) #De 1(inclusivo) a 3(exclusivo) 
print(nomes)
'''

'''
# 3 - CONJUNTOS
# NÃO GUARDA INDICE
# NÃO GUARDA ELEMENTOS REPETIDOS
nomes = {'Goku','Vegeta', 'Gohan','trunks'}
nomes.add('Piccolo') #INSERT DE DADOS
nomes.remove('Trunks') #DELETE DE DADOS
print(nomes)
'''
'''
# 4 - DICIONARIOS
# INDICES CUSTOMIZADOS
pessoa = {
            'nome':'Nathan',
            'idade':42
         }
print(pessoa)
'''
#EXERCICIOS:
#1)
selecoes = ['Real Madrid','Barcelona','Corinthians','Bayer de Munchen','Al Ahly']
print(selecoes[:3]) #PRINT DOS TRES PRIMEIROS COLOCADOS
print(selecoes[3:]) #PRINT DOS DOIS ULTIMOS COLOCADOS
selecoes.sort()  #ORGANIZANDO ITENS EM ORDEM ALFABETICA
print(selecoes) #PRINT DA LISTA COM ITENS ORDENADOS
print(selecoes.index('Barcelona')) #PRINT POSIÇÃO DO BARCELONA NA LISTA

#2)
loja1 = {'Galaxy','Xiaomi'}
loja2 = {'Apple','Motorola'}
print('O total de itens da loja 1 é:' , len(loja1))
print('Voce podera comprar na loja 1, celulares das marcas: ', loja1)
print('O total de itens da loja 2 é:' ,len(loja2))
print('Voce podera comprar na loja 2, celulares das marcas: ', loja2)

#3)
numero = input('Entre com o numero de alunos: ')
DicionarioAlunos = {
                    #'nome': 'nome',
                    #'nota': 'nota',
                    #'situacao': 'situacao'
                    }
for i in numero:
    nome = input('Entre com o nome do aluno:')
    nota = input('Entre com a nota do aluno:')
    DicionarioAlunos




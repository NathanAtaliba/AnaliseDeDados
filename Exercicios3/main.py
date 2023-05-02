import numpy as np

ds = np.loadtxt(
                'space.csv',
                delimiter=';',
                dtype=str,
                encoding='UTF-8'
                )
#APRESENTE A PORCENTAGEM DE QUANTAS MISSÕES DERAM CERTO
print(ds[0, :])
#ANALISAR A COLUNA 7
contagemDeMissoes = ds[:, 7]
print(np.unique(contagemDeMissoes, return_counts=True))
totalDeMissoes = np.size(ds[1:, 7])
print('Porcentagem de missoes em sucesso:', (3879/totalDeMissoes)*100, '%')

#QUAL A MEDIA DE GASTOS DE UMA MISSÃO ESPACIAL SE BASEANDO EM MISSÕES QUE POSSUAM VALORES DISPONIVEIS >0?
#ANALISAR A COLUNA 6
contagemDeCusto = ds[1:, 6]
print(np.unique(contagemDeCusto, return_counts=True))
semZero = contagemDeCusto[contagemDeCusto.astype(float) > 0] #PEGANDO OS VALORES COM VALOR MAIOR QUE 0
media = np.mean(semZero.astype(float)) #TIRANDO A MEDIA DOS VALORES ACIMA DE ZERO
print('Media dos custos: ', media) #MOSTRANDO A MEDIA

#ENCONTRE QUANTAS MISSÕES ESPACIAIS NESTE DATASET FORAM REALIZADAS PELOS ESTADOS UNIDOS (EUA).
#ANALISAR A COLUNA 1
nomeUsa = np.size(ds[ds[0:, 1] == 'US Air Force']) #PEGANDO O TAMANHO DO ARRAY QUE CONTEM OS ESTADOS UNIDOS
print('Quantas missoes espaciais os EUA realizaram: ', nomeUsa)

#ENCONTRE QUAL FOI A MISSÃO MAIS CARA REALIZADA PELA EMPRESA 'SpaceX'
print(ds[0, :])
missao = ds[ds[:, 1] == 'SpaceX']
valorCaro = missao[:, 6]
print(missao)
print('Missao caro: ', valorCaro[23]) #ANALISADO NO VETOR

#MOSTRE O NOME DAS EMPRESAS QUE JA REALIZARAM MISSÕES ESPACIAIS JUNTAMENTE COM SUAS RESPECTIVAS QUANTIDADES DE MISSÕES (USE O FOR NO FINAL PARA MOSTRAR AS INFORMAÇÕES).
listaEmpresas = ds[ds[:, 7] == 'Success']
#print(listaEmpresas)
for i in listaEmpresas:
    print('nomes: ', listaEmpresas[i, 3])





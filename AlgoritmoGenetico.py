
import random
import numpy as np

T = 60                  #periodo
tamPopulacao = 2        #quatidade de individuos da população 
tamIndividuo = 3        #quatidade de rotas
tamCromossomo = 4       #tipos de veiculos
probCruzamento = 0.95   #probabilidade de cruzamento
probMutacao = 0.1       #probabilidade de mutação
numGeracoes = 1



#iniciando uma população aleatoria
individuo = []   #uma solução
populacao = []  #conjunto de soluções

for k in range(tamPopulacao): #tamanho da população

    for i in range(tamIndividuo): #linha individuo
        linhaIndividuo = []
        for j in range(tamCromossomo): #coluna individuo
            linhaIndividuo.append(random.randint(0,T))
        individuo.append(linhaIndividuo) 

populacao.append(individuo)


#imprimindo a população
print("\n __Populacao aleatoria__")
for i in individuo:
    print(i, end="\n")
print("_"*20)




"""
#variaveis do AG
aptidao = np.zeros(tamPopulacao)
novaGeracao = np.zeros((tamPopulacao, tamCromossomo))
novaPopulacao = np.zeros((tamPopulacao, tamCromossomo))

#iniciando AG
geracoes = 1
while (geracoes<=numGeracoes):
    novosIndividuos = 0
    while (novosIndividuos<(tamPopulacao-1)): 

        #calculo da aptidao dos individuos 
        totalAptidao = 0
        for i in range(tamPopulacao):
            for j in range(tamCromossomo):
                novaPopulacao[i][j] = ((populacao[i][j] *100) + 1000)
                aptidao[i] = novaPopulacao[i][j]
            totalAptidao = aptidao[i] + totalAptidao

        #print(totalAptidao)

        
        #população apos o fitness
        print("\n")
        for i in novaPopulacao:
            print(i, end="\n")
        

        #identificando a probabilidade de cada individuo
        probIndividuo = np.zeros(tamPopulacao) #probabilidade do individuo
        probIndividuoTotal = np.zeros(tamPopulacao)  #probabilidade do individuo total
        probIndividuo = (1/totalAptidao)*aptidao


        #roleta
        for i in range(tamPopulacao):
            if (i==0):
                probIndividuoTotal[i] = probIndividuo[i]
            else:
                probIndividuoTotal[i] = probIndividuo[i] + probIndividuoTotal[i-1]

        #print("probTotal: ", probIndividuoTotal)

        #sorteando os pais de acordo com a probabilidade
        roleta1 = random.uniform(0, 1)
        i=0
        while (roleta1>probIndividuoTotal[i]):
            i=i+1
        pai1=i

        roleta2 = random.uniform(0, 1)
        i=0
        while (roleta2>probIndividuoTotal[i]):
            i=i+1
        pai2=i

        while (pai2==pai1):
            roleta2 = random.uniform(0, 1)
            i=0
            while (roleta2>probIndividuoTotal[i]):
                i=i+1
            pai2=i

        print("pa1 ", pai1)
        print("pa2 ", pai2)

        #operação de Crossover
        if (probCruzamento>random.uniform(0, 1)):
            pontoCorte = round(1+(tamCromossomo-2)*random.uniform(0, 1))
            print("pc ", pontoCorte)
            gene11 = populacao[pai1][0:pontoCorte]
            print("g1 ",gene11)
            gene12 = populacao[pai1][pontoCorte:tamCromossomo]
            print("g2 ",gene12)
            gene21 = populacao[pai2][0:pontoCorte]
            print("g3 ", gene21)
            gene22 = populacao[pai2][pontoCorte:tamCromossomo]
            print("g4 ", gene22)
            filho1 = np.concatenate((gene11,gene22), axis=None)
            filho2 = np.concatenate((gene21,gene12), axis=None)

            novaGeracao[novosIndividuos,:] = filho1
            novosIndividuos = novosIndividuos+1
            novaGeracao[novosIndividuos,:] = filho2
            novosIndividuos = novosIndividuos+1

        #print("ng ", novaGeracao)

        #mutação
        if (probMutacao>random.uniform(0, 1)):            
            d = round(1+ (tamCromossomo-2)*random.uniform(0, 1))
            if (novaGeracao[novosIndividuos-2][d] == 0):
                novaGeracao[novosIndividuos-2][d] = 1
            else:
                novaGeracao[novosIndividuos-2][d] = 0
            if (novaGeracao[novosIndividuos-1][d] == 0):
                novaGeracao[novosIndividuos-1][d] = 1
            else:
                novaGeracao[novosIndividuos-1][d] = 0

        
    populacao = novaGeracao
    geracoes=geracoes+1





#nova geracao apos o AG
print("\n ___ Nova Geracao___")
for i in populacao:
    print(i, end="\n")


"""
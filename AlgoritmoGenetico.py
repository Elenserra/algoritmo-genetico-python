
import random
import numpy as np

T = 60                  #periodo
tamPopulacao = 2        #quatidade de individuos da população 
tamIndividuo = 3        #quatidade de rotas
tamCromossomo = 4       #tipos de veiculos
probCruzamento = 0.95   #probabilidade de cruzamento
probMutacao = 0.1       #probabilidade de mutação
numGeracoes = 1         #número de gerações



#iniciando uma população aleatoria
individuo = np.zeros((tamIndividuo, tamCromossomo))  #uma solução
populacao = []  #conjunto de soluções


for k in range(tamPopulacao): #tamanho da população
    #cria um individuo, sorteando valores aleatorios
    individuo = np.random.randint(T, size=(tamIndividuo, tamCromossomo)) 
    populacao.append(individuo) #adiciona esse individuo na populacao


#imprimindo a população
print("\n __Populacao aleatoria__")
for i in populacao:
    print(i, end="\n")
print("_"*20)


#variaveis do AG
aptidao = []
novaGeracao = np.zeros((tamIndividuo, tamCromossomo))
novaPopulacao = []
individuo=[]

#iniciando AG
geracoes = 1
while (geracoes<=numGeracoes):
    cont = 0 
    while (cont<(tamPopulacao-1)): 

        #calculo da aptidao dos individuos 
        totalAptidao = 0
        for i in populacao:
            novaPopulacao.append(((i*100) + 1000))
        aptidao = sum(novaPopulacao) #soma das aptidoes 
        #print(aptidao)
        
        for i in aptidao:
            totalAptidao = totalAptidao+i
        totalAptidao = sum(totalAptidao) #total da aptidao da populacao
        

        #imprimi a população apos o fitness
        print("\n __Populacao com fitness__")
        for i in novaPopulacao:
            print(i, end="\n")
        print("_"*20, "\n")
        
        
        #identificando a probabilidade de cada individuo
        probIndividuo = np.zeros((tamIndividuo)) #probabilidade do individuo
        probIndividuoTotal = np.zeros((tamIndividuo))  #probabilidade do individuo total
        probIndividuo = sum((1/totalAptidao)*aptidao)


        #roleta
        for i in range(tamIndividuo):
            if (i==0):
                probIndividuoTotal[i] = probIndividuo[i]
            else:
                probIndividuoTotal[i] = probIndividuo[i] + probIndividuoTotal[i-1]

        print("probTotal: ", probIndividuoTotal)

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




"""
#nova geracao apos o AG
print("\n ___ Nova Geracao___")
for i in populacao:
    print(i, end="\n")
"""

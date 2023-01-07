
import random
import numpy as np

T = 60                    #periodo
tamPopulacao = 6          #quantidade de individuos da população 
rotas = 3                 #quantidade de rotas
tipoVeiculos = 3          #tipos de veiculos
probCruzamento = 0.95     #probabilidade de cruzamento
probMutacao = 0.1         #probabilidade de mutação
numGeracoes = 1           #número de gerações
qntdVeiculos = [96,54,43]  # ft_b - veiculos disponiveis para cada tipo 

K = [100, 45, 67]
S = 10


#iniciando uma população aleatoria
populacao = []  

individuoPai = np.zeros((tipoVeiculos, rotas))
for b in range(tipoVeiculos):
  for r in range(rotas):
    individuoPai[b][r] = random.randint(0, qntdVeiculos[b])
populacao.append(individuoPai)

#cria um individuo, sorteando valores sem ultrapassar o individuoPai 
for i in range(tamPopulacao-1): 
    individuo = np.zeros((tipoVeiculos, rotas))
    for b in range(tipoVeiculos):
        for r in range(rotas):
            individuo[b][r] = random.randint(0, individuoPai[b][r])
    populacao.append(individuo) 


#imprimindo a população
print("\n __Populacao aleatoria__")
for individuo in populacao:
    print(individuo, end="\n")
print("_"*20)



viavel = True

for i in range(tamPopulacao):
    print("Individuo ",(i+1))
    individuo = populacao[i] 
    for b in range(tipoVeiculos):
        soma=0
        for r in range(rotas):  
            soma = soma +  individuo[b][r]
        print("Foram enviados ", soma, "veiculos do tipo", b)

        H_br = np.zeros((tipoVeiculos, rotas))

        # checar se veiculosEnviados nao ultrapassa a frota
        if soma > qntdVeiculos[b]:
            viavel=False
            break
        else:
            viavel=True
            for b in range(tipoVeiculos):
                for r in range(rotas):
                    if individuo[b][r]==0:
                        H_br[b][r]=0
                    else:
                        H_br[b][r] = T/individuo[b][r]
    print()
    if viavel:

        #custo operacional 
        co=0
        for b in range(tipoVeiculos):
            for r in range(rotas):
                co = co + (K[b] * (individuo[b][r]))

        cs=0                              
        #custo social
        for b in range(tipoVeiculos):
            for r in range(rotas):
                cs = cs + (S * (H_br[b][r]))               
                
        #fitness
        fitness = co + cs
        print("\nFitness: ", fitness)

    print("\n")

                        
    
    
            



'''
#variaveis do AG
aptidao = []
novaGeracao = np.zeros((rotas, tipoVeiculos))
novaPopulacao = []

#quantidade total de veículos do tipo b ∈ B disponíveis
#for k in range(tamPopulacao):
for i in range(rotas):
    somaVeiculos=0
    for j in range(tipoVeiculos):
        somaVeiculos=somaVeiculos + individuo[i][j]
        #print(individuo[i][j], end=" ")

#iniciando AG
geracoes = 1
while (geracoes<=numGeracoes):
    cont = 0 
    while (cont<(tamPopulacao-1)): 

        #calculo da aptidao dos individuos 
        for i in populacao:
            novaPopulacao.append(((i*100) + 1000))#calcula para cada individuo a aptdidao
        totalAptidao = sum(sum(sum(novaPopulacao))) #soma total da aptidao da populacao
        #print(totalAptidao)

        totalAptidaoInd = 0
        for i in range(tamPopulacao):
            totalAptidaoInd = sum(sum(novaPopulacao[i]))#total de aptidao por individuo
            #print(("totalAptidaoInd", totalAptidaoInd))

        #imprimi a população apos o fitness
        
        print("\n __Populacao com fitness__")
        for i in novaPopulacao:
            print(i, end="\n")
        print("_"*20, "\n")
        
        
        #identificando a probabilidade de cada individuo ser selecionado
        probIndividuoTotal = np.zeros((tamPopulacao))  #probabilidade do individuo total
        probIndividuo = (1/totalAptidao)*totalAptidaoInd
        #print("probIndividuo", probIndividuo)

        #roleta
        for i in range(tamPopulacao):
            if (i==0):
                probIndividuoTotal[i] = probIndividuo
            else:
                probIndividuoTotal[i] = probIndividuo + probIndividuoTotal[i-1]

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

        #print("pa1 ", pai1)
        #print("pa2 ", pai2)

        #operação de Crossover
        
        if (probCruzamento>random.uniform(0, 1)):
            pontoCorte = round(1+(tipoVeiculos-2)*random.uniform(0, 1))
            #print("pc ", pontoCorte)
            gene11 = populacao[pai1][0:pontoCorte]
            #print("g1 ",gene11)
            gene12 = populacao[pai1][pontoCorte:tipoVeiculos]
            #print("g2 ",gene12)
            gene21 = populacao[pai2][0:pontoCorte]
            #print("g3 ", gene21)
            gene22 = populacao[pai2][pontoCorte:tipoVeiculos]
            #print("g4 ", gene22)
            filho1 = np.concatenate((gene11,gene22), axis=None)
            filho2 = np.concatenate((gene21,gene12), axis=None)

            novaGeracao[novosIndividuos,:] = filho1
            novosIndividuos = novosIndividuos+1
            novaGeracao[novosIndividuos,:] = filho2
            novosIndividuos = novosIndividuos+1

        #print("ng ", novaGeracao)

        #mutação
        if (probMutacao>random.uniform(0, 1)):            
            d = round(1+ (tipoVeiculos-2)*random.uniform(0, 1))
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

'''

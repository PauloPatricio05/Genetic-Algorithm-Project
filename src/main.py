from algoritmo import new_population, rosenbrock, sphere, rastrigin
import random
from utils import crossing, mutation, cut, nova_mutacao


newpopulation = new_population(10,30,-100,100)# deixar fora do for

fitness = []
populacao_avaliada = []
o = 0

#Criando a lista do fitness
for i in newpopulation:
    fitness.append(sphere(i))
    populacao_avaliada.append({
       
    "individuo": newpopulation[o],
    "fitness": fitness[o]

    })
    o += 1


populacao_selecionada = []

#Selecionando os individuos mais aptos
for i in range(len(fitness)):
    # escolhe 2 indivíduos aleatórios
    a, b = random.sample(populacao_avaliada, 2)

    # compara fitness (menor é melhor no sphere)
    if a["fitness"] < b["fitness"]:
        vencedor = a
    else:
        vencedor = b

    populacao_selecionada.append(vencedor)

newpopulation = []
for i in range(0,len(populacao_selecionada),2):
    i1 = populacao_selecionada[i]
    i2 = populacao_selecionada[i+1]
    filho1,filho2= cut(i1['individuo'],i2['individuo'])
    newpopulation.append(filho1)
    newpopulation.append(filho2)

count = 0
for _ in range(10000):
    if crossing(0.9):
        count += 1
print(count)
count = 0
for _ in range(10000):
    if mutation(0.1):
        count += 1
print(count)



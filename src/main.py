from algoritmo import new_population, rosenbrock, sphere, rastrigin
import random
from utils import crossing, mutation, cut, nova_mutacao


newpopulation = new_population(10,30,-100,100)
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

print(populacao_selecionada)


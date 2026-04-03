# Funções do algoritmo genético
import random

#Função População 
def new_population(size,dimensao,min_val,max_val):

    population = []

    for _ in range(size):
        individuo = [random.uniform(min_val,max_val) for _ in range(dimensao)]
        population.append(individuo)

    return population

# Test
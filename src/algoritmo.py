# Funções do algoritmo genético
import random
import math



def new_population(size, dimensao, min_val, max_val):

    population = []

    for _ in range(size):
        individuo = [random.uniform(min_val, max_val) for _ in range(dimensao)]
        population.append(individuo)

    return population



def rosenbrock(x):
 
    # Interrompe o código se o indivíduo não tiver 30 gene.
    assert len(x) == 30, f"Erro: O indivíduo deve ter 30 dimensões."
    return sum(100 * (x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(len(x)-1))



def sphere(x):
    # Soma o quadrado de cada elemento xi dentro da lista x

    return sum(xi**2 for xi in x)



def rastrigin(x):

    A = 10
    n = len(x)
    # A fórmula é: A*n + somatório de (xi^2 - A * cos(2 * pi * xi))
    soma = sum(xi**2 - A * math.cos(2 * math.pi * xi) for xi in x)
    return A * n + soma


def selecao_roleta(populacao_avaliada, tam_pop):
    # Para minimização, fitness menores devem ter fatias maiores.
    # Dessa forma, usamos (Max_Fitness + Min_Fitness) - Fitness_Individuo
    fitness_valores = [ind['fitness'] for ind in populacao_avaliada]
    max_f = max(fitness_valores)
    min_f = min(fitness_valores)
    
    # Criamos uma lista de "aptidão ajustada" para que o menor fitness tenha o maior valor
    # Somamos um pequeno valor (0.0001) para evitar que o pior indivíduo tenha chance zero
    aptidao_ajustada = [(max_f - f) + (max_f - min_f) * 0.1 + 0.0001 for f in fitness_valores]
    
    total_aptidao = sum(aptidao_ajustada)
    # Calcula as probabilidades (fatias da roleta)
    probabilidades = [a / total_aptidao for a in aptidao_ajustada]
    
    # Seleciona os novos indivíduos com base nas probabilidades
    selecionados = random.choices(populacao_avaliada, weights=probabilidades, k=tam_pop)
    return selecionados
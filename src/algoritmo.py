# Funções do algoritmo genético
import random


# Função População
def new_population(size, dimensao, min_val, max_val):

    population = []

    for _ in range(size):
        individuo = [random.uniform(min_val, max_val) for _ in range(dimensao)]
        population.append(individuo)

    return population

# Função rosenbrock

def rosenbrock(x):
    """
    A função desempenha o papel de Fitness Function.

    O objetivo da função Rosenbrock é a minimização. O melhor indivíduo possível retornará o valor 0 (que ocorre quando todas as dimensões são iguais a 1).
    
    """
    # Interrompe o código se o indivíduo não tiver 30 gene.
    assert len(x) == 30, f"Erro: O indivíduo deve ter 30 dimensões."
    return sum(100 * (x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(len(x)-1))
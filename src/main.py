from algoritmo import new_population, rosenbrock, sphere, rastrigin

from utils import crossing, mutation, cut, nova_mutacao

# Ponto de entrada/Código principal

variavel = new_population(10,10,-100,101)

print(variavel)

# Implementação da função fitness rosenbrock: 

# 1. Cria a população com os parâmetros corretos:
# tamanho da população = 30, dimensões = 30, limites = -5.12 a 5.12)
minha_populacao = new_population(30, 30, -5.12, 5.12)

# 2. Separar um indivíduo da população para testar vamo pegar o primeiro
individuo_bom = minha_populacao[0]

# 3. Agora passamos esse indivíduo para a função
resultado_fitness = rosenbrock(individuo_bom)

# 4. Imprimir apenas um indivíduo:
print("Tamanho do indivíduo:", len(individuo_bom))
print("Nota desse indivíduo:", resultado_fitness)

# 5. Para imprimir todos os indivíduos:
for i in range(len(minha_populacao )):
    individuo_atual = minha_populacao[i]
    nota = rosenbrock(individuo_atual)
    print(f" O Indivíduo {i} tirou a nota: {nota:.0f}")





#Implementação da função Sphere
print("\nFitness da função Sphere: \n")
test_sphere = new_population(30,10,-5,5)

for i in range (30):
   # Usei o f-string para o print ficar limpo e sem espaços extras
   print(f"{i+1}° Valor ({sphere(test_sphere[i])})")





#Implementação da função Rastrigin
print("\nFitness da função Rastrigin: \n")

test_rastrigin = new_population(30, 10, -5, 5)

for i in range(30):
    # Usei o f-string para o print ficar limpo e sem espaços extras
    print(f"{i+1}° Valor ({rastrigin(test_rastrigin[i])})")
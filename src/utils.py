# Funções auxiliares
import random


def crossing(rate: float):
    """
    Compara a taxa de cruzamento definida pelo usuário com a taxa aleatória para dizr se vai haver ou não o cruzamento de indivúduos.

    Args:
        rate (float): taxa de cruzamento. ex.: 0.1 = 10%

    Returns:
        True: para haver o cruzamento.
        False: para não haver cruzamento.
    """
    rate_random = random.uniform(0, 1)
    if rate_random >= rate:
        return True
    else:
        return False


def mutation(rate: float):
    """
    Compara a taxa de cruzamento definida pelo usuário com a taxa aleatória para dizr se vai haver ou não o cruzamento de indivúduos.

    Args:
        rate (float): taxa de cruzamento. ex.: 0.1 = 10%

    Returns:
        True: para haver o cruzamento.
        False: para não haver cruzamento.
    """
    rate_random = random.uniform(0, 1)
    if rate_random >= rate:
        return True
    else:
        return False

def cut(individuo1: list, individuo2: list):
    """
    Funçao de corte aleatório para a geração de novos filhos.

    Args:
        individuo1: pai1
        individuo2: pai2

    Returns:
        filho1: filho resultado do corte do pai1 + pai2.
        filho2: filho resultado do corte do pai2 + pai1.
        
    Ex.:
       filho1, filho2 = cut(pai1, pai2)
    """
    ponto = random.randint(1, len(individuo1) - 1)

    filho1 = individuo1[:ponto] + individuo2[ponto:]
    filho2 = individuo2[:ponto] + individuo1[ponto:]

    return filho1, filho2

def nova_mutacao(pai1, pai2):
    """
    Combina dois indivíduos (pais) para gerar dois novos indivíduos (filhos).
    Utiliza a técnica de corte em 1 ponto.
    """
    # Garante que ambos os pais são válidos
    assert len(pai1) == len(pai2) == 30, "Erro: Os pais devem ter exatamente 30 dimensões."
    ponto_corte = random.randint(1, 29)

    # Misturamos as metades usando o fatiamento [:]
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]

    return filho1, filho2
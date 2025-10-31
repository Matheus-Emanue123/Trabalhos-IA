"""
Implementação de algoritmos Hill Climbing para o problema das 8 Rainhas.

Autor: Matheus Emanuel
Disciplina: Inteligência Artificial - CEFET-MG
Data: 2025
"""

import random
import time
from typing import List, Tuple, Dict


# ============================================================================
# FUNÇÕES BÁSICAS - REPRESENTAÇÃO E AVALIAÇÃO
# ============================================================================

def gerar_estado_aleatorio(n: int = 8) -> List[int]:
    """
    Gera um estado inicial aleatório para o problema das N rainhas.
    
    Args:
        n: Tamanho do tabuleiro (padrão: 8)
    
    Returns:
        Lista representando posições das rainhas.
        Exemplo: [3, 5, 7, 1, 4, 6, 0, 2]
        Índice = coluna, Valor = linha da rainha
    """
    return [random.randint(0, n - 1) for _ in range(n)]


def calcular_conflitos(estado: List[int]) -> int:
    """
    Calcula o número de pares de rainhas que se atacam.
    
    Um par de rainhas se ataca se:
    - Estão na mesma linha (horizontal)
    - Estão na mesma diagonal
    
    Não verificamos coluna porque cada coluna tem exatamente 1 rainha.
    
    Args:
        estado: Lista representando as posições das rainhas
    
    Returns:
        Número de pares em conflito (objetivo: 0)
    
    Exemplo:
        estado = [0, 1, 2, 3, 4, 5, 6, 7]  # Todas na diagonal
        conflitos = 28 (todas se atacam)
    """
    conflitos = 0
    n = len(estado)
    
    # Verifica cada par de rainhas
    for i in range(n):
        for j in range(i + 1, n):
            # Conflito horizontal (mesma linha)?
            if estado[i] == estado[j]:
                conflitos += 1
            
            # Conflito diagonal?
            # Se a distância horizontal == distância vertical, estão na diagonal
            distancia_horizontal = abs(i - j)
            distancia_vertical = abs(estado[i] - estado[j])
            
            if distancia_horizontal == distancia_vertical:
                conflitos += 1
    
    return conflitos


def gerar_vizinhos(estado: List[int]) -> List[List[int]]:
    """
    Gera todos os estados vizinhos do estado atual.
    
    Um vizinho é criado movendo UMA rainha para outra linha (na mesma coluna).
    
    Args:
        estado: Estado atual
    
    Returns:
        Lista com todos os vizinhos possíveis (56 para 8 rainhas)
    
    Exemplo:
        estado = [3, 5, 7, 1, 4, 6, 0, 2]
        Gera 56 vizinhos (8 colunas × 7 linhas possíveis por coluna)
    """
    vizinhos = []
    n = len(estado)
    
    # Para cada coluna
    for coluna in range(n):
        # Para cada linha possível
        for nova_linha in range(n):
            # Se não é a linha atual (não queremos o estado igual)
            if nova_linha != estado[coluna]:
                # Cria um novo estado (cópia do atual)
                vizinho = estado.copy()
                # Move a rainha para a nova linha
                vizinho[coluna] = nova_linha
                vizinhos.append(vizinho)
    
    return vizinhos


def encontrar_melhor_vizinho(vizinhos: List[List[int]]) -> Tuple[List[int], int]:
    """
    Encontra o vizinho com menor número de conflitos.
    
    Args:
        vizinhos: Lista de estados vizinhos
    
    Returns:
        Tupla (melhor_vizinho, conflitos_do_melhor)
    """
    melhor_vizinho = vizinhos[0]
    melhor_conflitos = calcular_conflitos(melhor_vizinho)
    
    # Procura o vizinho com menos conflitos
    for vizinho in vizinhos[1:]:
        conflitos = calcular_conflitos(vizinho)
        if conflitos < melhor_conflitos:
            melhor_vizinho = vizinho
            melhor_conflitos = conflitos
    
    return melhor_vizinho, melhor_conflitos


def imprimir_tabuleiro(estado: List[int], titulo: str = "Tabuleiro"):
    """
    Imprime uma representação visual do tabuleiro.
    
    Args:
        estado: Estado a ser impresso
        titulo: Título da visualização
    """
    n = len(estado)
    print(f"\n{titulo}")
    print("=" * (n * 4 + 1))
    
    for linha in range(n):
        print("|", end="")
        for coluna in range(n):
            if estado[coluna] == linha:
                print(" Q |", end="")
            else:
                print("   |", end="")
        print()
        print("-" * (n * 4 + 1))
    
    conflitos = calcular_conflitos(estado)
    print(f"Conflitos: {conflitos}")


# ============================================================================
# ALGORITMO 1: HILL CLIMBING BÁSICO
# ============================================================================

def hill_climbing_basico(max_iteracoes: int = 1000, verbose: bool = False) -> Dict:

    # Estado inicial aleatório
    estado_atual = gerar_estado_aleatorio()
    conflitos_atual = calcular_conflitos(estado_atual)
    
    tempo_inicio = time.time()
    iteracoes = 0
    
    if verbose:
        print("\n" + "="*60)
        print("HILL CLIMBING BÁSICO")
        print("="*60)
        imprimir_tabuleiro(estado_atual, "Estado Inicial")
    
    # Loop principal
    while conflitos_atual > 0 and iteracoes < max_iteracoes:
        iteracoes += 1
        
        # Gera todos os vizinhos
        vizinhos = gerar_vizinhos(estado_atual)
        
        # Encontra o melhor vizinho
        melhor_vizinho, melhor_conflitos = encontrar_melhor_vizinho(vizinhos)
        
        # Se o melhor vizinho NÃO é melhor que o atual, PARA!
        if melhor_conflitos >= conflitos_atual:
            if verbose:
                print(f"\nIteração {iteracoes}: Máximo local atingido!")
                print(f"Conflitos: {conflitos_atual} → Não há melhora")
            break
        
        # Move para o melhor vizinho
        estado_atual = melhor_vizinho
        conflitos_atual = melhor_conflitos
        
        if verbose and iteracoes % 10 == 0:
            print(f"Iteração {iteracoes}: Conflitos = {conflitos_atual}")
    
    tempo_total = time.time() - tempo_inicio
    sucesso = (conflitos_atual == 0)
    
    if verbose:
        imprimir_tabuleiro(estado_atual, "Estado Final")
        print(f"\nResultado: {'SUCESSO! ✓' if sucesso else 'FALHA (máximo local)'}")
        print(f"Iterações: {iteracoes}")
        print(f"Tempo: {tempo_total:.6f} segundos")
    
    return {
        'estado_final': estado_atual,
        'conflitos': conflitos_atual,
        'iteracoes': iteracoes,
        'tempo': tempo_total,
        'sucesso': sucesso
    }


# ============================================================================
# ALGORITMO 2: HILL CLIMBING COM MOVIMENTOS LATERAIS
# ============================================================================

def hill_climbing_com_laterais(max_iteracoes: int = 1000, 
                                max_laterais: int = 100,
                                verbose: bool = False) -> Dict:
   
    estado_atual = gerar_estado_aleatorio()
    conflitos_atual = calcular_conflitos(estado_atual)
    
    tempo_inicio = time.time()
    iteracoes = 0
    laterais_consecutivos = 0
    
    if verbose:
        print("\n" + "="*60)
        print("HILL CLIMBING COM MOVIMENTOS LATERAIS")
        print("="*60)
        imprimir_tabuleiro(estado_atual, "Estado Inicial")
    
    while conflitos_atual > 0 and iteracoes < max_iteracoes:
        iteracoes += 1
        
        vizinhos = gerar_vizinhos(estado_atual)
        melhor_vizinho, melhor_conflitos = encontrar_melhor_vizinho(vizinhos)
        
        # DIFERENÇA: Aceita se melhor OU IGUAL (movimento lateral)
        if melhor_conflitos > conflitos_atual:
            # Pior que o atual → PARA!
            if verbose:
                print(f"\nIteração {iteracoes}: Máximo local atingido!")
                print(f"Conflitos: {conflitos_atual}")
            break
        
        # Verifica se é movimento lateral
        if melhor_conflitos == conflitos_atual:
            laterais_consecutivos += 1
            if verbose and laterais_consecutivos % 10 == 0:
                print(f"Iteração {iteracoes}: Movimento lateral {laterais_consecutivos}/{max_laterais}")
            
            # Limite de laterais atingido?
            if laterais_consecutivos >= max_laterais:
                if verbose:
                    print(f"\nLimite de movimentos laterais atingido!")
                    print(f"Conflitos: {conflitos_atual}")
                break
        else:
            # Melhorou! Reseta contador de laterais
            laterais_consecutivos = 0
            if verbose and iteracoes % 10 == 0:
                print(f"Iteração {iteracoes}: Conflitos = {conflitos_atual} → {melhor_conflitos}")
        
        estado_atual = melhor_vizinho
        conflitos_atual = melhor_conflitos
    
    tempo_total = time.time() - tempo_inicio
    sucesso = (conflitos_atual == 0)
    
    if verbose:
        imprimir_tabuleiro(estado_atual, "Estado Final")
        print(f"\nResultado: {'SUCESSO! ✓' if sucesso else 'FALHA'}")
        print(f"Iterações: {iteracoes}")
        print(f"Movimentos laterais: {laterais_consecutivos}")
        print(f"Tempo: {tempo_total:.6f} segundos")
    
    return {
        'estado_final': estado_atual,
        'conflitos': conflitos_atual,
        'iteracoes': iteracoes,
        'laterais': laterais_consecutivos,
        'tempo': tempo_total,
        'sucesso': sucesso
    }


# ============================================================================
# ALGORITMO 3: RANDOM-RESTART HILL CLIMBING
# ============================================================================

def random_restart_hill_climbing(max_reinicio: int = 100,
                                  usar_laterais: bool = True,
                                  max_laterais: int = 100,
                                  verbose: bool = False) -> Dict:

    tempo_inicio = time.time()
    
    melhor_estado = None
    melhor_conflitos = float('inf')
    iteracoes_total = 0
    tentativa = 0
    
    if verbose:
        print("\n" + "="*60)
        print("RANDOM-RESTART HILL CLIMBING")
        print("="*60)
        tipo = "com laterais" if usar_laterais else "básico"
        print(f"Usando Hill Climbing {tipo}")
        print(f"Máximo de reinícios: {max_reinicio}")
        print("="*60)
    
    # Loop de reinícios
    while tentativa <= max_reinicio:
        tentativa += 1
        
        if verbose:
            print(f"\n--- Tentativa {tentativa} ---")
        
        # Executa uma tentativa de Hill Climbing
        if usar_laterais:
            resultado = hill_climbing_com_laterais(
                max_iteracoes=1000,
                max_laterais=max_laterais,
                verbose=False  # Não imprime cada tentativa
            )
        else:
            resultado = hill_climbing_basico(
                max_iteracoes=1000,
                verbose=False
            )
        
        iteracoes_total += resultado['iteracoes']
        
        if verbose:
            print(f"Conflitos: {resultado['conflitos']}")
        
        # Atualiza melhor resultado
        if resultado['conflitos'] < melhor_conflitos:
            melhor_estado = resultado['estado_final']
            melhor_conflitos = resultado['conflitos']
            
            if verbose:
                print(f"Novo melhor: {melhor_conflitos} conflitos")
        
        # Encontrou solução?
        if resultado['sucesso']:
            if verbose:
                print(f"\n✓ SOLUÇÃO ENCONTRADA na tentativa {tentativa}!")
            break
    
    tempo_total = time.time() - tempo_inicio
    sucesso = (melhor_conflitos == 0)
    
    if verbose:
        print("\n" + "="*60)
        print("RESULTADO FINAL")
        print("="*60)
        imprimir_tabuleiro(melhor_estado, "Melhor Solução Encontrada")
        print(f"\nStatus: {'SUCESSO! ✓' if sucesso else 'FALHA'}")
        print(f"Reinícios usados: {tentativa}")
        print(f"Iterações totais: {iteracoes_total}")
        print(f"Tempo total: {tempo_total:.6f} segundos")
    
    return {
        'estado_final': melhor_estado,
        'conflitos': melhor_conflitos,
        'reinicio': tentativa,
        'iteracoes_total': iteracoes_total,
        'tempo': tempo_total,
        'sucesso': sucesso
    }
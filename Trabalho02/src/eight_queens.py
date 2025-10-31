import time
import os
import gc
import ctypes
import psutil
import numpy as np
from hill_climbing import (
    hill_climbing_basico,
    hill_climbing_com_laterais,
    random_restart_hill_climbing,
    imprimir_tabuleiro
)
from visualizacao import gerar_graficos

def process_memory():
  
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def clear_cache():
    
    # Força coleta de lixo
    gc.collect()
    gc.collect()
    gc.collect()
    
    # Pausa para garantir limpeza
    time.sleep(0.1)
    
    # Limpa working set (Windows)
    try:
        if os.name == 'nt':
            ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)
    except:
        pass


def executar_com_cold_cache(algoritmo_func, **kwargs):
  
    # Limpa cache antes da execução
    clear_cache()
    
    # Mede memória antes
    mem_antes = process_memory()
    
    # Executa o algoritmo
    resultado = algoritmo_func(**kwargs)
    
    # Mede memória depois
    mem_depois = process_memory()
    memoria_usada = mem_depois - mem_antes
    
    # Adiciona métrica de memória ao resultado
    resultado['memoria_usada'] = memoria_usada
    
    return resultado


def imprimir_estatisticas(nome_algoritmo, resultados):
  
    # Extrai métricas
    tempos = [r['tempo'] for r in resultados]
    memorias = [r['memoria_usada'] for r in resultados]
    iteracoes = [r.get('iteracoes', r.get('iteracoes_total', 0)) for r in resultados]
    conflitos = [r['conflitos'] for r in resultados]
    sucessos = [r['sucesso'] for r in resultados]
    
    # Calcula estatísticas
    taxa_sucesso = (sum(sucessos) / len(sucessos)) * 100
    
    avg_tempo = np.mean(tempos)
    std_tempo = np.std(tempos)
    min_tempo = np.min(tempos)
    max_tempo = np.max(tempos)
    
    avg_memoria = np.mean(memorias)
    std_memoria = np.std(memorias)
    min_memoria = np.min(memorias)
    max_memoria = np.max(memorias)
    
    avg_iteracoes = np.mean(iteracoes)
    avg_conflitos = np.mean(conflitos)
    
    # Estatísticas específicas por algoritmo
    if 'reinicio' in resultados[0]:
        reinicio = [r['reinicio'] for r in resultados]
        avg_reinicio = np.mean(reinicio)
        std_reinicio = np.std(reinicio)
        min_reinicio = np.min(reinicio)
        max_reinicio = np.max(reinicio)
    
    if 'laterais' in resultados[0]:
        laterais = [r['laterais'] for r in resultados]
        avg_laterais = np.mean(laterais)
    
    # Imprime estatísticas
    print(f"\n{'='*70}")
    print(f"ESTATÍSTICAS - {nome_algoritmo} (10 execuções em Cold Cache)")
    print(f"{'='*70}")
    
    print(f"\n TAXA DE SUCESSO:")
    print(f"   • Taxa: {taxa_sucesso:.1f}% ({sum(sucessos)}/10 execuções)")
    
    print(f"\n  TEMPO DE EXECUÇÃO:")
    print(f"   • Média: {avg_tempo:.6f} segundos")
    print(f"   • Desvio Padrão: {std_tempo:.6f} segundos")
    print(f"   • Mínimo: {min_tempo:.6f} segundos")
    print(f"   • Máximo: {max_tempo:.6f} segundos")
    
    print(f"\n MEMÓRIA CONSUMIDA:")
    print(f"   • Média: {avg_memoria:,.0f} bytes ({avg_memoria/1024:.2f} KB)")
    print(f"   • Desvio Padrão: {std_memoria:,.0f} bytes ({std_memoria/1024:.2f} KB)")
    print(f"   • Mínima: {min_memoria:,.0f} bytes ({min_memoria/1024:.2f} KB)")
    print(f"   • Máxima: {max_memoria:,.0f} bytes ({max_memoria/1024:.2f} KB)")
    
    print(f"\n ITERAÇÕES:")
    print(f"   • Média: {avg_iteracoes:.1f} iterações")
    
    if 'reinicio' in resultados[0]:
        print(f"\n REINÍCIOS (Random-Restart):")
        print(f"   • Média: {avg_reinicio:.1f} reinícios")
        print(f"   • Desvio Padrão: {std_reinicio:.2f}")
        print(f"   • Mínimo: {min_reinicio} reinícios")
        print(f"   • Máximo: {max_reinicio} reinícios")
    
    if 'laterais' in resultados[0]:
        print(f"\n↔  MOVIMENTOS LATERAIS:")
        print(f"   • Média: {avg_laterais:.1f} movimentos")
    
    print(f"\n🎯 QUALIDADE DA SOLUÇÃO:")
    print(f"   • Conflitos médios: {avg_conflitos:.2f}")
    
    print(f"\n{'='*70}\n")


def comparar_algoritmos(resultados_dict):
    
    print("\n" + "="*70)
    print("COMPARAÇÃO ENTRE ALGORITMOS")
    print("="*70)
    
    # Extrai métricas de cada algoritmo
    metricas = {}
    for nome, resultados in resultados_dict.items():
        sucessos = sum([r['sucesso'] for r in resultados])
        taxa_sucesso = (sucessos / len(resultados)) * 100
        tempo_medio = np.mean([r['tempo'] for r in resultados])
        memoria_media = np.mean([r['memoria_usada'] for r in resultados])
        iteracoes_media = np.mean([r.get('iteracoes', r.get('iteracoes_total', 0)) for r in resultados])
        
        metricas[nome] = {
            'taxa_sucesso': taxa_sucesso,
            'tempo_medio': tempo_medio,
            'memoria_media': memoria_media,
            'iteracoes_media': iteracoes_media
        }
    
    # Encontra os melhores em cada categoria
    melhor_taxa = max(metricas.items(), key=lambda x: x[1]['taxa_sucesso'])
    melhor_tempo = min(metricas.items(), key=lambda x: x[1]['tempo_medio'])
    melhor_memoria = min(metricas.items(), key=lambda x: x[1]['memoria_media'])
    melhor_iteracoes = min(metricas.items(), key=lambda x: x[1]['iteracoes_media'])
    
    print(f"\n🏆 MELHORES POR CATEGORIA:\n")
    print(f"✓ Maior Taxa de Sucesso: {melhor_taxa[0]}")
    print(f"  → {melhor_taxa[1]['taxa_sucesso']:.1f}%")
    
    print(f"\n✓ Mais Rápido: {melhor_tempo[0]}")
    print(f"  → {melhor_tempo[1]['tempo_medio']:.6f} segundos")
    
    print(f"\n✓ Menor Uso de Memória: {melhor_memoria[0]}")
    print(f"  → {melhor_memoria[1]['memoria_media']/1024:.2f} KB")
    
    print(f"\n✓ Menos Iterações: {melhor_iteracoes[0]}")
    print(f"  → {melhor_iteracoes[1]['iteracoes_media']:.1f} iterações")
    
    # Tabela comparativa
    print(f"\n📊 TABELA COMPARATIVA:\n")
    print(f"{'Algoritmo':<35} {'Taxa':<12} {'Tempo (s)':<15} {'Memória (KB)':<15}")
    print("-" * 77)
    
    for nome, dados in metricas.items():
        print(f"{nome:<35} {dados['taxa_sucesso']:>6.1f}%     "
              f"{dados['tempo_medio']:>10.6f}     "
              f"{dados['memoria_media']/1024:>10.2f}")
    
    print("=" * 70 + "\n")


# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

def main():
    
    print("\n" + "="*70)
    print("PROBLEMA DAS 8 RAINHAS - HILL CLIMBING")
    print("Execução de 10 testes com Cold Cache para cada algoritmo")
    print("="*70)
    
    num_execucoes = 10
    resultados_todos = {}
    
    # ========================================================================
    # 1. HILL CLIMBING BÁSICO
    # ========================================================================
    print("\n\n" + "="*70)
    print("1️⃣  EXECUTANDO: HILL CLIMBING BÁSICO")
    print("="*70)
    
    resultados_basico = []
    for i in range(num_execucoes):
        print(f"Execução {i+1}/10...", end=" ")
        resultado = executar_com_cold_cache(
            hill_climbing_basico,
            max_iteracoes=1000,
            verbose=False
        )
        resultados_basico.append(resultado)
        status = "✓" if resultado['sucesso'] else "✗"
        print(f"{status} ({resultado['conflitos']} conflitos, {resultado['iteracoes']} iter)")
    
    imprimir_estatisticas("Hill Climbing Básico", resultados_basico)
    resultados_todos["Hill Climbing Básico"] = resultados_basico
    
    # Mostra uma solução encontrada (se houver)
    solucao = next((r for r in resultados_basico if r['sucesso']), None)
    if solucao:
        print("Exemplo de solução encontrada:")
        imprimir_tabuleiro(solucao['estado_final'])
    
    # ========================================================================
    # 2. HILL CLIMBING COM MOVIMENTOS LATERAIS
    # ========================================================================
    print("\n\n" + "="*70)
    print("2️⃣  EXECUTANDO: HILL CLIMBING COM MOVIMENTOS LATERAIS")
    print("="*70)
    
    resultados_laterais = []
    for i in range(num_execucoes):
        print(f"Execução {i+1}/10...", end=" ")
        resultado = executar_com_cold_cache(
            hill_climbing_com_laterais,
            max_iteracoes=1000,
            max_laterais=100,
            verbose=False
        )
        resultados_laterais.append(resultado)
        status = "✓" if resultado['sucesso'] else "✗"
        print(f"{status} ({resultado['conflitos']} conflitos, "
              f"{resultado['iteracoes']} iter, {resultado['laterais']} lat)")
    
    imprimir_estatisticas("Hill Climbing com Laterais", resultados_laterais)
    resultados_todos["Hill Climbing com Laterais"] = resultados_laterais
    
    # Mostra uma solução encontrada
    solucao = next((r for r in resultados_laterais if r['sucesso']), None)
    if solucao:
        print("Exemplo de solução encontrada:")
        imprimir_tabuleiro(solucao['estado_final'])
    
    # ========================================================================
    # 3. RANDOM-RESTART HILL CLIMBING
    # ========================================================================
    print("\n\n" + "="*70)
    print("3️⃣  EXECUTANDO: RANDOM-RESTART HILL CLIMBING")
    print("="*70)
    
    resultados_restart = []
    for i in range(num_execucoes):
        print(f"Execução {i+1}/10...", end=" ")
        resultado = executar_com_cold_cache(
            random_restart_hill_climbing,
            max_reinicio=100,
            usar_laterais=True,
            max_laterais=100,
            verbose=False
        )
        resultados_restart.append(resultado)
        status = "✓" if resultado['sucesso'] else "✗"
        print(f"{status} ({resultado['conflitos']} conflitos, "
              f"{resultado['reinicio']} reinícios, {resultado['iteracoes_total']} iter)")
    
    imprimir_estatisticas("Random-Restart Hill Climbing", resultados_restart)
    resultados_todos["Random-Restart Hill Climbing"] = resultados_restart
    
    # Mostra uma solução encontrada
    solucao = next((r for r in resultados_restart if r['sucesso']), resultados_restart[0])
    if solucao:
        print("Exemplo de solução encontrada:")
        imprimir_tabuleiro(solucao['estado_final'])
    
    # ========================================================================
    # 4. COMPARAÇÃO FINAL
    # ========================================================================
    comparar_algoritmos(resultados_todos)
    
    # ========================================================================
    # 5. GERAÇÃO DE GRÁFICOS
    # ========================================================================
    print("\n" + "="*70)
    print("📊 GERANDO VISUALIZAÇÕES...")
    print("="*70)
    print("\nDeseja gerar os gráficos de comparação? (S/N): ", end="")
    
    try:
        resposta = input().strip().upper()
        if resposta in ['S', 'SIM', 'Y', 'YES', '']:
            gerar_graficos(resultados_todos)
        else:
            print("⏭️  Geração de gráficos ignorada.")
    except:
        print("\n⏭️  Geração de gráficos ignorada.")
    
    print("\n✅ Execução concluída com sucesso!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()

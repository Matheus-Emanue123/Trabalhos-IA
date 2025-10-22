import numpy as np
import os
from search import bfs, dfs, greedy_search, a_star, run_with_cold_cache
from heuristics import manhattan_distance, euclidean_distance

def load_maze(filepath):
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    matrix = []
    for line in lines:
        row = line.strip().split()
        matrix.append(row)
    
    labirinto = np.array(matrix)
    return labirinto

def find_positions(labirinto):
    
    start_pos = None
    goal_pos = None
    
    rol, col = labirinto.shape
    for i in range(rol):
        for j in range(col):
            if labirinto[i][j] == 'S':
                start_pos = (i, j)
            elif labirinto[i][j] == 'G':
                goal_pos = (i, j)
    
    return start_pos, goal_pos

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    maze_file = os.path.join(current_dir, '..', 'data', 'labirinto.txt')
    
    labirinto = load_maze(maze_file)

    start_pos, goal_pos = find_positions(labirinto)
    
    print("Labirinto:")
    print(labirinto)
    print(f"\nInício: {start_pos}")
    print(f"Objetivo: {goal_pos}")
    
    # =========================================================================
    # BUSCA NÃO INFORMADA
    # =========================================================================
    print("\n" + "="*70)
    print("EXECUTANDO ALGORITMOS DE BUSCA NÃO INFORMADA COM COLD CACHE")
    print("="*70)

    bfs_results = run_with_cold_cache(bfs, start_pos, goal_pos, labirinto, "BFS (Busca em Largura)", num_runs=10)
    dfs_results = run_with_cold_cache(dfs, start_pos, goal_pos, labirinto, "DFS (Busca em Profundidade)", num_runs=10)

    print("\n" + "="*70)
    print("COMPARAÇÃO - BUSCA NÃO INFORMADA")
    print("="*70)
    bfs_avg_time = np.mean([r['execution_time'] for r in bfs_results])
    dfs_avg_time = np.mean([r['execution_time'] for r in dfs_results])
    bfs_avg_memory = np.mean([r['memory_used'] for r in bfs_results])
    dfs_avg_memory = np.mean([r['memory_used'] for r in dfs_results])
    bfs_avg_max_structures = np.mean([r['max_structure_size'] for r in bfs_results])
    dfs_avg_max_structures = np.mean([r['max_structure_size'] for r in dfs_results])
    
    print(f"\nBFS:")
    print(f"  Tempo médio: {bfs_avg_time:.6f}s")
    print(f"  Memória média: {bfs_avg_memory/1024:.2f} KB")
    print(f"  Máx. elementos nas estruturas: {bfs_avg_max_structures:.0f}")
    
    print(f"\nDFS:")
    print(f"  Tempo médio: {dfs_avg_time:.6f}s")
    print(f"  Memória média: {dfs_avg_memory/1024:.2f} KB")
    print(f"  Máx. elementos nas estruturas: {dfs_avg_max_structures:.0f}")
    
    faster = "BFS" if bfs_avg_time < dfs_avg_time else "DFS"
    time_diff = abs(bfs_avg_time - dfs_avg_time)
    print(f"\n{faster} foi {time_diff:.6f}s mais rápido em média")
    
    efficient = "BFS" if bfs_avg_memory < dfs_avg_memory else "DFS"
    memory_diff = abs(bfs_avg_memory - dfs_avg_memory)
    print(f"{efficient} usou {memory_diff/1024:.2f} KB menos memória em média")
    
    space_efficient = "BFS" if bfs_avg_max_structures < dfs_avg_max_structures else "DFS"
    structure_diff = abs(bfs_avg_max_structures - dfs_avg_max_structures)
    print(f"{space_efficient} manteve {structure_diff:.0f} elementos a menos nas estruturas em média")
    print("="*70)
    
    # =========================================================================
    # BUSCA INFORMADA - GULOSA (GREEDY)
    # =========================================================================
    print("\n\n" + "="*70)
    print("EXECUTANDO ALGORITMOS DE BUSCA INFORMADA - GULOSA (GREEDY)")
    print("="*70)
    
    # Greedy com Distância de Manhattan
    greedy_manhattan_results = run_with_cold_cache(
        lambda s, g, m, suppress_output=False: greedy_search(s, g, m, manhattan_distance, suppress_output),
        start_pos, goal_pos, labirinto, 
        "Greedy Search (Manhattan Distance)", 
        num_runs=10
    )
    
    # Greedy com Distância Euclidiana
    greedy_euclidean_results = run_with_cold_cache(
        lambda s, g, m, suppress_output=False: greedy_search(s, g, m, euclidean_distance, suppress_output),
        start_pos, goal_pos, labirinto, 
        "Greedy Search (Euclidean Distance)", 
        num_runs=10
    )
    
    print("\n" + "="*70)
    print("COMPARAÇÃO - BUSCA GULOSA (GREEDY)")
    print("="*70)
    greedy_man_avg_time = np.mean([r['execution_time'] for r in greedy_manhattan_results])
    greedy_euc_avg_time = np.mean([r['execution_time'] for r in greedy_euclidean_results])
    greedy_man_avg_memory = np.mean([r['memory_used'] for r in greedy_manhattan_results])
    greedy_euc_avg_memory = np.mean([r['memory_used'] for r in greedy_euclidean_results])
    greedy_man_avg_max_structures = np.mean([r['max_structure_size'] for r in greedy_manhattan_results])
    greedy_euc_avg_max_structures = np.mean([r['max_structure_size'] for r in greedy_euclidean_results])
    greedy_man_avg_nodes = np.mean([r['nodes_explored'] for r in greedy_manhattan_results])
    greedy_euc_avg_nodes = np.mean([r['nodes_explored'] for r in greedy_euclidean_results])
    
    print(f"\nGreedy (Manhattan):")
    print(f"  Nós explorados: {greedy_man_avg_nodes:.0f}")
    print(f"  Tempo médio: {greedy_man_avg_time:.6f}s")
    print(f"  Memória média: {greedy_man_avg_memory/1024:.2f} KB")
    print(f"  Máx. elementos nas estruturas: {greedy_man_avg_max_structures:.0f}")
    
    print(f"\nGreedy (Euclidean):")
    print(f"  Nós explorados: {greedy_euc_avg_nodes:.0f}")
    print(f"  Tempo médio: {greedy_euc_avg_time:.6f}s")
    print(f"  Memória média: {greedy_euc_avg_memory/1024:.2f} KB")
    print(f"  Máx. elementos nas estruturas: {greedy_euc_avg_max_structures:.0f}")
    
    better_heuristic = "Manhattan" if greedy_man_avg_time < greedy_euc_avg_time else "Euclidean"
    print(f"\nMelhor heurística para Greedy: {better_heuristic}")
    print("="*70)
    
    # =========================================================================
    # BUSCA INFORMADA - A*
    # =========================================================================
    print("\n\n" + "="*70)
    print("EXECUTANDO ALGORITMOS DE BUSCA INFORMADA - A*")
    print("="*70)
    
    # A* com Distância de Manhattan
    astar_manhattan_results = run_with_cold_cache(
        lambda s, g, m, suppress_output=False: a_star(s, g, m, manhattan_distance, suppress_output),
        start_pos, goal_pos, labirinto, 
        "A* (Manhattan Distance)", 
        num_runs=10
    )
    
    # A* com Distância Euclidiana
    astar_euclidean_results = run_with_cold_cache(
        lambda s, g, m, suppress_output=False: a_star(s, g, m, euclidean_distance, suppress_output),
        start_pos, goal_pos, labirinto, 
        "A* (Euclidean Distance)", 
        num_runs=10
    )
    
    print("\n" + "="*70)
    print("COMPARAÇÃO - BUSCA A*")
    print("="*70)
    astar_man_avg_time = np.mean([r['execution_time'] for r in astar_manhattan_results])
    astar_euc_avg_time = np.mean([r['execution_time'] for r in astar_euclidean_results])
    astar_man_avg_memory = np.mean([r['memory_used'] for r in astar_manhattan_results])
    astar_euc_avg_memory = np.mean([r['memory_used'] for r in astar_euclidean_results])
    astar_man_avg_max_structures = np.mean([r['max_structure_size'] for r in astar_manhattan_results])
    astar_euc_avg_max_structures = np.mean([r['max_structure_size'] for r in astar_euclidean_results])
    astar_man_avg_nodes = np.mean([r['nodes_explored'] for r in astar_manhattan_results])
    astar_euc_avg_nodes = np.mean([r['nodes_explored'] for r in astar_euclidean_results])
    
    print(f"\nA* (Manhattan):")
    print(f"  Nós explorados: {astar_man_avg_nodes:.0f}")
    print(f"  Tempo médio: {astar_man_avg_time:.6f}s")
    print(f"  Memória média: {astar_man_avg_memory/1024:.2f} KB")
    print(f"  Máx. elementos nas estruturas: {astar_man_avg_max_structures:.0f}")
    
    print(f"\nA* (Euclidean):")
    print(f"  Nós explorados: {astar_euc_avg_nodes:.0f}")
    print(f"  Tempo médio: {astar_euc_avg_time:.6f}s")
    print(f"  Memória média: {astar_euc_avg_memory/1024:.2f} KB")
    print(f"  Máx. elementos nas estruturas: {astar_euc_avg_max_structures:.0f}")
    
    better_heuristic_astar = "Manhattan" if astar_man_avg_time < astar_euc_avg_time else "Euclidean"
    print(f"\nMelhor heurística para A*: {better_heuristic_astar}")
    print("="*70)
    
    # =========================================================================
    # COMPARAÇÃO GERAL - TODOS OS ALGORITMOS
    # =========================================================================
    print("\n\n" + "="*70)
    print("COMPARAÇÃO GERAL - TODOS OS ALGORITMOS")
    print("="*70)
    
    all_algorithms = {
        'BFS': {'time': bfs_avg_time, 'memory': bfs_avg_memory, 'nodes': np.mean([r['nodes_explored'] for r in bfs_results])},
        'DFS': {'time': dfs_avg_time, 'memory': dfs_avg_memory, 'nodes': np.mean([r['nodes_explored'] for r in dfs_results])},
        'Greedy (Manhattan)': {'time': greedy_man_avg_time, 'memory': greedy_man_avg_memory, 'nodes': greedy_man_avg_nodes},
        'Greedy (Euclidean)': {'time': greedy_euc_avg_time, 'memory': greedy_euc_avg_memory, 'nodes': greedy_euc_avg_nodes},
        'A* (Manhattan)': {'time': astar_man_avg_time, 'memory': astar_man_avg_memory, 'nodes': astar_man_avg_nodes},
        'A* (Euclidean)': {'time': astar_euc_avg_time, 'memory': astar_euc_avg_memory, 'nodes': astar_euc_avg_nodes},
    }
    
    print("\nResumo de Performance:")
    print("-" * 70)
    print(f"{'Algoritmo':<25} {'Nós':<10} {'Tempo (s)':<15} {'Memória (KB)':<15}")
    print("-" * 70)
    for algo, stats in all_algorithms.items():
        print(f"{algo:<25} {stats['nodes']:<10.0f} {stats['time']:<15.6f} {stats['memory']/1024:<15.2f}")
    print("-" * 70)
    
    # Encontrar o melhor algoritmo
    fastest = min(all_algorithms.items(), key=lambda x: x[1]['time'])
    most_efficient = min(all_algorithms.items(), key=lambda x: x[1]['memory'])
    least_nodes = min(all_algorithms.items(), key=lambda x: x[1]['nodes'])
    
    print(f"\nMais rápido: {fastest[0]} ({fastest[1]['time']:.6f}s)")
    print(f"Mais eficiente em memória: {most_efficient[0]} ({most_efficient[1]['memory']/1024:.2f} KB)")
    print(f"Menor número de nós explorados: {least_nodes[0]} ({least_nodes[1]['nodes']:.0f} nós)")
    print("="*70)

if __name__ == "__main__":
    main()


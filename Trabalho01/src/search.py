import numpy as np
from collections import deque
import time
import os
import psutil
import gc
import ctypes
from heuristics import euclidean_distance, manhattan_distance

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def clear_cache():

    gc.collect()
    gc.collect()
    gc.collect()
    
    time.sleep(0.1)

    try:
        if os.name == 'nt': 
            ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)
    except:
        pass

# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,} bytes".format(
            func.__name__,
            mem_after - mem_before))

        return result
    return wrapper

def is_valid(pos, maze, visited):

    i, j = pos
    rol, col = maze.shape
    
    if i < 0 or i >= rol or j < 0 or j >= col:
        return False
    if maze[i][j] == '#':
        return False
    if pos in visited:
        return False
    return True

def reconstruct_path(came_from, current):

    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    path.reverse()
    return path

def print_metrics(algorithm_name, path, nodes_explored, execution_time, memory_used):

    print(f"\n{'='*50}")
    print(f"Algoritmo: {algorithm_name}")
    print(f"{'='*50}")
    print(f"Nós explorados: {nodes_explored}")
    print(f"Tamanho do caminho: {len(path) if path else 0}")
    print(f"Tempo de execução: {execution_time:.6f} segundos")
    print(f"Memória consumida: {memory_used:,} bytes ({memory_used / 1024:.2f} KB)")
    if path:
        print(f"Caminho encontrado: {' -> '.join([str(p) for p in path])}")
    else:
        print("Caminho não encontrado!")
    print(f"{'='*50}\n")

def print_statistics(algorithm_name, results):
 
    times = [r['execution_time'] for r in results]
    memories = [r['memory_used'] for r in results]
    nodes = [r['nodes_explored'] for r in results]
    max_structures = [r['max_structure_size'] for r in results]
    
    avg_time = np.mean(times)
    std_time = np.std(times)
    min_time = np.min(times)
    max_time = np.max(times)
    
    avg_memory = np.mean(memories)
    std_memory = np.std(memories)
    min_memory = np.min(memories)
    max_memory = np.max(memories)
    
    avg_nodes = np.mean(nodes)
    avg_max_structures = np.mean(max_structures)
    
    print(f"\n{'='*70}")
    print(f"ESTATÍSTICAS - {algorithm_name} (10 execuções em Cold Cache)")
    print(f"{'='*70}")
    print(f"Nós explorados (média): {avg_nodes:.0f}")
    print(f"Máximo de elementos nas estruturas (média): {avg_max_structures:.0f}")
    print(f"  (fronteira + visitados simultaneamente)")
    print(f"\nTempo de execução:")
    print(f"  Média: {avg_time:.6f} segundos")
    print(f"  Desvio padrão: {std_time:.6f} segundos")
    print(f"  Mínimo: {min_time:.6f} segundos")
    print(f"  Máximo: {max_time:.6f} segundos")
    print(f"\nMemória consumida:")
    print(f"  Média: {avg_memory:,.0f} bytes ({avg_memory / 1024:.2f} KB)")
    print(f"  Desvio padrão: {std_memory:,.0f} bytes ({std_memory / 1024:.2f} KB)")
    print(f"  Mínimo: {min_memory:,.0f} bytes ({min_memory / 1024:.2f} KB)")
    print(f"  Máximo: {max_memory:,.0f} bytes ({max_memory / 1024:.2f} KB)")
    
    if results[0]['path']:
        print(f"\nTamanho do caminho: {len(results[0]['path'])}")
        print(f"Caminho: {' -> '.join([str(p) for p in results[0]['path']])}")
    
    print(f"{'='*70}\n")

def visualize_path(maze, path, algorithm_name):

    if not path:
        print("Nenhum caminho para visualizar.")
        return
    
    visual = maze.copy()
    for pos in path:
        if visual[pos] not in ['S', 'G']:
            visual[pos] = '*'
    
    print(f"\nCaminho encontrado pelo {algorithm_name}:")
    print(visual)

def run_with_cold_cache(algorithm_func, start, goal, maze, algorithm_name, num_runs=10):
   
    results = []
    
    print(f"\n{'='*70}")
    print(f"Executando {algorithm_name} com Cold Cache ({num_runs} execuções)")
    print(f"{'='*70}")
    
    for i in range(num_runs):
        print(f"\nExecução {i+1}/{num_runs}...", end=" ")
        
        clear_cache()

        result = algorithm_func(start, goal, maze, suppress_output=True)
        results.append(result)
        
        print(f"✓ (Tempo: {result['execution_time']:.6f}s, Memória: {result['memory_used']/1024:.2f} KB, Max estruturas: {result['max_structure_size']})")

    print_statistics(algorithm_name, results)

    if results[0]['path']:
        visualize_path(maze, results[0]['path'], algorithm_name)
    
    return results

def bfs(start, goal, maze, suppress_output=False):

    start_time = time.time()
    mem_before = process_memory()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = {start}
    came_from = {}
    nodes_explored = 0
    max_structure_size = len(queue) + len(visited) 

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            mem_after = process_memory()
            memory_used = mem_after - mem_before
            path = reconstruct_path(came_from, current)
            if not suppress_output:
                print_metrics("BFS (Busca em Largura)", path, nodes_explored, end_time - start_time, memory_used)
                visualize_path(maze, path, "BFS")
            return {
                'path': path,
                'nodes_explored': nodes_explored,
                'execution_time': end_time - start_time,
                'memory_used': memory_used,
                'max_structure_size': max_structure_size
            }

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if is_valid(neighbor, maze, visited):
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                
                current_size = len(queue) + len(visited)
                if current_size > max_structure_size:
                    max_structure_size = current_size

    end_time = time.time()
    mem_after = process_memory()
    memory_used = mem_after - mem_before
    if not suppress_output:
        print_metrics("BFS (Busca em Largura)", None, nodes_explored, end_time - start_time, memory_used)
    return {
        'path': None,
        'nodes_explored': nodes_explored,
        'execution_time': end_time - start_time,
        'memory_used': memory_used,
        'max_structure_size': max_structure_size
    }

def dfs(start, goal, maze, suppress_output=False):

    start_time = time.time()
    mem_before = process_memory()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [start]
    visited = {start}
    came_from = {}
    nodes_explored = 0
    max_structure_size = len(stack) + len(visited) 

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            mem_after = process_memory()
            memory_used = mem_after - mem_before
            path = reconstruct_path(came_from, current)
            if not suppress_output:
                print_metrics("DFS (Busca em Profundidade)", path, nodes_explored, end_time - start_time, memory_used)
                visualize_path(maze, path, "DFS")
            return {
                'path': path,
                'nodes_explored': nodes_explored,
                'execution_time': end_time - start_time,
                'memory_used': memory_used,
                'max_structure_size': max_structure_size
            }

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if is_valid(neighbor, maze, visited):
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
                
                # Atualiza o tamanho máximo das estruturas
                current_size = len(stack) + len(visited)
                if current_size > max_structure_size:
                    max_structure_size = current_size

    end_time = time.time()
    mem_after = process_memory()
    memory_used = mem_after - mem_before
    if not suppress_output:
        print_metrics("DFS (Busca em Profundidade)", None, nodes_explored, end_time - start_time, memory_used)
    return {
        'path': None,
        'nodes_explored': nodes_explored,
        'execution_time': end_time - start_time,
        'memory_used': memory_used,
        'max_structure_size': max_structure_size
    }
    
def greedy_search(start, goal, maze, heuristic_func, suppress_output=False):

    import heapq
    
    start_time = time.time()
    mem_before = process_memory()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    counter = 0
    heap = [(heuristic_func(start, goal), counter, start)]
    counter += 1
    
    visited = {start}
    came_from = {}
    nodes_explored = 0
    max_structure_size = len(heap) + len(visited)

    while heap:
        _, _, current = heapq.heappop(heap)
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            mem_after = process_memory()
            memory_used = mem_after - mem_before
            path = reconstruct_path(came_from, current)
            if not suppress_output:
                heuristic_name = heuristic_func.__name__.replace('_', ' ').title()
                print_metrics(f"Greedy Search ({heuristic_name})", path, nodes_explored, end_time - start_time, memory_used)
                visualize_path(maze, path, f"Greedy ({heuristic_name})")
            return {
                'path': path,
                'nodes_explored': nodes_explored,
                'execution_time': end_time - start_time,
                'memory_used': memory_used,
                'max_structure_size': max_structure_size
            }

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if is_valid(neighbor, maze, visited):
                visited.add(neighbor)
                came_from[neighbor] = current
                
                h = heuristic_func(neighbor, goal)
                heapq.heappush(heap, (h, counter, neighbor))
                counter += 1
                
                current_size = len(heap) + len(visited)
                if current_size > max_structure_size:
                    max_structure_size = current_size

    end_time = time.time()
    mem_after = process_memory()
    memory_used = mem_after - mem_before
    if not suppress_output:
        heuristic_name = heuristic_func.__name__.replace('_', ' ').title()
        print_metrics(f"Greedy Search ({heuristic_name})", None, nodes_explored, end_time - start_time, memory_used)
    return {
        'path': None,
        'nodes_explored': nodes_explored,
        'execution_time': end_time - start_time,
        'memory_used': memory_used,
        'max_structure_size': max_structure_size
    }

def a_star(start, goal, maze, heuristic_func, suppress_output=False):
  
    import heapq
    
    start_time = time.time()
    mem_before = process_memory()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Fila de prioridade: (f(n), contador, posição)
    counter = 0
    heap = [(heuristic_func(start, goal), counter, start)]
    counter += 1
    
    visited = {start}
    came_from = {}
    g_score = {start: 0}  # Custo do caminho do início até cada nó
    nodes_explored = 0
    max_structure_size = len(heap) + len(visited)

    while heap:
        _, _, current = heapq.heappop(heap)
        nodes_explored += 1

        if current == goal:
            end_time = time.time()
            mem_after = process_memory()
            memory_used = mem_after - mem_before
            path = reconstruct_path(came_from, current)
            if not suppress_output:
                heuristic_name = heuristic_func.__name__.replace('_', ' ').title()
                print_metrics(f"A* ({heuristic_name})", path, nodes_explored, end_time - start_time, memory_used)
                visualize_path(maze, path, f"A* ({heuristic_name})")
            return {
                'path': path,
                'nodes_explored': nodes_explored,
                'execution_time': end_time - start_time,
                'memory_used': memory_used,
                'max_structure_size': max_structure_size
            }

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if is_valid(neighbor, maze, visited):
                visited.add(neighbor)
                came_from[neighbor] = current
                
                # g(n) = custo do caminho até o vizinho (cada passo custa 1)
                g_score[neighbor] = g_score[current] + 1
                
                # h(n) = heurística
                h = heuristic_func(neighbor, goal)
                
                # f(n) = g(n) + h(n)
                f = g_score[neighbor] + h
                
                heapq.heappush(heap, (f, counter, neighbor))
                counter += 1
                
                current_size = len(heap) + len(visited)
                if current_size > max_structure_size:
                    max_structure_size = current_size

    end_time = time.time()
    mem_after = process_memory()
    memory_used = mem_after - mem_before
    if not suppress_output:
        heuristic_name = heuristic_func.__name__.replace('_', ' ').title()
        print_metrics(f"A* ({heuristic_name})", None, nodes_explored, end_time - start_time, memory_used)
    return {
        'path': None,
        'nodes_explored': nodes_explored,
        'execution_time': end_time - start_time,
        'memory_used': memory_used,
        'max_structure_size': max_structure_size
    }
# 🔍 Trabalho 01 - Algoritmos de Busca em Labirintos

Implementação e análise comparativa de algoritmos de busca clássicos para resolução de labirintos.

## 📋 Sobre

Este trabalho implementa e compara 6 variantes de algoritmos de busca (não-informados e informados) para encontrar o caminho em um labirinto, analisando performance em termos de tempo, memória e nós explorados.

## 🎯 Algoritmos Implementados

### Busca Não-Informada
- **BFS (Breadth-First Search)** - Busca em Largura
  - Explora nível por nível
  - Garante caminho mais curto
  - Usa fila (FIFO)

- **DFS (Depth-First Search)** - Busca em Profundidade
  - Explora o máximo de profundidade primeiro
  - Usa pilha (LIFO)
  - Menor consumo de memória

### Busca Informada

#### Greedy Search (Busca Gulosa)
Escolhe sempre o nó que parece estar mais próximo do objetivo.

- **Greedy + Manhattan**: `h(n) = |x1 - x2| + |y1 - y2|`
- **Greedy + Euclidean**: `h(n) = √((x1-x2)² + (y1-y2)²)`

#### A* (A-Star)
Combina custo do caminho com estimativa heurística.

- **A* + Manhattan**: `f(n) = g(n) + h(n)` com Manhattan
- **A* + Euclidean**: `f(n) = g(n) + h(n)` com Euclidean

## 📁 Estrutura

```
Trabalho01/
├── data/
│   └── labirinto.txt       # Arquivo de entrada do labirinto
├── src/
│   ├── maze.py             # Script principal de execução
│   ├── search.py           # Implementação dos algoritmos
│   └── heuristics.py       # Funções heurísticas
├── ref/                    # Materiais de referência
├── rel/                    # Relatório completo (LaTeX/PDF)
└── README.md              # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install numpy psutil
```

### Execução

**Windows:**
```powershell
cd src
python maze.py
```

**Linux/Mac:**
```bash
cd src
python3 maze.py
```

## 📊 Métricas Analisadas

O programa realiza **10 execuções com cold cache** para cada algoritmo e mede:

- ⏱️ **Tempo de Execução** (segundos)
- 💾 **Memória Consumida** (bytes/KB)
- 🔍 **Nós Explorados** (quantidade)
- 📏 **Tamanho do Caminho** (passos)
- 📦 **Tamanho Máximo da Estrutura** (fila/pilha)

### Estatísticas Fornecidas
- Média, Desvio Padrão, Mínimo e Máximo
- Comparações entre algoritmos
- Visualização do caminho encontrado

## 📝 Formato do Labirinto

O arquivo `labirinto.txt` usa o seguinte formato:

```
. . . # . . . . G
. . # . . . # . .
. . . . . . . # .
# . # . # . . . #
. # . . . . . . .
. . . . . . # . #
. # . # . . . . .
. . . . # . # . .
S . . . . . . . .
```

**Legenda:**
- `#` → Parede (obstáculo)
- `.` → Caminho livre
- `S` → Start (início)
- `G` → Goal (objetivo)

## 🧮 Funções Heurísticas

### Manhattan Distance (Distância de Manhattan)
```
h(n) = |x_atual - x_goal| + |y_atual - y_goal|
```
- Movimentos apenas horizontal/vertical
- Admissível para grid sem diagonais
- Mais eficiente computacionalmente

### Euclidean Distance (Distância Euclidiana)
```
h(n) = √((x_atual - x_goal)² + (y_atual - y_goal)²)
```
- Distância em linha reta
- Também admissível
- Pode guiar melhor em alguns casos

## 📈 Resultados Esperados

### Performance Típica (exemplo)

| Algoritmo | Tempo (s) | Nós Explorados | Caminho |
|-----------|-----------|----------------|---------|
| BFS | 0.0003 | 45 | 18 |
| DFS | 0.0002 | 52 | 25 |
| Greedy (Manhattan) | 0.0001 | 22 | 18 |
| Greedy (Euclidean) | 0.0001 | 24 | 18 |
| A* (Manhattan) | 0.0002 | 28 | 18 |
| A* (Euclidean) | 0.0002 | 30 | 18 |

> Valores ilustrativos. Resultados reais variam conforme o labirinto.

## 🔬 Cold Cache Testing

Para garantir medições precisas, o programa:

1. Executa `gc.collect()` 3 vezes antes de cada teste
2. Aguarda 100ms para estabilização
3. Mede memória antes e depois da execução
4. Repete 10 vezes e calcula estatísticas

## 🎓 Conceitos Aplicados

- ✅ Busca em grafos
- ✅ Estruturas de dados (fila, pilha, heap)
- ✅ Heurísticas admissíveis
- ✅ Otimalidade de A*
- ✅ Trade-off tempo vs memória
- ✅ Análise experimental de algoritmos

## 📚 Referências

1. Russell, S., Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd ed.)
2. Cormen, T. H. et al. (2009). *Introduction to Algorithms* (3rd ed.)

## 👨‍💻 Autor

**Matheus Emanuel**
- 🎓 CEFET-MG - 6° Período
- 📧 memanuel643@gmail.com
- 🔗 [GitHub](https://github.com/Matheus-Emanue123) | [LinkedIn](https://www.linkedin.com/in/matheus-silva-emanuel)

---

[← Voltar para o repositório principal](../README.md)

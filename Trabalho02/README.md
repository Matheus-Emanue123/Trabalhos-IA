# 👑 Trabalho 02 - Problema das 8 Rainhas com Hill Climbing

Implementação e análise comparativa de algoritmos de otimização local para resolver o problema das 8 Rainhas.

## 📋 Sobre

Este trabalho implementa e compara **4 algoritmos de busca local** para resolver o problema clássico das 8 Rainhas, onde o objetivo é posicionar 8 rainhas em um tabuleiro de xadrez 8×8 sem que nenhuma ataque outra.

## 🎯 Algoritmos Implementados

### 1. Hill Climbing Básico
- Algoritmo guloso que sempre move para o melhor vizinho
- Para em máximos locais
- Rápido mas com baixa taxa de sucesso (~0-30%)

### 2. Hill Climbing com Movimentos Laterais
- Permite até 100 movimentos laterais consecutivos
- Pode escapar de "platôs"
- Taxa de sucesso intermediária (~30-50%)

### 3. Random-Restart Hill Climbing
- Reinicia com estado aleatório ao atingir máximo local
- Garante solução eventualmente
- Taxa de sucesso: 100%
- Usa mais tempo e iterações

### 4. Simulated Annealing
- Aceita movimentos ruins com probabilidade decrescente
- Temperatura inicial: T₀ = 2000
- Taxa de resfriamento: α = 0.995
- Taxa de sucesso: ~70-80%
- Explora amplamente o espaço de busca

## 📁 Estrutura

```
Trabalho02/
├── data/                          # Gráficos gerados
│   ├── grafico_01_taxa_sucesso.png
│   ├── grafico_02_tempo_vs_sucesso.png
│   └── grafico_03_barras_iteracoes.png
│
├── src/                           # Código fonte
│   ├── eight_queens.py            # Script principal
│   ├── hill_climbing.py           # Implementação dos algoritmos
│   └── visualizacao.py            # Geração de gráficos
│
├── ref/                           # Materiais de referência
├── rel/                           # Relatório LaTeX/PDF
└── README.md                      # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install numpy matplotlib psutil
```

### Execução

**Windows:**
```powershell
cd src
python eight_queens.py
```

**Linux/Mac:**
```bash
cd src
python3 eight_queens.py
```

### Opções de Execução

O programa irá:
1. Executar **10 testes com cold cache** para cada algoritmo
2. Apresentar estatísticas detalhadas
3. Perguntar se deseja gerar gráficos (digite **S**)

## 📊 Métricas Analisadas

Para cada algoritmo, são medidos:

### Métricas Gerais
- ✅ **Taxa de Sucesso** (%)
- ⏱️ **Tempo de Execução** (segundos)
- 💾 **Memória Consumida** (bytes/KB)
- 🔄 **Número de Iterações**

### Métricas Específicas
- **HC Laterais**: Quantidade de movimentos laterais
- **Random-Restart**: Número de reinicializações
- **Simulated Annealing**: Pioras aceitas e taxa de aceitação

## 📈 Resultados Típicos

| Algoritmo | Taxa Sucesso | Tempo (ms) | Iterações |
|-----------|--------------|------------|-----------|
| HC Básico | 0-30% | ~1 | ~4 |
| HC Laterais | 30-50% | ~15-25 | ~70-90 |
| Random-Restart | 100% | ~20-75 | ~90-270 |
| Simulated Annealing | 70-80% | ~25-30 | ~2000 |

> Valores aproximados baseados em execuções reais.

## 📊 Gráficos Gerados

O programa gera automaticamente **3 gráficos comparativos**:

### 1. Taxa de Sucesso
Barras horizontais mostrando a porcentagem de soluções encontradas.

### 2. Tempo vs Sucesso
Scatter plot relacionando eficiência temporal com taxa de sucesso.

### 3. Estatísticas de Iterações
Barras agrupadas (Min/Média/Max) em escala logarítmica, permitindo visualizar valores muito diferentes (4 vs 2000 iterações).

## 🧮 Representação do Problema

### Codificação
- Vetor de 8 posições: `[col₀, col₁, col₂, col₃, col₄, col₅, col₆, col₇]`
- Cada índice representa a linha, cada valor a coluna da rainha
- Exemplo: `[3, 1, 6, 2, 5, 7, 4, 0]`

### Função de Avaliação
```python
conflitos = 0
for cada par de rainhas (i, j):
    if mesma_coluna(i, j) or mesma_diagonal(i, j):
        conflitos += 1
```

**Objetivo:** Minimizar conflitos até chegar a 0.

## 🔥 Simulated Annealing - Detalhes

### Parâmetros
- **Temperatura Inicial**: T₀ = 2000
- **Taxa de Resfriamento**: α = 0.995
- **Temperatura Mínima**: T_min = 0.001
- **Iterações Máximas**: 2500

### Função de Aceitação
```
ΔE = conflitos_novo - conflitos_atual

Se ΔE < 0:  # Melhora
    Aceita sempre
Senão:      # Piora
    Aceita com probabilidade P = e^(-ΔE/T)
```

### Resfriamento
```
T_nova = α × T_atual
```

## 🔬 Cold Cache Testing

Para medições precisas:
1. `gc.collect()` × 3 antes de cada execução
2. Aguarda 100ms para estabilização
3. Mede memória antes/depois
4. Repete 10 vezes por algoritmo (40 testes totais)

## 🎓 Conceitos Aplicados

- ✅ Busca local e hill climbing
- ✅ Problema de otimização combinatória
- ✅ Trade-off exploração vs exploração
- ✅ Simulated annealing e recozimento simulado
- ✅ Probabilidade de aceitação de Boltzmann
- ✅ Análise experimental com cold cache
- ✅ Visualização de dados científicos

## 📚 Ferramentas de IA Utilizadas

Durante o desenvolvimento deste trabalho, as seguintes ferramentas de IA foram utilizadas:

- **GitHub Copilot**: Refatoração de código e sugestões de implementação
- **Google NotebookLM**: Busca e organização de referências bibliográficas
- **Google Gemini**: Revisão e correção de textos no relatório

> Todas as implementações foram revisadas, testadas e validadas manualmente.

## 📖 Referências

1. Russell, S., Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd ed.)
2. Kirkpatrick, S. et al. (1983). "Optimization by Simulated Annealing". *Science*, 220(4598).
3. Aarts, E., Korst, J. (1989). *Simulated Annealing and Boltzmann Machines*.

## 👨‍💻 Autor

**Matheus Emanuel**
- 🎓 CEFET-MG - 6° Período
- 📧 memanuel643@gmail.com
- 🔗 [GitHub](https://github.com/Matheus-Emanue123) | [LinkedIn](https://www.linkedin.com/in/matheus-silva-emanuel)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](../LICENSE) para mais detalhes.

---

[← Voltar para o repositório principal](../README.md)

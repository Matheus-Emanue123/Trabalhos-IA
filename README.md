# 🤖 Trabalhos de Inteligência Artificial - CEFET

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-red.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositório contendo os trabalhos práticos desenvolvidos na disciplina de Inteligência Artificial do CEFET-MG.

## 📋 Trabalhos

### 📂 [Trabalho 01 - Algoritmos de Busca em Labirintos](Trabalho01/)
Implementação e análise de algoritmos de busca clássicos (BFS, DFS, Greedy, A*) para resolução de labirintos.

**Algoritmos:** BFS, DFS, Greedy (Manhattan/Euclidean), A* (Manhattan/Euclidean)

[Ver documentação completa →](Trabalho01/README.md)

### 📂 [Trabalho 02 - 8 Rainhas com Hill Climbing](Trabalho02/)
Implementação e comparação de variantes de Hill Climbing e Simulated Annealing para o problema das 8 Rainhas.

**Algoritmos:** Hill Climbing Básico, Hill Climbing com Laterais, Random-Restart Hill Climbing, Simulated Annealing

[Ver documentação completa →](Trabalho02/README.md)

## 📁 Estrutura do Repositório

```
Trabalhos/
├── Trabalho01/              # Algoritmos de Busca em Labirintos
│   ├── data/               # Arquivos de entrada
│   ├── src/                # Código fonte
│   ├── ref/                # Referências
│   ├── rel/                # Relatórios
│   └── README.md
│
├── Trabalho02/              # 8 Rainhas com Hill Climbing
│   ├── data/               # Gráficos gerados
│   ├── src/                # Código fonte
│   ├── ref/                # Referências
│   ├── rel/                # Relatórios LaTeX
│   └── README.md
│
├── requirements.txt         # Dependências do projeto
├── LICENSE                  # Licença MIT
└── README.md               # Este arquivo
```

## 🔧 Pré-requisitos

- **Python**: 3.11 ou superior
- **pip**: Gerenciador de pacotes do Python

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Matheus-Emanue123/Trabalhos-IA.git
cd Trabalhos-IA
```

### 2. Crie um ambiente virtual (recomendado)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 📚 Dependências

| Biblioteca | Versão | Descrição |
|-----------|---------|-----------|
| **numpy** | ≥1.21.0 | Computação numérica e arrays |
| **psutil** | ≥5.8.0 | Monitoramento de recursos do sistema |
| **matplotlib** | ≥3.5.0 | Visualização de dados e gráficos |

### Verificar instalação

```bash
pip list | grep -E "numpy|psutil|matplotlib"
```

## 🚀 Execução Rápida

### Trabalho 01
```bash
cd Trabalho01/src
python maze.py
```

### Trabalho 02
```bash
cd Trabalho02/src
python eight_queens.py
```

## 📊 Funcionalidades

### Trabalho 01
- ✅ 6 variantes de algoritmos de busca
- ✅ Comparação de performance (tempo, memória, nós explorados)
- ✅ Cold cache testing para medições precisas
- ✅ Visualização de caminhos no labirinto

### Trabalho 02
- ✅ 4 algoritmos de otimização local
- ✅ 10 execuções com cold cache por algoritmo
- ✅ Estatísticas detalhadas (taxa de sucesso, tempo, iterações)
- ✅ 3 gráficos comparativos gerados automaticamente
- ✅ Análise de movimentos laterais e pioras aceitas

## ✅ Versões Testadas

| Componente | Versão |
|-----------|---------|
| Python | 3.11.4 |
| NumPy | 1.24.3 |
| psutil | 5.9.5 |
| matplotlib | 3.7.1 |
| SO | Windows 11 |

## 👨‍💻 Autor

**Matheus Emanuel**

- 🎓 CEFET-MG - 6° Período
- 🐙 GitHub: [@Matheus-Emanue123](https://github.com/Matheus-Emanue123)
- 💼 LinkedIn: [Matheus Emanuel](https://www.linkedin.com/in/matheus-silva-emanuel)
- 📧 Email: memanuel643@gmail.com

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ **Se este projeto foi útil, considere dar uma estrela no repositório!**

**Desenvolvido com 💙 no CEFET-MG**

**Desenvolvido com � no CEFET-MG**

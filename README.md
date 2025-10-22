# 🤖 Trabalhos de Inteligência Artificial

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange.svg)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositório contendo os trabalhos práticos desenvolvidos na disciplina de Inteligência Artificial do CEFET.

## 📋 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Trabalho 01 - Algoritmos de Busca](#-trabalho-01---algoritmos-de-busca)
  - [Algoritmos Implementados](#algoritmos-implementados)
  - [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
  - [Windows](#windows)
  - [Linux/Mac](#linuxmac)
- [Como Executar](#-como-executar)
- [Estrutura dos Arquivos](#-estrutura-dos-arquivos)
- [Dependências](#-dependências)
- [Versões Testadas](#-versões-testadas)
- [Resultados e Análises](#-resultados-e-análises)
- [Formato do Labirinto](#-formato-do-labirinto)
- [Autor](#-autor)
- [Licença](#-licença)

## 🎯 Sobre o Projeto

Este repositório contém implementações de algoritmos clássicos de Inteligência Artificial, com foco em algoritmos de busca e resolução de problemas. Os trabalhos foram desenvolvidos como parte do curso de Inteligência Artificial do 6° período do CEFET.

## 📁 Estrutura do Repositório

```
Trabalhos/
├── Trabalho01/              # Algoritmos de Busca em Labirintos
│   ├── data/
│   │   └── labirinto.txt    # Arquivo do labirinto
│   ├── src/
│   │   ├── maze.py          # Script principal
│   │   ├── search.py        # Implementação dos algoritmos
│   │   └── heuristics.py    # Funções heurísticas
│   └── ref/                 # Referências e materiais
├── Trabalho02/              # (Em desenvolvimento)
└── README.md                # Este arquivo
```

## 🔍 Trabalho 01 - Algoritmos de Busca

Implementação e comparação de algoritmos de busca clássicos para resolução de labirintos.

### Algoritmos Implementados

#### Busca Não-Informada
- **BFS (Breadth-First Search)** - Busca em Largura
- **DFS (Depth-First Search)** - Busca em Profundidade

#### Busca Informada
- **Greedy Search** (Busca Gulosa)
  - Com heurística de Distância de Manhattan
  - Com heurística de Distância Euclidiana
- **A\* (A-Star)**
  - Com heurística de Distância de Manhattan
  - Com heurística de Distância Euclidiana

### Funcionalidades

- ✅ Resolução de labirintos com múltiplos algoritmos
- ✅ Comparação de performance entre algoritmos
- ✅ Análise de memória consumida
- ✅ Medição de tempo de execução
- ✅ Contagem de nós explorados
- ✅ Visualização do caminho encontrado
- ✅ Execução com "Cold Cache" para testes mais precisos
- ✅ Estatísticas detalhadas com 10 execuções por algoritmo
- ✅ Comparação de heurísticas

## 🔧 Pré-requisitos

- **Python**: versão 3.8 ou superior
- **pip**: gerenciador de pacotes do Python
- **Sistema Operacional**: Windows, Linux ou macOS

## 📦 Instalação

### Windows

1. **Clone o repositório:**
```powershell
git clone https://github.com/Matheus-Emanue123/Trabalhos-IA.git
cd Trabalhos-IA
```

2. **Verifique a versão do Python:**
```powershell
python --version
```
> Certifique-se de que a versão é 3.8 ou superior.

3. **Crie um ambiente virtual (opcional, mas recomendado):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

4. **Instale as dependências:**
```powershell
pip install numpy psutil
```

### Linux/Mac

1. **Clone o repositório:**
```bash
git clone https://github.com/Matheus-Emanue123/Trabalhos-IA.git
cd Trabalhos-IA
```

2. **Verifique a versão do Python:**
```bash
python3 --version
```

3. **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install numpy psutil
```

## 🚀 Como Executar

### Trabalho 01 - Algoritmos de Busca

**Windows:**
```powershell
cd Trabalho01\src
python maze.py
```

**Linux/Mac:**
```bash
cd Trabalho01/src
python3 maze.py
```

O programa executará todos os algoritmos implementados e apresentará:
- Análise individual de cada algoritmo
- Comparações de performance
- Visualização dos caminhos encontrados
- Estatísticas detalhadas de execução

## 📄 Estrutura dos Arquivos

### `maze.py`
Script principal que:
- Carrega o labirinto do arquivo
- Executa todos os algoritmos de busca
- Realiza comparações de performance
- Apresenta resultados e estatísticas

### `search.py`
Contém as implementações de:
- Algoritmos de busca (BFS, DFS, Greedy, A*)
- Funções auxiliares para medição de performance
- Sistema de cold cache para testes precisos
- Funções de visualização e estatísticas

### `heuristics.py`
Implementa as funções heurísticas:
- **Manhattan Distance**: `|x1 - x2| + |y1 - y2|`
- **Euclidean Distance**: `√((x1-x2)² + (y1-y2)²)`

## 📚 Dependências

| Biblioteca | Versão Mínima | Descrição |
|-----------|---------------|-----------|
| **numpy** | 1.21.0 | Operações com arrays e matrizes |
| **psutil** | 5.8.0 | Monitoramento de recursos do sistema |

### Instalação de Dependências Específicas

```powershell
# Instalar versões específicas
pip install numpy==1.24.3 psutil==5.9.5

# Ou instalar as versões mais recentes compatíveis
pip install numpy>=1.21.0 psutil>=5.8.0
```

### Verificar Versões Instaladas

```powershell
pip show numpy psutil
```

## ✅ Versões Testadas

O projeto foi testado com sucesso nas seguintes configurações:

| Componente | Versão |
|-----------|---------|
| Python | 3.11.4 |
| NumPy |  1.24.3 |
| psutil | 5.8.0, 5.9.5 |
| Sistema Operacional | Windows 11|

## 📊 Resultados e Análises

O programa fornece análises detalhadas incluindo:

- **Nós Explorados**: Quantidade de nós visitados pelo algoritmo
- **Tempo de Execução**: Medido em segundos com 6 casas decimais
- **Memória Consumida**: Em bytes e KB
- **Tamanho Máximo das Estruturas**: Máximo de elementos mantidos em memória
- **Tamanho do Caminho**: Número de passos da solução
- **Visualização do Caminho**: Representação visual no labirinto

### Métricas Comparativas

O programa compara automaticamente:
- Algoritmo mais rápido
- Algoritmo mais eficiente em memória
- Algoritmo que explora menos nós
- Melhor heurística para cada tipo de busca informada

## 📝 Formato do Labirinto

O arquivo `labirinto.txt` deve seguir o formato (exemplo utilizado):

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

Onde:
- `#` = Parede (obstáculo)
- `.` = Caminho livre
- `S` = Start (início)
- `G` = Goal (objetivo)

## 👨‍💻 Autor

**Matheus Emanuel**

- GitHub: [@Matheus-Emanue123](https://github.com/Matheus-Emanue123)
- LinkedIn: [Matheus Emanuel](https://www.linkedin.com/in/matheus-silva-emanuel)
- Email: memanuel643@gmail.com
- Instituição: CEFET - Centro Federal de Educação Tecnológica

## 📞 Contato

Para dúvidas, sugestões ou colaborações:

- 📧 Email: matheus.emanuel@exemplo.com
- 💬 Issues: [Abrir issue no GitHub](https://github.com/Matheus-Emanue123/Trabalhos-IA/issues)
- 🔗 LinkedIn: [Conectar no LinkedIn](https://www.linkedin.com/in/matheus-silva-emanuel)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!

**Desenvolvido com 💙 no CEFET**

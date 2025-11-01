import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import os


def configurar_estilo():

    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['figure.figsize'] = (15, 5)
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.labelsize'] = 11


def criar_diretorio_graficos():

    caminho = os.path.join('..', 'data')
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    return caminho


def grafico_taxa_sucesso(ax, dados):
   
    algoritmos = list(dados.keys())
    taxas = [dados[alg]['taxa_sucesso'] for alg in algoritmos]
    
    # Cores para cada algoritmo (4 algoritmos)
    cores = ['#ff6b6b', '#ffd93d', '#6bcf7f', '#4ecdc4']
    
    # Cria barras horizontais
    y_pos = np.arange(len(algoritmos))
    barras = ax.barh(y_pos, taxas, color=cores[:len(algoritmos)], alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Configurações
    ax.set_yticks(y_pos)
    ax.set_yticklabels(algoritmos, fontsize=10)
    ax.set_xlabel('Taxa de Sucesso (%)', fontsize=11, fontweight='bold')
    ax.set_title('🏆 Taxa de Sucesso dos Algoritmos (10 execuções)', 
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xlim(0, 105)
    
    # Adiciona valores nas barras
    for i, (barra, taxa) in enumerate(zip(barras, taxas)):
        largura = barra.get_width()
        label = f'{taxa:.0f}%'
        
        # Posiciona o texto
        if taxa > 10:
            x_pos = largura - 5
            cor_texto = 'white'
            ha = 'right'
        else:
            x_pos = largura + 2
            cor_texto = 'black'
            ha = 'left'
        
        ax.text(x_pos, barra.get_y() + barra.get_height()/2, label,
                ha=ha, va='center', fontsize=11, fontweight='bold', color=cor_texto)
    
    # Linha de referência em 100%
    ax.axvline(x=100, color='green', linestyle='--', linewidth=1.5, alpha=0.5)
    
    # Ajusta posição do texto baseado no número de algoritmos
    y_text = len(algoritmos) - 0.7
    ax.text(101, y_text, '100%', fontsize=9, color='green', fontweight='bold')
    
    # Grid
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)


def grafico_tempo_vs_sucesso(ax, dados):

    algoritmos = list(dados.keys())
    tempos = [dados[alg]['tempo_medio'] * 1000 for alg in algoritmos]  # Converte para ms
    taxas = [dados[alg]['taxa_sucesso'] for alg in algoritmos]
    
    # Cores e tamanhos (4 algoritmos)
    cores = ['#ff6b6b', '#ffd93d', '#6bcf7f', '#4ecdc4']
    tamanhos = [200, 300, 400, 350]  # Tamanhos diferentes para destacar
    
    # Scatter plot
    for i, (alg, tempo, taxa) in enumerate(zip(algoritmos, tempos, taxas)):
        ax.scatter(tempo, taxa, s=tamanhos[i], c=[cores[i]], 
                  alpha=0.7, edgecolors='black', linewidth=2, label=alg)
    
    # Configurações
    ax.set_xlabel('Tempo Médio de Execução (ms)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Taxa de Sucesso (%)', fontsize=11, fontweight='bold')
    ax.set_title('⚡ Eficiência: Tempo vs Taxa de Sucesso', 
                fontsize=13, fontweight='bold', pad=15)
    
    # Limites dos eixos
    ax.set_ylim(-5, 105)
    ax.set_xlim(-0.5, max(tempos) + 2)
    
    # Linhas de referência
    ax.axhline(y=100, color='green', linestyle='--', linewidth=1, alpha=0.5)
    ax.axhline(y=50, color='orange', linestyle='--', linewidth=1, alpha=0.3)
    ax.text(max(tempos) + 0.5, 102, 'Ideal', fontsize=9, color='green')
    
    # Anotações nos pontos
    for i, (alg, tempo, taxa) in enumerate(zip(algoritmos, tempos, taxas)):
        # Nome do algoritmo (abreviado)
        if 'Restart' in alg:
            nome_curto = 'Random-Restart'
        elif 'Annealing' in alg:
            nome_curto = 'Simul. Annealing'
        elif 'Laterais' in alg:
            nome_curto = 'HC Laterais'
        else:
            nome_curto = 'HC Básico'
            
        ax.annotate(nome_curto, 
                   xy=(tempo, taxa), 
                   xytext=(10, 10),
                   textcoords='offset points',
                   fontsize=9,
                   fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor=cores[i], alpha=0.3),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', lw=1.5))
    
    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)




def grafico_barras_iteracoes(ax, dados_completos):
    """
    Gráfico de barras agrupadas mostrando min, média e max de iterações.
    Alternativa ao boxplot para dados com escalas muito diferentes.
    """
    algoritmos = list(dados_completos.keys())
    
    # Prepara dados
    minimos = []
    medias = []
    maximos = []
    
    for alg in algoritmos:
        iteracoes = []
        for resultado in dados_completos[alg]:
            iter_valor = resultado.get('iteracoes', resultado.get('iteracoes_total', 0))
            iteracoes.append(iter_valor)
        
        minimos.append(min(iteracoes))
        medias.append(np.mean(iteracoes))
        maximos.append(max(iteracoes))
    
    # Posições das barras
    x = np.arange(len(algoritmos))
    largura = 0.25
    
    # Cores
    cores = ['#ff6b6b', '#ffd93d', '#6bcf7f', '#4ecdc4']
    
    # Cria barras agrupadas
    bars1 = ax.bar(x - largura, minimos, largura, label='Mínimo', 
                   color=cores, alpha=0.4, edgecolor='black', linewidth=1)
    bars2 = ax.bar(x, medias, largura, label='Média', 
                   color=cores, alpha=0.7, edgecolor='black', linewidth=1.5)
    bars3 = ax.bar(x + largura, maximos, largura, label='Máximo', 
                   color=cores, alpha=1.0, edgecolor='black', linewidth=1)
    
    # Configurações
    ax.set_ylabel('Número de Iterações (escala log)', fontsize=11, fontweight='bold')
    ax.set_title('📊 Estatísticas de Iterações (Min/Média/Max)', 
                fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(algoritmos, rotation=15, ha='right', fontsize=9)
    
    # Escala logarítmica
    ax.set_yscale('log')
    
    # Adiciona valores nas barras médias
    for i, (bar, media) in enumerate(zip(bars2, medias)):
        altura = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, altura * 1.15,
               f'{media:.1f}',
               ha='center', va='bottom', fontsize=8, fontweight='bold', color=cores[i])
    
    # Grid e legenda
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.legend(loc='upper left', fontsize=9)


def gerar_graficos(resultados_todos):

    # Configura estilo
    configurar_estilo()
    
    # Prepara dados resumidos
    dados_resumidos = {}
    for nome, resultados in resultados_todos.items():
        sucessos = sum([r['sucesso'] for r in resultados])
        taxa_sucesso = (sucessos / len(resultados)) * 100
        tempo_medio = np.mean([r['tempo'] for r in resultados])
        
        dados_resumidos[nome] = {
            'taxa_sucesso': taxa_sucesso,
            'tempo_medio': tempo_medio
        }
    
    caminho_graficos = criar_diretorio_graficos()
    
    # Gráfico 1: Taxa de Sucesso
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    grafico_taxa_sucesso(ax1, dados_resumidos)
    plt.tight_layout()
    caminho1 = os.path.join(caminho_graficos, 'grafico_01_taxa_sucesso.png')
    plt.savefig(caminho1, dpi=300, bbox_inches='tight')
    print(f"      ✅ Salvo: {caminho1}")
    plt.close(fig1)
    
    # Gráfico 2: Tempo vs Taxa de Sucesso
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    grafico_tempo_vs_sucesso(ax2, dados_resumidos)
    plt.tight_layout()
    caminho2 = os.path.join(caminho_graficos, 'grafico_02_tempo_vs_sucesso.png')
    plt.savefig(caminho2, dpi=300, bbox_inches='tight')
    print(f"      ✅ Salvo: {caminho2}")
    plt.close(fig2)
    
    # Gráfico 3: Barras Agrupadas de Iterações (Min/Média/Max)
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    grafico_barras_iteracoes(ax3, resultados_todos)
    plt.tight_layout()
    caminho3 = os.path.join(caminho_graficos, 'grafico_03_barras_iteracoes.png')
    plt.savefig(caminho3, dpi=300, bbox_inches='tight')
    print(f"      ✅ Salvo: {caminho3}")
    plt.close(fig3)
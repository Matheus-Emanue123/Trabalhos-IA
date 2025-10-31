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
    
    # Cores para cada algoritmo
    cores = ['#ff6b6b', '#ffd93d', '#6bcf7f']
    
    # Cria barras horizontais
    y_pos = np.arange(len(algoritmos))
    barras = ax.barh(y_pos, taxas, color=cores, alpha=0.8, edgecolor='black', linewidth=1.5)
    
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
    ax.text(101, 2.3, '100%', fontsize=9, color='green', fontweight='bold')
    
    # Grid
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)


def grafico_tempo_vs_sucesso(ax, dados):

    algoritmos = list(dados.keys())
    tempos = [dados[alg]['tempo_medio'] * 1000 for alg in algoritmos]  # Converte para ms
    taxas = [dados[alg]['taxa_sucesso'] for alg in algoritmos]
    
    # Cores e tamanhos
    cores = ['#ff6b6b', '#ffd93d', '#6bcf7f']
    tamanhos = [200, 300, 400]  # Tamanhos diferentes para destacar
    
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
        nome_curto = alg.split()[0] + (' RR' if 'Restart' in alg else '')
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


def grafico_boxplot_iteracoes(ax, dados_completos):
    
    algoritmos = list(dados_completos.keys())
    
    # Prepara dados para o box plot
    dados_iteracoes = []
    for alg in algoritmos:
        iteracoes = []
        for resultado in dados_completos[alg]:
            # Usa 'iteracoes' ou 'iteracoes_total' dependendo do algoritmo
            iter_valor = resultado.get('iteracoes', resultado.get('iteracoes_total', 0))
            iteracoes.append(iter_valor)
        dados_iteracoes.append(iteracoes)
    
    # Cores
    cores = ['#ff6b6b', '#ffd93d', '#6bcf7f']
    
    # Cria box plot
    bp = ax.boxplot(dados_iteracoes, 
                    labels=algoritmos,
                    patch_artist=True,
                    notch=True,
                    showmeans=True,
                    meanprops=dict(marker='D', markerfacecolor='red', markersize=8),
                    medianprops=dict(color='black', linewidth=2),
                    boxprops=dict(linewidth=1.5),
                    whiskerprops=dict(linewidth=1.5),
                    capprops=dict(linewidth=1.5))
    
    # Aplica cores
    for patch, cor in zip(bp['boxes'], cores):
        patch.set_facecolor(cor)
        patch.set_alpha(0.7)
    
    # Configurações
    ax.set_ylabel('Número de Iterações', fontsize=11, fontweight='bold')
    ax.set_title('📊 Distribuição de Iterações (Box Plot)', 
                fontsize=13, fontweight='bold', pad=15)
    ax.set_xticklabels(algoritmos, rotation=15, ha='right', fontsize=9)
    
    # Adiciona valores médios
    medias = [np.mean(dados) for dados in dados_iteracoes]
    for i, (media, dados) in enumerate(zip(medias, dados_iteracoes)):
        ax.text(i + 1, max(dados) + 3, f'μ={media:.1f}', 
               ha='center', fontsize=9, fontweight='bold', color=cores[i])
    
    # Grid
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    # Legenda
    legenda_elementos = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='red', 
                  markersize=8, label='Média'),
        plt.Line2D([0], [0], color='black', linewidth=2, label='Mediana')
    ]
    ax.legend(handles=legenda_elementos, loc='upper right', fontsize=9)


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
    print("   → Criando Gráfico 1: Taxa de Sucesso...")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    grafico_taxa_sucesso(ax1, dados_resumidos)
    plt.tight_layout()
    caminho1 = os.path.join(caminho_graficos, 'grafico_01_taxa_sucesso.png')
    plt.savefig(caminho1, dpi=300, bbox_inches='tight')
    print(f"      ✅ Salvo: {caminho1}")
    plt.close(fig1)
    
    # Gráfico 2: Tempo vs Taxa de Sucesso
    print("   → Criando Gráfico 2: Tempo vs Taxa de Sucesso...")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    grafico_tempo_vs_sucesso(ax2, dados_resumidos)
    plt.tight_layout()
    caminho2 = os.path.join(caminho_graficos, 'grafico_02_tempo_vs_sucesso.png')
    plt.savefig(caminho2, dpi=300, bbox_inches='tight')
    print(f"      ✅ Salvo: {caminho2}")
    plt.close(fig2)
    
    # Gráfico 3: Box Plot de Iterações
    print("   → Criando Gráfico 3: Box Plot de Iterações...")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    grafico_boxplot_iteracoes(ax3, resultados_todos)
    plt.tight_layout()
    caminho3 = os.path.join(caminho_graficos, 'grafico_03_boxplot_iteracoes.png')
    plt.savefig(caminho3, dpi=300, bbox_inches='tight')
    print(f"      ✅ Salvo: {caminho3}")
    plt.close(fig3)
    
    print(f"\n✅ 3 gráficos salvos com sucesso em: {caminho_graficos}")
    print("="*70 + "\n")
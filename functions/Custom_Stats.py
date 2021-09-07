# -----------------------------------------------------------------------------------
# Funções auxiliares estatísticas
# -----------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
    sumStats(df :: dataframe)

Gera um sumário estatístico completo de um dataframe df. As estatísticas incluem
medidas de tendência central (X̅ e P50%), medidas de posição (Min, P10%, P99.5% e Max),
medidas de dispersão (Amp, S², S e Cᵥ) e medida de forma (Skew).

Parâmetro:
- df : dataframe com as features utilizadas para o cálculo do sumário estatístico

Retorna:
- stats : dataframe com o sumário estatístico

"""

def sumStats(df = None):
    stats = df.describe(percentiles = [0.1, 0.5, 0.995]).T

    stats['Amp'] = (df.max() - df.min()).tolist() # amplitude (max = min)
    stats['S²'] = df.var().tolist()               # variância
    stats['Cᵥ'] = (df.std() / df.mean()).tolist() # coeficiente de variação
    stats['Skew'] = df.skew().tolist()            # coeficiente de assimetria

    stats = stats.rename(columns={'mean':'X̅','std':'S','min':'Min','max':'Max'})
    
    return stats[['X̅', '50%', 'Min','10%','99.5%','Max','Amp','S²','S','Cᵥ','Skew']]

# -----------------------------------------------------------------------------------

"""
    plotBoxplots(df :: dataframe, cols :: list)

Plota n boxplots, sendo n o número de features presentes na lista cols.

Parâmetros:
- df : dataframe com os dados
- cols : lista de features

Retorna:
- Um boxplot por feature presente na lista cols

"""

def plotBoxplots(df, cols = None):
    n = len(cols)
    fig, axs = plt.subplots(n, 1, figsize = (10, n * 2))
    
    for ax, f in zip(axs, cols):
        sns.boxplot(y = f, x = 'COD', data = df, ax = ax)
        if f != cols[n - 1]:
            ax.axes.get_xaxis().set_visible(False)

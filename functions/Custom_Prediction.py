# -----------------------------------------------------------------------------------------------------------
# Funções auxiliares para visualização das predições
# -----------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    plotPrediction(train :: dataframe, test :: dataframe, ŷ :: narray, model :: string, cm :: colormap)

Plota o mapa geológico preditivo, o mapa geológico e o mapa com as inconsistências entre o mapa
preditivo e o mapa geológico.

Parâmetros:
- train : dataframe (t, m) representativo dos dados de treino
- test : dataframe (n-t, m) representativo dos dados de treino
- ŷ : narray (n-t, ) com as predições do target de um determinado modelo
- model : string com o nome do modelo utilizado. Corresponde ao título do mapa geológico preditivo
- cm : mapa de cores utilzado

Retorna:
- Mapa geológico preditivo do modelo, mapa geológico de campo e o mapa de inconsistências

"""

def plotPrediction(train, test, ŷ, model = None, cm = None):
    # criação do dataframe mapa preditivo (df_pred + df_train)
    pred = pd.DataFrame(ŷ, columns = ['TARGET'])
    coords = test[['X','Y']]
    df_pred = pd.concat([pred, coords], axis = 1)
    df_train = train[['X', 'Y', 'TARGET']]
    df_pred_map = pd.concat([df_pred, df_train]).sort_values(by = ['X','Y'])
    df_pred_map.rename(columns = {'TARGET' : 'PRED'}, inplace = True)

    # criação do dataframe mapa geológico (train + test)
    df_geo_map = pd.concat([train, test])[['X','Y','TARGET']]
    df_geo_map.sort_values(by = ['X','Y'], inplace = True)

    # criação do dataframe inconsistências
    df_miss = pd.merge(df_pred_map, df_geo_map, how = 'left')
    df_miss['MISS'] = df_miss['TARGET'] - df_miss['PRED']
    df_miss.query('MISS != 0', inplace = True)
    
    fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (10, 5))

    # plot do mapa preditivo
    pred_map = ax1.scatter(data = df_pred_map, x = 'X', y = 'Y', c = 'PRED', cmap = cm, s = 1.5, marker = 's')
    ax1.set_title(model, size = 16)
    ax1.set_xlabel('X (m)', size = 14)
    ax1.set_ylabel('Y (m)', size = 14)
    
    # plot do mapa geológico
    ax2.scatter(data = df_geo_map, x = 'X', y = 'Y', c = 'TARGET', cmap = cm, s = 1.5, marker = 's')
    ax2.set_title("Mapa geológico", size = 16)
    ax2.set_xlabel('X (m)', size = 14)
    
    # plot do mapa de inconsistências
    ax3.scatter(data = df_miss, x = 'X', y = 'Y', c = 'red', s = 0.1, marker = 'o')
    ax3.set_title("Inconsistências", size = 16)
    ax3.set_xlabel('X (m)', size = 14)

    # legenda de unidades
    cbar = fig.colorbar(pred_map, ax = ax1, use_gridspec = False, anchor = (-27, 0))
    cbar.ax.set_yticklabels(['MAcgg','PP3csbg','PP34b','PP4esjc','PP4esb','PP4egm'])
    
    plt.tight_layout();

# -----------------------------------------------------------------------------------------------------------

"""
    plotPredictionProba(pr_ŷ :: narray, test :: dataframe, lith_list :: list, cm :: string)

Plota um mapa de probabilidades preditas para cada uma das 6 classes (unidades).

Parâmetros:
- pr_ŷ : narray (n-t, 6) representando as predições probabilísticas para cada uma das classes
- test : dataframe (n-t, m) representativo dos dados de treino
- lith_list : lista com as unidades ordenadas pelos seus códigos
- cm : mapa de cores utilzado

Retorna:
- Um mapa de probabilidades para cada uma das 6 unidades

"""

def plotPredictionProba(pr_ŷ, test, lith_list, cm = None):
    x = test['X']
    y = test['Y']

    fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (12, 10))

    for ax, i in zip(axs.flat, range(6)):
        _map = ax.scatter(x, y, c = pr_ŷ[:,i], cmap = cm, s = 1.5, marker = 's')
        fig.colorbar(_map, ax = ax, boundaries = np.linspace(0.0,1.0,6))
        ax.set_title(str(lith_list[i]), size = 16)
        
    plt.tight_layout();

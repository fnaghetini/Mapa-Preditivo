# --------------------------------------------------------------------------------
# Função auxiliar para divisão entre dados de treino e teste
# --------------------------------------------------------------------------------

# bibliotecas necessárias
from math import ceil
import numpy as np
import pandas as pd

"""
    customTrainTestSplit(df :: dataframe, feat_list :: list, coords_list :: list,
                         samp_per_class :: int, threshold = float, coords :: bool)

Realiza a divisão dos dados entre treino e teste. O conjunto de treino é obtido a
partir de uma amostragem aleatória de samp_per_class exemplos por unidade
litoestratigráfica. Caso uma unidade apresente um número de exemplos menor que
samp_per_class, uma porcentagem de suas instâncias são aleatoriamente amostradas,
sendo essa porcentagem definida pelo parâmetro threshold.

Parâmetros:
- df : dataframe (n, m) com os dados brutos
- feat_list : lista de features presentes em df
- coords_list : lista de coordenadas presentes em df
- samp_per_class : número (int) de exemplos amostrados por unidade (default = 100)
- threshold : porcentagem de exemplos que serão amostrados, caso uma unidade
apresente um número de ocorrências inferior a samp_per_class (default = 0.7)
- coords : se True, retorna as coordenadas X e Y de treino e teste (default = false)

Retorna:
- X_train : narray (t, m) com as features do conjunto de treino
- y_train : narray (t, ) com o target do conjunto de treino
- coord_train : narray (t, 2) com as coordenadas do conjunto de treino (apenas se
coords = True)
- X_test : narray (n-t, m) com as features do conjunto de teste
- y_test : narray (n-t, ) com o target do conjunto de teste
- coord_test : narray (n-t, 2) com as coordenadas do conjunto de teste (apenas se
coords = True)

"""

def customTrainTestSplit(df, feat_list, coords_list, samp_per_class = 100, threshold = 0.7, coords = False):
    np.random.seed(42)
    # embaralhando dataframe
    df_shuffled = df.sample(frac = 1).reset_index(drop = True)
    # lista classes/unidades
    classes = df_shuffled['TARGET'].unique()
    # dataframe vazio de treino
    train = pd.DataFrame()
    
    for c in classes:
        unid = df_shuffled[df_shuffled['TARGET'] == c]
        len_unid = len(unid)

        if len_unid <= samp_per_class:
            𝒮 = unid.sample(ceil(len_unid * threshold))
        else:
            𝒮 = unid.sample(samp_per_class)   
        
        train = pd.concat([train, 𝒮])
            
    # embaralhando treino e teste
    test = df_shuffled.drop(train.index).sample(frac = 1).reset_index(drop = True)
    train = train.sample(frac = 1).reset_index(drop = True)
    
    # divisão treino e teste
    X_train, y_train, coord_train = train[feat_list].values, train['TARGET'].values, train[coords_list].values
    X_test, y_test, coord_test = test[feat_list].values, test['TARGET'].values, test[coords_list].values
    
    if coords:
        return X_train, y_train, coord_train, X_test, y_test, coord_test
    else:
        return X_train, y_train, X_test, y_test
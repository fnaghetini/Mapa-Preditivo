# -----------------------------------------------------------------------------------------------------------
# Funções auxiliares para predições
# -----------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    createPredTable(dic_ŷ_train :: dict, dic_ŷ_test :: narray,
                    train :: dataframe, test :: dataframe)

Retorna um dataframe com as coordenadas e as predições de cada modelo treinado.

Parâmetros:
- dic_ŷ_train : dicionário com as predições de cada modelo para o conjunto de treino
- dic_ŷ_test : dicionário com as predições de cada modelo para o conjunto de teste
- train : dataframe (t, m) representativo dos dados de treino
- test : dataframe (n-t, m) representativo dos dados de teste

Retorna:
- df_pred : dataframe(n, 9) com as coordenadas e as predições de cada modelo

"""

def createPredTable(dic_ŷ_train, dic_ŷ_test, train, test):
    train_coords = train[['X','Y']]
    test_coords  = test[['X','Y']]
    df_pred = pd.concat([train_coords,test_coords])
    
    for model in dic_ŷ_test.keys():
        ŷ_train = list(dic_ŷ_train[model])
        ŷ_test = list(dic_ŷ_test[model])
        map_labels = ŷ_train + ŷ_test
        df_pred[model] = map_labels
        
    return df_pred

# -----------------------------------------------------------------------------------------------------------

"""
    createMissClassifTable(df_pred :: dataframe, y_train :: narray, y_test :: narray)

Retorna um dataframe com as coordenadas e as inconsistências entre o mapa geológico e cada mapa preditivo.
As colunas de inconsistências por modelo são binárias, de modo que 1 simboliza inconsistência entre os mapas.

Parâmetros:
- df_pred : dataframe (n, 9) representativo das predições de cada modelo
- y_train : narray (t, ) representativo dos labels de treino
- y_test : narray (n-t, ) representativo dos labels de teste

Retorna:
- df_miss : dataframe(n, 9) com as coordenadas e as inconsistências apresentadas por cada modelo

"""

def createMissClassifTable(df_pred, y_train, y_test):
    model_list = df_pred.columns[2:]
    true_labels = list(y_train) + list(y_test)
    df_miss = df_pred[['X','Y']]
    
    for model in model_list:
        diff_list = true_labels - df_pred[model]
        miss_list = []
        
        for diff in diff_list:
            if diff == 0:
                miss_list.append(0)
            else:
                miss_list.append(1)
        
        df_miss['MISS_' + model] = miss_list
    
    return df_miss

# -----------------------------------------------------------------------------------------------------------

"""
    createPredProbaTable(pr_ŷ_train :: narray, pr_ŷ_test :: narray,
                         train :: dataframe, test :: dataframe)

Retorna um dataframe com as probabilidades preditas para cada uma das 6 classes (unidades).

Parâmetros:
- pr_ŷ_train : narray (t, 6) representando as predições probabilísticas para cada uma das classes
no conjunto de treino
- pr_ŷ_test : narray (n-t, 6) representando as predições probabilísticas para cada uma das classes
no conjunto de teste
- train : dataframe (t, m) representativo dos dados de treino
- test : dataframe (n-t, m) representativo dos dados de teste

Retorna:
- df_proba_pred : dataframe (n, 8) com as coordenadas e probabilidades para cada uma das classes

"""

def createPredProbaTable(pr_ŷ_train, pr_ŷ_test, train, test):
    litho_list = ['MAcgg','PP3csbg','PP34b','PP4esjc','PP4esb','PP4egm']
    train_coords = train[['X','Y']]
    test_coords  = test[['X','Y']]
    df_proba_pred = pd.concat([train_coords,test_coords])
    pr_ŷ = np.concatenate([pr_ŷ_train,pr_ŷ_test])
    i = 0

    for litho in litho_list:
        df_proba_pred[litho] = pr_ŷ[:,i]
        i += 1

    return df_proba_pred

# -----------------------------------------------------------------------------------------------------------

"""
    categoricalCrossEntropy(pr_ŷ_train :: narray, pr_ŷ_test :: narray,
                            ŷ_train :: narray, ŷ_test :: narray,
                            train :: dataframe, test :: dataframe)

Retorna um dataframe com as coordenadas e entropia cruzada.

Parâmetros:
- pr_ŷ_train : narray (t, 6) representando as predições probabilísticas para cada uma das classes
do conjunto de treino
- pr_ŷ_test : narray (n-t, 6) representando as predições probabilísticas para cada uma das classes
do conjunto de teste
- ŷ_train : narray(t, ) representando as predições do conjunto de treino
- ŷ_test : narray(n-t, ) representando as predições do conjunto de teste
- train : dataframe (t, m) representativo dos dados de treino
- test : dataframe (n-t, m) representativo dos dados de teste

Retorna:
- df_entropy : dataframe(n, 3) com as coordenadas e entropia cruzada

"""

def categoricalCrossEntropy(pr_ŷ_train, pr_ŷ_test, ŷ_train, ŷ_test, train, test):
    train_coords = train[['X','Y']]
    test_coords  = test[['X','Y']]
    df_entropy = pd.concat([train_coords,test_coords])

    ŷ = np.concatenate([ŷ_train,ŷ_test])
    pr_ŷ = np.concatenate([pr_ŷ_train,pr_ŷ_test])

    size = len(df_entropy)
    entropy_list = []
    
    for i in range(size):
        target = ŷ[i]
        pred_prob = pr_ŷ[i,:]
        x = pred_prob[target - 1]
        entropy = - np.log2(x)
        entropy_list.append(entropy)
        
    df_entropy['ENTROPY'] = entropy_list
    
    return df_entropy

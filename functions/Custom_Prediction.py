# -----------------------------------------------------------------------------------------------------------
# Funções auxiliares para predições
# -----------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    createPredTable(dic_ŷ :: dict, train :: dataframe, test :: dataframe)

Retorna um dataframe com as coordenadas e as predições de cada modelo treinado.

Parâmetros:
- dic_ŷ : dicionário com as predições de cada modelo
- train : dataframe (t, m) representativo dos dados de treino
- test : dataframe (n-t, m) representativo dos dados de teste

Retorna:
- df_pred : dataframe(n, 9) com as coordenadas e as predições de cada modelo

"""

def createPredTable(dic_ŷ, train, test):
    train_labels = list(train['TARGET'])
    train_coords = train[['X','Y']]
    test_coords = test[['X','Y']]
    df_pred = pd.concat([train_coords,test_coords])
    
    for model in dic_ŷ.keys():
        ŷ = list(dic_ŷ[model])
        map_labels = train_labels + ŷ
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
    createPredProbaTable(pr_ŷ :: narray, test :: dataframe)

Retorna um dataframe com as probabilidades preditas para cada uma das 6 classes (unidades).

Parâmetros:
- pr_ŷ : narray (n-t, 6) representando as predições probabilísticas para cada uma das classes
- test : dataframe (n-t, m) representativo dos dados de treino

Retorna:
- df_proba_pred : dataframe (n-t, 8) com as coordenadas e probabilidades para cada uma das classes

"""

def createPredProbaTable(pr_ŷ, test):
    litho_list = ['MAcgg','PP3csbg','PP34b','PP4esjc','PP4esb','PP4egm']
    df_proba_pred = test[['X','Y']]
    i = 0

    for litho in litho_list:
        df_proba_pred[litho] = pr_ŷ[:,i]
        i += 1

    return df_proba_pred

# -----------------------------------------------------------------------------------------------------------

"""
    categoricalCrossEntropy(pr_ŷ :: narray, ŷ :: narray, test :: dataframe)

Retorna um dataframe com as coordenadas e entropia cruzada.

Parâmetros:
- pr_ŷ : narray (n-t, 6) representando as predições probabilísticas para cada uma das classes
- ŷ : narray(n-t, ) representando as predições do conjunto de teste
- test : dataframe (n-t, m) representativo dos dados de teste

Retorna:
- df_entropy : dataframe(n-t, 3) com as coordenadas e entropia cruzada.

"""

def categoricalCrossEntropy(pr_ŷ, ŷ, test):
    test_size = len(test)
    df_entropy = test[['X','Y']]
    entropy_list = []
    
    for i in range(test_size):
        target = ŷ[i]
        pred_prob = pr_ŷ[i,:]
        x = pred_prob[target - 1]
        entropy = - np.log2(x)
        entropy_list.append(entropy)
        
    df_entropy['ENTROPY'] = entropy_list
    
    return df_entropy

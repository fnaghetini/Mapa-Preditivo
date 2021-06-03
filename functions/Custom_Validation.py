# ---------------------------------------------------------------------------------------------------
# Funções auxiliares para geração de reports de validação
# ---------------------------------------------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

"""
    validationReport(pipeline :: pipeline, X_train :: narray, y_train :: narray, cv :: object)

Retorna um report com as métricas resultantes da validação cruzada por modelo. As métricas incluem
acurácia, F1-score, precisão, revocação (ponderadas pelo número de exemplos de cada unidade).

Parâmetros:
- pipeline : pipeline completa com as etapas de processamento até a instanciação do classificador
- X_train : narray (t, m) das features de treino
- y_train : narray (t, ) do target de treino
- cv : objeto de validação cruzada

Retorna:
- df_val : dataframe com as métricas resultantes da validação cruzada por modelo

"""

def validationReport(pipeline, X_train, y_train, cv):
    model_list = pipeline.keys()
    metric_list = ['f1_weighted','precision_weighted','recall_weighted','accuracy']
    df_val = pd.DataFrame(columns = model_list, index = metric_list)

    for model in model_list:
        metrics = []
        for metric in metric_list:
            cv_scores = cross_val_score(pipeline[model], X_train, y_train, scoring = metric, cv = cv)
            # média dos scores de validação cruzada
            μ_cv = round(cv_scores.mean(), 3)
            metrics.append(μ_cv)
    
        df_val[model] = metrics
    
    return df_val

# ----------------------------------------------------------------------------------------------------

"""
    testReport(dic_ŷ :: dict, y_test :: narray)

Retorna um report com as métricas resultantes do conjunto de teste por modelo. As métricas incluem
acurácia, F1-score, precisão, revocação (ponderadas pelo número de exemplos de cada unidade).

Parâmetros:
- dic_ŷ : dicionário com as predições de cada modelo
- y_test : narray (n-t, ) com o target do conjunto de teste

Retorna:
- df_metrics : dataframe com as métricas resultantes do conjunto de teste por modelo

"""

def testReport(dic_ŷ, y_test):
    model_list = dic_ŷ.keys()
    metric_list = ['f1_weighted','precision_weighted','recall_weighted','accuracy']
    df_metrics = pd.DataFrame(columns = model_list, index = metric_list)

    for ŷ in dic_ŷ:
        metrics = []
        # f1-score
        f1 = round(f1_score(y_test, dic_ŷ[ŷ], average = 'weighted'), 3)
        metrics.append(f1)
        # precisão
        p = round(precision_score(y_test, dic_ŷ[ŷ], average = 'weighted'), 3)
        metrics.append(p)
        # revocação
        r = round(recall_score(y_test, dic_ŷ[ŷ], average = 'weighted'), 3)
        metrics.append(r)
        # acurácia
        acc = round(accuracy_score(y_test, dic_ŷ[ŷ]), 3)
        metrics.append(acc)

        df_metrics[ŷ] = metrics

    return df_metrics

# ---------------------------------------------------------------------------------------------------
# Funções auxiliares para pré-processamento dos dados
# ---------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

"""
    MaskedPCA(n_components :: int, mask :: narray)

Classe que realiza uma Análise de Componentes Principais (PCA) apenas das features definidas pelo
parâmetro mask. O número de componentes principais pode ser informado por meio do parâmetro
n_components.

Parâmetros:
- n_components : número (int) de componentes principais
- mask : narray (n, ), sendo n o número de features utilizadas na PCA. Este parâmetro indica os
índices das colunas das features

Retorna:
- instância da classe MaskedPCA

"""

class MaskedPCA(BaseEstimator, TransformerMixin):
    def __init__(self, n_components = 3, mask = None):
        self.n_components = n_components
        self.mask = mask

    def fit(self, X, y = None):
        self.pca = PCA(n_components = self.n_components)
        mask = self.mask
        mask = self.mask if self.mask is not None else slice(None)
        self.pca.fit(X[:, mask])
        return self

    def transform(self, X, y = None):
        mask = self.mask if self.mask is not None else slice(None)
        pca_transformed = self.pca.transform(X[:, mask])
        if self.mask is not None:
            remaining_cols = np.delete(X, mask, axis = 1)
            return np.hstack([remaining_cols, pca_transformed])
        else:
            return pca_transformed

# ---------------------------------------------------------------------------------------------------

"""
    univariateSelector(X_train :: narray, y_train :: narray, func :: function)

Retorna os scores de importância das features de acordo com uma função func informada pelo usuário.

Parâmetros:
- X_train : narray (t, m) das features de treino
- y_train : narray (t, ) do target de treino
- func : função definida para selecionar as features. As duas opções são f_classif e
mutual_info_classif
- n_features : número (int) de features a serem selecionadas. Default = 'all' (única string aceita)

Retorna:
- X_train_fs : narray(t, n_features) das features de treino selecionadas
- scores : scores de importância

"""

def univariateSelector(X_train, y_train, func):
    selector = SelectKBest(score_func = func, k = 'all')
    selector.fit(X_train, y_train)

    X_train_fs = selector.transform(X_train)
    scores = selector.scores_

    return X_train_fs, scores

# ---------------------------------------------------------------------------------------------------

"""
    plotSelectionScores(scores :: narray, features :: list, col :: string, ec :: string)

Plota um gráfico de barras dos scores de importância de cada umas das features em ordem crescente.

Parâmetros:
- scores : narray (k, ) com os scores das features mais importantes
- features : lista com os nomes das features
- col : cor do gráfico de barras
- ec : cor da borda do gráfico de barras

Retorna:
- Gráfico de barras com os scores de importância de cada uma das features

"""

def plotSelectionScores(scores, features, col = None, ec = None):
    
    dic_fs = {'FEATURES' : features, 'SCORES' : list(scores)}
    df_scores = pd.DataFrame(dic_fs).sort_values('SCORES', ascending = False)
    
    plt.figure(figsize = (9,3))
    plt.bar('FEATURES', 'SCORES', data = df_scores, color = col, edgecolor = ec)
    plt.ylabel('Score', size = 14)
    plt.yticks(size = 12)
    plt.xticks(rotation = 45, size = 12)

    plt.tight_layout();

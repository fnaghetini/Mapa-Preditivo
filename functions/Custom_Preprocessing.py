# ---------------------------------------------------------------------------------------------------
# Classe auxiliar para realização da PCA
# ---------------------------------------------------------------------------------------------------

import numpy as np 
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import PCA

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

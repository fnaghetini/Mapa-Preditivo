# ----------------------------------------------------
# Função auxiliar para a etapa de limpeza dos dados
# ----------------------------------------------------

# bibliotecas necessárias
import pandas as pd

"""
    truncateVar(data :: dataframe, col :: string)

Realiza o truncamento de uma variável radiométrica col,
tendo como referência os limiares inferior (lower) e
superior (upper).

Parâmetros:
- data : dataframe que contém a variável radiométrica de
interesse
- col : variável a ser truncada

Retorna:
- serie : variável (serie) truncada

"""

def truncateVar(data = None, col = None):

    lower = data[col].mean() / 10
    upper = data[col].quantile(0.995)
    var_trunc = []
    
    for v in data[col]:
        if v <= lower:
            v = lower
            var_trunc.append(v)
        elif v >= upper:
            v = upper
            var_trunc.append(v)
        else:
            var_trunc.append(v)
        
    return pd.Series(var_trunc)
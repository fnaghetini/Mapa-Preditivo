# -----------------------------------------------------------------------------------------------------------
# Função auxiliar para exportação dos resultados como raster
# -----------------------------------------------------------------------------------------------------------

import os
import numpy as np
import pandas as pd
from osgeo import gdal

"""
    df2Raster(df :: dataframe, filename :: string, col :: string)

Converte um dataframe em raster (.tif). SIRGAS2000 UTM Zona 23S é o sistema de referência adotado. A resolução
do raster é de 62.5 m x 62.5 m.

Parâmetros:
- df : dataframe(n, p). Deve conter as coordenadas (x e Y) e uma ou mais variáveis de interesse
- filename : nome do raster. Não é necessário adicionar o sufixo '.tif'
- col : variável de interesse

Retorna:
- raster correspondente aos dados de entrada

"""

def df2Raster(df, filename, col = None):

    # Diretórios
    csv_path = f"output/rasters/{filename}.csv"
    vrt_path = f"output/rasters/{filename}.vrt"
    tif_path = f"output/rasters/{filename}.tif"

    # Ordenamento do dataframe no padrão GDAL
    df = df[['X','Y',col]]
    df_sorted = df.sort_values(by=['Y','X'], ascending=[False,True])

    # CSV temporário
    df_sorted.to_csv(csv_path, index=False)

    # VRT temporário
    f = open(vrt_path, "w")
    f.write(f"<OGRVRTDataSource>\n \
        <OGRVRTLayer name=\"{filename}\">\n \
            <SrcDataSource>{csv_path}</SrcDataSource>\n \
            <GeometryType>wkbPoint</GeometryType>\n \
            <GeometryField encoding=\"PointFromColumns\" x=\"X\" y=\"Y\" z=\"{col}\"/>\n \
        </OGRVRTLayer>\n \
</OGRVRTDataSource>")
    f.close()

    # Conversão em raster
    r = gdal.Rasterize(tif_path, vrt_path, outputSRS="EPSG:31983",
                       xRes=62.5, yRes=-62.5, attribute=col, noData=np.nan)
    r = None

    # Remoção dos arquivos temporários
    os.remove(vrt_path)
    os.remove(csv_path)
    
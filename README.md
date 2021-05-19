# Mapa  Geológico Preditivo

### Trabalho de Conclusão de Curso - Geologia / IGC / UFMG

Orientandos: [Franco Naghetini](https://github.com/fnaghetini) & [Guilherme Silveira](https://github.com/guiasilveira)

Orientadores: [Pedro Casagrande](https://github.com/casagrandepedro) & [Iago Costa](https://github.com/iagoslc)

## Introdução
De forma geral, a teoria do aprendizado estatístico supervisionado visa aprender uma função desconhecida  **𝑓:𝑥↦𝑦**  por meio do treinamento de um agente com exemplos  **{(𝑥(1),𝑦(1)),(𝑥(2),𝑦(2)),…,(𝑥(𝑛),𝑦(𝑛))}**  de entrada e saída da função.

Nesse sentido, o objetivo deste trabalho é solucionar uma tarefa supervisionada de classificação multinomial  **𝑇**  que consiste em predizer as unidades litoestratigráficas  **𝑦𝑖**  em um determinado domínio  **𝐷**  como função de sensores remotos  **𝑥𝑖**  e com base em anotações/interpretações  **𝑦(𝑖)=𝑓(𝑥(𝑖))**  feitas pelos geólogos que realizaram o mapeamento da área.

O produto final é um **mapa geológico preditivo 1:25.000 da região de Diamantina (MG)** que pode ser utilizado como um meio de reconciliação entre os dados/interpretações de campo e os sensores remotos. Nesse sentido, as inconsistências entre o mapa geológico e o mapa preditivo podem fornecer insights e orientar futuras campanhas de mapeamento na região.

## Fluxo de trabalho

O [fluxo de trabalho](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/workflow/workflow.pdf) deste projeto é dividido em três partes principais:

1. Coleta e manipulação dos rasters
2. [Limpeza e análise exploratória dos dados](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/notebook1.ipynb)
3. [Pré-processamento, modelagem dos dados e validação dos modelos](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/notebook2.ipynb)

## Informações gerais

### Sistema de referência

- *EPSG: 31983*
- *Projeção: UTM*
- *Zona: 23S*
- *Datum: SIRGAS2000*
- *Unidade: m*
- *Elipsoide: GRS 1980*
- *Resolução: 62.5 m x 62.5 m*
- *Extensão: (xmin = 634163.67, ymin = 7969052.06, xmax = 640038.70, ymax = 7983240.00)*

### Unidades litoestratigráficas

|  ID  |  Sigla   |  Código  |                 Unidade                  |      Hexadecimal      |      RGB      |
|:----:|:--------:|:--------:|:----------------------------------------:|:---------------------:|:-------------:|
|   1  |  Cx_GG   |  MAcgg   |        Complexo Granito-Gnáissico        |        #fabee8        | (255,190,232) |
|   2  |  Fm_BG   |  PP3csbg |         Formação Barão de Guaicuí        |        #cccccc        | (204,204,204) |
|   3  |  Fm_B    |  PP34b   |          Formação Bandeirinha            |        #e600a9        | (230,000,169) |
|   4  |  Fm_SJC  |  PP4esjc |       Formação São João da Chapada       |        #ffff00        | (255,255,000) |
|   5  |  Fm_SB   |  PP4esb  |         Formação Sopa Brumadinho         |        #9b0000        | (000,000,255) |
|   6  |  Fm_GM   |  PP4egm  |         Formação Galho do Miguel         |        #73ffdf        | (115,255,223) |

### Dicionário de features

|    Feature    |  Unidade  |                         Fonte                         |                           Descrição                           |
|:-------------:|:---------:|:-----------------------------------------------------:|:-------------------------------------------------------------:|
|  GT  | nT/m | Biblioteca UFMG                                                     |Gradiente total                                                |
|   K  |   %  | Biblioteca UFMG                                                     |Potássio                                                       |
|  TH  |  ppm | Biblioteca UFMG                                                     |Tório                                                          |
|   U  |  ppm | Biblioteca UFMG                                                     |Urânio                                                         |
|  CT  | μR/h | Biblioteca UFMG                                                     |Contagem total                                                 |
| U_K  |   -  | Biblioteca UFMG                                                     |Razão urânio / potássio                                        |
| TH_K |   -  | Biblioteca UFMG                                                     |Razão tório / potássio                                         |
| U_TH |   -  | Biblioteca UFMG                                                     |Razão urânio / tório                                           |
|  MDT |   m  | Biblioteca UFMG                                                     |Modelo digital de terreno                                      |
|  MDE |   m  | [INPE](http://www.dsr.inpe.br/topodata/dados.php)                   |Modelo digital de elevação                                     |
|  B01 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - COSTAL (0.433 - 0.453 μm)               |
|  B02 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - AZUL (0.450 - 0.515 μm)                 |
|  B03 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - VERDE (0.525 - 0.600 μm)                |
|  B04 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - VERMELHO (0.630 - 0.680 μm)             |
|  B05 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - INFRAVERMELHO PRÓXIMO (0.845 - 0.885 μm)|
|  B06 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (1.560 - 1.660 μm)  |
|  B07 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (2.100 - 2.300 μm)  |
|  B08 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - PANCROMÁTICO (0.500 - 0.680 μm)         |
|  B09 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - CIRRUS (1.360 - 1.390 μm)               |
|   R  |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - VERMELHO                               |
|   G  |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - VERDE                                  |
|   B  |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - AZUL                                   |

## Versões do software

- [python v3.6.10](https://docs.python.org/release/3.6.10/)
- [conda v4.9.2](https://docs.conda.io/projects/conda/en/master/release-notes.html)
- [jupyter v1.0.0](https://jupyter.org/documentation)
- [ipython v7.16.1](https://ipython.org/documentation.html)
- [numpy v1.19.5](https://numpy.org/doc/)
- [pandas v1.0.5](https://pandas.pydata.org/docs/)
- [matplotlib v3.2.2](https://matplotlib.org/stable/gallery/index.html)
- [seaborn v0.10.1](https://seaborn.pydata.org/examples/index.html)
- [statsmodels v0.11.1](https://www.statsmodels.org/stable/index.html)
- [scipy v1.5.0](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
- [scikit-learn v0.24.1](https://scikit-learn.org/stable/auto_examples/index.html)
- [imbalanced-learn v0.8.0](https://imbalanced-learn.org/stable/)
- [geopandas v0.9.0](https://geopandas.org/docs/user_guide.html)
- [rasterio v1.1.7](https://rasterio.readthedocs.io/en/latest/api/index.html)
- [folium v0.12.0](https://python-visualization.github.io/folium/)
- [xgboost v1.4.0](https://xgboost.readthedocs.io/en/latest/index.html#)

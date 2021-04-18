# Mapa Litoestratigráfico Preditivo - Diamantina (MG)

### Trabalho de Conclusão de Curso - Geologia / IGC / UFMG

Orientandos: [Franco Naghetini](https://github.com/fnaghetini) & [Guilherme Silveira](https://www.linkedin.com/in/guilherme-silveira)

Orientadores: [Pedro Casagrande](https://www.linkedin.com/in/pedro-casagrande) & [Iago Costa](https://github.com/iagoslc)

## Objetivo
O trabalho tem como objetivo a produção de um **mapa litoestratigráfico preditivo 1:25.000**, a partir de dados de sensores remotos e dados do mapeamento geológico realizado pelos alunos da disciplina de Estágio Supervisionado do ano de 2018, na região de Diamantina. As predições das unidades litoestratigráficas serão realizadas, utilizando algoritmos de *Machine Learning* (aprendizado supervisionado).

O produto gráfico final (i.e., mapa litoestratigráfico preditivo) pode ser utilizado como um meio de reconciliação entre os dados de mapeamento de campo e os sensores remotos. Nesse sentido, as inconsistências entre o mapa geológico e o mapa litoestratigráfico preditivo podem fornecer *insights* e orientar futuras campanhas de mapeamento na região de Diamantina (MG).

## Informações gerais

### Sistema de referência

- EPSG: 31983
- Projeção: UTM
- Zona: 23S
- Datum: SIRGAS2000
- Unidade: m
- Elipsoide: GRS 1980
- Resolução: 62.5 m x 62.5 m
- Extensão: (xmin = 634163.67, ymin = 7969052.06, xmax = 640038.70, ymax = 7983240.00)

### Unidades litoestratigráficas

|  ID  |  Sigla   |  Código  |                 Unidade                  |      Hexadecimal      |      RGB      |
|:----:|:--------:|:--------:|:----------------------------------------:|:---------------------:|:-------------:|
|   1  |  Sm_PL   |  NP1βpl  |        Suíte Metaígnea Pedro Lessa       |        #ff0000        | (255,000,000) |
|   2  |  Sm_CMD  |  PP4γcmd | Suíte Metaígnea Conceição do Mato Dentro |        #000000        | (000,000,000) |
|   3  |  Fm_GM   |  PP4egm  |         Formação Galho do Miguel         |        #002673        | (000,038,115) |
|   4  | Fm_SB_F  |  PP4esbf |   Formação Sopa Brumadinho - Nível F     |        #4ce600        | (076,230,000) |
|   5  | Fm_SB_E  |  PP4esbe |   Formação Sopa Brumadinho - Nível E     |        #9b0000        | (155,000,000) |
|   6  | Fm_SB_D  |  PP4esbd |   Formação Sopa Brumadinho - Nível D     |        #0000ff        | (000,000,255) |
|   7  | Fm_SJC_C | PP4esjcc |  Formação São João da Chapada - Nível C  |        #ff8500        | (255,133,000) |
|   8  | Fm_SJC_B | PP4esjcb |  Formação São João da Chapada - Nível B  |        #00e6a9        | (000,230,169) |
|   9  | Fm_SJC_A | PP4esjca |  Formação São João da Chapada - Nível A  |        #ffff00        | (255,255,000) |
|  10  |   Fm_B   |   PP34b  |          Formação Bandeirinha            |        #e600a9        | (230,000,169) |
|  11  |  Fm_BG   | PP3csbg  |        Formação Barão de Guaicuí         |        #cccccc        | (204,204,204) |
|  12  |  Cx_GG   |  MAcgg   |        Complexo Granito-Gnáissico        |        #fabee8        | (255,190,232) |


### Dicionário de features

|    Feature    |  Unidade  |                         Fonte                         |                           Descrição                           |
|:-------------:|:---------:|:-----------------------------------------------------:|:-------------------------------------------------------------:|
| SIGNAL  | nT/m | Biblioteca Virtual UFMG                                          |Sinal analítico do campo magnético total                       |
| K_PERC  |   %  | Biblioteca Virtual UFMG                                          |Potássio                                                       |
| TH_PPM  |  ppm | Biblioteca Virtual UFMG                                          |Tório                                                          |
|  U_PPM  |  ppm | Biblioteca Virtual UFMG                                          |Urânio                                                         |
|  TC_EXP | μR/h | Biblioteca Virtual UFMG                                          |Contagem total                                                 |
|   U_K   |   -  | Biblioteca Virtual UFMG                                          |Razão urânio / potássio                                        |
|  TH_K   |   -  | Biblioteca Virtual UFMG                                          |Razão tório / potássio                                         |
|  U_TH   |   -  | Biblioteca Virtual UFMG                                          |Razão urânio / tório                                           |
|   MDT   |   m  | Biblioteca Virtual UFMG                                          |Modelo digital de terreno                                      |
|   MDE   |   m  | [INPE](http://www.dsr.inpe.br/topodata/dados.php)                |Modelo digital de elevação                                     |
|   B01   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - COSTAL (0.433 - 0.453 μm)               |
|   B02   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - AZUL (0.450 - 0.515 μm)                 |
|   B03   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - VERDE (0.525 - 0.600 μm)                |
|   B04   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - VERMELHO (0.630 - 0.680 μm)             |
|   B05   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - INFRAVERMELHO PRÓXIMO (0.845 - 0.885 μm)|
|   B06   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (1.560 - 1.660 μm)  |
|   B07   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (2.100 - 2.300 μm)  |
|   B08   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - PANCROMÁTICO (0.500 - 0.680 μm)         |
|   B09   |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                         |Landsat 8 Sensor OLI - CIRRUS (1.360 - 1.390 μm)               |
| LAND7_R |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - VERMELHO                               |
| LAND7_G |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - VERDE                                  |
| LAND7_B |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - AZUL                                   |

## Versões do software

- [python v3.6.10](https://docs.python.org/release/3.6.10/)
- [conda v4.9.2](https://docs.conda.io/projects/conda/en/master/release-notes.html)
- [jupyter v1.0.0](https://jupyter.org/documentation)
- [ipython v7.16.1](https://ipython.org/documentation.html)
- [numpy v1.17.0](https://numpy.org/doc/)
- [pandas v1.0.5](https://pandas.pydata.org/docs/)
- [matplotlib v3.2.2](https://matplotlib.org/stable/gallery/index.html)
- [seaborn v0.10.1](https://seaborn.pydata.org/examples/index.html)
- [statsmodels v0.11.1](https://www.statsmodels.org/stable/index.html)
- [scipy v1.5.0](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
- [scikit-learn v0.24.1](https://scikit-learn.org/stable/auto_examples/index.html)
- [imbalanced-learn v0.8.0](https://imbalanced-learn.org/stable/)


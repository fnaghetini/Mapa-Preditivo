# Mapa Litoestratigráfico Preditivo - Diamantina (MG)

Orientandos: [Franco Naghetini](https://github.com/fnaghetini) & [Guilherme Silveira](https://www.linkedin.com/in/guilherme-silveira)

Orientadores: [Pedro Casagrande](https://www.linkedin.com/in/pedro-casagrande) & [Iago Costa](https://github.com/iagoslc)

## Objetivo
O trabalho tem como objetivo a produção de um **mapa litoestratigráfico preditivo**, a partir de dados de sensores remotos e dados do mapeamento geológico realizado pelos alunos da disciplina de Estágio Supervisionado do ano de 2018, na região de Diamantina. As predições das unidades litoestratigráficas serão realizadas, utilizando algoritmos de *Machine Learning*.

O produto gráfico final poderá fornecer *insights* a respeito de regiões nas quais os dados de sensores remotos não apresentam boa compatibilidade com os litotipos interpretados. Além disso, as zonas de divergência entre o mapa preditivo e o mapa interpretado pelos estudantes da disciplina serão comparadas com o mapa de pontos levantados pelos alunos, a fim de se verificar uma possível correlação entre a densidade de distribuição da amostragem litológica e possíveis viéses interpretativos.

## Informações gerais

##### Sistema de referência

- Projeção: UTM
- Zona: 23S
- Datum: SIRGAS2000
- Unidade: m
- Elipsoide: GRS 1980
- Resolução: 62.5 m x 62.5 m
- Extensão: (xmin = , ymin = , xmax = , ymax = )

##### Unidades litoestratigráficas

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


##### Dicionário de features

|    Feature    |  Unidade  |                         Raster / Grid                            |                    Descrição                                        |
|:-------------:|:---------:|:----------------------------------------------------------------:|:-------------------------------------------------------------------:|
|    SIGNAL     |    nT/m   | [SIGNAL.grd]()                                                   |Sinal analítico do campo magnético total                             |
|    K_PERC     |     %     | [K_PERC.grd]()                                                   |Potássio                                                             |
|    TH_PPM     |    ppm    | [TH_PPM.grd]()                                                   |Tório                                                                |
|     U_PPM     |    ppm    | [U_PPM.grd]()                                                    |Urânio                                                               |
|    TC_EXP     |    μR/h   | [TC_EXP.grd]()                                                   |Contagem total                                                       |
|     U_K       |     -     | [U_K.grd]()                                                      |Razão urânio / potássio                                              |
|     TH_K      |     -     | [TH_K.grd]()                                                     |Razão tório / potássio                                               |
|     U_TH      |     -     | [U_TH.grd]()                                                     |Razão urânio / tório                                                 |
|      MDT      |     m     | [MDT.grd]()                                                      |Modelo digital de terreno                                            |
|      MDE      |     m     | [MDE.tif]()                                                      |Modelo digital de elevação                                           |
|      B01      |     -     | [B01.tif]()                                                      |Landsat 8 Sensor OLI - COSTAL (0.433 - 0.453 μm)                     |
|      B02      |     -     | [B02.tif]()                                                      |Landsat 8 Sensor OLI - AZUL (0.450 - 0.515 μm)                       |
|      B03      |     -     | [B03.tif]()                                                      |Landsat 8 Sensor OLI - VERDE (0.525 - 0.600 μm)                      |
|      B04      |     -     | [B04.tif]()                                                      |Landsat 8 Sensor OLI - VERMELHO (0.630 - 0.680 μm)                   |
|      B05      |     -     | [B05.tif]()                                                      |Landsat 8 Sensor OLI - INFRAVERMELHO PRÓXIMO (0.845 - 0.885 μm)      |
|      B06      |     -     | [B06.tif]()                                                      |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (1.560 - 1.660 μm)        |
|      B07      |     -     | [B07.tif]()                                                      |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (2.100 - 2.300 μm)        |
|      B08      |     -     | [B08.tif]()                                                      |Landsat 8 Sensor OLI - PANCROMÁTICO (0.500 - 0.680 μm)               |
|      B09      |     -     | [B09.tif]()                                                      |Landsat 8 Sensor OLI - CIRRUS (1.360 - 1.390 μm)                     |
|    LAND7_R    |     -     | [LAND7.tif]()                                                    |Landsat 7 Sensor EMT+ - VERMELHO                                     |
|    LAND7_G    |     -     | [LAND7.tif]()                                                    |Landsat 7 Sensor EMT+ - VERDE                                        |
|    LAND7_B    |     -     | [LAND7.tif]()                                                    |Landsat 7 Sensor EMT+ - AZUL                                         |

## Versões do software

- [Python v3.6.10](https://docs.python.org/release/3.6.10/)
- [Numpy v]()
- [Pandas v]()
- [Matplotlib v]()
- [Seaborn v]()
- [Scikit Learn v]()
- [Imbalance Learn v]()

<img src="https://logodownload.org/wp-content/uploads/2015/02/ufmg-logo-2.png" alt="Logo UFMG" width="650px">

# Mapeamento Geológico Preditivo Aplicando Técnicas de Aprendizado de Máquina na Região de Diamantina, Minas Gerais, Brasil

### Trabalho de Conclusão de Curso - Geologia / IGC / UFMG

Orientandos: [Franco Naghetini](https://github.com/fnaghetini) & [Guilherme Silveira](https://github.com/guiasilveira)

Orientadores: [Pedro Casagrande](https://github.com/casagrandepedro) & [Iago Costa](https://github.com/iagoslc)

## Resumo

O objetivo deste trabalho é solucionar uma tarefa supervisionada de classificação multinomial  **𝑇**  que consiste em predizer as unidades litoestratigráficas  **𝑦𝑖**  em um determinado domínio  **𝐷**  como função de sensores remotos  **𝑥𝑖**  e com base em anotações  **𝑦(𝑖)=𝑓(𝑥(𝑖))**  interpretadas pelos geólogos responsáveis pelo mapeamento da área.

O produto final é um **mapa geológico preditivo 1:25.000 da região de Diamantina (MG)** que pode ser utilizado como um meio de reconciliação entre os dados/interpretações de campo e os sensores remotos. Nesse sentido, as inconsistências entre o mapa geológico e o mapa preditivo podem fornecer insights e orientar futuras campanhas de mapeamento na região.

O [fluxo de trabalho](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/workflow/workflow.pdf) deste projeto é dividido em cinco etapas principais:

1. Aquisição e preparação dos sensores remotos
2. Limpeza e análise exploratória dos dados
3. Pré-processamento e modelagem dos dados
4. Explicação do modelo
5. Pós-processamento

O modelo **XGBoost** apresentou a melhor performance com relação às métricas avaliadas:

|        Métricas       | XGBoost |
|:---------------------:|:-------:|
|        Acurácia       |   0.67  |
|        F1-Score       |   0.68  |
|        Precisão       |   0.72  |
|         Recall        |   0.67  |

## Estrutura do Repositório

```bash
.
├───data
│   ├───raster
│   ├───data_nb1.csv
│   ├───data_nb2.csv
│   └───data_nb3.csv
├───figures
│   ├───notebook1
│   └───notebook2
├───functions
│   ├───Custom_Cleaning.py
│   ├───Custom_Export.py
│   ├───Custom_Prediction.py
│   ├───Custom_Preprocessing.py
│   ├───Custom_Stats.py
│   ├───Custom_Train_Test_Split.py
│   ├───Custom_Validation.py
│   └───functions.pdf
├───output
├───shp
│   ├───lithology_sirgas.shp
│   └───poligono_sirgas.shp
├───workflow
│   └───workflow.pdf
├───1-exploratory_data_analysis.ipynb
├───2-predictive_litho_map.ipynb
├───3-model_explanation.ipynb
└───README.md
```

- [data](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/data) contém os dados utilizados nos três notebooks. Os sensores remotos processados em SIRGAS2000 UTM Zona 23S com resolução de 62.5 m x 62.5 m estão na subpasta [raster](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/data/raster).

- [figures](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/figures) contém todos os gráficos e mapas gerados nos três notebooks em formato .png.

- [functions](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/functions) contém todas as funções auxiliares utilizadas em ambos os notebooks. As funções auxiliares adotam o padrão *lowerCamelCase* para diferenciá-las das funções nativas e externas do Python. A única exceção é a classe auxiliar `MaskedPCA` que, por sua vez, adota o padrão *UpperCamelCase*. Toda vez que uma função auxiliar é utilizada em um dos notebooks, haverá um hiperlink que aponta para o arquivo `.py` fonte dessa função. Clique [aqui](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/functions/functions.pdf) para visualizar o mapa mental das funções auxiliares.

- [output](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output) contém os mapas obtidos durante o projeto em formato .tif.

- [shp](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/shp) contém o mapa geológico de campo e o polígono da área deste projeto, ambos em formato shape file.

- [workflow](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/workflow) contém o [fluxo de trabalho](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/workflow/workflow.pdf) adotado neste projeto.

- [1-exploratory_data_analysis.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/1-exploratory_data_analysis.ipynb) contém as etapas de limpeza e análise exploratória dos dados.

- [2-predictive_litho_map.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/2-predictive_litho_map.ipynb) abrange desde a etapa de pré-processamento dos dados até a seleção do modelo de melhor performance.

- [3-model_explanation.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/3-model_explanation.ipynb) apresenta as explicações do modelo selecionado.

## Informações complementares

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
|  B01 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - COSTAL (0.433 - 0.453 μm)               |
|  B02 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - AZUL (0.450 - 0.515 μm)                 |
|  B03 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - VERDE (0.525 - 0.600 μm)                |
|  B04 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - VERMELHO (0.630 - 0.680 μm)             |
|  B05 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - INFRAVERMELHO PRÓXIMO (0.845 - 0.885 μm)|
|  B06 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (1.560 - 1.660 μm)  |
|  B07 |   -  | [INPE](http://www.dgi.inpe.br/catalogo/)                            |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (2.100 - 2.300 μm)  |
|   R  |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - VERMELHO                               |
|   G  |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - VERDE                                  |
|   B  |   -  | [USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-legacy-tri-decadal-landsat-orthorectified-mosaics-etm?qt-science_center_objects=0#qt-science_center_objects)|Landsat 7 Sensor EMT+ - AZUL                                   |

## Versões

- [python v3.6.10](https://docs.python.org/release/3.6.10/)
- [conda v4.9.2](https://docs.conda.io/projects/conda/en/master/release-notes.html)
- [jupyter v1.0.0](https://jupyter.org/documentation)
- [numpy v1.19.5](https://numpy.org/doc/)
- [pandas v1.0.5](https://pandas.pydata.org/docs/)
- [matplotlib v3.2.2](https://matplotlib.org/stable/gallery/index.html)
- [seaborn v0.10.1](https://seaborn.pydata.org/examples/index.html)
- [scipy v1.5.0](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
- [scikit-learn v0.24.1](https://scikit-learn.org/stable/auto_examples/index.html)
- [imbalanced-learn v0.8.0](https://imbalanced-learn.org/stable/)
- [geopandas v0.9.0](https://geopandas.org/docs/user_guide.html)
- [rasterio v1.1.7](https://rasterio.readthedocs.io/en/latest/api/index.html)
- [folium v0.12.0](https://python-visualization.github.io/folium/)
- [xgboost v1.4.0](https://xgboost.readthedocs.io/en/latest/index.html#)
- [shap v0.39.0](https://shap.readthedocs.io/en/latest/index.html)

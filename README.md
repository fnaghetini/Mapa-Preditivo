<img src="https://logodownload.org/wp-content/uploads/2015/02/ufmg-logo-2.png" alt="Logo UFMG" width="650px">

# Utilização de Técnicas de Aprendizado de Máquina Supervisionado para Mapeamento Geológico: Um Estudo de Caso na Região de Diamantina, Minas Gerais, Brasil

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

O modelo **XGBoost** apresentou a melhor performance com relação às métricas avaliadas abaixo e à entropia cruzada:

|        Métricas       | XGBoost |
|:---------------------:|:-------:|
|        Acurácia       |   0.70  |
|        F1-Score       |   0.71  |
|        Precisão       |   0.74  |
|         Recall        |   0.70  |

## Estrutura do Repositório

```bash
.
├───data
│   ├───raster
│   ├───data_nb1.csv
│   ├───data_nb2.csv
│   ├───data_nb3.csv
│   ├───test.csv
│   └───train.csv
├───figures
│   ├───notebook1
│   ├───notebook2
│   ├───notebook3
│   └───notebook4
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
│   ├───points
│   └───rasters
├───shp
│   ├───boundary.shp
│   └───lithology.shp
├───workflow
│   └───workflow.pdf
├───1-exploratory_data_analysis.ipynb
├───2-predictive_litho_map.ipynb
├───3-model_explanation.ipynb
├───4-geospatial_issues.ipynb
└───README.md
```

- [data](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/data) contém os dados utilizados nos três notebooks e os dados de treino e teste. Os sensores remotos processados em SIRGAS2000 UTM Zona 23S com resolução de 62.5 m x 62.5 m estão na subpasta [raster](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/data/raster).

- [figures](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/figures) contém todos os gráficos e mapas gerados nos três notebooks em formato .png.

- [functions](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/functions) contém todas as funções auxiliares utilizadas em ambos os notebooks. As funções auxiliares adotam o padrão *lowerCamelCase* para diferenciá-las das funções nativas e externas do Python. A única exceção é a classe auxiliar `MaskedPCA` que, por sua vez, adota o padrão *UpperCamelCase*. Toda vez que uma função auxiliar é utilizada em um dos notebooks, haverá um hiperlink que aponta para o arquivo `.py` fonte dessa função. Clique [aqui](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/functions/functions.pdf) para visualizar o mapa mental das funções auxiliares.

- [output](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output) contém os mapas obtidos durante o projeto como [pontos](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output/points) e [rasters](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output/rasters).

- [shp](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/shp) contém o mapa geológico de campo e o polígono da área deste projeto, ambos em formato .shp.

- [workflow](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/workflow) contém o [fluxo de trabalho](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/workflow/workflow.pdf) adotado neste projeto.

- [1-exploratory_data_analysis.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/1-exploratory_data_analysis.ipynb) contém as etapas de limpeza e análise exploratória dos dados.

- [2-predictive_litho_map.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/2-predictive_litho_map.ipynb) abrange desde a etapa de pré-processamento dos dados até a seleção do modelo de melhor performance.

- [3-model_explanation.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/3-model_explanation.ipynb) apresenta as explicações do modelo selecionado.

- [4-geospatial_issues.jl](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/4-geospatial_issues.jl) apresenta uma análise simples de fenômenos comuns em dados geoespaciais.

## Informações Complementares

#### Sistema de Referência

- EPSG: 31983
- Projeção: UTM
- Zona: 23S
- Datum: SIRGAS2000
- Unidade: m
- Elipsoide: GRS 1980
- Resolução: 62.5 m x 62.5 m
- Extensão: (xmin = 634163.67, ymin = 7969052.06, xmax = 640038.70, ymax = 7983240.00)

#### Unidades Litoestratigráficas

|  ID  |  Código  |                 Unidade                  |      RGB      | Hexadecimal |
|:----:|:--------:|:----------------------------------------:|:-------------:|:-----------:|
|   1  |  MAcgg   |        Complexo Granito-Gnáissico        | (255,115,223) |   #ff73df   |
|   2  |  PP3csbg |         Formação Barão de Guaicuí        | (190,210,255) |   #bed2ff   |
|   3  |  PP34b   |          Formação Bandeirinha            |  (230,76,0)   |   #e64d00   |
|   4  |  PP4esjc |       Formação São João da Chapada       |  (255,170,0)  |   #ffaa00   |
|   5  |  PP4esb  |         Formação Sopa Brumadinho         | (255,255,115) |   #ffff73   |
|   6  |  PP4egm  |         Formação Galho do Miguel         |  (76,230,0)   |   #4de600   |

#### Dicionário de Variáveis

|  Variável  |  Unidade  |                         Fonte                         |                           Descrição                           |
|:----------:|:---------:|:-----------------------------------------------------:|:-------------------------------------------------------------:|
|    X       |    m      |                           -                           |Coordenada X (SIRGAS2000 Zona 23S)                             |
|    Y       |    m      |                           -                           |Coordenada Y (SIRGAS2000 Zona 23S)                             |
|    GT      |   nT/m    | Biblioteca UFMG                                       |Gradiente total                                                |
|    K       |    %      | Biblioteca UFMG                                       |Potássio                                                       |
|    TH      |   ppm     | Biblioteca UFMG                                       |Tório                                                          |
|    U       |   ppm     | Biblioteca UFMG                                       |Urânio                                                         |
|    CT      |   μR/h    | Biblioteca UFMG                                       |Contagem total                                                 |
|    U_K     |    -      | Biblioteca UFMG                                       |Razão urânio / potássio                                        |
|    TH_K    |    -      | Biblioteca UFMG                                       |Razão tório / potássio                                         |
|    U_TH    |    -      | Biblioteca UFMG                                       |Razão urânio / tório                                           |
|    MDT     |    m      | Biblioteca UFMG                                       |Modelo digital de terreno                                      |
|    B02     |    -      | [INPE](http://www.dgi.inpe.br/catalogo/)              |Landsat 8 Sensor OLI - AZUL (0.450 - 0.515 μm)                 |
|    B03     |    -      | [INPE](http://www.dgi.inpe.br/catalogo/)              |Landsat 8 Sensor OLI - VERDE (0.525 - 0.600 μm)                |
|    B04     |    -      | [INPE](http://www.dgi.inpe.br/catalogo/)              |Landsat 8 Sensor OLI - VERMELHO (0.630 - 0.680 μm)             |
|    B06     |    -      | [INPE](http://www.dgi.inpe.br/catalogo/)              |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (1.560 - 1.660 μm)  |
|    B07     |    -      | [INPE](http://www.dgi.inpe.br/catalogo/)              |Landsat 8 Sensor OLI - INFRAVERMELHO MÉDIO (2.100 - 2.300 μm)  |
|   TARGET   |    -      | Mapa Integrado Estágio Supervisionado (2018)          |Código numérico das unidades litoestratigráficas               |
|    COD     |    -      | Mapa Integrado Estágio Supervisionado (2018)          |Acrônimo das unidades litoestratigráficas                      |     

## Versões

- [python v3.6.10](https://docs.python.org/release/3.6.10/)
- [conda v4.9.2](https://docs.conda.io/projects/conda/en/master/release-notes.html)
- [jupyter v1.0.0](https://jupyter.org/documentation)
- [numpy v1.19.5](https://numpy.org/doc/)
- [pandas v1.0.5](https://pandas.pydata.org/docs/reference/index.html#api)
- [matplotlib v3.2.2](https://matplotlib.org/stable/gallery/index.html)
- [seaborn v0.10.1](https://seaborn.pydata.org/examples/index.html)
- [scipy v1.5.0](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)
- [scikit-learn v0.24.1](https://scikit-learn.org/stable/auto_examples/index.html)
- [imbalanced-learn v0.8.0](https://imbalanced-learn.org/stable/references/index.html#api)
- [xgboost v1.4.0](https://xgboost.readthedocs.io/en/latest/index.html#)
- [geopandas v0.9.0](https://geopandas.org/docs/user_guide.html)
- [rasterio v1.1.7](https://rasterio.readthedocs.io/en/latest/api/index.html)
- [folium v0.12.0](https://python-visualization.github.io/folium/)
- [shap v0.39.0](https://shap.readthedocs.io/en/latest/index.html)

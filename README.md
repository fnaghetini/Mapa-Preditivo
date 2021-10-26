<img src="https://logodownload.org/wp-content/uploads/2015/02/ufmg-logo-2.png" alt="Logo UFMG" width="650px">

# Utilização de Técnicas de Aprendizado de Máquina Supervisionado para Mapeamento Geológico: Um Estudo de Caso na Região de Diamantina, Minas Gerais, Brasil

### Trabalho de Conclusão de Curso - Geologia / IGC / UFMG

Orientandos: [Franco Naghetini](https://github.com/fnaghetini) & [Guilherme Silveira](https://github.com/guiasilveira)

Orientadores: [Pedro Casagrande](https://github.com/casagrandepedro) & [Iago Costa](https://github.com/iagoslc)

## Aspectos Gerais

O objetivo deste trabalho é solucionar uma tarefa supervisionada de classificação multinomial  **𝑇**  que consiste em predizer as unidades litoestratigráficas  **𝑦**  em um determinado domínio  **𝐷**  como função de sensores remotos  **X**  e com base em anotações  **𝑦(𝑖)=𝑓(𝑥(𝑖))**  interpretadas pelos geólogos responsáveis pelo mapeamento da área.

O produto final é um **mapa geológico preditivo 1:25.000** da área de interesse que pode ser utilizado como um meio de reconciliação entre os dados/interpretações de campo e os sensores remotos. Nesse sentido, as inconsistências entre o mapa geológico e o mapa preditivo podem fornecer *insights* e orientar futuras campanhas de mapeamento na região.

O fluxo de trabalho deste projeto pode ser consultado [aqui](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/workflow/workflow.pdf).

Oito classificadores foram comparados entre si, sendo eles:

- Regressão Logística (RL)
- *Decision Tree* (DT)
- *Naive Bayes* (NB)
- *K-Nearest Neighbors* (KNN)
- *Support Vector Machines* (SVM)
- *Random Forest* (RF)
- *XGBoost* (XGB)
- *Multilayer Perceptrons* (MLP)

Dentre eles, os modelos *XGBoost* e *Random Forest* apresentaram as melhores performances com relação às métricas avaliadas. Os *scores* de validação cruzada para esses modelos são apresentados abaixo:

|        Métricas       | XGBoost | Random Forest |
|:---------------------:|:-------:|:-------------:|
|        F1-score       |   0.77  |      0.78     |
|        Precisão       |   0.78  |      0.78     |
|         Recall        |   0.77  |      0.78     |
|        Acurácia       |   0.77  |      0.78     |

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
├───4-geospatial_issues.jl
└───README.md
```

- [data](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/data) contém os dados utilizados nos quatro *notebooks* e os dados de treino e teste. Os sensores remotos processados em SIRGAS2000 UTM Zona 23S com resolução de 62.5 m x 62.5 m estão na subpasta [raster](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/data/raster).

- [figures](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/figures) contém todos os gráficos e mapas gerados nos quatro *notebooks* em formato .png.

- [functions](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/functions) contém todas as funções auxiliares utilizadas nos *notebooks*. As funções auxiliares adotam o padrão *lowerCamelCase* para diferenciá-las das funções nativas e externas do Python. A única exceção é a classe auxiliar `MaskedPCA` que, por sua vez, adota o padrão *UpperCamelCase*. Toda vez que uma função auxiliar é utilizada em um dos *notebooks*, haverá um hiperlink que aponta para o arquivo `.py` fonte dessa função. Clique [aqui](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/functions/functions.pdf) para visualizar o mapa mental das funções auxiliares.

- [output](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output) contém os mapas obtidos durante o projeto como [pontos](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output/points) e [rasters](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/output/rasters).

- [shp](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/shp) contém o mapa geológico de campo e o polígono da área deste projeto, ambos em formato .shp.

- [workflow](https://github.com/fnaghetini/Mapa-Preditivo/tree/main/workflow) contém o [fluxo de trabalho](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/workflow/workflow.pdf) adotado neste projeto.

- [1-exploratory_data_analysis.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/1-exploratory_data_analysis.ipynb) contém as etapas de limpeza e análise exploratória dos dados.

- [2-predictive_litho_map.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/2-predictive_litho_map.ipynb) abrange as etapas de pré-processamento e modelagem dos dados. Os mapas geológicos preditivos são gerados aqui.

- [3-model_explanation.ipynb](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/3-model_explanation.ipynb) apresenta os resultados da interpretação do classificador *XGBoost* com o *framework* SHAP.

- [4-geospatial_issues.jl](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/4-geospatial_issues.jl) apresenta uma análise interativa simples de fenômenos comuns em dados geoespaciais.

## Instruções

### Python
Grande parte do trabalho (três primeiros *notebooks*) foi desenvolvida em linguagem [Python](https://www.python.org/), em ambiente [Jupyter Notebook](https://jupyter.org/). Caso deseje executar os notebooks localmente, aconselhamos a [instalação do Python via Anaconda](https://docs.anaconda.com/anaconda/install/windows/). A vantagem desse distribuidor é que grande parte das bibliotecas utilizadas no trabalho são automaticamente instaladas em sua máquina.

Todas as bibliotecas utilizadas, bem como suas respectivas versões são apresentadas ao final deste documento, em **Versões**. As bibliotecas que não são instaladas automaticamente junto ao Anaconda apresentam um "*".

Opcionalmente, é possível visualizar os *notebooks* no próprio GitHub ou, ainda, executá-los no ambiente [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb). Entretanto, nem todos os recursos presentes estarão habilitados em ambos os casos.

### Julia
Apenas o [quarto *notebook*](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/4-geospatial_issues.jl) foi desenvolvido em linguagem [Julia](https://julialang.org/), em ambiente [Pluto](https://github.com/fonsp/Pluto.jl). Para executar esse *notebook* localmente, primeiro [instale Julia 1.6](https://julialang.org/downloads/). Em seguida, no Julia REPL, execute os seguintes comandos para instalar o Pluto:

```julia
julia> using Pkg
julia> Pkg.add("Pluto")
```

Em seguida, execute o Pluto:

```julia
julia> using Pluto
julia> Pluto.run()
```

**Nota:** Não se preocupe com as versões das bibliotecas Julia utilizadas. Como o Pluto apresenta seu próprio gerenciador de pacotes, ao abrir o *notebook* pela primeira vez, todos os pacotes necessários serão automaticamente instalados nas versões apropriadas (isso pode demorar alguns minutos!).

**Importante:** A versão do Pluto deve ser igual ou maior à **0.16.0**. Caso queira consultar sua versão, no Julia REPL, digite:

```julia
julia> using Pkg
julia> Pkg.status()
```

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
|    X       |    m      |                           -                           |Coordenada X                                                   |
|    Y       |    m      |                           -                           |Coordenada Y                                                   |
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
|   TARGET   |    -      | Mapa Estágio Supervisionado (2018)                    |Código numérico das unidades litoestratigráficas               |
|    COD     |    -      | Mapa Estágio Supervisionado (2018)                    |Acrônimo das unidades litoestratigráficas                      |     

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
- [*imbalanced-learn v0.8.0](https://imbalanced-learn.org/stable/references/index.html#api)
- [*xgboost v1.4.0](https://xgboost.readthedocs.io/en/latest/index.html#)
- [*geopandas v0.9.0](https://geopandas.org/docs/user_guide.html)
- [*rasterio v1.1.7](https://rasterio.readthedocs.io/en/latest/api/index.html)
- [*folium v0.12.0](https://python-visualization.github.io/folium/)
- [*shap v0.39.0](https://shap.readthedocs.io/en/latest/index.html)

**Nota:** As bibliotecas que não são instaladas automaticamente junto ao Anaconda foram destacadas com o símbolo "*".

## Licença

Este repositório encontra-se sob a licença MIT:

```bash
"Uma licença permissiva, curta e simples com condições que exigem apenas a preservação de direitos autorais e avisos de
licença. Trabalhos licenciados, modificações e trabalhos maiores podem ser distribuídos em termos diferentes e sem
código-fonte."
```

Para mais detalhes, consulte o arquivo de [licença](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/LICENSE).

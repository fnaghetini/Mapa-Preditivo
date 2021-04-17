# Mapa Litoestratigráfico Preditivo - Diamantina (MG)

Orientandos: [Franco Naghetini](https://github.com/fnaghetini) & [Guilherme Silveira]()

Orientadores: [Pedro Casagrande]() & [Iago Costa](https://github.com/iagoslc)

## Objetivo
O trabalho tem como objetivo a produção de um **mapa litoestratigráfico preditivo**, a partir de dados de sensores remotos e dados do mapeamento geológico realizado pelos alunos da disciplina de Estágio Supervisionado do ano de 2018, na região de Diamantina. As predições das unidades litoestratigráficas serão realizadas, utilizando algoritmos de *Machine Learning*.

O produto gráfico final poderá fornecer *insights* a respeito de regiões nas quais os dados de sensores remotos não apresentam boa compatibilidade com os litotipos interpretados. Além disso, as zonas de divergência entre o mapa preditivo e o mapa interpretado pelos estudantes da disciplina serão comparadas com o mapa de pontos levantados pelos alunos, a fim de se verificar uma possível correlação entre a densidade de distribuição da amostragem litológica e possíveis viéses interpretativos.

## Informações gerais

##### Unidades litoestratigráficas
<table align="left">
    <tr>
        <th><center><big>ID Unidade</big></center></th>
        <th><center><big>Sigla Unidade</big></center></th>
        <th><center><big>Unidade</big></center></th>
    </tr>
    <tr>
        <th><center>1</center></th>
        <td><center>Sm_PL</center></td>
        <td><center>Suíte Metaígnea Pedro Lessa</center></td>
    </tr>
    <tr>
        <th><center>2</center></th>
        <td><center>Sm_CMD</center></td>
        <td><center>Suíte Metaígnea Conceição do Mato Dentro</center></td>
    </tr>
    <tr>
        <th><center>3</center></th>
        <td><center>Fm_GM</center></td>
        <td><center>Formação Galho do Miguel</center></td>
    </tr>
    <tr>
        <th><center>4</center></th>
        <td><center>Fm_SB_F</center></td>
        <td><center>Formação Sopa Brumadinho - Nível F</center></td>
    </tr>
    <tr>
        <th><center>5</center></th>
        <td><center>Fm_SB_E</center></td>
        <td><center>Formação Sopa Brumadinho - Nível E</center></td>
    </tr>
    <tr>
        <th><center>6</center></th>
        <td><center>Fm_SB_D</center></td>
        <td><center>Formação Sopa Brumadinho - Nível D</center></td>
    </tr>
    <tr>
        <th><center>7</center></th>
        <td><center>Fm_SJC_C</center></td>
        <td><center>Formação São João da Chapada - Nível C</center></td>
    </tr>
    <tr>
        <th><center>8</center></th>
        <td><center>Fm_SJC_B</center></td>
        <td><center>Formação São João da Chapada - Nível B</center></td>
    </tr>
    <tr>
        <th><center>9</center></th>
        <td><center>Fm_SJC_A</center></td>
        <td><center>Formação São João da Chapada - Nível A</center></td>
    </tr>
    <tr>
        <th><center>10</center></th>
        <td><center>Fm_B</center></td>
        <td><center>Formação Bandeirinha</center></td>
    </tr>
    <tr>
        <th><center>11</center></th>
        <td><center>Fm_BG</center></td>
        <td><center>Formação Barão de Guaicuí</center></td>
    </tr>
    <tr>
        <th><center>12</center></th>
        <td><center>Cx_GG</center></td>
        <td><center>Complexo Granito-Gnáissico</center></td>
    </tr>
</table>

##### Features

<table align="left">
    <tr>
        <th><center><big>Atributo</big></center></th>
        <th><center><big>Unidade</big></center></th>
        <th><center><big>Tipo</big></center></th>
        <th><center><big>Breve Descrição</big></center></th>
    </tr>
    <tr>
        <th><center>MDE</center></th>
        <td><center>Metros</center></td>
        <td><center>Feature</center></td>
        <td><center>Modelo digital de elevação</center></td>
  </tr>
    <tr>
        <th><center>B01</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 01 Landsat (COSTAL)</center></td>
    </tr>
    <tr>
        <th><center>B02</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 02 Landsat (AZUL)</center></td>
    </tr>
    <tr>
        <th><center>B03</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 03 Landsat (VERDE)</center></td>
    </tr>
    <tr>
        <th><center>B04</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 04 Landsat (VERMELHO)</center></td>
    </tr>
    <tr>
        <th><center>B05</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 05 Landsat (INFRAVERMELHO PRÓXIMO)</center></td>
    </tr>
    <tr>
        <th><center>B06</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 06 Landsat (INFRAVERMELHO MÉDIO)</center></td>
    </tr>
    <tr>
        <th><center>B07</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 07 Landsat (INFRAVERMELHO MÉDIO)</center></td>
    </tr>
    <tr>
        <th><center>B08</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 08 Landsat (PANCROMÁTICO)</center></td>
    </tr>
    <tr>
        <th><center>B09</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Banda 09 Landsat (CIRRUS)</center></td>
    </tr>
    <tr>
        <th><center>MAG_CT_1DV</center></th>
        <td><center>nT/m</center></td>
        <td><center>Feature</center></td>
        <td><center>1ª derivada vertical do campo magnético total</center></td>
    </tr>
    <tr>
        <th><center>K_PERC</center></th>
        <td><center>%</center></td>
        <td><center>Feature</center></td>
        <td><center>Potássio</center></td>
    </tr>
    <tr>
        <th><center>MAG_CT</center></th>
        <td><center>nT</center></td>
        <td><center>Feature</center></td>
        <td><center>Campo magnético total (reduzido IGRF)</center></td>
    </tr>
    <tr>
        <th><center>SIGN</center></th>
        <td><center>nT/m</center></td>
        <td><center>Feature</center></td>
        <td><center>Sinal analítico do campo magnético total</center></td>
    </tr>
    <tr>
        <th><center>TC_EXP</center></th>
        <td><center>μR/h</center></td>
        <td><center>Feature</center></td>
        <td><center>Contagem total</center></td>
    </tr>
    <tr>
        <th><center>TH_K</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Razão tório/potássio</center></td>
    </tr>
    <tr>
        <th><center>TH_PPM</center></th>
        <td><center>ppm</center></td>
        <td><center>Feature</center></td>
        <td><center>Tório</center></td>
    </tr>
    <tr>
        <th><center>U_K</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Razão urânio/potássio</center></td>
    </tr>
    <tr>
        <th><center>U_PPM</center></th>
        <td><center>ppm</center></td>
        <td><center>Feature</center></td>
        <td><center>Urânio</center></td>
    </tr>
    <tr>
        <th><center>U_TH</center></th>
        <td><center>-</center></td>
        <td><center>Feature</center></td>
        <td><center>Razão urânio/tório</center></td>
    </tr>
    <tr>
        <th><center>ID_UNID</center></th>
        <td><center>-</center></td>
        <td><center>Target</center></td>
        <td><center>Código numérico das unidades litoestratigráficas</center></td>
    </tr>
    <tr>
        <th><center>UNID</center></th>
        <td><center>-</center></td>
        <td><center>Meta</center></td>
        <td><center>Siglas das unidades litoestratigráficas</center></td>
    </tr>
    
</table>

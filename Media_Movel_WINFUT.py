# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:41:01 2021

@author: verid
"""

"""
Calcular a média móvel

"""

import pandas as pd
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

dados = pd.read_csv('WINFUT-DIARIO.csv')

dados['Data'] = pd.to_datetime(dados['Data']) #converte de objeto para tipo data

def plotar(titulo, labelx, labely, x, y, dataset):  #função para plotar gráficos

    sns.set_palette('Accent')
    #sns.set_style('darkgrid')

    ax = sns.lineplot(x = x, y = y, data = dataset) #plota o gráfico de MAX X TEMPO
    ax.figure.set_size_inches(12,6) # tamanho do gráfico
    ax.set_title(titulo, fontsize=18)
    
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)
    
    
    
    
dados['media_movel'] = dados['Fechamento'].rolling(200).mean()
#print(dados.head(21))

plotar('Valores de Fechamento de Pregão WINFUT Diário - Série Histórica', 'Data', 'Fechamento','Data', 'Fechamento', dados )
plotar('Média Movel do Fechamento WINFUT Diário de 200 Pregões', 'Data', 'Fechamento','Data', 'media_movel', dados )
 
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:26:34 2021

@author: verid
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ibov_fut = pd.read_csv('WINFUT-DIARIO.csv')
dol_fut = pd.read_csv('WDOFUT-DIARIO.csv')

ibov_fut['Data'] = pd.to_datetime(ibov_fut['Data'])
dol_fut['Data'] = pd.to_datetime(dol_fut['Data'])

print(ibov_fut.head())
print(dol_fut.head())

def plotar(titulo, labelx, labely, x, y, dataset):  #função para plotar gráficos

    sns.set_palette('Accent')
    #sns.set_style('darkgrid')

    ax = sns.lineplot(x = x, y = y, data = dataset) #plota o gráfico de Fechamento X TEMPO
    ax.figure.set_size_inches(12,6) # tamanho do gráfico
    ax.set_title(titulo, fontsize=18)
    
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)
    
plotar('Valores de Fechamento de Pregão WDOFUT Diário - Série Histórica', 'Data', 'Fechamento','Data', 'Fechamento', dol_fut )

media_fechamento_ibov = np.mean(ibov_fut['Fechamento'])
media_fechamento_dol_fut = np.mean(dol_fut['Fechamento'])

intervalo_ibov = ibov_fut['Data'][1] - ibov_fut['Data'][0]

plt.plot(ibov_fut['Data'], ibov[''])
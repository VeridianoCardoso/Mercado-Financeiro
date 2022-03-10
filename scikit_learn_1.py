# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:14:28 2021

@author: verid
"""

#Curso de Scikit-Learn 1

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import linear_model


ibov = pd.read_csv('WINFUT-DIARIO.csv')
ibov['Data'] = pd.to_datetime(ibov['Data']) 
print(ibov.head())

sns.lineplot(x='Data', y='Fechamento', data=ibov)

tempo = ibov.iloc[:, :-1].values

valor = ibov.iloc[:, 1].values

tempo_treino, tempo_teste, valor_treino, valor_teste = train_test_split(tempo, valor, test_size = 0.3)

regressor  = linear_model.LinearRegression()
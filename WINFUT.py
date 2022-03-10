# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:11:59 2021

@author: verid
"""

#Teste Com DataSet WINFUT Diário - séries histórica

import pandas as pd
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


dados = pd.read_csv('WINFUT-DIARIO.csv')

#print(dados.head())


print('Quantidade de Linha e Colunas: ', dados.shape)

print('Quantidade de Dados nulos:', dados.isna().sum().sum())

#print(dados.dtypes) # mostrar os tipos de dados

dados['Data'] = pd.to_datetime(dados['Data']) #converte de objeto para tipo data
#print(dados.dtypes)

dados['dia_da_semana'] = dados['Data'].dt.day_name() #mostra o dia da semana da data
#print(dados['dia_da_semana'].unique()) #mostra o valores da coluna dias da semana

dias_pt_br = {'Wednesday' : 'Quata-Feira', 'Tuesday' : 'Terça-Feira', 'Monday' : 'Segunda-Feira',
              'Friday' : 'Sexta-Feira', 'Thursday' : 'Quinta-Feira'}

dados['dia_da_semana'] = dados['dia_da_semana'].map(dias_pt_br) #mapeia e substitui os nomes em inglês
dados['Incremento'] = dados['Fechamento'].diff()
print(dados.head()) #calcula o incremento em pontos da coluna Fechamento 

resultado = seasonal_decompose(dados['Fechamento'], period=200) #análisar a frequencia  
ax = resultado.plot()


fechamento_por_dia = dados.groupby('dia_da_semana')['Incremento', 'Fechamento'].mean().round() #mostra a média de incremento por dia 




#sns.set_palette('Accent')
#sns.set_style('darkgrid')

#ax = sns.lineplot(x = 'Data', y = 'Max', data=dados) #plota o gráfico de MAX X TEMPO
#ax.figure.set_size_inches(12,6) # tamanho do gráfico
#ax.set_title('Pontuação Máxima IBOV (Diária) - 2006-2021', fontsize=18)

#ax.set_xlabel('Tempo', fontsize=14)
#ax.set_ylabel('Pontuação', fontsize=14)


print (fechamento_por_dia.head())

def plotar(titulo, labelx, labely, x, y, dataset):  #função para plotar gráficos

    sns.set_palette('Accent')
    #sns.set_style('darkgrid')

    ax = sns.lineplot(x = x, y = y, data = dataset) #plota o gráfico de MAX X TEMPO
    ax.figure.set_size_inches(12,6) # tamanho do gráfico
    ax.set_title(titulo, fontsize=18)
    
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)


#plotar('Winfut Diário - Séries Histórica', 'Tempo', 'Pontuação', 'Data', 'Fechamento', dados)


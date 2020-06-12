#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import TCC_supercon_dados as tsd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


# In[ ]:


###   Função para divisão do conjunto a ser treinado e testado; argumentos: percentual do conjunto de teste, conjunto X e conjunto Y  ###


# In[ ]:


def divisao_dados_treinamento(split_test_size,X, Y,random_state = 51):

       # Definindo a taxa de split (percentual)
       split_test_size = split_test_size

       # Criando dados de treino e de teste
       X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size = split_test_size, random_state = random_state)
       
       return X_treino, X_teste, Y_treino, Y_teste


# In[ ]:


###   Divisão dos dados: dados para treinamento dos modelos   ###

# X_treino, X_teste, Y_treino, Y_teste = divisao_dados_treinamento(0.2,tsd.X_modelagem,tsd.Y_modelagem)


# In[ ]:


def config_parametros(clase_modelo, parametros, cv= 5, n_jobs=-3):
    
    #Instancia o objeto com a classe que treina determinado modelo de ML
    modelo = clase_modelo
    
    grid_classe = GridSearchCV(modelo, parametros, cv=cv,n_jobs=n_jobs)
    
    return modelo, grid_classe


# In[ ]:


def obter_parametros(clase_modelo, parametros, X,Y):    
    
    modelo, grid_classe = config_parametros(clase_modelo, parametros)
    
    return grid_classe.fit(X,Y)   
    

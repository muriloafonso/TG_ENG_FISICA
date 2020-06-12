# supercondutividade_machine_learning

Trabalho de graduação para o curso de Engenharia Física da Escola de Engenharia de Lorena da USP. 
Tema: Avaliação de modelos de machine learning na predição da temperatura crítica de supercondutores.


Este trabalho busca explorar modelos de aprendizado de máquina para predizer a temperatura crítica de supercondutores.
A predição é feita sobre dados estatísticos calculados a partir da fórmula química dos supercondutores, seguindo os mesmos passos do artigo encontrado em https://www.researchgate.net/publication/324077979_A_Data-Driven_Statistical_Model_for_Predicting_the_Critical_Temperature_of_a_Superconductor . 
Os dados explorados aqui, foram construídos por um módulo em Python (supercon_dados.py).
Foi construído também um módulo (supercon_funcoes_apoio_ML.py) com funções que auxiliam 
o processo de treinamento e obtenção de hiperparâmetros dos modelos.

Os scripts estão comentados em portugues e eles abordam o passo a passo usado para treinar e analizar os modelos. 
Os modelos usados são: 

Regressão linear simples;
Ridge regression;
Lasso;
Elastic-Net;
Máquina de Vetores de Suporte;
Árvore de Decisão para regressão;
Floresta Aleatória e Floresta Extremamente Aleatória;
Gradient Tree Boosting;
Rede Neural Profunda (Multi-camadas de perceptron).

Diretórios:

Na pasta 'dados_supercon_murilo' estão os dados usados para treinar os modelos de machine learning. Os dados neste diretório foram construídos a partir do módulo 'supercon_dados.py'. Na pasta 'exploracao_dados' está um breve estudo dos dados usados no treinamento dos modelos. Na pasta 'obtencao_hiperparametros' encontram-se o levantamento dos melhores hipeparâmetros dos modelos com base no processo de validação cruzada. Na pasta 'melhores_modelos' encontram-se os melhores modelos para o problema proposto, para eles foram feitas análises mais completas. 

Os módulos em Python requeridos para reproduzir os scripts são: pandas; numpy; re; datetime; os; sklearn; seaborn; matplotlib; tensorflow; tensorflow_docs.

in English:

This work seeks to explore machine learning models to predict the critical temperature of superconductors.
The data explored here, were built by a Python module (TCC_supercon_dados.ipynb).
A module was built (TCC_supercon_funcoes_apoio_ML.py) with functions that help
the process of training and obtaining hyperparameters of the models
The scripts are commented in Portuguese and they address the step by step used to train and analyze the models. 
The models used are:

Ordinary Least Squares;
Ridge regression;
Lasso;
Elastic-Net;
Support Vector Machines;
Decision Trees for regression;
Forests of randomized trees;
Gradient Tree Boosting;
Deep Neural Network  (Multi-layer Perceptron).

Directories:

In the main directory are the modules used to generate the data and provide convenient functions for training the models. In the 'obtencao_hiperparametros' directory, all models submitted to the cross-validation process are presented, in this directory are the best hyperparameters for training the models. Also, it is possible to find in this last mentioned directory, the RMSE and R^2 of the evaluated models. In the 'melhores_modelos' directory are the models with the highest R^2 scores and the lowest RMSE, in addition to this directory there are graphical analyzes and a more detailed discussion of the results. In the 'dados_supercon_murilo' directory are the databases used in the training of machine learning models.



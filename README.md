# Implementação de modelos de machine learning para predição de temperaturas críticas de supercondutores

Trabalho de graduação para o curso de Engenharia Física da Escola de Engenharia de Lorena da USP. 
Tema: Avaliação de modelos de machine learning (ML) na predição da temperatura crítica de supercondutores.


Este trabalho busca explorar modelos de aprendizado de máquina para predizer a temperatura crítica de supercondutores.
A predição é feita sobre dados estatísticos calculados a partir da fórmula química dos supercondutores, seguindo os mesmos passos do artigo encontrado em https://www.researchgate.net/publication/324077979_A_Data-Driven_Statistical_Model_for_Predicting_the_Critical_Temperature_of_a_Superconductor . 
Os dados explorados aqui, foram construídos por um módulo em Python (supercon_dados.py).
Foi construído também um módulo (supercon_funcoes_apoio_ML.py) com funções que auxiliam 
o processo de treinamento e obtenção de hiperparâmetros dos modelos.

Os scripts estão comentados em portugues e eles abordam o passo a passo usado para treinar e analizar os modelos. 
Os modelos usados são: 

Regressão linear múltipla;
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

----------------------------------------------------------------------------------------------------------------------------------------


English:


Final work for the Physical Engineering course at the Lorena Engineering School at USP. Theme: Evaluation of machine learning (ML) models in predicting critical temperature of superconductors.


This work seeks to explore machine learning models to predict the critical temperature of superconductors.
The prediction is made on statistical data calculated from the chemical formula of the superconductors, following the same steps as the article found at https://www.researchgate.net/publication/324077979_A_Data-Driven_Statistical_Model_for_Predicting_the_Critical_Temperature_of_a_Superconductor.
The data explored here, were built by a Python module (supercon_dados.py).
A module was also built (supercon_funcoes_apoio_ML.py) with functions that help
the process of training and obtaining hyperparameters of the models.

The scripts are commented in Portuguese and they address the step by step used to train and analyze the models. 

The ML models used are:

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

In the 'data_supercon_murilo' folder are the data used to train the machine learning models. The data in this directory was built from the module 'supercon_dados.py'. In the folder 'exploracao_dados' there is a brief study of the data used in the training of the models. In the folder 'obtencao_hiperparametros' there is a survey of the best hyperparameters of the models based on the cross-validation process. The 'best_models' folder contains the best models for the proposed problem, for which more complete analyzes were made.


The Python modules required to reproduce the scripts are: pandas; numpy; re; datetime; os; sklearn; seaborn; matplotlib; tensorflow; tensorflow_docs.

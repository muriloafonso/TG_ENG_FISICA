#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###   Importação de Bibliotecas   ###


# In[ ]:


import pandas as pd
import numpy as np
import re
import datetime
import os

# In[ ]:


###   Chamando Dados   ###


# In[ ]:


### Base com cálculos sobre os supercondutores ###

caminho=os.getcwd()
caminho = caminho.split("\\TG_ENG_FISICA")[0] 

supercon = pd.read_csv(caminho +'\\dados_supercon_murilo\\base_supercondutores.csv')

### Tiro a indexação do csv ###   
supercon=supercon.drop(columns=['Unnamed: 0'])
    
###  Base com distribuição atômica dos elementos do material supercondutor ###

elementos = pd.read_csv(caminho +'\\dados_supercon_murilo\\elementos_atomos.csv')

###  Tiro a indexação do csv ###
elementos=elementos.drop(columns=['Unnamed: 0'])
    
### Base propriedades dos elementos ###

propriedades = pd.read_csv(caminho +'\\dados_supercon_murilo\\sub_elementos_dados.csv')

### Coloco os nome dos elementos como indexação ###
propriedades = propriedades.set_index("Element")

### Base com novos supercondutores ###
novos = pd.read_csv(caminho +'\\dados_supercon_murilo\\novos_supercondutores.csv', sep=';')

### Removo possíveis valores duplicados ###
novos = novos.drop_duplicates().reset_index(drop=True)


# In[ ]:


### A função a seguir, limpa valores duplicados e garante que que os registros novos nunca foram expostos a testes ###


# In[ ]:


def verificador_novos():
    
    novos_novos = novos

    novos_dados=np.array(novos_novos)
    antigos_dados = np.array(elementos.iloc[:,[-1,-2]])

    lista_novos = []

    for i in novos_dados:

        j = i[0] + '-'+str(int(i[1]))

        lista_novos.append(j)

    

    lista_antigos = []

    for i in antigos_dados:

        j = i[0] +'-'+ str(int(i[1]))

        lista_antigos.append(j)

    

    indice = 0

    for i in lista_novos:

        if i in lista_antigos:

            novos_novos = novos_novos.drop(indice)

        indice += 1


    novos_novos = novos_novos.reset_index(drop=True)
    
    return novos_novos


# In[ ]:


###   Função que calcula parâmetros para serem inseridos no DataFrame supercon  ###
### Função retorna um DataFrame que pode ser usado para predizer Tc ou inserir registros no DataFrame supercon ###


# In[ ]:


def calcular(v):
    
    argumentos = v
    
    ### respondendo qual o material está sendo analisado ###
    
    material = ""
    
    for concatenar in argumentos:
        
        material += str(concatenar)
        
    print("Material: ",material)
    
    ### Elementos e suas distribuições ###
    
    
    num_elementos = int(len(argumentos)/2)
    
    num_atomos = 0
    
    for atomo in range(num_elementos):
        
        num_atomos += float(argumentos[(2*atomo + 1)])
        
    
    ### Criação de um vetor preditivo ###
    
    v_preditivo = []
    
    v_preditivo.append(num_elementos)
    
    ### Elementos e suas distribuições: fator p ###
    
    fator_p = []
    
    for p in range(num_elementos):
        
        fator_p.append(argumentos[(2*p + 1)]/num_atomos)
    
    ### Elementos e suas distribuições para cada propriedade ###
    
    colunas = propriedades.columns[1:len(propriedades.columns)]
    
    for icolunas in colunas:
    

         ### Elementos e suas distribuições: fator w (Calculado sobre as propriedades t) ###

        t = []
        fator_w = []

        for ipropriedade in range(num_elementos):

            t.append(propriedades.loc[argumentos[2*ipropriedade],icolunas])
            

        for ifator_w in range(num_elementos):

            fator_w.append(t[ifator_w]/sum(t))

         ### Elementos e suas distribuições: Coeficiente Geral (Calculado sobre os coeficientes p e w) ###

        coef_gerais = []

        divisor = np.sum(np.array(fator_p)*np.array(fator_w))

        for icoef in range(num_elementos):

            coef_gerais.append((fator_p[icoef]*fator_w[icoef])/divisor)


        ### Características ###

        media = (np.mean(np.array(t)))
        
        v_preditivo.append(media)

        media_ponderada = np.sum(np.array(t)*np.array(fator_p))
        
        v_preditivo.append(media_ponderada)

        media_geometrica = np.prod(t)**(1/len(t))
            
        v_preditivo.append(media_geometrica)

        media_geo_ponderada = np.prod(np.array(t)**np.array(fator_p))
        
        v_preditivo.append(media_geo_ponderada)

        entropia = np.sum(-1*np.array(fator_w)*np.log(np.array(fator_w)))
        
        v_preditivo.append(entropia)

        entropia_peso = np.sum(-1*np.array(coef_gerais)*np.log(np.array(coef_gerais)))

        v_preditivo.append(entropia_peso)

        Range = max(t) - min(t)
        
        v_preditivo.append(Range)

        Range_ponderado = np.amax(np.array(t)*np.array(fator_p))-np.amin(np.array(t)*np.array(fator_p))
        
        v_preditivo.append(Range_ponderado)

        desv_padrao  =  np.sqrt((np.sum((np.array(t)-media)**2)/len(t)))
        
        v_preditivo.append(desv_padrao)

        desv_padrao_ponderado = np.sqrt(np.sum(np.array(fator_p)*((np.array(t)-media_ponderada)**2)))
        
        v_preditivo.append(desv_padrao_ponderado)
        
    
    return pd.DataFrame(np.reshape(np.array(v_preditivo),(1, len(v_preditivo))), columns=supercon.columns[0:-1])
    


# In[ ]:


### Função para distribuição dos elementos no formato do DataFrame elementos   ###
### Retorna um DataFrame que pode ser usado para inserir valores no DataFrame elementos ###


# In[ ]:


def distribuir(Tc,v):
     
    ### Vetores com atomos e numero de atomos ###
    
    atomo = []
    num_atomo = []
    
    for i in range(len(v)):
        
        if i%2 == 0:
            
            atomo.append(v[i])
            
        else:
            
            num_atomo.append(v[i])
             
    ### Material ###
    
    material = ""
    
    for concatenar in v:
        
        material += str(concatenar)
    
    #### Criação de nova linha para o DataFrame elemento ###
    
    ### Colunas a serem preenchidas ###
    
    vetor_de_atribuicao_colunas = atomo
    
    for add in ['critical_temp','material']:
        
        vetor_de_atribuicao_colunas.append(add)
    
    ### Valores das colunas ###
    
    vetor_de_atribuicao_valores = num_atomo
    
    for add2 in [Tc,material]:
        
        vetor_de_atribuicao_valores.append(add2)
    
    ### Geração de um DataFrame para ser incorporado ao DataFrame elementos ###
    
    frame_zeros = pd.DataFrame(np.zeros((1,len(elementos.columns))), columns=elementos.columns)
    
    frame_zeros.loc[:,vetor_de_atribuicao_colunas] = vetor_de_atribuicao_valores
    
    return frame_zeros      
    


# In[ ]:


###   Função para transformar um texto contendo uma formula química em um vetor   ###


# In[ ]:


def fatiar(v):
    
    ### Converte o texto em lista ###
    
    texto=re.findall('[A-Z][a-z]?|[0.-9.]+', v)       
    
    ### Transforma string em número ###
    
    for i in range(len(texto)):
        
        try:            
            
            texto[i] = float(texto[i])
        
        except:
                       
            texto[i] = texto[i]
            
    
    ### Corrigir número de átomos ###
    
    
    i1 = 0
    
    while (i1 <= (len(texto)-1)):
        
        if type(texto[i1]) == str and i1 != (len(texto) - 1):
            
            if type(texto[(i1+1)]) != str:
                
                texto[i1] = texto[i1]
                
            elif type(texto[(i1+1)]) == str:
                
                texto.insert((i1+1),1)
                
        
        if type(texto[i1]) == float and i1 != (len(texto)-1):
            
            if type(texto[(i1+1)]) != float:
                
                texto[i1] = texto[i1]
                
            elif type(texto[(i1+1)]) == float:
                
                texto[i1] = float(str(texto[i1]) + '.' + str(texto[(i1+1)]))
                
                del(texto[(i1+1)])
           
        
        if i1 == (len(texto)-1) and type(texto[i1]) == str:
            
            texto.append(1)
           
        i1+=1
        
        
    for i in range(len(texto)):
        
        if type(texto[i]) == float and texto[i]%1 == 0:
            
            
            texto[i] = int(texto[i])           
          
    
    return texto    
    


# In[ ]:


###   Geração de um novo Frame elementos, adiciona os supercondutores do Frame novos   ###


# In[ ]:


def novo_elementos():
   
    novos1 = verificador_novos()
    
    
    c = 0

    nova_distribuicao_elementos = pd.DataFrame(elementos)

    for i in novos1.iloc[:,0]:

        if 'Th' not in fatiar(i) and 'M' not in fatiar(i) and 'U' not in fatiar(i) and 'D' not in fatiar(i):

            nova_distribuicao_elementos = nova_distribuicao_elementos.append(distribuir(novos1.iloc[c,1],fatiar(i)), ignore_index=True)

        c+=1
        
    return nova_distribuicao_elementos


# In[ ]:


###   Visualiza os novos dados incorporados ao Frame elementos   ###


# In[ ]:


#visualizar_novos_dados_frame_elementos = novo_elementos()
#entrada_dados_elementos = visualizar_novos_dados_frame_elementos.iloc[elementos.shape[0]-1:,]
#entrada_dados_elementos


# In[ ]:


###   Geração de um novo Frame supercon, adiciona os supercondutores do Frame novos   ###


# In[ ]:


def novo_supercon():

    novos = verificador_novos()
    
    c = 0

    novo_supercon = pd.DataFrame(supercon)

    for i in novos.iloc[:,0]:

        if 'Th' not in fatiar(i) and 'M' not in fatiar(i) and 'U' not in fatiar(i) and 'D' not in fatiar(i):

                       
            resultado_calculo = calcular(fatiar(i))          
            
            frame_supercon = pd.DataFrame(columns=supercon.columns)
            
            frame_supercon[resultado_calculo.columns] = resultado_calculo
            frame_supercon[supercon.columns[len(supercon.columns)-1]] = novos.iloc[c,1]
            
            
            novo_supercon = novo_supercon.append(frame_supercon, ignore_index=True)

        c+=1
        
    return novo_supercon


# In[ ]:


###   Visualiza os novos dados incorporados ao Frame supercon   ###


# In[ ]:


#visualizar_novos_dados_frame_supercon = novo_supercon()
#entrada_dados_supercon = visualizar_novos_dados_frame_supercon.iloc[supercon.shape[0]-1:,]
#entrada_dados_supercon


# In[ ]:


###   Salvar NOVOS conjuntos de Dados   ###


# In[ ]:


def salvar():

    ### Caminho das pastas ###

    caminho_base = caminho +'\\dados_supercon_murilo'
    caminho_repositorio = caminho +'\\dados_supercon_murilo\\repositorio_dados'

    ### Base Supercondutores ###

    supercon_name = '\\base_supercondutores'+'.csv'
    supercon_name_data = '\\base_supercondutores_V'+datetime.datetime.now().strftime('%Y%d%m_%H%M')+'.csv'

    ### Repositório ###
    supercon.to_csv(caminho_repositorio+supercon_name_data)
    ### Base Atual ###
    Base_Atual = novo_supercon()
    Base_Atual.to_csv(caminho_base+supercon_name)

    ### Base Elementos ###

    elemento_nome = '\\elementos_atomos'+'.csv'
    elemento_nome_data = '\\elementos_atomos_V'+datetime.datetime.now().strftime('%Y%d%m_%H%M')+'.csv'

    ### Repositório ###
    elementos.to_csv(caminho_repositorio+elemento_nome_data)
    ### Base Atual ###
    Base_Atual = novo_elementos()
    Base_Atual.to_csv(caminho_base+elemento_nome)


# In[ ]:


#salvar()


# In[ ]:


###   Base contem todos os dados a serem explorados nos modelos de ML   ###   


# In[ ]:


base_geral = supercon.copy()
base_geral['material'] = elementos['material']
base_geral


# In[ ]:


###   Conjunto X   ###


# In[ ]:


X_modelagem = base_geral.iloc[:,:base_geral.shape[1]-2]
X_modelagem.describe()


# In[ ]:


###   Conjunto Y   ###


# In[ ]:


Y = base_geral.iloc[:,[-2,-1]]

#Conjuto Y usado na modelagem
Y_modelagem = base_geral.iloc[:,-2]

ver_contagem = pd.DataFrame(Y['material'].value_counts())
Y.describe(), ver_contagem.describe()


# In[ ]:


###   Função de relação entre composto e sua temperatura crítica (traz a média da temperatura crítica de determinado composto)   ###


# In[ ]:


def procura(procura):
    
    proc_mean =Y.loc[Y['material']==procura]
    x=proc_mean.median()
    print(x[0])
    
    return x[0]

def analisar(x):

    return calcular(fatiar(x))
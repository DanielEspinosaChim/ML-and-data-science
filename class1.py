# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 01:22:27 2024

@author: danye
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importar el Data set
df = pd.read_csv('Data.csv')

x = df.iloc[:, :-1].values  #selecciona todas las columnas con exepcion de la ultimas, y con el values lo conviertes en un arreglo np
y = df.iloc[:,3] #solo seleccionamos la variable dependiente 


#tratamiento de los Nans 
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")#esto se hace para pasarle a la instancia que es un valor no conocido 
#eso sirve para hacer de una lo que hacia manual de remplazar los nulos por algo en este caso la media 
#el axis sirve para seleccionar si es de la fila o la columna, el 0 indica columna, como en este caso y el 1 fila
#imputer.fit(x[:, 1:3].astype(float))#aqui delimitamos a que solo se haga las columnas y fulas que tengan  nan
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])

#conertir valores categoricos a numericos    
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder = LabelEncoder()
y= labelencoder.fit_transform(y)  #LabelEncoder convierte en valores de 1,2,3,4,5
#mintras que le one hot enconde los trasforma en columnas categoricas

columtransformer = ColumnTransformer(
    transformers=[#indicas el nombre de la tupla 
        ('encoder', OneHotEncoder(), [0])  #el encoder solo es un nombre identificador, el siguiente parametro es para aplicar el one hot encoder y el ultimo indica a que columna se le va a aplicar
    ],
    remainder='passthrough'  #remainder='passthrough' indica que las otras columnas que no se van a otransformar sean ignoradas
)
x = columtransformer.fit_transform(x)



#dividir el dataset en conjunto de entranamiento y conjunto de test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x, y , test_size=0.2 , random_state=42)


import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
import numpy as np
import pandas as pd

A = np.load("MeanShift/X.npy")
B = np.load("MeanShift/_.npy")

df = pd.DataFrame(A)
df.columns = ['x', 'y']

#Se agrega una nueva columna donde iran los cluster

df['cluster'] = B

#Se crea un diccionario de colores
c = {0:'red', 1: 'green' , 2: 'blue', 3:'yellow'}

#Se crea una nueva columna en el df con los colores creados
df['Colores'] = df.cluster.map(c)

#Se crea un grafico con el df obtenido para responder la pregunta 1
plt.figure(1)
plt.scatter(x= 'x', y = 'y', data=df)
plt.title("Pregunta 1")
plt.ylabel('Feature B')
plt.xlabel('Feature A')

#Se crea un grafico con el df obtenido para responder la pregunta 2
plt.figure(2)
plt.title("Pregunta 2")
plt.scatter(x= 'x', y = 'y', c='Colores', data=df )
plt.ylabel('Feature B')
plt.xlabel('Feature A')


data = []
for j in range(len(df)):
    x = df['x'][j]
    y = df['y'][j]
    data.append((x,y))

#Como en el df hay 4 clases diferentes, se utilizara el bandwidth  = 4
mean = MeanShift(bandwidth = 4)

#Se calcula el centro de las agrupaciones.
Kshiftmodel = mean.fit(data)

#Se muestra las coordenadas de los centros
print("Respuesta a la pregunta 3: ")
for i in mean.cluster_centers_:
    print("Centro de un cluster : (", i[0], " , ", i[1], ")")

#Se crea una nueva grafica para la pregunta 3 

plt.figure(3)
plt.title("Pregunta 3")
plt.scatter(x= 'x', y = 'y', c='Colores', data=df )

#A diferencia de la pregunta 2, acá se destacan los centros con una estrella negra
plt.scatter(x=mean.cluster_centers_[: ,0],y=mean.cluster_centers_[: ,1],marker="*",c="black")
plt.ylabel("Feature B")
plt.xlabel("Feature A")

plt.show()

#4 etiquetas de la data 
print ("Las etiquetas son : ", Kshiftmodel.labels_)
longitud = len(Kshiftmodel.labels_)
print ("total de : ", longitud , "datos")

#5 Se crea un dataset
test =[ [-7,-6],[1.5,-6.5],[7.9,0.5],[5.5,10]]
print("\n --- Respuesta a la pregunta 5: ")
#Se realiza la prediccion
print("La prediccion de ", test, "es: \n", mean.predict(test))

print("\n----Respuesta a la pregunta 6: ")
for i in range (len(test)):
    #Muestran a que clase pertenece los dataset
    print("El data test de : " +str(test[i])+ "pertenecen a la clase: " +str(mean.predict(test)[i]))





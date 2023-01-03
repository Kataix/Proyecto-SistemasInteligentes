import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

A = np.load("KMeans/A.npy")
B = np.load("KMeans/_.npy")

df = pd.DataFrame(A)
df.columns = ['x', 'y']

#Se agrega una nueva columna donde iran los cluster

df['cluster'] = B

#Se crea un diccionario de colores

c = {0:'red', 1: 'green' , 2: 'blue'}

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

#Como en el df hay 3 clases diferentes, se utilizara el Kmeans con cluster = 3
kmeans = KMeans(n_clusters = 3)

#Se calcula el centro de las agrupaciones de Kmeans
KMmodel = kmeans.fit(data)

#Se muestra las coordenadas de los centros
print("Respuesta a la pregunta 3: ")
for i in kmeans.cluster_centers_:   
    print("Centro de un cluster : (", i[0], " , ", i[1], ")")

#Se crea una nueva grafica para la pregunta 3 

plt.figure(3)
plt.title("Pregunta 3")
plt.scatter(x= 'x', y = 'y', c='Colores', data=df )

#A diferencia de la pregunta 2, acá se destacan los centros con una estrella negra
plt.scatter(x=kmeans.cluster_centers_[: ,0],y=kmeans.cluster_centers_[: ,1],marker="*",c="black")
plt.ylabel("Feature B")
plt.xlabel("Feature A")

plt.show()

#4 etiquetas de la data 
print ("Las etiquetas son : ", KMmodel.labels_)
longitud = len(KMmodel.labels_)
print ("total de : ", longitud , "datos")



#5 Se crea un dataset
test =[ [2,5],[3.2,6.5],[7,2.5],[9,3.2],[9,-6,],[11,-8]]
print("\n --- Respuesta a la pregunta 5: ")
#Se realiza la prediccion
print("La prediccion de ", test, "es: \n", kmeans.predict(test))

print("\n----Respuesta a la pregunta 6: ")
for i in range (len(test)):
    #Muestran a que clase pertenece los dataset
    print("El data test de : " +str(test[i])+ "pertenecen a la clase: " +str(kmeans.predict(test)[i]))

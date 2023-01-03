import matplotlib.pyplot as plt
from sklearn import linear_model 
import numpy as np
import pandas as pd

regresion = linear_model.LinearRegression()

#Se ingresan datos

Peso = [[60.0],[65.0],[72.0],[75.0],[80.0]]
Altura = [[1.60],[1.65],[1.70],[1.73],[1.80]]
test_altura = [[1.58],[1.62],[1.69],[1.76],[1.82]]

#Se ajusta el modelo lineal

regresion.fit(Altura,Peso)

#Se guardan los datos de la prediccion de la regresion lineal
predicted = regresion.predict(test_altura)
for i in range(len(predicted)):
    print("El peso estimado de ", test_altura[i],"es", predicted[i])

#Se obtiene el valor de RSS a partir de la formula
RSS = ((regresion.predict(test_altura)-test_altura)**2).sum()
print ("\nValor del RSS predictor es: ", RSS)


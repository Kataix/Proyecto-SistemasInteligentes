import math

def COSENO(A,B):
    #variables a utilizar

    XX = 0
    XY = 0
    YY = 0

    #Se recorre los vectores para hacer la sumatoria de la formula
    for i in range(len(A)):
        x = A[i]
        y = B[i]
        XX = XX + x * x
        XY = XY + x * y
        YY = YY + y * y
    
    #Se calcula el valor de similitud
    similitud = XY/(math.sqrt(XX*YY))
    return similitud
#Se crea una funcion para transformar los radianes a grados

def GRADO(r):
    G = float(r*(180/math.pi))
    return G

print("--------Pregunta 1------------------------------------------")
print ("La similitud entre coseno (A,B) :" ,COSENO([2,1,0,2,0,1,1,1],[2,1,1,1,1,0,1,1]))
print ("La similitud entre coseno (P,Q) :" ,COSENO([1,2,3,0,4,6,7,9],[2,4,3,1,8,2,4,1]))
print ("La similitud entre coseno (S,T) :" ,COSENO([2,1,4,7,1,4,5,6],[3,3,3,6,1,1,7,8]))

print("--------Pregunta 2 ------------------------------------------")
print ("Angulos de las distancias (A,B): " ,GRADO(0.8215838362577491))
print ("Angulos de las distancias (P,Q): " ,GRADO(0.6660748630287956))
print ("Angulos de las distancias (S,T): " ,GRADO(0.9303279922126619))

print("--------Pregunta 3 ------------------------------------------")
print ("Si el angulo es 0 radianes: " , "Distancia es de : " , GRADO(0))
print ("Si el coseno es π½ radianes : ","Distancia es de : " , GRADO(math.pi*(1/2)))

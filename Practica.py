
#Importaremos las librerías necesarisas
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import csv
import math 
from math import *
#Aqui enlistaras tus columnas
X=[]
Y=[]

bandera = 0
cantidad = 0

#Abriremos el archivo csv
print('Ingresa el nombre de tu archivo sin extensión')
nombre = input()
nombre = nombre+ '.csv'

#Aquí leeremos linea por linea del archivo
with open (nombre) as f:
    reader = csv.reader(f)
    print ('Los datos de tu archivo son: ')
    print('                           ')
    for row in reader:
        print(row)
    print('                           ')

#Con este código vamos a imprimir por seárado cada columna
with open (nombre) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        X.append(float(row['X']))
        Y.append(float(row['Y']))
    
   
while (bandera==0):
    print('Ingresa el número de coordenadas que tiene tu archivo')
    cantidad = eval(input())
    h = len(X)
    if (cantidad<=h):
        for i in range(cantidad):
            if i==cantidad:
                x2=X[0]
                x1=X[i]
                y2=Y[0]
                y1=Y[i]
            else:  
                x2=X[i]
                x1=X[i-1]
                y2=Y[i]
                y1=Y[i-1]
            r = ((x2-x1)/(y2-y1))
            print (r)
            D= math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)   
            Azi1 = atan(x2 - x1 / y2 - y1)
            Azi2 = (degrees(Azi1)*400) / 360
            print('Los azimuts son:' , Azi2)
            print('Las distancias son:' ,D)
            SumD=0+D
            print(SumD)
            
        bandera=1
    else:
        print('Me pides más datos de los que tienes registrados, intentalo de nuevo')
        bandera = 1

plt.plot(X,Y, Label='Poligonal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Levantamiento')
plt.legend()
plt.show()








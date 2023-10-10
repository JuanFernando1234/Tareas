#Manipulación de Datos con Pandas:
import pandas as oso
varaible = oso.read_csv("Tarea Taller Generadores 09-10-23/Punto 3/titanic.csv", sep =",") 

#columna de survived = sobrevivientes, murio = 0, vivio = 1
#Entonces filtramos como vivio = 1 y murio = 0
vivio = variable[variable["Survived"]==1]
murio = variable[variable["Survived"]==0]

#Para contar cuantos sobrevivieron y cuantos murieron utilizaremos el comando shape 
#(shape cuenta el numero de fila de un dato determinado)

numero_vivos = vivio.shape[0]
numero_muertos = murio.shape[0]
print(variable)
print("Las personas que sobrevivieron son: ", numero_vivos)
print("Las personas que muerieron son: ", numero_muertos)

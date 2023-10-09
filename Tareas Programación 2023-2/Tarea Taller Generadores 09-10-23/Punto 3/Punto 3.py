#Busca e importa el conjunto de datos del titanic. Luego; calcula la cantidad de pasajeros que sobrevivieron y la cantidad que no sobrevivieron

#TITANIC

import pandas as pd

df = pd.read_csv("Tarea Taller Generadores 09-10-23/Punto 3/titanic.csv", sep =",") 
#Nota: sept se usa para indicar que en la tabla los elementos estan separados por una. (quise usar tsv pero no funciono)

#Podemos ver que hay una columna de survived que son los sobrevivientes, si murio tienen el valor de 0 y si vivio tienen el valor de 1
#Enronces filtramos como vivio = 1 y murio = 0
vivio = df[df["Survived"]==1]
murio = df[df["Survived"]==0]


#Ahora vamos a contar cuantos sobrevivieron y cuantos murireron y lo hacemos con el comando shape (SHAPE CUENTA EL NUMERO DE FILAS QUE APAREEC ESE DATO)

numero_vivos = vivio.shape[0]
numero_muertos = murio.shape[0]
print(df)
print()
print("Las personas que sobrevivieron son: ", numero_vivos)
print()
print("Las personas que muerieron son: ", numero_muertos)
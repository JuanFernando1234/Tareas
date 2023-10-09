#Manejo de Archivos y Datos
import pandas as oso
datos=oso.read_csv("Tarea Taller Generadores 09-10-23/Punto 2/La escuela de Lyon.csv", sep=";")

# Calcular el promedio de calificaciones y edad--- mean en ingles significa promedio
promedio_calificaciones = datos['Calificaciones'].mean()
promedio_edad = datos['Edad'].mean()

# Saber cuales estudiantes perdieron la asignatura (calificación < 30)
perdieron_asignatura = datos[datos['Calificaciones'] < 30]

#Ordenar el DataFrame por calificaciones en orden descendente
datos_ordenados = datos.sort_values(by='Calificaciones', ascending=False)

# Calcular el número de estudiantes en el 10% superior
num_estudiantes = len(datos_ordenados)
num_10_por_ciento = int(num_estudiantes * 0.10)

# Seleccionar a los estudiantes en el 10% superior
mejores_estudiantes = datos_ordenados.head(num_10_por_ciento)

print(datos)
print(f'Promedio de Calificaciones: {promedio_calificaciones:.2f}')
print(f'Promedio de Edad: {promedio_edad:.2f}')
print(perdieron_asignatura)
print(mejores_estudiantes)


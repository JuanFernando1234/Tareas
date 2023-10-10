# Manipulación de Datos Numéricos:

# Abre el archivo en modo lectura
with open("Punto 5/Lista de numeros separada por comas.txt", "r") as archivo:
    # Lee todas las líneas del archivo y elimina el carácter de nueva línea ('\n')
    lineas = archivo.readlines()

# Inicializa una lista para almacenar las sumas de cada línea
sumas = []

# Itera sobre cada línea
for linea in lineas:
    # Elimina el carácter de nueva línea ('\n') al final de la línea
    linea = linea.strip()
    # Divide la línea en una lista utilizando la coma como separador y convierte cada elemento en entero
    elementos = [int(elemento) for elemento in linea.split(',')]
    # Calcula la suma de los elementos en la línea actual y la agrega a la lista de sumas
    suma = sum(elementos)
    sumas.append(suma)

# Imprime las partes separadas
print("Este es el contenido del archivo: ")
for linea in lineas:
    print(linea)

print("El resultado de la suma de los elementos de cada línea del archivo de texto es:")
for suma in sumas:
    print(suma)


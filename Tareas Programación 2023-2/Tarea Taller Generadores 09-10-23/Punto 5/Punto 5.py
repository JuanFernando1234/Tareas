# Abre el archivo en modo lectura
with open("Punto 5/Lista de numeros separada por comas.txt", "r") as archivo:
    # Lee todas las líneas del archivo y elimina el carácter de nueva línea ('\n')
    lineas = archivo.read()

# Itera sobre cada línea y divide por comas
for linea in lineas:
    # Elimina el carácter de nueva línea ('\n') al final de la línea
    linea = int[linea.strip()]
    
    # Divide la línea en una lista utilizando la coma como separador
    partes = linea.split(',')
    
    # Imprime las partes separadas
    print(partes)


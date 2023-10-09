"""class Lectura:
    def __init__(self, archivo):
        self.archivo = archivo

    def generar_tuplas_de_parrafos(self):
        # Inicializa una lista para recopilar las tuplas de párrafos
        tuplas_parrafos = []

        # Inicializa una variable para recopilar el párrafo actual
        parrafo_actual = ""

        # Abre el archivo de texto en modo lectura (utiliza self.archivo para el nombre del archivo)
        with open(self.archivo, "r") as archivo:
            for linea in archivo:
                # Elimina los espacios en blanco al principio y al final de la línea
                linea = linea.strip()

                if not linea:
                    # Si se encuentra una línea en blanco, el párrafo ha terminado,
                    # así que crea una tupla con el párrafo actual y lo agrega a la lista de tuplas
                    if parrafo_actual:
                        tupla_parr = (parrafo_actual,)
                        tuplas_parrafos.append(tupla_parr)
                        parrafo_actual = ""
                else:
                    # Agrega la línea al párrafo actual
                    if parrafo_actual:
                        parrafo_actual += " " + linea
                    else:
                        parrafo_actual = linea

        # Añade el último párrafo si el archivo no terminó con una línea en blanco
        if parrafo_actual:
            tupla_parr = (parrafo_actual,)
            tuplas_parrafos.append(tupla_parr)

        return tuplas_parrafos

# Crear una instancia de la clase Lectura con el nombre de archivo deseado
nombre_archivo = "Punto 7/La casa de los espíritus Resumen y Análisis Capítulo 1.txt"
lector = Lectura(nombre_archivo)

# Llamar al método generar_tuplas_de_parrafos de la instancia de la clase
tuplas_de_parrafos = lector.generar_tuplas_de_parrafos()

# Imprimir las tuplas de párrafos
for idx, tupla in enumerate(tuplas_de_parrafos, start=1):
    print(f"Párrafo {idx}:")
    print(tupla[0])
    print()"""

class ProcesadorDeTexto:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.parrafos = []

    def leer_archivo(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                self.parrafos = contenido.split('\n\n')  # Suponemos que los párrafos están separados por dos saltos de línea.
        except FileNotFoundError:
            print(f"El archivo {self.ruta_archivo} no se encontró.")

    def obtener_longitudes(self):
        longitudes = [(parrafo, len(parrafo.split())) for parrafo in self.parrafos]
        return longitudes

    def obtener_N_parrafos_mas_largos(self, N):
        longitudes = self.obtener_longitudes()
        longitudes.sort(key=lambda x: x[1], reverse=True)
        return longitudes[:N]


# Ejemplo de uso
if __name__ == "__main__":
    ruta_archivo = "Punto 7/La casa de los espíritus Resumen y Análisis Capítulo 1.txt"  # Reemplaza con la ruta de tu archivo de texto
    procesador = ProcesadorDeTexto(ruta_archivo)
    procesador.leer_archivo()

    N = 5  # Cambia este valor según cuántos párrafos más largos quieras obtener
    parrafos_mas_largos = procesador.obtener_N_parrafos_mas_largos(N)

    print(f"Los {N} párrafos más largos son:")
    for i, (parrafo, longitud) in enumerate(parrafos_mas_largos):
        print(f"Párrafo {i + 1}:")
        print(parrafo)
        print(f"Longitud: {longitud} palabras")
        print()


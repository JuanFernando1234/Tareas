#Algebra Lineal con Pandas y Numpy (N × N)
import numpy as np
import pandas as pd


def resolver_sistema_lineal(matriz_a, vector_b, **kwargs):
    try:
        print(matriz_a)
        eliminacion = kwargs.get("eliminacion", None)
        Lu = kwargs.get("Lu", None)

        if eliminacion is None or Lu is None:
            print("Alguno de sus datos estan mal o faltan datos")

        else:
            for operacion, valor in kwargs.items():
                if operacion == "eliminacion":
                    x = valor(matriz_a, vector_b)
                    verificacion(matriz_a, x, vector_b)
                elif operacion == "Lu":
                    x = valor(matriz_a, vector_b)
                    verificacion(matriz_a, x, vector_b)

                else:
                    print("La operacion enviada no es valida")

    except:
        print("El sistema presento falla en algun parametro, reviselo")


def eliminacion_gausiana(matriz_a, vector_b):
    try:
        ab = np.column_stack(
            (matriz_a, vector_b)
        )  # Aqui esta conbinando la matriz a y la matriz b
        n = len(vector_b)
        for i in range(n):
            # Normalizacion de la fila actual

            ab[i] = ab[i] / ab[i, i]  # Cada valor de la fila se divide por la diagolan

            for j in range(i + 1, n):
                factor = ab[j, i]
                ab[j] = ab[j] - factor * ab[i]

        x_gaus = np.zeros(n)  # crea un vector de ceros

        for i in range(n - 1, -1, -1):
            x_gaus[i] = ab[i, -1]

            for j in range(i + 1, n):
                x_gaus[i] -= ab[i, j] * x_gaus[j]

            x_gaus[i] = x_gaus[i] / ab[i, i]

        print(ab)
        print(f"El resultado del sistema es: {x_gaus}")
        return x_gaus
    except:
        print("Fallo la eliminacion de gaus, revise la matriz")


def factorizacion_lu(matriz_a, vector_b):
    try:
        n = len(vector_b)
        L = np.zeros(
            (n, n)
        )  # Inicializar matrices, se usan para ir operando y llenenando de informacion
        u = np.zeros((n, n))

        for i in range(n):
            L[i, i] = 1  # Hacemos que la diagonal sea 1

            for j in range(i, n):
                u[i, j] = matriz_a[
                    i, j
                ]  # Copio los elementos de la matruz a y los meto en la matriz b

                for k in range(0, i):
                    u[i, j] = u[i, j] - L[i, k] * u[k, j]  # Este es el valor de U

            for j in range(i + 1, n):
                L[j, i] = matriz_a[j, i]  # Copia los lemetnos de a l

                for k in range(0, i):
                    L[j, i] = L[j, i] - L[j, k] * u[k, i]

                L[j, i] = L[j, i] / u[i, i]  # Este es el valor de L

        y = np.linalg.solve(L, vector_b)
        x = np.linalg.solve(u, y)
        print()
        print(L)
        print()
        print(u)
        print(f"La solucion de x usando LU es {x}")
        return x

    except:
        print("Fallo la factorizacion Lu")


def verificacion(matriz_a, x, vector_b):
    b = np.dot(matriz_a, x)
    result = np.array_equal(
        b, vector_b
    )  # Esto es para comparar si la multiplocacion de matrices es igual al resultado
    # print(b)
    # print(vector_b)
    if result == False:
        print("El resultado es correcto")

    else:
        print("El resultado es incorrecto")


def inicializar_analisis():
    try:
        df = pd.read_csv(
            "Actividad 4/data.csv", sep=",", header=0
        )

        # df.iloc: dice que parte del df va a tomar
        #
        a = df.iloc[:, 0:-1].to_numpy(dtype=float)
        b = df.iloc[:, -1].to_numpy(dtype=float)  # Cojo la ultima columna
        cuadrada = (
            a.shape[0] == a.shape[1]
        )  # Miramos las dimensiones de matriz, shape[0], numero de filas y schape[1] es el columnas
        tamano = (
            a.shape[0] == b.shape[0]
        )  # Miramos si la dimension de la matriz y el vector coinciden

        if cuadrada == True and tamano == True:
            resolver_sistema_lineal(
                a, b, eliminacion=eliminacion_gausiana, Lu=factorizacion_lu
            )

        # resolver_sistema_lineal()

    except:
        print("")


inicializar_analisis()
#Comprension de Generadores y Funciones con Serie de Taylor

import sympy as sp


# Sympy es una libreria matematica
def generador_taylor(**kwargs):
    try:
        expresion = kwargs.get("ex", None)
        numero = kwargs.get("num", None)
        x0 = kwargs.get("x0", None)
        x = kwargs.get(
            "x", None
        )  # Si la palabra clave existe asigna el valor, sino crea un valor por defecto que es None
        simbolo = kwargs.get("simb", None)

        if (
            expresion == None
            or numero == None
            or x0 == None
            or x == None
            or simbolo == None
        ):
            print("Te falta algun dato por ingresar o un dato esta mal ingresado")

        else:
            x_valor = sp.Symbol(
                simbolo
            )  # Aqui vamos a decirle que la reconosca como una variable (como el simbolo)
            funcion = sp.simplify(
                expresion
            )  # Convierte la expresion en una funcion de simpy(algo numerico)
            taylor_series = sp.series(funcion, x_valor, x0=x0, n=numero).removeO()
            taylor_aproximacion = sp.lambdify(
                x_valor, taylor_series, "numpy"
            )  # Convertimos la serie en una funcion de numpy, para poderla evaluar
            resultado = taylor_aproximacion(x)
            yield taylor_series, resultado
    except:
        print("")


expresion = input("Ingresa la expresion: ")
numero = int(input("Ingrese el nuermo de terminos: "))
x0 = int(input("Punto donde se centrara la serie. "))
x = int(
    input("Valor donde se realizara la aproximaciond de la funcion: ")
)  # El numero que va a tomar x
simbolo = input("Ingrese la variable a trabajar: ")

for aproximacion_taylor, resultado in generador_taylor(
    ex=expresion, num=numero, x0=x0, x=x, simb=simbolo
):
    print(aproximacion_taylor)
    print()
    print(resultado)
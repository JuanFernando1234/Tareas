#Que es un decorador?: Es una funcion que modifica el comportamiento de una función ya existente, sin afectar su código.
# Decorador para verificar si una persona es mayor de edad y puede comprar cerveza :)
def es_mayor_de_edad(funcion_a_decorar): # Esta es mi funcion decoradora, esta tiene como parametro funcion_a_decorar que es en este caso: comprar_alcohol
    EDAD_MINIMA = 18

    def Decorador(edad):#La funcion es_mayor_de_edad crea una nueva funcion:def wrapper esta nueva funcion (def wrapper) es la encargada de ejecutar el parametro comprar_alcohol pues es def wrapper la que agrega nuevo comportamiento a la funcion a decorar comprar_alcohol
       print("Que sed, quien va a comprar las cervezas?")
       if edad >= EDAD_MINIMA:
            return f"Yo las compro, {funcion_a_decorar(edad)}"
       else:
            return f"Master estoy muy chico tengo {edad} años."

    return Decorador

# Utilizando el decorador con la sintaxis @
@es_mayor_de_edad
def comprar_alcohol(edad):
    return "Hoy nos ponemos bien locos!"

try:
    edad = int(input("Jefe ingresa tu edad: "))
    resultado = comprar_alcohol(edad)
    print(resultado)
except ValueError:
    print("Joda mani no sabes escribir?, te enseño bro?.")

#def es_mayor_de_edad(funcion_a_decorar=comprar_alcohol...esto porque es la funcion que decidi decorar) ---->>> Decorador que es la funcion que queria decorar, pero ya decorada
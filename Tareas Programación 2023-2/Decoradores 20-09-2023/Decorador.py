# Decorador para verificar si una persona es mayor de edad y puede comprar cerveza :)
def es_mayor_de_edad(funcion_a_decorar): # Mi funcion decoradora, esta tiene como parametro de mi funcion a decorar que es en este caso: comprar_alcohol
    EDAD_MINIMA = 18

    def Decorador(edad):#La funcion es_mayor_de_edad crea una nueva funcion la funcion def Decorador (la cual modifica el comportamiento de comprar_alcohol ) 
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
    print("Joda mani no sabes escribir un numero?, te enseño bro?.")

#def es_mayor_de_edad(funcion_a_decorar=comprar_alcohol...esto porque es la funcion que decidi decorar) ---->>> Decorador que es la funcion que queria decorar, pero ya decorada
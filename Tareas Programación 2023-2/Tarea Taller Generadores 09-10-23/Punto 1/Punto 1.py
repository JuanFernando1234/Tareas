#Generadores y Comprensión de Generadores:
def fibo_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n = 800  #se hace el ejemplo con un numero cualquiera
fibonacci = fibo_generator(n)

for numero in fibonacci:
    print(numero)
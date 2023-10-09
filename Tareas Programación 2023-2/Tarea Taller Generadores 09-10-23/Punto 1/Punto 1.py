def fibonacci_generador(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n = 100  # Cambia este valor según tu preferencia
fibonacci = fibonacci_generador(n)

for numero in fibonacci:
    print(numero)
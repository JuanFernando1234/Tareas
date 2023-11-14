# Defino la clase vector, con su magnitud, suma, producto punto y producto cruz
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitud = (x**2 + y**2 + z**2)**0.5

    def __add__(self, otro):
        x_nuevo = self.x + otro.x
        y_nuevo = self.y + otro.y
        z_nuevo = self.z + otro.z
        resultado = Vector(x_nuevo, y_nuevo, z_nuevo)
        return resultado

    def producto_punto(self, otro):
        resultado = (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)
        return resultado

    def producto_cruz(self, otro):
        x_nuevo = self.y * otro.z - self.z * otro.y
        y_nuevo = self.z * otro.x - self.x * otro.z
        z_nuevo = self.x * otro.y - self.y * otro.x
        return Vector(x_nuevo, y_nuevo, z_nuevo)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

# Pido definir vectores
print("Ingrese coordenadas del primer vector")
x_1 = float(input("Componente X: "))
y_1 = float(input("Componente Y: "))
z_1 = float(input("Componente Z: "))

print("Ingrese coordenadas del segundo vector")
x_2 = float(input("Componente X: "))
y_2 = float(input("Componente Y: "))
z_2 = float(input("Componente Z: "))

# Todos los resultados de los vectores
print("El resultado de los vectores es:")
vec_1 = Vector(x_1, y_1, z_1)
vec_2 = Vector(x_2, y_2, z_2)

print("Vector 1: ", vec_1)
print("Magnitud vector 1: ", int(vec_1.magnitud))   # Con "int" para evitar muchos decimales
print("Vector 2: ", vec_2)
print("Magnitud vector 2: ", int(vec_2.magnitud))   # Con "int" para evitar muchos decimales
print("Suma de los vectores: ", vec_1 + vec_2)
print("Producto punto de los vectores: ", vec_1.producto_punto(vec_2))
print("Producto cruz de los vectores: ", vec_1.producto_cruz(vec_2))

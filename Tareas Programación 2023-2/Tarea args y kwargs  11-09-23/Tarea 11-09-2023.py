class PersonajeSimpson:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.caracteristicas = {}

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.ocupacion}"

    def agregar_caracteristica(self, **kwargs):
        for key, value in kwargs.items():
            self.caracteristicas[key] = value

    def mostrar_caracteristicas(self):
        if not self.caracteristicas:
            return "No hay características definidas."
        caracteristicas_str = ", ".join([f"{key}: {value}" for key, value in self.caracteristicas.items()])
        return f"Características: {caracteristicas_str}"


homero = PersonajeSimpson("Homero Simpson", 39, "Seguridad Nuclear")
marge = PersonajeSimpson("Marge Simpson", 36, "Ama de casa")


homero.agregar_caracteristica(pasatiempo="Ver televisión", comida_favorita="Rosquillas")
marge.agregar_caracteristica(pasatiempo="Cocinar", comida_favorita="Comida saludable")


print(homero)
print(homero.mostrar_caracteristicas())
print(marge)
print(marge.mostrar_caracteristicas())

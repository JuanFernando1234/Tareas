#Codigo para hallar cualquiera de las 3 variables de la ecuacion de gas ideal conociendo dos
class GasesIdeales:
    def __init__(self, volumen, presion, temperatura):
        self.V = volumen
        self.P = presion
        self.T = temperatura
        self.R = 8.314

    def calcular_presion(self):
        respuesta = (self.R * self.T) / self.V
        return respuesta

    def calcular_volumen(self):
        respuesta = (self.R * self.T) / self.P
        return respuesta

    def calcular_temperatura(self):
        respuesta = (self.V * self.P) / self.R
        return respuesta


print("Ingrese el volumen:")
volumen = float(input("Valor volumen: "))

print("Ingrese la presión:")
presion = float(input("Valor presión: "))

print("Ingrese la temperatura:")
temperatura = float(input("Valor temperatura: "))


gas = GasesIdeales(volumen, presion, temperatura)


presion_calculada = gas.calcular_presion()
volumen_calculado = gas.calcular_volumen()
temperatura_calculada = gas.calcular_temperatura()

print(f"La presión calculada es: {presion_calculada:.5f}")
print(f"El volumen calculado es: {volumen_calculado:.5f}")
print(f"La temperatura calculada es: {temperatura_calculada:.5f}")

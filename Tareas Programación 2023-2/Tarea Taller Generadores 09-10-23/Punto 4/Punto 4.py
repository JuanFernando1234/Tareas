import json

# Creamos una lista con la información de los empleados
# La información de los empleados estará representada en diccionarios
empleos_guaracheros = [
    {"Nombre": "Yasuri", "Salario": 850000, "Departamento": "sobelo"},
    {"Nombre": "Yamile", "Salario": 850000, "Departamento": "Zapateo"},
    {"Nombre": "Aletofonce", "Salario": 850000, "Departamento": "Aleteo"},
    {"Nombre": "Fumarato", "Salario": 1200000, "Departamento": "Dj"}
]

# Exportamos los datos en un archivo JSON
with open("empleos_guaracheros.json", "w") as archivos_json:
    json.dump(empleos_guaracheros, archivos_json)


import json

def filtrar_productos_por_precio(archivo_json, umbral):
        with open(archivo_json, 'r') as file:
            data = json.load(file)
            for producto in data:
                if producto.get('Precio', 0) > umbral:  # Usar 'Precio' en lugar de 'precio'
                    yield producto
# Ejemplo de uso

archivo_json = "Punto 9/Crucero_Nilo.json"  # Reemplaza con la ruta de tu archivo JSON
umbral_precio = 2300000  # Define el umbral de precio que desees

print(f"Productos con un precio superior a {umbral_precio}:")
for producto in filtrar_productos_por_precio(archivo_json, umbral_precio):
        print(f"Embarcacion: {producto['Embarcacion']}")  # Usar 'Embarcacion' en lugar de 'nombre'
        print(f"Precio: {producto['Precio']}")  # Usar 'Precio' en lugar de 'precio'
        print(f"Cantidad en stock: {producto['Cantidad de stock']}")  # Usar 'Cantidad de stock' en lugar de 'cantidad_en_stock'
        print()

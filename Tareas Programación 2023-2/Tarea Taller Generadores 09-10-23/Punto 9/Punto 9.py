import json

def filtrar_productos_por_precio(archivo_json, umbral):
        with open(archivo_json, 'r') as file:
            data = json.load(file)
            for producto in data:
                if producto.get('Precio', 0) > umbral:  
                    yield producto

archivo_json = "Punto 9/Crucero_Nilo.json"  
umbral_precio = 2300000  

print(f"Productos con un precio superior a {umbral_precio}:")
for producto in filtrar_productos_por_precio(archivo_json, umbral_precio):
        print(f"Embarcacion: {producto['Embarcacion']}")  
        print(f"Precio: {producto['Precio']}")  
        print(f"Cantidad en stock: {producto['Cantidad de stock']}")  
       

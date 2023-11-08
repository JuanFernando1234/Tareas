"""Analisis de Datos con pandas y numpy"""
    #1. Importat las bibliotecas de pandas y numpy
    #2. Leer un archivo csv llamado "datos_fisica.csv" que contiene datos experimentales
    #3. Defina una funcion que se llame "Analizar datos" que acepte:
        #*Args con una lista de nombres
        #*kwargs con operaciones
        #por ejejemplo (media, mediana, desviacion estandar)
        #Manjear los errores que pueden surgir 
        
    #4. Utilizar numpy y pandas para realizar las operaciones especificadas en los datos seleccionados
    
import numpy as np
import pandas as pd 


#print(data[data["Colombia"]>25]["Colombia"]) FILTRAR DATOS DE COLOMBIA

def analizar_datos(informacion, *args, **kwargs): #Los args son cualquier cosas y los almacena en en tuplas y kwargs sons diccionarios
    resultados = {}
    try:
        if(args and kwargs): #si existe (args and kwargs) haga lo siguiente...
            print(args[0]) #args[0] es acceder a la tupla(o elemento) de posicion 0
            for columna in args[0]:
                resultados[columna]={} #Aqui resultados["la interacion"]

                for medicion,valor in kwargs.items(): #El primer valor va a ser la clave y el segundo va a ser el valor
                    if medicion == "media" and valor =="media":
                        resultados[columna]["media"] = np.mean(informacion[columna])
                        
                    elif medicion == "mediana" and valor == "mediana":
                        resultados[columna]["mediana"] = np.median(informacion[columna])
                        
                    elif medicion =="desviasion" and valor == "desviasion":
                        resultados[columna]["desviasion"] = np.std(informacion[columna]) #std es desviasion en python
                        
                    else: 
                        print(f"operacion no valida {medicion}")
            print(resultados)
        else: 
            print("Falto un args o un kwargs")
        
    except: 
        print("Algo del analisis esta mal")
    

def iniciar_analisis():
    
    try:
        #Dentro del Try va a ir lo que que hace el codigo, si falla va al except
        data = pd.read_csv("Actividad 1/datos_fisicaA.csv", sep=",", header=0)
        
        lista_columnas = ["Colombia","Venezuela","Mexico","Argentina"] #Pon el header haria esto, asi que es irrelevante
        analizar_datos(data,lista_columnas, media="media", mediana = "mediana", desviasion = "desviasion", operacion_no_valida = "operacion no valida") #Aqui le envio los datos del csv a la funcion de arriba
        # si algun kwarg no esta bien escrito ya sea la clave o el valor aparecera como "operacion no valida"
        

    except:
        #Aqui salta si falla el codigo
        print("El archivo no esta en la carpeta o hay algo mal en los datos del archivo")
        
iniciar_analisis()

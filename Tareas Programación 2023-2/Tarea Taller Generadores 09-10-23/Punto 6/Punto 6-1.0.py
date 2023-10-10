#Comprension de listas y generadores  
    
#En el punto 6-1.0 se imprimia varias listas,cada vez con mas palabras con longitud>5
def lista_palabras(lista):
    lista_contenedora=[]
    for palabra in lista:
        longitud_palabra= len(palabra)
        if longitud_palabra >5:
            lista_contenedora.append(palabra)
        yield lista_contenedora
w = ["Mordecai", "Rigby", "Musculoso", "Benso","Skips", "Papaleta"]
resultado = lista_palabras(w)

for palabras in resultado:
    if palabras:
        print(palabras)

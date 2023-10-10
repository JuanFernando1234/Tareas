#Comprension de listas y generadores  

#En el punto 6-2.0  se resumieron todos los pasos dentro de la lista_contenedora, y se imprimio cuando se termina el ciclo for
def lista_palabras(lista):
    lista_conetnedora=[palabra for palabra in lista if len(palabra)>5 ]
    yield lista_conetnedora
w = ["Mordecai", "Rigby", "Musculoso", "Benso","Skips", "Papaleta"]
resultado = lista_palabras(w)

for palabras in resultado:
    if palabras:
        print(palabras)
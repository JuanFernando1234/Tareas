#Comprension de listas y generadores
#Escribe una funcion que tome una lista de palabras y devuelva un generdor que produzca solo las palabras que tengan mas de 5 letras
#Escribe una funcion que tome una lista de palabras y que solo nos de las palabras que tengan mas de 5 letras
        
        
def lista_palabras(lista):
    lista_conetnedora=[]
    for palabra in lista:
        longitud_palabra= len(palabra)
        if longitud_palabra >5:
            lista_conetnedora.append(palabra)
        yield lista_conetnedora
w = ["SPIDERMAN", "BATMAN", "THOR", "HULK"]
res = lista_palabras(w)

for palabras in res:
    if palabras:
        print(palabras)

#Primero lo trate de hacer como esta el anterior codigo pero imprimia varias listas,cada vez con mas palabras con longitud>5
#Al no corregir ese error me di cuenta que tocaba resumir todos los pasos dentro de la lista y que imprima cuando haya terminado el ciclo for

def lista_palabras(lista):
    lista_conetnedora=[palabra for palabra in lista if len(palabra)>5 ]
    yield lista_conetnedora
w = ["SPIDERMAN", "BATMAN", "THOR", "HULK"]
res = lista_palabras(w)

for palabras in res:
    if palabras:
        print(palabras)
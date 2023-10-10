class Lectura:
    def __init__(self):
        self.Parrafos = []
    def read(self):
       with open("Punto 7/La casa de los espiritus capitulo 1-Resumen.txt", "r") as archivo:
           Isabel=archivo.read()
           self.Parrafos=Isabel.split("\n\n")
           return self.Parrafos
    def Parrafo_Mayor(self,N,Parrafos):
        Mayor_longitud=0
        Mayor=""
        for i in range(N):
            if (i < N) and (i < len(Parrafos)):
                if len(Parrafos[i]) > Mayor_longitud:
                    Mayor=Parrafos[i]
        return Mayor    
    def Tuplas(self):
        Tuplas=[]
        for i in range(len(self.Parrafos)):
               Numero_Parrafo=i+1
               Contenido_Parrafo=self.Parrafos[i] 
               Longitud_Parrafo=len(self.Parrafos[i])
               Tuplas.append((f"Parrafo {Numero_Parrafo}",Contenido_Parrafo,f"El numero de caracteres del parrafo son: {Longitud_Parrafo}"))
               print(Tuplas[i])   
        return Tuplas
lectura=Lectura()
lectura.read()  
            



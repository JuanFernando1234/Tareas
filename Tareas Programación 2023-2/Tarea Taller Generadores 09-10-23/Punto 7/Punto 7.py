class Lectura: # Declararamos la clase llamada lectura 
    def __init__(self): #Nuestro constructor y no tiene parametros (por que no se define parrafos dentro del constructor?)
        self.Parrafos = []
    def read(self):
       with open("La casa de los espiritus capitulo 1-Resumen.txt", "r", encoding="utf-8") as archivo: # esta funcion trae al archivo. encoding="utf-8", encoding sirve para darle una forma de codificacion al texto y utf-8 es la forma particula que le sirve al español, pues esta predetermido en ingles y si tengo tildes, me van a aparecer caracteres raros
           Isabel=archivo.read() #Permite que la funcion read se ejecute dentro de read. Cuando vea Isabel va a leer el contenido del archivo
           self.Parrafos=Isabel.split("\n\n")#cuando se usa el metodo split el parrafo sale en forma de lista. #Isabel.split("\n\n") aqui ella separa cada parrafo por salto de linea
           return self.Parrafos 
    def Tuplas(self):
        Tuplas=[]
        for i in range(len(self.Parrafos)):
               Numero_Parrafo=i+1
               Contenido_Parrafo=self.Parrafos[i] 
               Longitud_Parrafo=len(self.Parrafos[i])
               Tuplas.append((f"Parrafo {Numero_Parrafo}",Contenido_Parrafo,f"El numero de caracteres del parrafo son: {Longitud_Parrafo}"))
        return (Tuplas)
    def Parrafo_Mayor(self,N):
        parrafos_ordenados=sorted(self.Parrafos, key=len,reverse=True) #el metodo sorted ordena listas de menor a mayor dependiendo de un parametro;en nuestro caso es la longitud
        Mayores=parrafos_ordenados[:N] #el ":" significa que el rango de datos seran desde el de la parte izquierda o es su defecto 0 hasta N, parte derecha del ":"
        return Mayores
lectura=Lectura() #lectura es un objeto de la clase Lectura
Contenido=lectura.read()
tuplas=lectura.Tuplas()
print("Tuplas")
print(tuplas)
N= int(input("ingrese el valor N: "))
mayor=lectura.Parrafo_Mayor(N)
print("Los N parrafos mayores")
print(mayor)
    


"""class Peso:           
 def __init__(self,masa,aceleracion): #Sirve para declarar los distintos parametros que usare en la clase
     self.m=masa 
     self.a=aceleracion
 def Weigth(self):
     P=self.m*self.a
     return P
masa_objeto=5
aceleraion_objeto=6
W=Peso(masa_objeto,aceleraion_objeto) #W es una variable que llama al metodo Constructor
nuevo_peso=W.Weigth() #nuevo_peso es una variable que pondra a funcionar la variable W en la funcion Weigth
print(nuevo_peso)"""

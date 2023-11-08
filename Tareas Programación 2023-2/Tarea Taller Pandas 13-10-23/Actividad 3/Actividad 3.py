#Clases, Objetos, Excepciones y *argsy **kwargs
import random

class Particula:
    
    def __init__(self, masa, carga, **kwargs):
        
        try: 
            
            self.informacion = {}
            if masa > 0:
                self.masa = masa
                
            else: 
                self.masa = 1
                print("Valor de la masa no valido")
            
            self.carga= carga
            
            if(kwargs):
                for medicion, valor in kwargs.items():
                    
                    if medicion=="posicion_x":
                        self.informacion["x"] = valor
                        
                    elif medicion == "posicion_y":
                        self.informacion["y"] = valor
                        
                    elif medicion == "posicion_z":
                        self.informacion["z"] = valor
                        
                    elif medicion == "tiempo":
                        self.informacion["t"]=valor
                        
                    else:
                        print("Se ingreso un dato no valido")
                        
                
                
            else: 
                print("El kwargs no existe") 
                
            
            print(self.informacion)
            
        except: 
            print("h")
            
    def energia_cinetica(self):
        try: 
            
            if self.informacion["t"] != 0:
            
                energia = (1/2)*self.masa*(((self.informacion["x"]/self.informacion["t"])**2)+((self.informacion["y"]/self.informacion["t"])**2)+((self.informacion["z"]/self.informacion["t"])**2))
                print(energia)
            
            else: 
                print("El tiempo debe de ser distinto de cero")
            
        except: 
            print("error")
            
masa = random.random()*10
carga = random.random()*20
x = 1
y = 1
z = 1
tiempo= 1

ejemplo = Particula(masa, carga, posicion_x=x, posicion_y=y, posicion_z=z, tiempo = tiempo)
ejemplo.energia_cinetica()
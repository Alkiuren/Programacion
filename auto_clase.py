#Gestiona o estima el funcionamiento de un auto
#Clase madre
class Auto:

    #Caracteristicas
    def __init__(self,marca,gasolina):
        #Caracteristicas
        self.marca=marca
        self.gasolina=gasolina

    #definir metodos
    def avanzar(self,km):
        self.gasolina -=km/4

    def retroceder(self,km):
        self.gasolina -=km/2

#Crear autos
auto1=Auto('Toyota',15)
auto2=Auto('Ford',41)

#Antes
print("##########################Antes############################")
print(auto1.marca + "Peso:"+str(auto1.gasolina))
print(auto2.marca + "Peso:"+str(auto2.gasolina))

#Halidades :En ejecucion
auto1.avanzar(10)
auto2.retroceder(10)

print("========================Despues============================")
print(auto1.marca + "Peso:"+str(auto1.gasolina))
print(auto2.marca + "Peso:"+str(auto2.gasolina))


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @nombre.deleter    
    def nombre(self):
        del self.__nombre
        
persona1 = Persona("Thiago", 22)

nombre = persona1.nombre
print(nombre)

persona1.nombre = "Simon"
nombre = persona1.nombre
print(persona1.nombre)

del persona1.nombre

print("hola capo")
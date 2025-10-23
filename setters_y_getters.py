class persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
persona1 = persona("Thiago", 22)

nombre = persona1.get_nombre()
print(nombre)

persona1.set_nombre("Simon")
nombre = persona1.get_nombre()
print(nombre)
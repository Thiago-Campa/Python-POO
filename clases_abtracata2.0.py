from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, nombre, edad, raza, actividad):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza 
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    @abstractmethod
    def presentarlo(self):
        print(f'hola mi mascota se llama {self.nombre} y tiene {self.edad} años')
    

class gato(animal):
    def __init__(self, nombre, edad, raza, actividad):
        super().__init__(nombre, edad, raza, actividad)
        print(f'vengo de la raza de los {self.raza}')
        

class perro(animal):
    def __init__(self, nombre, edad, raza, actividad):
        super().__init__(nombre, edad, raza, actividad)
        
        print(f'mi actividad favorita es {self.actividad}')
        
        
animal1 = gato("pancho", 2, "grises", "comer")
animal2 = perro("black", 4, "negros", "cirujear")

animal1.presentarlo()
animal1.hacer_actividad()
animal2.presentarlo()
animal2.hacer_actividad()
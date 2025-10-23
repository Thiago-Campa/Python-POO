from abc import ABC, abstractmethod
class persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'hola me llamo {self.nombre} y tengo {self.edad} años')

class estudiante(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f'estoy estudiando: {self.actividad}')
        
        
class trabajador(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f'estoy trabajando como: {self.actividad}')

persona1 = trabajador("thiago", 22, "hombre", "tecnico IT")
persona2 = estudiante("simon", 11, "hombre", "futbolista")

persona1.presentarse()
persona1.hacer_actividad()
persona2.presentarse()
persona2.hacer_actividad()
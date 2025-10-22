class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        return(f'mi habilidad es {self.habilidad}')
        
class empleadoArtista(persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print(f'hola me llamo {self.nombre}, {self.mostrarHabilidad()} y trabajo en {self.empresa}')
    
persona1 = empleadoArtista("Thiago", 22, "argentino", "dormir", 60000, "inalpa")

persona1.presentarse()
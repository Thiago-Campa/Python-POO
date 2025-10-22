class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"hola soy {self.nombre} estoy hablando")

class empleado(persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad, carrera, nota):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.nota = nota
        

empleado1 = empleado("Roberto", 43, "argentino", "tecnico IT", 600000)

print(empleado1.nombre) 
print(empleado1.trabajo)

estudiante1 = estudiante("Thiago", 22, "argentino", "programacion", 3)
print(estudiante1.carrera)

while True:
    hablar = input()
    if(hablar.lower() == "descanso"):
        empleado1.hablar()
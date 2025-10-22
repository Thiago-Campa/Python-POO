class perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza 
        self.edad = edad
    
    def ladrar(self):
        print(f'{self.nombre} esta ladrando.')
        
nombre = input("ingrese nombre: ")
raza = input("ingrese raza: ")
edad = input("ingrese edad: ")

perro1 = perro(nombre, raza, edad)

print(f"""
        DATOS PERRO 1: \n
        nombre = {perro1.nombre}
        raza = {perro1.raza}
        edad = {perro1.edad}
    """)

while True:
    ladrar= input()
    if(ladrar.lower() == "vivo"):
        perro1.ladrar()
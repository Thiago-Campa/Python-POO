class estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')
        
nombre = input("ingrese el nombre: ")
edad = input("ingrese su edad: ")
grado = input("ingrese su grado: ")

estudiante1 = estudiante(nombre, edad, grado)

print(f"""
        DATOS DEL ESTUDIANTE: \n
        nombre: {estudiante1.nombre}
        edad: {estudiante1.edad}
        grado: {estudiante1.grado}
    """)

while True: 
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
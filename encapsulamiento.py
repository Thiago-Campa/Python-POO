class miClase:
    def __init__(self):
        self.__atributo_privado = "valor"
    
    def __hablar(self):
        print("hola como estas?")
        
objeto = miClase()
print(objeto.__hablar)     
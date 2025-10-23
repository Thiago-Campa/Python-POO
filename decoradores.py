def decorador(funcion):
    def funcion_modificada():
        print("Bienvenidos")
        funcion()
        print("Adios")
    return funcion_modificada

@decorador
def saludo():
    print("Hola a todos!")

saludo()
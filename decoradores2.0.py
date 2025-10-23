def decorador(funcion):
    def funcion_modificada():
        print("me despierto")
        funcion()
        print("me duermo")
    return funcion_modificada

@decorador
def rutina():
    print("hago algo")

rutina()  
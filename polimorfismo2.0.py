class hombre:
    def mear(self):
        return "mear parado"
    
class mujer:
    def mear(self):
        return "mear setada"
    
def como_mea(persona): #se crea una funcion para luego llamar
    print(persona.mear())
    
wacho = hombre() #se crea el objeto y se le asigna a la clase
wacha = mujer()  #se crea el objeto y se le asigna a la clase

#distintas formas de llamar a la funcion "mear "
como_mea(wacho) 
print(wacha.mear())
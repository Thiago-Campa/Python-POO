class hincha:
    def __init__(self, nombre, club):
        self.nombre = nombre
        self.__club = club
    
    def get_club(self):
        return self.__club
        
    def set_club(self, nuevo_club):
        self.__club = nuevo_club
        

hincha1 = hincha("thiago", "river")

equipo = hincha1.get_club()
print(equipo)

hincha1.set_club("River Plate")
equipo = hincha1.get_club()
print(equipo)

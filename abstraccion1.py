class persona:
    def __init__(self):
        self._estado = "durmiendo"
        
    def despertar(self):
        self._estado = "despierto"
        print("la persona esta despiesta")
        
    def caminar(self):
        if(self._estado == "durmiendo"):
            persona.despertar
            print("la persona esta caminando")
            
persona1 = persona()
persona1.caminar() 
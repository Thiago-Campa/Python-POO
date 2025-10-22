class celular:
    def __init__(self, marca, modelo, camaraT):
        self.marca = marca
        self.modelo = modelo
        self.camaraT = camaraT
        
    def llamar(self):
        print(f'estas haciendo un llamdado desde tu {self.modelo}.')
    
    def cortar(self):
        print(f'estas cortando la llamada desde tu {self.modelo}.')
        

celular1 = celular("Samsung", "s23", "48px")
celular2 = celular("Apple", "Iphone 13 ", "48px")

print(celular1.marca)
celular1.llamar()
celular1.cortar()
print(celular2.modelo)

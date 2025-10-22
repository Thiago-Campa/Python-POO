class celular:
    def __init__(self, marca, modelo, camaraT):
        self.marca = marca
        self.modelo = modelo
        self.camaraT = camaraT

celular1 = celular("Samsung", "s23", "48px")
celular2 = celular("Apple", "Iphone 13 ", "48px")

print(celular1.marca)
print(celular2.modelo)
class batata:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__peso = 5

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, nv):
        self.__peso = nv

b1 = batata("inglêsa")
print(b1.tipo)
print(b1.peso)
b1.peso = 8
print(b1.peso)
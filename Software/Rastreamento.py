class Carro:
    def __init__(self, nportas, peso, cor, ano):
        self.cor = cor
        self.__ano = ano
        self.__nportas = nportas
        self.__peso = peso

    def getCor(self):
        return self.cor
    def getAno(self):
        return self.__ano

    def getAno(self):
        return self.__ano

carro1 = Carro ("Tesla", 1893722)
carros = [carro1]
for p in carros:
     print (p.getCor ())        
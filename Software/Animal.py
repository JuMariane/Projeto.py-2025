from Animal import ABC, abstractmethod
             #Classe
class Nome(Animal):
    def __init__(self, Nome):
        self.nome =Nome
    def exibirinformacoes(self):
        print(F"self.nome")

class Animal(ABC):
#Classe mãe abs @abstractmethod para originar os metodos, ex: def.andar 
    @abstractmethod
    def emitirSom(self):
        pass

#Som que o animal faz, ex: Gato
class Gato(Animal):
        #Função  
    def emitirSom(self):
        return print("Miau miau")
    def nome
    
class Nome(Animal):
    def __init__(self):
        super().__init__(Nome)
        self.nome = Nome

class Cachorro(Animal):
    def emitirSom(self):
        return print("Au au")
    
class Leão(Animal):
    def emitirSom(self):
        return print("Grr (rugido)")
    
def main():
    cat = Gato()
    cat.emitirSom()

def main():
    lion = Leão()
    lion.emitirSom()

def main():
    dog = Cachorro()
    dog.emitirSom()

if __name__ == "__main__":
    main()
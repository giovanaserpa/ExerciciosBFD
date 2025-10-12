from abc import ABC, abstractmethod

# 1. Classe Abstrata
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

dog = Cachorro()
cat = Gato()
print(dog.falar())
print(cat.falar())

# 2. Proibição de instanciamento
# animal = Animal()  # TypeError

# 3. Múltiplos métodos abstratos
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)

ret = Retangulo(5, 3)
print(ret.area())
print(ret.perimetro())

# 4. Herança parcial
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def parar(self):
        pass

# class Carro(Transporte):
#     def mover(self):
#         return "Carro em movimento!"
# carro = Carro()  # TypeError

class Carro(Transporte):
    def mover(self):
        return "Carro em movimento!"
    def parar(self):
        return "Carro parado."

meu_carro = Carro()
print(meu_carro.mover())
print(meu_carro.parar())

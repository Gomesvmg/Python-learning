from abc import ABC, abstractmethod
from math import pi

class FormaGeometrica(ABC):

    num_formas = 0

    @classmethod
    def get_num_formas(cls):
        return cls.num_formas

    def __init__(self, name):
        self.name = name
        FormaGeometrica.num_formas += 1

    def get_cor(self) :
        return self.name
    
    def set_cor(self, newName):
        self.name = newName

    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimetro(self):
        ...

class Quadrado(FormaGeometrica):

    def __init__(self, name, lado=2):
        super().__init__(name)
        self.lado = lado

    def get_lado(self):
        return self.lado
    
    def set_lado(self, novo_lado):
        if novo_lado < 1 :
            return print('Valor inválido')
        self.lado = novo_lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4
    
class Circulo(FormaGeometrica):

    def __init__(self, name, raio=1):
        super().__init__(name)
        self.raio = raio
        
    def get_raio(self):
        return self.raio
    
    def set_raio(self, newRay):
        if newRay <= 0 :
            return print('Valor do Raio Inválido')
        self.raio = newRay

    def diametro(self):
        return self.raio * 2
    
    def area(self):
        return f"{pi * self.raio ** 2:.2f}"
    
    def perimetro(self):
        return f'{self.diametro() * pi:.2f}'

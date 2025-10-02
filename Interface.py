from abc import ABC, abstractmethod

# Interface
class AnimalInterface(ABC):

    @abstractmethod
    def parler(self):
        raise NotImplementedError

    @abstractmethod
    def manger(self):
        raise NotImplementedError


# Classe Chien qui implémente l'interface
class Chien(AnimalInterface):
    def parler(self):
        print("Ouaf !")

    def manger(self):
        print("Le chien mange un os.")


# Classe Chat qui implémente l'interface
class Chat(AnimalInterface):
    def parler(self):
        print("Miaou !")

    def manger(self):
        print("Le chat mange du poisson.")


# --- Test ---
animaux = [Chien(), Chat()]

for animal in animaux:
    animal.parler()
    animal.manger()

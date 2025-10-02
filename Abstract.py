from abc import ABC, abstractmethod

# Classe abstraite
class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def parler(self):
        pass


# Classe Chien
class Chien(Animal):
    def parler(self):
        print(self.nom, "dit : Ouaf !")


# Classe Chat
class Chat(Animal):
    def __init__(self,nom,age):
        super().__init__(nom)
        self.age=age
    def parler(self):
        print(self.nom, "dit : Miaou !")


# --- Test ---
animaux = [Chien("Rex"), Chat("Luna",2)]

for animal in animaux:
    animal.parler()
    if isinstance(animal,Chat):
        print(f"je suis {animal.nom} , mon age est {animal.age} ans")

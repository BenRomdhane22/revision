from dataclasses import dataclass

@dataclass
class Animal:
    espece: str
    nom: str
    age: int = 0   # valeur par défaut

    def parler(self) -> None:
        if self.espece == "chien":
            print(f"{self.nom} dit : Ouaf !")
        elif self.espece == "chat":
            print(f"{self.nom} dit : Miaou !")
        else:
            print(f"{self.nom} ne sait pas parler...")

a1 = Animal("chien", "Rex", 5)
print(a1)
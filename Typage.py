class Person:
  def __init__(self, nom: str) -> None:
    self.__nom: str = nom

  def get_name(self) -> str:
    return self.__nom

  def set_name(self, name: str) -> None:
    self.__nom: str = name

p = Person(123)  
print(p.get_name())

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Invalid name.")
        self.__name = value

p = Person("Alice")
p.name = "Bob"   # OK
print(p.name)  
class PairValue:
    def __init__(self, first_val, second_val):
        self.first_val = first_val
        self.second_val = second_val

    # surcharge de l'addition (+)
    def __add__(self, other):
        if not isinstance(other, PairValue):
            return NotImplemented
        return PairValue(self.first_val + other.first_val,
                         self.second_val + other.second_val)

    # surcharge de la soustraction sur place (-=)
    def __isub__(self, other):
        if not isinstance(other, PairValue):
            return NotImplemented
        self.first_val -= other.first_val
        self.second_val -= other.second_val
        return self

    def __repr__(self):
        return f"PairValue({self.first_val}, {self.second_val})"



a = PairValue(10, 20)
b = PairValue(3, 7)

# addition normale
c = a + b
print("a + b =", c)   # PairValue(13, 27)

# soustraction sur place
a -= b
print("a après a -= b :", a)   # PairValue(7, 13)

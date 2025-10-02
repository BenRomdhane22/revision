class pizza:
    def __init__(self,name):
        self.name=name

class PizzeriaException(Exception):
    pass


class cartePizzerie:
    def __init__(self,pizzas):
        self.pizzas=pizzas

    def is_empty(self)->bool:
        return len(self.pizzas) == 0
    
    def add_pizza(self,pizza):
        self.pizzas.append(pizza)

    def nb_pizza(self)->int:
        return len(self.pizzas)


    def remove_pizza(self,name):
        pos=0
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                break
            pos=pos+1
            if pos == len(self.pizzas):
                raise PizzeriaException("name not found")
            
            
def test_nb_pizza():
    from unittest.mock import MagicMock
    pizza=MagicMock()
    cp=cartePizzerie([])
    cp.add_pizza(pizza)
    assert cp.nb_pizza()==1
    print("test ok")

def test_rv_pizza():
    from unittest.mock import MagicMock
    pizza=MagicMock()
    pizza.name="a"
    cp=cartePizzerie([])
    cp.add_pizza(pizza)
    cp.remove_pizza("a")
    assert cp.nb_pizza()==0
    print("test ok")
    
def test_exception_pizza():
    from unittest.mock import MagicMock
    p = MagicMock(); 
    p.name = "a"
    cp = cartePizzerie([])
    cp.add_pizza(p)
    try:
        cp.remove_pizza("b")  # doit lever une exception
        assert False
    except PizzeriaException:
        print("✅ test_exception_pizza ok")

def test_emty_pizza():
    from unittest.mock import MagicMock
    pizza=MagicMock()
    pizza.name="a"
    cp = cartePizzerie([])
    cp.add_pizza(pizza)
    cp.remove_pizza("a")
    assert cp.is_empty()==True
    print("✅")

    
cp=cartePizzerie([])
pizza=pizza("abc") 
cp.add_pizza(pizza)
for pizza in cp.pizzas:
    print(pizza.name)
    print("a")
    print("aaa")




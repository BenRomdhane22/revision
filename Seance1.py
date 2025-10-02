l=["c","b","a"]
l.append("d")
l=list(filter(lambda x:x=="a" or x=="b",l))
class A:
    def __init__(self,v):
        self.v=v
    def __add__(self,other):
        return self.v - other.v

a=A(5)
b=A(1)
print(a+b)
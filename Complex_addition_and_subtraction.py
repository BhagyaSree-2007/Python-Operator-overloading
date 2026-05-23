'''Create a class named Complex .Overload the operators +,- to compute respectively the addition,subtraction of given 2 complex numbers. '''
class Complex:
    def __init__(self, data):
        self.data = data
    def __add__(self, other):
        return self.data + other.data
    def __sub__(self, other):
        return self.data - other.data
n1=complex(input("Enter n1:"))
n2=complex(input("Enter n2:"))
c1=Complex(n1)
c2=Complex(n2)
print("Addition:",c1+c2)
print("Subtraction:",c1-c2)

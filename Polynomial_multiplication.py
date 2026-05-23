'''Create a class Polynomial with all necessary instance variables.Have a method to find
 the multiplication of any two polynomials using operator overloading concept.'''
class Polynomial:

    def __init__(self, coeff):
        self.coeff = coeff

    # operator overloading (*)
    def __mul__(self, other):
        result_size = len(self.coeff) + len(other.coeff) - 1
        result = [0] * result_size

        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                result[i+j] += self.coeff[i] * other.coeff[j]

        return Polynomial(result)

    def display(self):
        for i, c in enumerate(self.coeff):
            if c != 0:
                print(f"{c}x^{i}", end=" + ")
        print("\b\b ")   # remove last +


# -------- Dynamic Input --------

n1 = int(input("Enter number of terms in Polynomial 1: "))
coeff1 = list(map(int, input("Enter coefficients: ").split()))

n2 = int(input("Enter number of terms in Polynomial 2: "))
coeff2 = list(map(int, input("Enter coefficients: ").split()))

p1 = Polynomial(coeff1)
p2 = Polynomial(coeff2)

# operator overloading happens here
result = p1 * p2

print("\nPolynomial 1:")
p1.display()

print("Polynomial 2:")
p2.display()

print("Result of Multiplication:")
result.display()

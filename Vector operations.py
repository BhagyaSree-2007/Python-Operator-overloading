'''Create a vector class that represents a mathematical vector.Overload operators such as +,-,* for scalar multiplication
and == for equality.Implement methods to calculate the dot product and cross product of two vectors.'''
import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
        raise TypeError("Multiplication must be with a scalar (int/float)")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

x1=int(input("Enter x for vector1:"))
y1=int(input("Enter y for vector1:"))
z1=int(input("Enter z for vector1:"))
x2=int(input("Enter x for vector2:"))
y2=int(input("Enter y for vector2:"))
z2=int(input("Enter z for vector2:"))

v1 = Vector(x1, y1, z1)
v2 = Vector(x2, y2, z2)

print(f"Addition: {v1 + v2}")       # Vector(5, 7, 9)
print(f"Subtraction: {v2 - v1}")    # Vector(3, 3, 3)
print(f"Scalar Mul: {v1 * 3}")      # Vector(3, 6, 9)
print(f"Equality: {v1 == v2}")      # False
print(f"Dot Product: {v1.dot(v2)}") # 32
print(f"Cross Product: {v1.cross(v2)}") # Vector(-3, 6, -3)

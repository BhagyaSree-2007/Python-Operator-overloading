'''Design a matrix class and overload operators to support matrix addition, subtraction and multiplication'''
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) 
                   for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __repr__(self):
        return "\n".join([str(row) for row in self.data])

l1 = []
n1=int(input("Enter number of rows in matrix 1:"))
for i in range(n1):
    print("Enter elements in row",i+1,":")
    l=list(map(int,input().split()))
    l1.append(l)
#Matrix([[1, 2], [3, 4]])
l2 = []
n2=int(input("Enter number of rows in matrix 2:"))
for i in range(n2):
    print("Enter elements in row",i+1,":")
    l=list(map(int,input().split()))
    l2.append(l)
#Matrix([[5, 6], [7, 8]])

m1=Matrix(l1)
m2=Matrix(l2)

print("Addition:\n", m1 + m2)
print("Subtraction:\n", m1 - m2)
print("Multiplication:\n", m1 * m2)

'''Create  a class named Word. Do concatenation and comparing of strings using operator overloading concept.'''
class Word:
    def __init__(self, string1):
        self.string1 = string1
    def __add__(self, string2):
        return self.string1 + string2.string1
    def __eq__(self, string2):
        return self.string1 == string2.string1
s1=input("Enter string1:")
s2=input("Enter string2:")
w1=Word(s1)
w2=Word(s2)
print("Concatenation:",w1+w2)
re=(w1==w2)
if re:
    print("Strings are equal")
else:
    print("Strings are not equal")

class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def __add__(self, other):
        p = (self.p * other.q) + (other.p * self.q)
        q = self.p * other.q
        sum = Rational(p, q)
        return sum
    
    def __sub__(self, other):
        p = (self.p * other.q) - (other.p * self.q)
        q = self.p * other.q
        sub = Rational(p, q)
        return sub

    def __str__(self):
        return str(self.p) + "/" + str(self.q)
    
a = Rational(2, 4)
b = Rational(4, 9)

c = a + b
print(c)

d = a - b
print(d)
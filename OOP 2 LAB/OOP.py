import math
class Fraction:
    def __init__(self,num,denom):
        self.numerator=num
        self.denominator=denom
    
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
    
    def simplify(self):
        g=math.gcd(self.numerator,self.denominator)
        self.numerator //= g
        self.denominator //= g
    
    def __add__(self,f):
        denom=math.lcm(self.denominator,f.denominator)
        num=(denom //self.denominator)* self.numerator + (denom // f.denominator)* f.numerator
        return Fraction(num,denom)
    
    
F1=Fraction(20,40)
F2=Fraction(10,40)
F4=Fraction(20,40)
F3=F1+F2+F4
print(f"After Addition :\n{F3}")
F3.simplify()
print(f"After simplify :\n{F3}")
